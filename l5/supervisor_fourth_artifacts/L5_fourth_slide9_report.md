# Slide 9 fourth revised inspection

Slide size: 10.00 x 7.50 in

- shape 0: type=AUTO_SHAPE (1); box=(0.00,0.00,10.00,1.08); text=''
- shape 1: type=AUTO_SHAPE (1); box=(0.00,1.08,10.00,0.16); text=''
- shape 2: type=AUTO_SHAPE (1); box=(0.28,0.22,9.35,0.68); text='硅的气相外延（Silicon VPE）'
- shape 3: type=AUTO_SHAPE (1); box=(9.30,7.12,0.45,0.24); text='9'
- shape 4: type=AUTO_SHAPE (1); box=(0.32,7.12,2.20,0.24); text='原 PDF 第 9 页'
- shape 5: type=AUTO_SHAPE (1); box=(0.42,1.42,2.20,0.35); text='VPE 方法'
- shape 6: type=AUTO_SHAPE (1); box=(0.42,1.86,5.40,0.32); text='氯化物：  SiCl₄ + 2H₂ ⇌ Si + 4HCl'
- shape 7: type=AUTO_SHAPE (1); box=(0.42,2.24,5.40,0.32); text='硅烷热分解：  SiH₄ → Si + 2H₂'
- shape 8: type=PICTURE (13); box=(0.55,3.05,1.45,1.85); text=''
- shape 9: type=AUTO_SHAPE (1); box=(0.46,4.96,1.70,0.24); text='原设备照片'
- shape 10: type=PICTURE (13); box=(2.55,2.82,3.75,2.60); text=''
- shape 11: type=AUTO_SHAPE (1); box=(2.85,5.48,3.35,0.25); text='VPE 桶式反应器示意'
- shape 12: type=AUTO_SHAPE (1); box=(2.30,6.20,5.80,0.42); text=''
- shape 13: type=AUTO_SHAPE (1); box=(2.36,6.24,5.68,0.34); text='气相反应 + 均匀气流 + 加热承载 = 外延均匀性'
- shape 14: type=TEXT_BOX (17); box=(5.25,2.04,1.15,0.28); text='气体入口 | Gas inlet'
- shape 15: type=TEXT_BOX (17); box=(6.75,2.58,1.35,0.28); text='挡流板 | Gas baffle'
- shape 16: type=TEXT_BOX (17); box=(7.22,3.05,1.45,0.28); text='石英反应腔'
- shape 17: type=TEXT_BOX (17); box=(5.78,3.25,1.00,0.28); text='硅片 | Wafers'
- shape 18: type=TEXT_BOX (17); box=(7.25,3.72,1.20,0.28); text='基座盘 | Susceptor'
- shape 19: type=TEXT_BOX (17); box=(7.23,4.90,1.15,0.28); text='支座 | Pedestal'
- shape 20: type=TEXT_BOX (17); box=(5.72,5.25,0.92,0.25); text='排气口 | Vent'
- shape 21: type=TEXT_BOX (17); box=(3.62,3.75,1.35,0.35); text='射频源 | RF source'

## Required-content checks

- old text absent [关键标签中英对应]: True
- old text absent [Wafers 晶圆]: True
- old text absent [承载/加热基座]: True
- old text absent [Pedestal 支撑台]: True
- old text absent [• Vent 排气口]: True
- required present [气体入口]: True
- required present [挡流板]: True
- required present [石英反应腔]: True
- required present [硅片]: True
- required present [基座盘]: True
- required present [支座]: True
- required present [排气口]: True
- required present [射频源]: True
- required present [SiCl₄ + 2H₂ ⇌ Si + 4HCl]: True
- required present [SiH₄ → Si + 2H₂]: True

## Text-text geometric overlaps

- overlap shape 6 vs 14: ratio/min=0.25; A='氯化物：  SiCl₄ + 2H₂ ⇌ Si + 4HCl'; B='气体入口 | Gas inlet'

## Notes

这一页具体看硅的气相外延，也就是 Silicon VPE。请先看上方两条反应式。第一条读作：四氯化硅加两分子氢气，可以可逆生成硅和四分子氯化氢，SiCl4 + 2H2 ⇌ Si + 4HCl。可逆箭头提醒我们，反应条件、温度和气体分压会影响沉积与刻蚀的平衡。第二条读作：硅烷热分解，SiH4 → Si + 2H2，它更直接地把硅烷分解为硅和氢气。再看右侧设备示意图，观察顺序是从上方进气口进入，经过气体挡板分配气流，气体进入石英反应腔；中间倾斜的托盘上放置 wafers，也就是晶圆；susceptor 是承载并被射频源加热的基座；底部 pedestal 支撑旋转或定位结构，最终气体从 vent 排出。左侧设备照片保留原来源，帮助大家把抽象示意和真实装备联系起来。课堂问题是：为什么要用气体挡板和特殊托盘形状？参考答案是为了改善气流均匀性，让晶圆不同位置的反应物浓度和温度尽量一致，否则外延层厚度和掺杂都会不均匀。半导体制造中的安全责任也很突出，因为氯化物、氢气和硅烷都需要严格的尾气处理和防爆设计。下一页转到 MOCVD 的早期系统。

[Sources]
ECE340_L5_S18_Posted.pdf, original page 9
教材：《固态电子器件》第七版；原页设备网址：http://www.hitachi-kokusai.co.jp/global/products/semicon/batch/epi.html。

## XML freeze check

- slide 8: same=True
- slide 9: same=False
- slide 10: same=True
- slide 11: same=True
- slide 12: same=True
- slide 13: same=True
- slide 14: same=True
- slide 15: same=True
- slide 16: same=True
- slide 17: same=True
- slide 18: same=True
- slide 19: same=True
- slide 20: same=True
- slide 21: same=True
- slide 22: same=True
- slide 23: same=True
- slide 24: same=True