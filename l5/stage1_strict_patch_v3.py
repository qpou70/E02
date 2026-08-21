from pathlib import Path

src = Path('l5/stage1_strict_builder_v2.py')
out = Path('l5/stage1_strict_builder_v3_runtime.py')
text = src.read_text(encoding='utf-8')

replacements = [
    (
        'textbox(s,6.02,3.98,1.40,0.24,"基座（Susceptor）",8,True,GRAY,PP_ALIGN.CENTER)',
        'textbox(s,4.62,4.02,1.62,0.28,"基座 / Susceptor",7.5,True,GRAY,PP_ALIGN.RIGHT)\nconnector(s,6.20,4.15,5.95,3.91,GRAY,0.7)'
    ),
    (
        'micro=render_crop(12,(390,126,720,535),"p12_right_source.png")',
        'micro=render_crop(12,(390,126,720,446),"p12_right_source.png")'
    ),
    (
        'p20=render_crop(20,(42,126,754,535),"p20_formula_geometry_source.png",270)',
        'p20=render_crop(20,(42,126,754,doc[19].rect.height),"p20_formula_geometry_source.png",270)'
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
