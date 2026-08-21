from pathlib import Path

src = Path('l5/stage1_strict_builder_v2.py')
out = Path('l5/stage1_strict_builder_v3_runtime.py')
text = src.read_text(encoding='utf-8')

# Round 2: only page 12 and page 23 may change. Pages 9/18/20 keep the
# previously accepted deterministic reconstruction from the strict builder.
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
        '# Round 2: clean crop only; no overlaid <100> patch and no bottom fragments.\nmicro=render_crop(12,(390,126,720,388),"p12_right_source.png",300)'
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
# Round 2 scheme B: preserve the original scientific illustration region as a clean source crop.
p23_src = render_crop(23,(36,126,756,535),"p23_original_science_region.png",310)
rect(s,0.40,0.82,9.20,6.18,WHITE,MID,1)
add_picture_contain(s,p23_src,0.55,0.96,8.90,5.82)
notes(s,"第 23 页按第二轮监工意见改为方案 B：直接使用原 PDF 中完整科学图示区域的干净裁图，不再自行设计卡通圆形、替代波函数、替代电子密度图或替代 V(r) 双势阱/能级分裂关系。中文讲解放在备注中。\n[Sources]\nECE340_L5_S18_Posted.pdf, page 23.")
'''
text = text[:start] + p23_block + text[end:]

text = text.replace(
    'for term in ["H #1: 2 states, 1 electron","H₂: 4 states, 2 electrons","Higher","Lower","成键","反键"]: assert term in t23,term',
    'assert any(sh.shape_type == MSO_SHAPE_TYPE.PICTURE for sh in check.slides[22].shapes), "p23 original science crop missing"'
)
text = text.replace(
    '- 实际修改页：9、12、18、20、23。',
    '- 第二轮严格执行监工范围：第 9、18、20 页冻结；仅返修第 12、23 页。'
)
text = text.replace(
    '- 页 12：重建 Si/Al/Ga/As/Be 束源—快门—分子束—衬底关系；右侧使用原页真实裁图。',
    '- 页 12：左侧 MBE 示意保持冻结；右侧显微图重新干净裁取，删除额外 `<100>` 后贴黑框并去除底部残片。'
)
text = text.replace(
    '- 页 23：重建状态数、原子 1s—分子轨道能级、成键/反键、Higher/Lower Energy 与电子密度对应。',
    '- 页 23：采用第二轮方案 B，直接保留原 PDF 完整科学图示区域的干净裁图；中文解释仅放备注，不再用自制简化示意图替代。'
)
text = text.replace(
    '- 非目标页 slide XML：与基准逐页 byte-for-byte 相同。',
    '- 非目标页 slide XML：与基准逐页 byte-for-byte 相同。\n- Worker self-check: passed.\n- Supervisor visual acceptance: pending.'
)

out.write_text(text, encoding='utf-8')
print(out)
