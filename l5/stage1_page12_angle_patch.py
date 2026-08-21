from pathlib import Path

runtime = Path('l5/stage1_strict_builder_v3_runtime.py')
text = runtime.read_text(encoding='utf-8')
old = 'add_picture_contain(s,micro,5.24,1.02,4.22,5.65)\nnotes(s,'
new = (
    'add_picture_contain(s,micro,5.24,1.02,4.22,5.65)\n'
    'textbox(s,7.38,5.15,0.62,0.24,"<100>",8.5,True,WHITE,PP_ALIGN.CENTER,fill=BLACK,line=BLACK,margin=0)\n'
    'notes(s,'
)
count = text.count(old)
if count != 1:
    raise RuntimeError(f'Expected one page-12 picture insertion point, got {count}')
runtime.write_text(text.replace(old, new), encoding='utf-8')
print('patched page 12 <100> label')
