from pathlib import Path
import fitz
import runpy

ROOT = Path(__file__).resolve().parents[1]
src_dir = ROOT / 'l5/stage1_source_reference'
pdf = src_dir / 'ECE340_L5_S18_Posted.pdf'
assert pdf.exists(), pdf

doc = fitz.open(str(pdf))
for p in (20, 22, 23):
    out = src_dir / f'original_pdf_page_{p:02d}.png'
    if not out.exists():
        pix = doc[p-1].get_pixmap(matrix=fitz.Matrix(3.0, 3.0), alpha=False)
        pix.save(str(out))
doc.close()

runpy.run_path(str(ROOT / 'l5/final_qa_image_rebuild_20_22_23.py'), run_name='__main__')
