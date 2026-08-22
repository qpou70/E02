from pathlib import Path
p = Path('l5/stage2_round2_repair.py')
s = p.read_text(encoding='utf-8')
old_crop = "p16=render_crop(16,(36,118,756,532),'round2_p16_original_bonding_diagrams.png',300,True)"
new_crop = "p16=render_crop(16,(36,118,756,532),'round2_p16_original_bonding_diagrams.png',300,True,mask_top_px=470)"
if old_crop not in s:
    raise RuntimeError('ROUND2 p16 crop target not found')
s = s.replace(old_crop, new_crop)
p.write_text(s, encoding='utf-8')
print('ROUND2 p16 source title-rule fragment masked inside the crop image')
