from pathlib import Path

# Round 2 feedback: do not overlay an artificial <100> label.
# The page-12 micrograph is handled only by a clean source-PDF crop in stage1_strict_patch_v3.py.

runtime = Path('l5/stage1_strict_builder_v3_runtime.py')
text = runtime.read_text(encoding='utf-8')

replacements = [
    ('mask(s,3.80,2.38,1.08,0.17)', 'mask(s,3.72,2.30,1.45,0.32)'),
    ('textbox(s,3.88,2.36,0.94,0.18,"原子轨道",7.0,True,RGBColor(0,174,222),PP_ALIGN.CENTER,margin=0)',
     'textbox(s,3.95,2.37,0.90,0.20,"原子轨道",7.0,True,RGBColor(0,174,222),PP_ALIGN.CENTER,margin=0)'),
    ('mask(s,5.83,1.83,1.16,0.19)', 'mask(s,5.70,1.74,1.70,0.35)'),
    ('mask(s,6.25,2.98,0.88,0.17)', 'mask(s,6.10,2.86,1.55,0.35)'),
    ('textbox(s,6.25,2.96,0.82,0.18,"成键轨道",6.6,True,RGBColor(0,174,222),PP_ALIGN.LEFT,margin=0)',
     'textbox(s,6.13,2.96,1.22,0.20,"成键轨道",6.6,True,RGBColor(0,174,222),PP_ALIGN.LEFT,margin=0)'),
    ('mask(s,7.36,1.40,2.28,0.26)', 'mask(s,6.05,1.30,3.55,0.45)'),
    ('textbox(s,7.36,1.39,2.20,0.23,"电子不位于两核之间",8.1,False,BLACK,PP_ALIGN.LEFT,margin=0)',
     'textbox(s,7.20,1.40,2.15,0.24,"电子不位于两核之间",8.1,False,BLACK,PP_ALIGN.LEFT,margin=0)'),
    ('mask(s,7.64,3.17,1.95,0.23)', 'mask(s,6.35,3.02,3.20,0.45)'),
    ('textbox(s,7.64,3.16,1.85,0.22,"电子位于两核之间",8.1,False,BLACK,PP_ALIGN.LEFT,margin=0)',
     'textbox(s,7.45,3.13,1.95,0.24,"电子位于两核之间",8.1,False,BLACK,PP_ALIGN.LEFT,margin=0)'),
    ('mask(s,7.54,2.00,1.66,0.34)', 'mask(s,7.20,1.85,2.30,0.60)'),
    ('textbox(s,7.56,1.99,1.52,0.31,"较高能量",12.0,False,BLACK,PP_ALIGN.CENTER,margin=0)',
     'textbox(s,7.63,2.01,1.45,0.31,"较高能量",12.0,False,BLACK,PP_ALIGN.CENTER,margin=0)'),
    ('mask(s,7.54,2.67,1.66,0.34)', 'mask(s,7.20,2.55,2.30,0.60)'),
    ('textbox(s,7.56,2.66,1.52,0.31,"较低能量",12.0,False,BLACK,PP_ALIGN.CENTER,margin=0)',
     'textbox(s,7.63,2.70,1.45,0.31,"较低能量",12.0,False,BLACK,PP_ALIGN.CENTER,margin=0)'),
    ('mask(s,5.78,3.42,1.56,0.17)', 'mask(s,5.65,3.32,1.90,0.32)'),
    ('mask(s,5.78,3.82,1.40,0.17)', 'mask(s,5.65,3.72,1.80,0.32)'),
    ('mask(s,1.52,5.04,7.16,1.20)', 'mask(s,1.40,4.96,7.50,1.35)'),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'Expected exactly one match for {old!r}, got {count}')
    text = text.replace(old, new)

anchor = '# Left lower density captions and figure caption.\n'
insert = '''# Left lower density captions and figure caption.
# Cover source URL / leftover caption fragments from the original English figure.
mask(s,0.72,4.78,1.95,0.48)
# Cover remaining original English micro-labels exposed after contain-scaling.
mask(s,3.55,2.60,1.55,0.36)
mask(s,5.92,2.98,1.30,0.34)
# Round 4: only remove the two remaining visual remnants on page 23.
mask(s,7.50,1.68,0.42,0.18)
mask(s,4.42,4.78,1.12,0.34)
'''
count = text.count(anchor)
if count != 1:
    raise RuntimeError(f'Expected one lower-caption anchor, got {count}')
text = text.replace(anchor, insert)

fig_caption = 'textbox(s,4.68,4.84,0.62,0.22,"图 3.2",8.4,False,GRAY,PP_ALIGN.CENTER,margin=0)\n'
count = text.count(fig_caption)
if count != 1:
    raise RuntimeError(f'Expected one page-23 figure-caption textbox to remove, got {count}')
text = text.replace(fig_caption, '')

runtime.write_text(text, encoding='utf-8')
print('round4 page 23 final two visual remnants cleaned')
