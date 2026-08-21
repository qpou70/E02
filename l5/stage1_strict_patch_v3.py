from pathlib import Path

src = Path('l5/stage1_strict_builder_v2.py')
out = Path('l5/stage1_strict_builder_v3_runtime.py')
text = src.read_text(encoding='utf-8')

replacements = [
    (
        'from PIL import Image',
        'from PIL import Image, ImageDraw'
    ),
    (
        'textbox(s,6.02,3.98,1.40,0.24,"基座（Susceptor）",8,True,GRAY,PP_ALIGN.CENTER)',
        'textbox(s,4.62,4.02,1.62,0.28,"基座 / Susceptor",7.5,True,GRAY,PP_ALIGN.RIGHT)\nconnector(s,6.20,4.15,5.95,3.91,GRAY,0.7)'
    ),
    (
        'micro=render_crop(12,(390,126,720,535),"p12_right_source.png")',
        'micro=render_crop(12,(390,126,720,397),"p12_right_source.png",270)'
    ),
    (
        'p20=render_crop(20,(42,126,754,535),"p20_formula_geometry_source.png",270)',
        'p20_clip=fitz.Rect(42,126,754,doc[19].rect.height)\np20=render_crop(20,(p20_clip.x0,p20_clip.y0,p20_clip.x1,p20_clip.y1),"p20_formula_geometry_source.png",270)\nwith Image.open(p20).convert("RGB") as im20:\n    draw20=ImageDraw.Draw(im20)\n    sx=im20.width/p20_clip.width; sy=im20.height/p20_clip.height\n    for block in doc[19].get_text("dict").get("blocks",[]):\n        for line20 in block.get("lines",[]):\n            for span20 in line20.get("spans",[]):\n                txt20=span20.get("text","").strip()\n                bb=span20.get("bbox")\n                if not bb: continue\n                remove_url = "http://www.ntu.ac.uk" in txt20 or "molecular_geometry/hybridization" in txt20\n                remove_pageno = txt20 == "20" and bb[1] > doc[19].rect.height*0.75\n                if remove_url or remove_pageno:\n                    x0=(bb[0]-p20_clip.x0)*sx-8; y0=(bb[1]-p20_clip.y0)*sy-5\n                    x1=(bb[2]-p20_clip.x0)*sx+8; y1=(bb[3]-p20_clip.y0)*sy+5\n                    draw20.rectangle([x0,y0,x1,y1],fill="white")\n    im20.save(p20)'
    ),
    (
        '"硅片 / 晶圆","基座（Susceptor）","支座 / Pedestal"',
        '"硅片 / 晶圆","基座 / Susceptor","支座 / Pedestal"'
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'Expected exactly one match for patch, got {count}: {old}')
    text = text.replace(old, new)

out.write_text(text, encoding='utf-8')
print(out)
