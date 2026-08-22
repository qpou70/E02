# ECE340 L5 R3 Visual Review — Supervisor Round 3

## 0. 结论

当前归档到 `master` 的 R3 **仍不通过**。

本轮已实际检查 GitHub `master` 中的最终渲染证据：

- `l5/final_qa_image_rebuild_20_22_23/rendered/page_20.png`
- `l5/final_qa_image_rebuild_20_22_23/rendered/page_22.png`
- `l5/final_qa_image_rebuild_20_22_23/rendered/page_23.png`

并核对：

- R3 generation commit：`425c3f832d46d6238ffaf2c18cb40ea2b1f4ef47`
- 当前 `master` 归档 HEAD：`1a1b3331078d37929232c918cff451403e681b4f`
- 主文件：`l5/ECE340_L5_S18_Posted_中文忠实重建_最终候选版_R3_第8-24页.pptx`

Build Report 记录 R3 只修改第 20 / 22 / 23 页、Notes 未改、Supervisor acceptance 仍为 pending。

**关键判断：工作 AI 在其本地沙盒中可能确实生成过质量更好的 image-generation 图片，但归档到 GitHub/master 的并不是那三张最终图片。当前 master 中的三页渲染结果仍然是旧式“原页 + 覆盖/叠字”的坏版本。**

因此本轮不能继续把当前 master R3 当作合格候选版。

---

# 1. 第20页实际问题

GitHub `master` 当前 `page_20.png` 仍存在：

1. 顶部明显残留英文：`The sp³ hybrids are`。
2. 图中英文标签仍与中文重复：
   - `1 s-orbital`
   - `3 p-orbitals`
   - `4 sp³-orbitals`
   - `109.5° Bond...`
   - `Tetrahedral geometry`
3. `109.5°` / 四面体图区出现明显覆盖与断裂，科学图并未做到“保持不变”。
4. 页面中部还残留长网址，整体不属于自然生成的全中文页。

结论：第20页当前 GitHub 版本 **不通过**。

---

# 2. 第22页实际问题

GitHub `master` 当前 `page_22.png` 仍存在：

1. 中文标题下方露出原英文正文残片：`Streetman’s book, and this...`。
2. E-k 图内部仍大量保留英文解释性标签：
   - `X-valley`
   - `Γ-valley`
   - `L-valley`
   - `Wave vector`
   - `Heavy holes`
   - `Light holes`
   - `Split-off band`
3. 左侧中文与上方残留英文形成重复。
4. 该页没有达到“解释性英文自然中文化、科学图结构完整”的新策略目标。

结论：第22页当前 GitHub 版本 **不通过**。

---

# 3. 第23页实际问题（最严重）

GitHub `master` 当前 `page_23.png` 明显不合格：

1. 中文蓝色标题条上方仍露出原英文标题大段残片。
2. 顶部仍有 `Elemental Hydrogen: 1s¹` 残片。
3. 右上仍有完整英文：`Electron not located between hydrogen atoms`。
4. 科学图内部仍存在：
   - `Atomic orbitals`
   - `Bonding orbital`
   - `Antibonding energy level`
   等英文与中文叠加。
5. 出现明显孤立残缺字符：
   - `y`
   - `L`
   - `located b`
6. `Figure 3.2` 仍保留。
7. 底部原英文 LCAO 长句仍残留，并被中文段落再次重复。
8. `H₂` 显示发生异常（当前渲染中出现错误字符），说明生成/字体链还存在问题。

结论：第23页当前 GitHub 版本 **严重不通过**。

---

# 4. 根本原因：真正 image-generation 输出没有被原样归档

下一轮不要再“重新生成一次脚本版本”。

如果工作 AI 本地沙盒里已经存在真正由 image generation / image editing 生成、视觉质量更好的三张 PNG，那么下一步必须做的是：

> **把那三张“实际 PNG 字节”原样上传到 GitHub，先让 supervisor 检查图片本身。**

禁止：

- 再运行 `l5/final_qa_image_rebuild_20_22_23.py` 重新造图；
- 用 PIL/ImageDraw/OpenCV 重新合成；
- 由 workflow 根据 Original PDF 再做白块覆盖；
- 在上传前二次栅格化或重绘；
- 先装入 PPT 再由 PPT/LibreOffice 反向导出作为“候选图”。

本轮必须确保：GitHub 中的候选 PNG 与 image-generation 工具实际输出的 PNG 是 **同一份二进制文件**。

---

# 5. 下一轮只做 Stage A：上传三张真实 image-generation 原图

## 5.1 本轮禁止修改 PPT

不要生成 R4 PPT。

不要修改：

- 任何 slide；
- 任何 Notes；
- 任何原有 R3 PPT；
- 第20/22/23页以外任何文件内容。

## 5.2 只上传三张真实候选图

目标路径：

- `l5/final_qa_imagegen_stageA_round4/page_20_cn_candidate.png`
- `l5/final_qa_imagegen_stageA_round4/page_22_cn_candidate.png`
- `l5/final_qa_imagegen_stageA_round4/page_23_cn_candidate.png`

这三张文件必须是 **image generation / image editing 工具直接输出的原始 PNG**。

如果工作 AI 当前沙盒中已经有这三张图：

- 直接上传现有文件；
- 不重新生成；
- 不重新画；
- 不经过 PIL 二次修改。

如果当前沙盒中的图不是 image-generation 直接输出，则重新调用真实 image generation / image editing，生成后直接上传。

---

# 6. 二进制一致性校验（强制）

上传前对本地三张 PNG 分别计算 SHA-256。

上传 GitHub 后，再从 GitHub 下载同一文件，重新计算 SHA-256。

必须报告：

- local SHA-256
- GitHub-downloaded SHA-256

二者必须逐页完全一致。

若不一致：

- 不得继续；
- 不得装 PPT；
- 报告上传链发生变换。

可使用 GitHub 的 binary-safe 上传方式，例如：

- `create_blob`（base64）→ `create_tree` → `create_commit` → 更新工作分支；
- 或任何能够保证 PNG 原始字节不变的 GitHub 文件上传能力。

禁止把 PNG 转成文本后错误重编码。

---

# 7. Stage A supervisor 验收点

Supervisor 将只检查三张 GitHub 中的候选 PNG。

### 第20页
必须满足：

- 无 `The sp³ hybrids are` 残片；
- 无英文 `1 s-orbital / 3 p-orbitals / 4 sp³-orbitals` 重复；
- 四条公式完全正确；
- 四面体图完整；
- 109.5°关系完整；
- 没有白块/灰块修补痕迹。

### 第22页
必须满足：

- 无顶部英文正文残片；
- E-k 曲线完整；
- `Ex / Eg / EL / Eso / <100> / <111>` 等科学符号正确；
- 解释性标签自然中文化；
- 晶格图、显微结构图、蝴蝶图、箭头关系完整；
- 无大块覆盖或裁切。

### 第23页
必须满足：

- 无英文原标题残片；
- 无 `Elemental Hydrogen` 残片；
- 无 `y / L / located b` 等孤立字符；
- `H₂` 正确显示；
- ψ1 / ψ2、成键/反键轨道曲线完整；
- V(r) 势阱及能级线完整；
- LCAO 教学关系完整；
- 无英文长段与中文长段重复；
- 无白块/灰块补丁。

---

# 8. Stage B 暂停

只有 supervisor 明确回复三张 Stage A 候选图全部通过后，才允许进入 Stage B：

- 把通过的三张 PNG 原样装入 PPT 第20/22/23页；
- 生成新的 R4 PPT；
- 渲染；
- 做 Original PDF vs R4 comparison。

未经 supervisor 明确通过，禁止进入 Stage B。

---

# 9. Notes 阶段继续暂停

第8–24页 Notes 字数不足问题仍存在，但本轮完全不处理。

待第20/22/23页视觉最终通过以后，再单独开 Notes 补写阶段。

---

# 10. Worker 最终回复格式

Stage A 完成后只允许报告：

- 第20页候选图 GitHub 路径；
- 第22页候选图 GitHub 路径；
- 第23页候选图 GitHub 路径；
- 三张图各自 local SHA-256；
- 三张图各自 GitHub-downloaded SHA-256；
- 实际生成方式：`image generation / image editing`；
- 是否使用 PIL/ImageDraw/OpenCV：`否`；
- 是否修改 PPT：`否`；
- 是否修改 Notes：`否`；
- commit SHA；
- current branch HEAD；
- Supervisor visual acceptance：`pending`。

不得自行写：

- visual passed
- final acceptance passed
- 最终验收通过

---

# 11. 邮件通知

Stage A 三张真实候选 PNG 上传 GitHub、SHA-256 双向校验完成后，如环境有已连接且已授权的 Gmail / Email 工具，发送到：

`849812169@qq.com`

主题：

`ECE340 L5 第20/22/23页真实 image-generation 候选图已上传，等待 supervisor 检查`

正文至少包含：

- 本轮只完成 Stage A；
- 尚未修改 PPT；
- 三张 GitHub 候选图路径；
- 对应 SHA-256 一致性结果；
- commit SHA / current branch HEAD；
- Supervisor visual acceptance: pending。

不得写“最终验收通过”。
