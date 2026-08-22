from pathlib import Path
p = Path('l5/stage2_round2_repair.py')
s = p.read_text(encoding='utf-8')
old = "p16=render_crop(16,(36,118,756,532),'round2_p16_original_bonding_diagrams.png',300,True)"
new = "p16=render_crop(16,(36,118,756,532),'round2_p16_original_bonding_diagrams.png',300,True,mask_top_px=230)"
if old not in s:
    raise RuntimeError('ROUND2 p16 crop target not found')
p.write_text(s.replace(old, new), encoding='utf-8')
print('ROUND2 p16 source title-rule fragment masked')
