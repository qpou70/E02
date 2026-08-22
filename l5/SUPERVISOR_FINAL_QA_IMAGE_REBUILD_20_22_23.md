# ECE340 L5 Final QA：第20/22/23页改用整页中文图重建

## 0. 本轮策略变更

此前第20、22、23页采用 PPT 内部裁图、文本框覆盖、白/灰遮罩等方式返修，导致原科学图出现遮挡、裁切、缩减或局部缺失。

本轮正式改用新策略：

> 以 Original PDF 对应页为视觉参考，分别生成第20、22、23页的高分辨率“整页中文图片”，要求科学示意图、公式、曲线、箭头、能级、结构关系保持不变，只把英文教学文字翻译成中文；然后把三张整页中文图作为整页图片装配回 PPT 对应页。

本轮 **明确允许使用 GPT 图像生成/图像编辑能力**，仅限第20、22、23页。该许可覆盖此前“禁止生图”的旧规则。

如果当前执行环境没有可用的图像生成/图像编辑能力，则必须停止并报告，不能退回到白块覆盖或裁图拼接旧方案。

---

## 1. 当前基准

唯一基准 PPT：

`l5/ECE340_L5_S18_Posted_中文忠实重建_最终候选版_R2_第8-24页.pptx`

对应 generation commit：

`3d888e10ca0d4fbb21ea14d50c42c21ab7122226`

Original PDF：ECE340 L5 原始英文课件，对应第20、22、23页。

本轮只允许改变第20、22、23页视觉内容。

其他所有页视觉冻结。

本轮禁止修改任何 Notes。

---

# 2. 总体生成原则

对第20、22、23页分别独立生成一张整页中文图。

要求：

1. 版式尽可能忠实于 Original PDF；
2. 科学图、公式、曲线、箭头、能级、轨道、势阱、晶格等结构关系必须保留；
3. 英文教学文字、标题、图注、说明文字翻译成中文；
4. 标准科学符号、变量、公式允许保留英文/拉丁字母，例如 `ψ`、`ΔE`、`E-k`、`Γ`、`X`、`L`、`<100>`、`<111>`；
5. 不得因中文化而重新解释、简化或改写科学关系；
6. 不得新增 Original PDF 没有的科学内容；
7. 不得出现白色/灰色矩形遮挡科学图；
8. 不得出现 Placeholder、施工说明或返修说明；
9. 必须高分辨率输出，适合整页铺入 PPT 后保持清晰。

生成前应先完整查看 Original PDF 对应页，再做图像编辑/重建。

---

# 3. 第20页：sp³ Hybridization

## 必须保留的科学内容

- 1 个 s orbital；
- 3 个 p orbitals；
- 4 个 sp³ orbitals；
- 加号与箭头关系；
- 四条公式 `ψ1`、`ψ2`、`ψ3`、`ψ4`；
- 每条公式中的 `1/2` 系数；
- `ψs`、`ψpx`、`ψpy`、`ψpz`；
- 每一项正负号必须和 Original PDF 一致；
- 109.5° 键角；
- 完整四面体几何图；
- 四个 sp³ 叶瓣和原方向关系。

## 中文化要求

可将下列英文教学文字翻译为中文：

- `The sp³ hybrids are obtained by adding and subtracting all combination of s and p wavefunctions`
  → `sp³ 杂化轨道由 s 与 p 波函数的不同加减组合得到。`

- `1 s-orbital`
  → `1 个 s 轨道`

- `3 p-orbitals`
  → `3 个 p 轨道`

- `4 sp³-orbitals`
  → `4 个 sp³ 杂化轨道`

- `109.5° Bond Angle`
  → `109.5° 键角`

- `Tetrahedral geometry`
  → `四面体几何`

- `Comments:` 及其后说明
  → 使用自然、简洁中文表达，但不得改科学含义。

## 红线

四条公式本身禁止由模型重新“理解后改写”。必须与 Original PDF 逐字符核对。

---

# 4. 第22页：Periodic Potential / E-k Relation

## 必须完整保留

- E-k 图；
- Energy 轴；
- Wave vector；
- X-valley；
- Γ-valley；
- L-valley；
- Ex / Eg / EL / Eso；
- `<100>` / `<111>`；
- Heavy holes；
- Light holes；
- Split-off band；
- 晶格结构图；
- 显微 / 周期微结构图；
- 蝴蝶图；
- 原页中表示类比/对应关系的蓝色箭头或指向关系。

## 中文化原则

标题、正文说明、图外文字全部中文化。

图内专业术语如果能够准确替换，可以翻译；如果翻译会导致 E-k 曲线、标签位置或箭头关系失真，则优先保留图内标准英文标签，在图外增加中文解释。

必须保证标签仍清晰可读，不能因为整体缩小而无法辨认。

---

# 5. 第23页：Bonding / Antibonding Orbitals in H₂

## 必须完整保留

1. 左上 atomic orbitals：
   - `ψ1`
   - `ψ2`
   - 两个原子轨道曲线

2. 从 atomic orbitals 分支到：
   - antibonding orbital
   - bonding orbital
   的箭头关系

3. 右上两组波函数：
   - 反键轨道曲线
   - 成键轨道曲线
   - Higher Energy / Lower Energy
   - electron not located between hydrogen atoms
   - electron located between hydrogen atoms

4. 左下两个电子密度 / 轨道组合图：
   - antibonding
   - bonding

5. 中央 `V(r)` 势阱图：
   - 完整势能曲线；
   - 虚线辅助曲线；
   - bonding energy level；
   - antibonding energy level；
   - 对应引线。

6. LCAO 教学逻辑完整。

## 中文化建议

- Bonding orbital → 成键轨道
- Antibonding orbital → 反键轨道
- Higher Energy → 较高能量
- Lower Energy → 较低能量
- Electron not located between hydrogen atoms → 电子不位于两个氢原子之间
- Electron located between hydrogen atoms → 电子位于两个氢原子之间
- Bonding energy level → 成键能级
- Antibonding energy level → 反键能级

`ψ1`、`ψ2`、`V(r)`、LCAO 等标准符号保持。

不得为了中文化改变曲线、势阱、能级线、箭头或轨道形状。

---

# 6. 图像生成后的强制核对

对每一页生成图，必须先和 Original PDF 原页并排检查，再装入 PPT。

逐项核对：

- 原页有几个科学子图，新图必须一个不少；
- 原页所有关键曲线必须存在；
- 原页所有箭头关系必须存在；
- 原页公式必须无误；
- 原页关键标签对应关系必须正确；
- 无文字压住科学图；
- 无图被裁掉；
- 无大块白/灰遮罩；
- 无模型自行新增的虚构结构；
- 中文文字无乱码、错别字和明显断句。

如果发现科学关系错了，应重新生成该页，而不是在 PPT 中用白块补丁修。

---

# 7. 装配回 PPT

生成 3 张整页中文图后：

- 第20页：用 `page_20_cn.png` 整页铺满；
- 第22页：用 `page_22_cn.png` 整页铺满；
- 第23页：用 `page_23_cn.png` 整页铺满；
- 保持原 PPT 页面尺寸；
- 图片不得拉伸变形；
- 图片边缘与页面边缘对齐；
- 不再在这三页上叠加额外 PPT 文本框去二次覆盖；
- 其他页保持完全不动；
- 本轮所有 Notes 保持不动。

---

# 8. 本轮输出

必须生成并提交：

1. 新 PPT：
   `l5/ECE340_L5_S18_Posted_中文忠实重建_最终候选版_R3_第8-24页.pptx`

2. 三张整页中文图：
   - `page_20_cn.png`
   - `page_22_cn.png`
   - `page_23_cn.png`

3. PPT 导出的三张最终渲染图：
   - `page_20.png`
   - `page_22.png`
   - `page_23.png`

4. 三张 Original PDF vs R3 对照图；

5. 一个只包含第20、22、23页的 contact sheet；

6. 简洁 Build Report；

7. generation commit SHA；

8. current branch HEAD。

---

# 9. Worker 权限边界

Worker 只负责施工和生成证据。

Worker 不得自行宣布：

- `visual passed`
- `final acceptance passed`
- `最终验收通过`

完成提交后必须停止，等待 supervisor。

最终状态只能写：

`第20、22、23页整页中文图已生成并装配回 PPT，视觉证据已提交，等待 supervisor 检查。`

---

# 10. 本轮禁止

- 禁止修改第20、22、23页以外任何视觉页面；
- 禁止修改任何 Notes；
- 禁止使用 Canvas / Work / Writing Block / Placeholder；
- 禁止退回白块覆盖、局部裁图拼接方案；
- 禁止用简化示意图替代 Original PDF 科学图；
- 禁止为了追求美观改动公式、曲线或科学关系。

---

# 11. 后续 Notes 阶段

Notes 字数问题已经在：

`l5/SUPERVISOR_FINAL_QA_REOPENED_VISUAL_NOTES.md`

中记录。

本轮不要处理 Notes。

等第20、22、23页视觉经 supervisor 通过后，再单独开一个纯 Notes 轮次。

---

# 12. 邮件通知

在 GitHub 中完成新 PPT、三张中文整页图、三张渲染图、三张对照图、contact sheet、Build Report 和 commit 后，如当前环境有已连接且已授权的 Gmail / Email 工具，发送邮件到：

`849812169@qq.com`

主题：

`ECE340 L5 第20/22/23页整页中文图已生成，等待 supervisor 检查`

正文至少包括：

- 本轮只修改第20、22、23页；
- 使用“整页中文图 + 装配回PPT”策略；
- 新 PPT 完整 GitHub 路径；
- generation commit SHA；
- current branch HEAD；
- Supervisor visual acceptance: pending。

邮件不得写“最终验收通过”。
