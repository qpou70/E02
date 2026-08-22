from pathlib import Path
p = Path('l5/stage2_round2_repair.py')
s = p.read_text(encoding='utf-8')
old = "rect(s,3.62,0.82,5.92,5.92,WHITE,MID,1); add_pic(s,p16,3.74,0.96,5.68,5.62)"
new = "rect(s,3.62,0.82,5.92,5.92,WHITE,MID,1); add_pic(s,p16,3.74,0.96,5.68,5.62)\nrect(s,3.68,1.52,5.78,0.58,WHITE,WHITE,0)"
if old not in s:
    raise RuntimeError('ROUND2 p16 image placement target not found')
p.write_text(s.replace(old, new), encoding='utf-8')
print('ROUND2 p16 source title-rule fragment covered on slide canvas')
