from pathlib import Path
p = Path('l5/stage2_round4_repair.py')
s = p.read_text(encoding='utf-8')
needle = "p16c=render_crop(16,(395,440,674,528),'round4_p16_metallic_only.png',320)\n"
inject = """p16c=render_crop(16,(395,440,674,528),'round4_p16_metallic_only.png',320)\n# Mask residual translatable English figure labels inside the cropped science images before placing them on the slide.\ndef _mask_png(path, boxes, fill):\n    im = Image.open(path).convert('RGB')\n    d = ImageDraw.Draw(im)\n    for box in boxes:\n        d.rectangle(box, fill=fill)\n    im.save(path)\n_mask_png(p16a, [(980, 356, 1378, 443)], 'white')\n_mask_png(p16c, [(595, 306, 1240, 391)], (232, 232, 232))\n"""
if needle not in s:
    raise RuntimeError('ROUND4 mask insertion target not found')
s = s.replace(needle, inject)
p.write_text(s, encoding='utf-8')
print('ROUND4 cropped-science-image masks inserted')
