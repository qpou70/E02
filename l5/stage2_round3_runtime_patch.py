from pathlib import Path
p=Path('l5/stage2_round3_repair.py')
s=p.read_text(encoding='utf-8')
repls={
"p16a=render_crop(16,(382,170,688,282),'round3_p16_lattice_only.png',320)":"p16a=render_crop(16,(382,170,692,270),'round3_p16_lattice_only.png',320)",
"p16b=render_crop(16,(320,333,700,432),'round3_p16_deltaE_only.png',320)":"p16b=render_crop(16,(350,350,708,435),'round3_p16_deltaE_only.png',320)",
"p16c=render_crop(16,(400,458,640,522),'round3_p16_metallic_only.png',320)":"p16c=render_crop(16,(395,440,674,528),'round3_p16_metallic_only.png',320,mask_top_px=100)",
"add_pic(s,p16c,4.02,4.86,4.96,0.92)":"add_pic(s,p16c,3.88,4.78,5.34,1.36)",
"p17=render_crop(17,(145,153,560,536),'round3_p17_full_orbital_population_table.png',330,mask_right_page_number=True)":"p17=render_crop(17,(145,153,600,600),'round3_p17_full_orbital_population_table.png',330,mask_right_page_number=True)",
"add_pic(s,p17,1.42,0.98,7.02,5.72)":"add_pic(s,p17,1.05,0.78,7.92,6.34)"
}
for old,new in repls.items():
    if old not in s:
        raise RuntimeError(f'ROUND3 crop patch target not found: {old}')
    s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
print('ROUND3 p16/p17 crop and placement targets patched')
