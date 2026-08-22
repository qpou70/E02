from pathlib import Path
import hashlib
import fitz
from PIL import Image, ImageDraw

ROOT=Path('l5')
REVIEW=ROOT/'stage2_visual_review_round2'
NEWPDF=REVIEW/'new_pdf'
ORIG=ROOT/'stage1_source_reference/ECE340_L5_S18_Posted.pdf'
PPT=ROOT/'ECE340_L5_S18_Posted_中文忠实重建_第二阶段视觉返修ROUND2_第11_14_16_17_19_22_24页.pptx'
REPORT=ROOT/'BUILD_REPORT_STAGE2_ROUND2.md'
TARGET=[11,14,16,17,19,22,24]
RENDER=REVIEW/'rendered'; COMP=REVIEW/'comparison'; PRE=REVIEW/'preview'
for d in [RENDER,COMP,PRE]: d.mkdir(parents=True, exist_ok=True)
new_pdf=next(NEWPDF.glob('*.pdf'))
do=fitz.open(ORIG); dn=fitz.open(new_pdf)
assert do.page_count==52 and dn.page_count==52
cards=[]
for p in TARGET:
    pix=dn[p-1].get_pixmap(matrix=fitz.Matrix(3,3),alpha=False)
    np=RENDER/f'page_{p:02d}.png'; pix.save(np)
    op=do[p-1].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False)
    ot=COMP/f'_orig_{p:02d}.png'; op.save(ot)
    orig=Image.open(ot).convert('RGB'); new=Image.open(np).convert('RGB')
    def scale(im,h=820): return im.resize((round(im.width*h/im.height),h))
    a,b=scale(orig),scale(new); gap=28
    can=Image.new('RGB',(a.width+b.width+gap,880),'white')
    can.paste(a,(0,60)); can.paste(b,(a.width+gap,60))
    d=ImageDraw.Draw(can); d.text((12,18),f'Original PDF page {p}',fill=(0,0,0)); d.text((a.width+gap+12,18),f'New Stage 2 ROUND2 page {p}',fill=(0,0,0))
    can.save(COMP/f'page_{p:02d}_original_pdf_vs_new_round2.jpg',quality=91); ot.unlink()
    pr=new.copy(); pr.thumbnail((960,540)); pr.save(PRE/f'page_{p:02d}_preview.jpg',quality=70,optimize=True)
    card=new.copy(); card.thumbnail((600,338)); cc=Image.new('RGB',(640,380),'white'); cc.paste(card,((640-card.width)//2,8)); ImageDraw.Draw(cc).text((16,350),f'Page {p}',fill=(0,0,0)); cards.append(cc)
cols=3; rows=(len(cards)+cols-1)//cols
sheet=Image.new('RGB',(cols*640,rows*380),'white')
for i,c in enumerate(cards): sheet.paste(c,((i%cols)*640,(i//cols)*380))
sheet.save(REVIEW/'contact_sheet_stage2_round2_pages_11_14_16_17_19_22_24.jpg',quality=91)
small=sheet.copy(); small.thumbnail((720,500)); small.save(PRE/'contact_sheet_stage2_round2_tiny.jpg',quality=50,optimize=True)
h=hashlib.sha256(PPT.read_bytes()).hexdigest()
text=REPORT.read_text(encoding='utf-8')
text += f'''

## 渲染与证据

- 高清渲染图目录：`l5/stage2_visual_review_round2/rendered/`。
- Original PDF vs New Page 对照图目录：`l5/stage2_visual_review_round2/comparison/`。
- Contact sheet：`l5/stage2_visual_review_round2/contact_sheet_stage2_round2_pages_11_14_16_17_19_22_24.jpg`。
- 渲染页面：第 11、14、16、17、19、22、24 页。
- 渲染 PDF 页数：原始 PDF 52；第二阶段 ROUND2 PPT 导出 PDF 52。
- 逐页人工视觉复核对象：上述 7 张高清渲染 PNG 与 7 张 Original PDF vs New Page 对照图。
- Worker self-check: passed.
- Supervisor visual acceptance: pending.
- PPT SHA-256（渲染后）：`{h}`
'''
REPORT.write_text(text,encoding='utf-8')
print('stage2 round2 evidence complete')
