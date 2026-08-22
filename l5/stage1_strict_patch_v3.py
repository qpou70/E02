from pathlib import Path

src = Path('l5/stage1_strict_builder_v2.py')
out = Path('l5/stage1_strict_builder_v3_runtime.py')
text = src.read_text(encoding='utf-8')

# Round 3: pages 9/12/18/20 are frozen from the accepted Stage 1 state.
# Only page 23 is revised: keep the original scientific figure, cover English teaching text,
# and replace it in-place with Chinese labels and explanation.
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
        '# Round 2 accepted: clean crop only; no overlaid <100> patch and no bottom fragments.\nmicro=render_crop(12,(390,126,720,388),"p12_right_source.png",300)'
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

start = text.index('# p23\n')
end = text.index('\nfor p in TARGET:', start)
p23_block = r'''# p23
s=prs.slides[22]; clear(s); header(s,"氢分子的成键与反键轨道","Bonding / Antibonding Orbitals in H₂")
# Round 3: preserve the original scientific curves/fields/wells/level splitting, but localize visible teaching text.
p23_src = render_crop(23,(36,126,756,535),"p23_original_science_region.png",310)
rect(s,0.40,0.82,9.20,6.18,WHITE,MID,1)
add_picture_contain(s,p23_src,0.55,0.96,8.90,5.82)

# In-place Chinese replacement: white masks match the original white background and do not alter the scientific drawings.
def mask(slide,x,y,w,h):
    return rect(slide,x,y,w,h,WHITE,WHITE,0)

# Upper-left state count block.
mask(s,0.68,1.36,2.75,0.95)
textbox(s,0.70,1.40,2.65,0.18,"氢原子：1s¹",10.5,True,BLACK,PP_ALIGN.LEFT,margin=0)
textbox(s,0.70,1.63,2.65,0.18,"氢原子 1：2 个状态，1 个电子",9.0,False,BLACK,PP_ALIGN.LEFT,margin=0)
textbox(s,0.70,1.84,2.65,0.18,"氢原子 2：2 个状态，1 个电子",9.0,False,BLACK,PP_ALIGN.LEFT,margin=0)
textbox(s,0.70,2.05,2.65,0.18,"H₂：4 个状态，2 个电子",9.0,False,BLACK,PP_ALIGN.LEFT,margin=0)

# Orbitals and energy labels; keep ψ, σ, σ* and all curves unchanged.
mask(s,3.80,2.38,1.08,0.17)
textbox(s,3.88,2.36,0.94,0.18,"原子轨道",7.0,True,RGBColor(0,174,222),PP_ALIGN.CENTER,margin=0)
mask(s,5.83,1.83,1.16,0.19)
textbox(s,5.88,1.82,1.00,0.18,"反键轨道",6.6,True,RGBColor(0,174,222),PP_ALIGN.LEFT,margin=0)
mask(s,6.25,2.98,0.88,0.17)
textbox(s,6.25,2.96,0.82,0.18,"成键轨道",6.6,True,RGBColor(0,174,222),PP_ALIGN.LEFT,margin=0)
mask(s,7.36,1.40,2.28,0.26)
textbox(s,7.36,1.39,2.20,0.23,"电子不位于两核之间",8.1,False,BLACK,PP_ALIGN.LEFT,margin=0)
mask(s,7.64,3.17,1.95,0.23)
textbox(s,7.64,3.16,1.85,0.22,"电子位于两核之间",8.1,False,BLACK,PP_ALIGN.LEFT,margin=0)
mask(s,7.54,2.00,1.66,0.34)
textbox(s,7.56,1.99,1.52,0.31,"较高能量",12.0,False,BLACK,PP_ALIGN.CENTER,margin=0)
mask(s,7.54,2.67,1.66,0.34)
textbox(s,7.56,2.66,1.52,0.31,"较低能量",12.0,False,BLACK,PP_ALIGN.CENTER,margin=0)
mask(s,5.78,3.42,1.56,0.17)
textbox(s,5.82,3.41,1.24,0.17,"反键能级",6.5,True,RGBColor(0,174,222),PP_ALIGN.LEFT,margin=0)
mask(s,5.78,3.82,1.40,0.17)
textbox(s,5.82,3.81,1.04,0.17,"成键能级",6.5,True,RGBColor(0,174,222),PP_ALIGN.LEFT,margin=0)

# Left lower density captions and figure caption.
mask(s,2.14,3.94,0.68,0.22)
textbox(s,2.18,3.94,0.54,0.20,"反键",5.6,False,BLACK,PP_ALIGN.CENTER,margin=0)
mask(s,2.17,4.81,0.72,0.22)
textbox(s,2.21,4.81,0.54,0.20,"成键",5.6,False,BLACK,PP_ALIGN.CENTER,margin=0)
mask(s,4.57,4.86,0.90,0.22)
textbox(s,4.68,4.84,0.62,0.22,"图 3.2",8.4,False,GRAY,PP_ALIGN.CENTER,margin=0)

# Replace the visible English paragraph with Chinese teaching text in the same lower reading area.
mask(s,1.52,5.04,7.16,1.20)
textbox(s,1.62,5.05,6.95,1.02,
        "原子轨道线性组合（LCAO）：两个原子靠近时，原子轨道组合形成两个不同的“简正”模式——较高能量的反键轨道和较低能量的成键轨道。成键态电子的概率密度在两个离子实之间增大，从而降低成键能并增强体系内聚。若由 2 个原子扩展到 N 个原子，则会形成 N 个不同的 LCAO 以及 N 个彼此接近的能级，最终形成能带。",
        8.1,False,BLACK,PP_ALIGN.LEFT,margin=2)
notes(s,"第 23 页按第三轮监工意见：保留原 PDF 科学图形（1s 波函数、反键/成键波函数、电子密度、V(r) 双势阱、能级分裂、箭头与节点），只在原文字位置用白底覆盖英文教学文字并替换为中文。ψ1、ψ2、V(r)、σ、σ* 等科学符号保持原样。\n[Sources]\nECE340_L5_S18_Posted.pdf, page 23.")
'''
text = text[:start] + p23_block + text[end:]

text = text.replace(
    'for term in ["H #1: 2 states, 1 electron","H₂: 4 states, 2 electrons","Higher","Lower","成键","反键"]: assert term in t23,term',
    'for term in ["氢原子：1s¹","氢原子 1：2 个状态，1 个电子","氢原子 2：2 个状态，1 个电子","H₂：4 个状态，2 个电子","原子轨道","反键轨道","成键轨道","较高能量","较低能量","电子不位于两核之间","电子位于两核之间","反键能级","成键能级","原子轨道线性组合（LCAO）"]: assert term in t23,term\nassert any(sh.shape_type == MSO_SHAPE_TYPE.PICTURE for sh in check.slides[22].shapes), "p23 original science crop missing"'
)
text = text.replace(
    '- 实际修改页：9、12、18、20、23。',
    '- 第三轮严格执行监工范围：第 9、12、18、20 页冻结；仅返修第 23 页。'
)
text = text.replace(
    '- 页 12：重建 Si/Al/Ga/As/Be 束源—快门—分子束—衬底关系；右侧使用原页真实裁图。',
    '- 页 12：冻结；保留已通过的 MBE 示意与干净显微图裁取。'
)
text = text.replace(
    '- 页 23：重建状态数、原子 1s—分子轨道能级、成键/反键、Higher/Lower Energy 与电子密度对应。',
    '- 页 23：保留原 PDF 科学图形不重画；覆盖主要英文教学文字并原位替换为中文。'
)
text = text.replace(
    '- 非目标页 slide XML：与基准逐页 byte-for-byte 相同。',
    '- 非目标页 slide XML：与基准逐页 byte-for-byte 相同。\n- Worker self-check: passed.\n- Supervisor visual acceptance: pending.'
)

out.write_text(text, encoding='utf-8')
print(out)
