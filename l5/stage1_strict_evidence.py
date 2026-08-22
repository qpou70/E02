from pathlib import Path
import subprocess

ROOT = Path('l5')
round2_ppt = ROOT / 'ECE340_L5_S18_Posted_中文忠实重建_第二阶段视觉返修ROUND2_第11_14_16_17_19_22_24页.pptx'
stage2_review = ROOT / 'stage2_visual_review_round2'

# This workflow remains the active GitHub-only runner for L5 visual rework.
# Stage 1 evidence is already accepted and committed; Stage 2 ROUND2 is generated from the committed ROUND1 PPT.
subprocess.run(['python', 'l5/stage2_round2_repair.py'], check=True)
subprocess.run(['rm', '-rf', str(stage2_review)], check=True)
(stage2_review / 'new_pdf').mkdir(parents=True, exist_ok=True)
subprocess.run([
    'libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', str(stage2_review / 'new_pdf'),
    str(round2_ppt)
], check=True)
subprocess.run(['python', 'l5/stage2_round2_evidence.py'], check=True)
subprocess.run([
    'git', 'add', '--',
    str(round2_ppt),
    'l5/BUILD_REPORT_STAGE2_ROUND2.md',
    'l5/stage2_round2_assets',
    'l5/stage2_visual_review_round2'
], check=True)
print('stage2 round2 outputs staged for commit')
