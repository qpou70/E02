from pathlib import Path
p = Path('l5/stage2_round5_repair.py')
s = p.read_text(encoding='utf-8')
s = s.replace(
    "removed += remove_shapes_in_region_by_center(slide, 3.60, 3.95, 9.55, 6.55)\nremoved += remove_residual_strip_by_top(slide, 3.60, 3.62, 9.55, 4.46, min_top=3.58)",
    "# Remove the old lower visual band, including the orphan internal 'Metallic Bonding' strip,\n# while preserving the accepted Delta-E text labels above it.\nremoved += remove_shapes_in_region_by_center(slide, 3.60, 3.05, 9.55, 6.55)"
)
s = s.replace(
    "# Crop only the true metallic-bonding science region from original PDF page 16.\nmetal_clean = render_crop(doc, 16, (418, 462, 660, 503), 'round5_p16_metallic_science_clean.png', 380)\n\ntextbox(slide, 3.86, 4.50, 5.25, 0.24, '金属键：正离子实 + 离域电子海', 9.2, True, NAVY, PP_ALIGN.CENTER)",
    "# Reinsert the accepted Delta-E electron-cloud figure as a clean crop that excludes the\n# orphan metallic-bonding title strip underneath it.\ndelta_clean = render_crop(doc, 16, (350, 350, 708, 400), 'round5_p16_deltaE_clean.png', 320)\nadd_pic(slide, delta_clean, 3.82, 3.08, 5.34, 0.92)\n\n# Crop only the true metallic-bonding science region from original PDF page 16.\nmetal_clean = render_crop(doc, 16, (418, 462, 660, 503), 'round5_p16_metallic_science_clean.png', 380)\n\ntextbox(slide, 3.86, 4.50, 5.25, 0.24, '金属键：正离子实 + 离域电子海', 9.2, True, NAVY, PP_ALIGN.CENTER)"
)
p.write_text(s, encoding='utf-8')
print('ROUND5 runtime patch applied: clean Delta-E crop and metal strip removal')
