from pathlib import Path
import hashlib
import fitz
from PIL import Image, ImageDraw

ROOT = Path("l5")
REVIEW = ROOT / "stage1_visual_review_08_24"
BASE_PDF_DIR = REVIEW / "baseline_pdf"
NEW_PDF_DIR = REVIEW / "new_pdf"
RENDER = REVIEW / "rendered"
COMPARE = REVIEW / "comparison"
PREVIEW = REVIEW / "preview"
REPORT = ROOT / "BUILD_REPORT_08_24_STAGE1_STRICT.md"
PPT = ROOT / "ECE340_L5_S18_Posted_中文忠实重建_第一阶段严格返修_第9_12_18_20_23页.pptx"
TARGET = [9,12,18,20,23]

for d in [RENDER,COMPARE,PREVIEW]:
    d.mkdir(parents=True, exist_ok=True)

base_pdf = next(BASE_PDF_DIR.glob("*.pdf"))
new_pdf = next(NEW_PDF_DIR.glob("*.pdf"))
db = fitz.open(base_pdf)
dn = fitz.open(new_pdf)
assert db.page_count == 52
assert dn.page_count == 52

cards = []
for p in TARGET:
    pix = dn[p-1].get_pixmap(matrix=fitz.Matrix(3.0,3.0), alpha=False)
    new_png = RENDER / f"page_{p:02d}.png"
    pix.save(new_png)

    pixb = db[p-1].get_pixmap(matrix=fitz.Matrix(2.0,2.0), alpha=False)
    old_tmp = COMPARE / f"_old_{p:02d}.png"
    pixb.save(old_tmp)

    old = Image.open(old_tmp).convert("RGB")
    new = Image.open(new_png).convert("RGB")
    scale_h = 820
    def scaled(im, h):
        w = round(im.width * h / im.height)
        return im.resize((w,h))
    oa = scaled(old, scale_h)
    nb = scaled(new, scale_h)
    gap = 28
    canvas = Image.new("RGB", (oa.width+nb.width+gap, scale_h+60), "white")
    canvas.paste(oa,(0,60)); canvas.paste(nb,(oa.width+gap,60))
    d = ImageDraw.Draw(canvas)
    d.text((12,18),f"Baseline page {p}",fill=(0,0,0))
    d.text((oa.width+gap+12,18),f"Stage 1 page {p}",fill=(0,0,0))
    canvas.save(COMPARE/f"page_{p:02d}_original_vs_new.jpg",quality=91)
    old_tmp.unlink()

    med = new.copy()
    med.thumbnail((960,540))
    med.save(PREVIEW/f"page_{p:02d}_preview.jpg",quality=63,optimize=True)
    tiny = new.copy()
    tiny.thumbnail((240,135))
    tiny.save(PREVIEW/f"page_{p:02d}_tiny.jpg",quality=22,optimize=True)

    card = new.copy()
    card.thumbnail((620,349))
    card_canvas = Image.new("RGB",(640,390),"white")
    card_canvas.paste(card,((640-card.width)//2,10))
    ImageDraw.Draw(card_canvas).text((16,362),f"Page {p}",fill=(0,0,0))
    cards.append(card_canvas)

sheet = Image.new("RGB",(1280,1170),"white")
for i, card in enumerate(cards):
    sheet.paste(card,((i%2)*640,(i//2)*390))
sheet.save(REVIEW/"contact_sheet_stage1_pages_09_12_18_20_23.jpg",quality=91)
tiny_sheet=sheet.copy()
tiny_sheet.thumbnail((400,366))
tiny_sheet.save(PREVIEW/"contact_sheet_tiny.jpg",quality=25,optimize=True)

digest = hashlib.sha256(PPT.read_bytes()).hexdigest()
text = REPORT.read_text(encoding="utf-8")
text += (
    "\n## 渲染与证据\n\n"
    "- 高清单页渲染目录：`l5/stage1_visual_review_08_24/rendered/`（page_09.png、page_12.png、page_18.png、page_20.png、page_23.png）。\n"
    "- 原页 vs 新页对照目录：`l5/stage1_visual_review_08_24/comparison/`。\n"
    "- 五页 contact sheet：`l5/stage1_visual_review_08_24/contact_sheet_stage1_pages_09_12_18_20_23.jpg`。\n"
    "- 渲染 PDF 页数：基准 52；阶段版 52。\n"
    "- 图片均按原始纵横比 contain/等比缩放，脚本未做非等比拉伸。\n"
    "- 手工视觉验收：待逐页打开已提交渲染图后填写最终结果；在此之前不得宣称完成。\n"
    f"- PPT SHA-256（渲染后）：`{digest}`\n"
)
REPORT.write_text(text,encoding="utf-8")
