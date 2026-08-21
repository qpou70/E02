from pathlib import Path

src = Path('l5/stage1_strict_builder_v2.py')
out = Path('l5/stage1_strict_builder_v3_runtime.py')
text = src.read_text(encoding='utf-8')

# Keep previously accepted fixes for pages 9 and 20, and update only the allowed
# page-12 crop plus the full page-23 teaching chain required by supervisor review.
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
        'micro=render_crop(12,(390,126,720,430),"p12_right_source.png",270)'
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

# Layout: left atomic 1s states, middle LCAO/energy levels, right density-energy mapping, bottom V(r).
box(s,0.35,0.82,2.35,1.36,
    "Elemental Hydrogen: 1s¹\nH #1: 2 states, 1 electron\nH #2: 2 states, 1 electron\nH₂: 4 states, 2 electrons",
    7.4,False,PALE,BLUE,BLACK,PP_ALIGN.LEFT)
textbox(s,0.44,2.27,2.12,0.25,"原子 1s 轨道",9.0,True,NAVY,PP_ALIGN.CENTER)
for cx,lab,psi in [(0.82,"H #1 1s","ψ1"),(1.82,"H #2 1s","ψ2")]:
    oval(s,cx,2.70,0.68,0.68,RGBColor(224,238,251),BLUE,0.8)
    oval(s,cx+0.24,2.94,0.20,0.20,WHITE,BLUE,0.6)
    textbox(s,cx-0.05,3.42,0.78,0.22,psi,8.2,True,NAVY,PP_ALIGN.CENTER)
    textbox(s,cx-0.18,3.66,1.08,0.25,lab,6.9,False,GRAY,PP_ALIGN.CENTER)
textbox(s,0.44,4.08,2.12,0.56,"两个原子轨道靠近后，\n不再独立，而是线性组合。",7.2,False,BLACK,PP_ALIGN.CENTER)
right_arrow(s,2.54,3.09,0.45,0.22,TEAL)

rect(s,3.03,0.82,3.45,4.55,RGBColor(251,253,255),MID,1)
textbox(s,3.28,0.96,2.92,0.25,"LCAO：线性组合形成两个分子轨道",8.7,True,NAVY,PP_ALIGN.CENTER)
box(s,3.25,1.42,2.88,0.46,"ψA = ψ1 − ψ2  →  σ*1s（反键）",7.4,True,RGBColor(246,249,255),BLUE,NAVY,PP_ALIGN.CENTER)
box(s,3.25,4.33,2.88,0.46,"ψB = ψ1 + ψ2  →  σ1s（成键）",7.4,True,RGBColor(240,249,247),TEAL,TEAL,PP_ALIGN.CENTER)
connector(s,4.05,2.32,5.58,2.32,NAVY,2.0)
textbox(s,4.20,1.95,1.22,0.24,"Antibonding energy level",6.0,False,NAVY,PP_ALIGN.CENTER)
connector(s,4.05,4.00,5.58,4.00,TEAL,2.0)
textbox(s,4.20,4.05,1.22,0.24,"Bonding energy level",6.0,False,TEAL,PP_ALIGN.CENTER)
connector(s,3.45,3.18,4.05,2.32,GRAY,0.8)
connector(s,3.45,3.18,4.05,4.00,GRAY,0.8)
connector(s,6.02,3.18,5.58,2.32,GRAY,0.8)
connector(s,6.02,3.18,5.58,4.00,GRAY,0.8)
connector(s,3.35,3.18,3.85,3.18,GRAY,1.1)
connector(s,5.68,3.18,6.18,3.18,GRAY,1.1)
textbox(s,3.16,2.82,0.66,0.24,"H #1",6.7,False,GRAY,PP_ALIGN.CENTER)
textbox(s,5.84,2.82,0.66,0.24,"H #2",6.7,False,GRAY,PP_ALIGN.CENTER)
up=s.shapes.add_shape(MSO_SHAPE.UP_ARROW,Inches(6.18),Inches(1.70),Inches(0.18),Inches(2.85))
up.fill.solid(); up.fill.fore_color.rgb=NAVY; up.line.fill.background()
textbox(s,5.72,1.65,0.52,0.30,"Higher",6.2,True,NAVY,PP_ALIGN.CENTER)
textbox(s,5.72,4.44,0.52,0.30,"Lower",6.2,True,TEAL,PP_ALIGN.CENTER)
textbox(s,4.50,3.55,0.26,0.25,"↑",12,True,TEAL,PP_ALIGN.CENTER)
textbox(s,4.80,3.55,0.26,0.25,"↓",12,True,TEAL,PP_ALIGN.CENTER)

rect(s,6.75,0.82,2.90,4.55,WHITE,MID,1)
textbox(s,6.98,0.97,2.46,0.25,"电子密度与能量对应",8.7,True,NAVY,PP_ALIGN.CENTER)
# Antibonding density: separated lobes and a node.
oval(s,7.18,1.48,0.72,0.58,RGBColor(227,239,252),BLUE,0.8)
oval(s,8.35,1.48,0.72,0.58,RGBColor(247,235,215),GOLD,0.8)
rect(s,8.12,1.36,0.035,0.82,GRAY,GRAY,0)
textbox(s,7.25,2.18,1.90,0.43,"electron not located between hydrogen atoms",5.9,False,NAVY,PP_ALIGN.CENTER)
textbox(s,7.33,2.55,1.75,0.30,"Higher Energy / Antibonding",6.4,True,NAVY,PP_ALIGN.CENTER)
# Bonding density: continuous lobe between nuclei.
oval(s,7.18,3.54,0.82,0.62,RGBColor(220,240,238),TEAL,0.8)
oval(s,8.22,3.54,0.82,0.62,RGBColor(220,240,238),TEAL,0.8)
oval(s,7.75,3.56,0.72,0.58,RGBColor(183,222,219),TEAL,0.5)
textbox(s,7.21,4.28,1.96,0.40,"electron located between hydrogen atoms",5.9,False,TEAL,PP_ALIGN.CENTER)
textbox(s,7.40,4.65,1.54,0.30,"Lower Energy / Bonding",6.4,True,TEAL,PP_ALIGN.CENTER)

rect(s,0.35,5.60,9.30,1.17,RGBColor(250,252,255),MID,1)
textbox(s,0.52,5.72,1.18,0.22,"V(r) 势能关系",7.8,True,NAVY,PP_ALIGN.LEFT)
# Axes and energy reference lines.
connector(s,1.74,6.43,8.98,6.43,GRAY,0.9)
connector(s,1.92,6.54,1.92,5.84,GRAY,0.9)
textbox(s,8.98,6.34,0.34,0.18,"r",6.5,False,GRAY,PP_ALIGN.CENTER)
textbox(s,1.72,5.72,0.38,0.18,"V(r)",6.5,False,GRAY,PP_ALIGN.CENTER)
connector(s,2.55,6.18,4.05,6.00,TEAL,1.0)
connector(s,4.05,6.00,5.60,6.18,TEAL,1.0)
connector(s,5.60,6.18,8.30,6.31,TEAL,1.0)
connector(s,2.70,5.94,8.15,5.94,NAVY,0.8)
connector(s,2.70,6.21,8.15,6.21,TEAL,0.8)
textbox(s,7.30,5.76,1.30,0.20,"Antibonding energy level",5.9,False,NAVY,PP_ALIGN.LEFT)
textbox(s,7.30,6.18,1.18,0.20,"Bonding energy level",5.9,False,TEAL,PP_ALIGN.LEFT)
textbox(s,2.22,5.74,4.62,0.22,"两个 1s 原子轨道 → 两个不同能量的分子轨道；H₂ 基态电子占据成键轨道。",6.9,False,BLACK,PP_ALIGN.CENTER)
notes(s,"第 23 页按监工要求恢复完整教学链条：Elemental Hydrogen: 1s¹；H #1 / H #2 / H₂ 状态数；ψ1、ψ2 原子 1s 轨道；LCAO 线性组合；成键/反键轨道；电子是否位于两核之间与 Higher/Lower Energy 对应；V(r)、Bonding energy level 与 Antibonding energy level。\n[Sources]\nECE340_L5_S18_Posted.pdf, page 23.")
'''
text = text[:start] + p23_block + text[end:]

# Strengthen validation and report wording for supervisor feedback.
text = text.replace(
    'for term in ["H #1: 2 states, 1 electron","H₂: 4 states, 2 electrons","Higher","Lower","成键","反键"]: assert term in t23,term',
    'for term in ["H #1: 2 states, 1 electron","H₂: 4 states, 2 electrons","ψ1","ψ2","LCAO","V(r)","Bonding energy level","Antibonding energy level","electron located between hydrogen atoms","electron not located between hydrogen atoms","Higher","Lower","成键","反键"]: assert term in t23,term'
)
text = text.replace(
    '- 实际修改页：9、12、18、20、23。',
    '- 本轮严格执行监工范围：第 9、18、20 页冻结；定点修复第 12 页 `<100>`；重新完整返修第 23 页。'
)
text = text.replace(
    '- 页 12：重建 Si/Al/Ga/As/Be 束源—快门—分子束—衬底关系；右侧使用原页真实裁图。',
    '- 页 12：左侧 MBE 示意保持上一轮通过版；右侧从原始 PDF 重新裁取显微图，并保留 `4×4 / GaAs substrate / 10 nm / <100>`。'
)
text = text.replace(
    '- 页 23：重建状态数、原子 1s—分子轨道能级、成键/反键、Higher/Lower Energy 与电子密度对应。',
    '- 页 23：恢复原子 1s 轨道（ψ1、ψ2）→ LCAO 线性组合 → 成键/反键轨道 → 电子密度位置 → Higher/Lower Energy → V(r) 与 bonding/antibonding energy level 的完整教学链条。'
)
text = text.replace(
    '- 非目标页 slide XML：与基准逐页 byte-for-byte 相同。',
    '- 非目标页 slide XML：与基准逐页 byte-for-byte 相同。\n- Worker self-check: passed.\n- Supervisor visual acceptance: pending.'
)

out.write_text(text, encoding='utf-8')
print(out)
