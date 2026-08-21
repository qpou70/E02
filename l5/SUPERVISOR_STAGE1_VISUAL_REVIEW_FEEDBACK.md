# ECE340 L5 第一阶段返修——监工视觉复核反馈

## 一、结论

**第一阶段目前仍不通过。不要开始第二阶段。**

本轮监工不采用 Build Report 的“自检通过”作为验收依据，而是实际打开了以下提交中的 5 页最终渲染图与对照图：

- `page_09.png`
- `page_12.png`
- `page_18.png`
- `page_20.png`
- `page_23.png`
- `contact_sheet_stage1_pages_09_12_18_20_23.jpg`

阶段版相较上一版已经明显改善：红框贴纸、Placeholder、施工说明、页面出界和第 20 页错误公式问题已经消除。

### 本轮可冻结，不再改动

**第 9、18、20 页。**

除非后续 Microsoft PowerPoint 实机打开出现渲染异常，这三页在本阶段不得再次改动。

### 本轮仍需返修

**第 12、23 页。**

此外，当前“原页 vs 新页”对照图制作方式不合格，必须整体重做证据包。

---

## 二、第 12 页：小问题，但属于硬性信息丢失

当前第 12 页整体视觉已经基本合格：

- 标题清晰；
- 无红框贴纸；
- 左侧 MBE 束源—快门—分子束—GaAs 衬底关系清楚；
- 右侧使用了真实显微图；
- 无 Placeholder、无施工说明、无明显重叠。

但是右侧显微图的晶向信息没有按监工要求完整保留。

监工上一轮明确要求保留原图中的：

`4×4 / GaAs substrate / 10 nm / <100>`

当前渲染中右下角只看到 `100`，`< >` 没有保留下来；Build Report 自己也写成了：

`4×4 / GaAs Substrate / 10 nm / 100`

这说明不是单纯视觉缩放问题，而是在裁图/处理时已经把 `<100>` 的完整表示丢失。

### 第 12 页只允许做以下定点修复

1. 从原始讲义 PDF 第 12 页重新裁取右侧显微图；
2. 必须完整保留 `4×4`、`GaAs substrate`、`10 nm`、`<100>`；
3. 不允许改变左侧已经通过的 MBE 示意；
4. 不允许重新设计整页；
5. 返修后重新输出第 12 页高清渲染图。

---

## 三、第 23 页：重大不合格，过度简化了原页科学关系

当前第 23 页比上一版干净很多，也没有文字重叠，但**科学内容忠实度仍不合格**。

原始讲义第 23 页不是只有一个简单的分子轨道能级图。原页至少同时包含以下几组互相关联的信息：

1. `Elemental Hydrogen: 1s¹`、H #1 / H #2 / H₂ 的状态数与电子数；
2. 两个原子 `ψ1 / ψ2` 的原子轨道波函数示意；
3. 成键轨道与反键轨道的波函数/电子密度分布，并明确说明：
   - electron located between hydrogen atoms → lower energy / bonding；
   - electron not located between hydrogen atoms → higher energy / antibonding；
4. 原子靠近后形成两个 LCAO 的关系；
5. `V(r)` 势能/能级关系图；
6. `Bonding energy level` 与 `Antibonding energy level`；
7. 原页 Figure 3.2 所表达的“两个原子轨道线性组合形成两个不同能量分子轨道”的完整逻辑。

当前新页只保留了：

- 状态数；
- 一个简化的 σ1s / σ*1s 能级图；
- 两个简化的电子密度示意。

**但原页中的 `ψ1 / ψ2` 原子轨道图、LCAO 形成关系、`V(r)` 势能关系以及 bonding/antibonding energy level 的来源关系都被删掉了。**

这违反了监工上一轮的硬性要求：

> 重绘不等于简化；不得用简化示意破坏原教学关系。

### 第 23 页必须重新返工

允许重新排版、中文化，但必须恢复原页的完整教学链条。至少需要在一页中明确表现：

**原子 1s 轨道（ψ1、ψ2） → 线性组合 → 成键/反键轨道 → 电子密度在两核之间/不在两核之间 → 能量降低/升高 → bonding/antibonding energy level。**

具体要求：

1. 保留 H #1 / H #2 / H₂ 的状态数和电子数；
2. 恢复 `ψ1 / ψ2` 原子轨道波函数关系；
3. 恢复成键与反键轨道的空间/电子密度对照；
4. 恢复 Higher Energy / Lower Energy 与“电子是否位于两核之间”的对应；
5. 恢复原页 LCAO / `V(r)` / bonding energy level / antibonding energy level 的关系；
6. 可以中文为主，必要英文术语小号括注；
7. 不允许用 3 个简单方框替代原页完整逻辑；
8. 不允许 Placeholder；
9. 不允许施工说明；
10. 不允许页面出界或文字重叠。

### 推荐版式

不要照搬原页杂乱布局，可以做成三栏或“左→中→右”的教学流程：

- 左：两个 H 原子的 1s / ψ1 / ψ2 + 状态数；
- 中：LCAO 与 bonding / antibonding 能级形成；
- 右：成键/反键电子密度 + Higher/Lower Energy；
- 底部：简化但不缺失的 `V(r)` / bonding energy / antibonding energy 关系。

重点是**关系完整，而不是图画得复杂**。

---

## 四、当前证据包不合格：所谓“原页 vs 新页”实际上是“旧返修页 vs 新页”

当前 `comparison/` 目录中的图片左侧标题明确写的是：

`Baseline page 9 / 12 / 18 / 20 / 23`

而且左侧内容可以直接看出是上一轮中文返修页，不是原始讲义 PDF 页面。

但第一阶段交付要求明确要求的是：

**原始 PDF 页 vs 新返修页。**

Build Report 当前却把 `comparison/` 写成“原页 vs 新页对照目录”，这一表述不准确。

### 必须重做 comparison

对第 9、12、18、20、23 页分别使用：

`l5/stage1_source_reference/ECE340_L5_S18_Posted.pdf`

中的真实原始页面作为左图，新阶段版作为右图。

输出：

- `page_09_original_pdf_vs_new.jpg`
- `page_12_original_pdf_vs_new.jpg`
- `page_18_original_pdf_vs_new.jpg`
- `page_20_original_pdf_vs_new.jpg`
- `page_23_original_pdf_vs_new.jpg`

左侧必须是真实原始 PDF 页面，不能再使用 baseline / 上一版 PPT。

---

## 五、Build Report 需要同步纠正

当前 Build Report 最后一段写：

> 第一阶段五页返修通过本轮自检

这个“自检通过”只能代表干活 AI 自己检查，不代表监工验收。

下一次报告请明确区分：

- `Worker self-check: passed/failed`
- `Supervisor visual acceptance: pending`

在监工明确回复“第一阶段通过”之前，不得写：

- “阶段验收通过”
- “最终通过”
- “可以开始第二阶段”

---

## 六、下一轮执行范围

下一轮只允许：

1. 定点修复第 12 页 `<100>`；
2. 重新完整返修第 23 页；
3. 重做 5 页真实“原始 PDF vs 新页”对照图；
4. 更新 contact sheet；
5. 更新 Build Report。

**第 9、18、20 页冻结。第 8、10、11、13、14、15、16、17、19、21、22、24 页仍不得改动。**

完成后再次提交：

- 新阶段 PPTX；
- 第 12、23 页高清渲染图；
- 5 张真实 original-PDF-vs-new 对照图；
- 更新后的 contact sheet；
- 更新后的 Build Report；
- commit SHA。

在上述内容通过监工视觉复核之前，**禁止开始第二阶段。**
