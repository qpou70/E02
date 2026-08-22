# ECE340 L5 R3 图像重建监工复核（Round 2）

## 0. 结论

当前 R3 **不通过**。

本轮检查对象：

- `ECE340_L5_S18_Posted_中文忠实重建_最终候选版_R3_第8-24页.pptx`
- 第 20 / 22 / 23 页中文整页图及对照图
- 生成脚本 `l5/final_qa_image_rebuild_20_22_23.py`

最重要的问题不是个别文字，而是：**上一轮要求使用 GPT / image generation 做“整页英文→中文、科学图保持不变”的图像重建，但实际执行没有使用 image generation，而是用 PIL/ImageDraw 在原页上画大量白色矩形，再覆盖中文文字。**

该方法正是前几轮反复产生遮挡、残留英文、图形缺失的根源，因此本轮必须停止继续沿用。

当前状态：

- Supervisor visual acceptance: **NOT PASSED**
- Final acceptance: **REOPENED / NOT PASSED**

---

# 1. 方法层面：当前 R3 实际没有执行“GPT 生图重建”

`l5/final_qa_image_rebuild_20_22_23.py` 中使用的是：

- `PIL.Image`
- `ImageDraw.rectangle(...)`
- 白色矩形覆盖英文
- 再用 `draw.text(...)` 写入中文

这不是上一轮要求的 GPT/image generation 图像重建。

因此以下行为本轮明确禁止：

- 用 `ImageDraw.rectangle` 大面积盖白；
- 用灰块/白块覆盖原图文字；
- 用 PIL/OpenCV 脚本模拟“生图”；
- 如果 image generation 工具不可用，就偷偷退化成白块覆盖方案；
- 在科学图内部进行高风险像素级遮挡。

如果当前执行环境没有真实 image generation / image editing 能力：

> **立即停止，明确报告“当前环境无 image generation 能力”，不得用 PIL 白块方案替代。**

---

# 2. 第20页当前 R3 问题

当前 R3 第20页仍不合格。

实际可见问题：

1. 顶部仍残留原英文正文片段：
   - `The sp³ hybrids are ...`

2. 原英文图内标签仍部分可见，与中文形成重复：
   - `1 s-orbital`
   - `3 p-orbitals`
   - `4 sp³-orbitals`
   - `109.5° Bond ...`
   - `Tetrahedral geometry`

3. 白色矩形覆盖区域与原科学图边界发生干涉，尤其 109.5° / 四面体区域存在明显“补丁感”。

4. 这并没有实现“英文全部中文化、科学图保持不变”，而是“原图 + 白块 + 中文叠加”。

## 第20页下一轮正确目标

必须使用 **真实 image generation / image editing**，以 Original PDF 第20页整页图作为参考图进行编辑：

- 科学轨道图、四条公式、四面体图、箭头、109.5°关系保持原结构；
- 公式中的 `ψ1–ψ4`、`ψs`、`ψpx`、`ψpy`、`ψpz`、`1/2`、正负号必须保持完全正确；
- 所有解释性英文转成中文；
- 不留下任何英文残片；
- 不使用白块遮挡；
- 输出必须是一张视觉上自然、完整、没有修补痕迹的中文整页图。

---

# 3. 第22页当前 R3 问题

当前 R3 第22页仍不合格。

实际可见问题：

1. 页面左上仍残留原英文正文片段：
   - `Streetman’s book, and this ...`

2. 右侧 E-k 图中的解释性英文仍大面积保留：
   - `X-valley`
   - `Γ-valley`
   - `L-valley`
   - `Wave vector`
   - `Heavy holes`
   - `Light holes`
   - `Split-off band`

3. 当前做法仍然是把左半原正文用大白块盖掉，再写中文；不属于真正的整页图像翻译。

4. 虽然 E-k、晶格、显微结构和蝴蝶图大体仍在，但“英文全部变中文”的目标没有实现。

## 第22页下一轮正确目标

使用真实 image generation / image editing，以 Original PDF 第22页作为参考图。

必须完整保留：

- E-k 曲线本体；
- `Ex / Eg / EL / Eso` 等符号；
- `<100> / <111>`；
- 晶格图；
- 显微结构图；
- 蝴蝶图；
- 蓝色箭头及图间类比关系。

允许保留不可翻译的科学符号，但解释性英文应中文化，例如：

- `Energy` → `能量`
- `Wave vector` → `波矢`
- `X-valley` → `X 谷`
- `Γ-valley` → `Γ 谷`
- `L-valley` → `L 谷`
- `Heavy holes` → `重空穴`
- `Light holes` → `轻空穴`
- `Split-off band` → `自旋–轨道分裂带`

必须做到：

> 科学曲线和结构不变，解释性英文自然地变成中文，而不是白块覆盖。

---

# 4. 第23页当前 R3 问题（最严重）

当前 R3 第23页 **严重不合格**。

实际可见问题包括：

1. 原英文标题残片仍从中文蓝色标题条上方露出。

2. 大量英文教学文字仍然存在：
   - `Elemental Hydrogen: 1s¹`
   - `Electron not located between hydrogen atoms`
   - `Atomic orbitals`
   - `Bonding orbital`
   - `Antibonding energy level`
   - `Figure 3.2`
   - 底部长段 LCAO 英文原文

3. 多处英文被白块切到一半，产生残缺字符和碎片。

4. 右侧出现孤立异常字符/残片，例如：
   - `y`
   - `L`
   - `located b...`

5. 页面存在明显“白块修补”痕迹，且白块靠近轨道曲线、箭头、能级线，风险极高。

6. 当前结果与用户此前在 ChatGPT 直接使用 image generation 得到的第23页中文图相比，质量明显更差。

## 第23页下一轮正确目标

必须完全停止 PIL 白块覆盖方案。

以 Original PDF 第23页整页作为参考图，通过真实 image generation / image editing：

- 保持 `ψ1 / ψ2` 原子轨道曲线；
- 保持分支箭头；
- 保持成键 / 反键轨道曲线；
- 保持 Higher / Lower Energy 的能量关系；
- 保持左下成键 / 反键电子密度图；
- 保持中央完整 `V(r)` 势阱；
- 保持 bonding / antibonding energy level 引线；
- 保持 LCAO 教学逻辑；
- 只把英文自然改成中文；
- 不得出现任何白块、残缺英文、孤立字母或人工拼接痕迹。

建议中文：

- `Atomic orbitals` → `原子轨道`
- `Antibonding orbital` → `反键轨道`
- `Bonding orbital` → `成键轨道`
- `Higher Energy` → `较高能量`
- `Lower Energy` → `较低能量`
- `Electron not located between hydrogen atoms` → `电子不位于两个氢原子之间`
- `Electron located between hydrogen atoms` → `电子位于两个氢原子之间`
- `Antibonding energy level` → `反键能级`
- `Bonding energy level` → `成键能级`

---

# 5. 下一轮流程必须拆成两个阶段

为了避免再次“生成图 + 装 PPT + 自己验收”一次性完成导致问题被带进 PPT，本轮必须拆开。

## Stage A：只生成三张候选中文图

只生成：

- `page_20_cn_candidate.png`
- `page_22_cn_candidate.png`
- `page_23_cn_candidate.png`

要求：

- 必须来自真实 image generation / image editing；
- 必须以 Original PDF 对应页作为参考图；
- 不修改 PPT；
- 不修改 Notes；
- 不提交新的 R4 PPT；
- 生成后立即停止，等待 supervisor 先看三张候选图。

### Stage A 的硬性停止条件

如果 image generation / image editing 工具不可用：

- 不生成任何替代图；
- 不调用 PIL/OpenCV 白块覆盖；
- 不改 PPT；
- 直接报告能力不可用并停止。

## Stage B：只有 supervisor 明确通过三张候选图后再做

Stage B 才允许：

- 把三张审核通过的中文图整页放入第20、22、23页；
- 生成新的 PPT；
- 渲染三页；
- 做 Original PDF vs New Page 对照；
- 保持 Notes 不变。

**未经 supervisor 对 Stage A 三张图片明确通过，禁止进入 Stage B。**

---

# 6. 本轮当前 Worker 任务（只做 Stage A）

Worker 只负责生成三张候选中文图，不负责 PPT 装配。

最终必须回复：

- `page_20_cn_candidate.png` 路径
- `page_22_cn_candidate.png` 路径
- `page_23_cn_candidate.png` 路径
- 实际使用的生成方式：必须明确写 `image generation / image editing`
- 是否使用 PIL/OpenCV 白块覆盖：必须写 `否`
- Supervisor visual acceptance: `pending`

Worker 不得自行宣布：

- visual passed
- final acceptance passed
- 最终验收通过

---

# 7. Notes 暂停

第8–24页 Notes 字数问题仍然存在，但本轮不要处理。

Notes 阶段必须等第20/22/23页视觉通过并装配 PPT 后再单独执行。

---

# 8. 邮件通知

Stage A 三张候选图真实生成完以后，如当前环境有已连接且已授权的 Gmail / Email 工具，发送到：

`849812169@qq.com`

主题：

`ECE340 L5 第20/22/23页 image-generation 候选图已生成，等待 supervisor 检查`

正文必须说明：

- 本轮只完成 Stage A；
- 只生成三张候选中文图；
- 尚未修改 PPT；
- 尚未获得 supervisor visual acceptance；
- 三张候选图路径。

不得写“最终验收通过”。
