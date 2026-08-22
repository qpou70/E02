# ECE340 L5 第二阶段 ROUND4：第五轮视觉监工意见

## 1. 总结论

当前检查文件：

`l5/ECE340_L5_S18_Posted_中文忠实重建_第二阶段视觉返修ROUND4_第16页.pptx`

对应 generation commit：

`0ed84630242c4d63c3544c807f4ddd1253e1bbee`

本轮 supervisor 已从 GitHub Actions artifact 只读取回 ROUND4 的：

- `page_16.png`
- `page_16_original_pdf_vs_new_round4.jpg`
- contact sheet
- build report
- ROUND4 PPTX

并实际打开最终高清渲染图与 Original PDF 对照图进行肉眼视觉检查。

结论：**ROUND4 仍不能最终通过，但现在只剩第 16 页金属键科学图的视觉清洁问题。第 16 页的科学内容已经基本正确，不允许再扩大返工。**

### 已经正确，不得回退

- 左侧四类键合中文说明完整；
- 原来整套英文 bullet list 已删除；
- 三幅 `ΔE` 电子云图已经分别补回：
  - `ΔE = 0（共价键）`
  - `ΔE 中等（极性共价键）`
  - `ΔE 较大（离子键）`
- `Two electrons per bond` 已中文化为 `每个键由两个电子共享`；
- `Swarm of delocalised electrons` 已中文化为 `离域电子海`；
- 没有原 PDF 顶部橙色标题条；
- 没有大段英文正文重新进入页面。

这些内容已经通过，不得重新设计。

---

## 2. 第 16 页唯一剩余不合格点：金属键图区仍有明显“遮盖补丁”痕迹

实际 `page_16.png` 中，右下“金属键”科学图仍存在明显的视觉污染：

1. 图的右下区域有一个很大的浅灰色矩形遮盖块，遮住了原图下边缘的一部分，肉眼非常明显；
2. 图上方仍残留原图内部英文标题 `Metallic Bonding`；
3. `Metallic Bonding` 下方还有一条大块灰白空白带，与下面实际金属键科学图分离，视觉上像被粗暴裁切/遮挡后的残片；
4. 当前做法虽然把英文 `Swarm of delocalised electrons` 用遮盖方式消掉了，但遮盖块本身成为新的明显错误。

这属于典型的：

> 文本内容修对了，但最终渲染图出现肉眼可见的修补痕迹。

本项目以最终视觉稿为第一验收标准，因此不能放行。

---

## 3. 第 16 页下一轮正确处理方式

### 只处理金属键科学图，其他全部冻结

不得重新调整左侧四个框。

不得重新调整三幅 `ΔE` 图。

不得重新调整离子键/共价键晶格图。

不得重新调整标题、字体、页边距和整体布局。

### 推荐做法：重新干净裁取原 PDF 金属键科学图的“真正科学内容区域”

从原 PDF 第 16 页原始 Metallic Bonding 图中，只提取：

- 左侧正离子实 + 小橙色离域电子；
- 中央红色箭头；
- 右侧电子云中的正离子实；
- 原图必要的结构关系。

不要把以下内容一起裁进新图：

- 原英文标题 `Metallic Bonding`；
- 原英文 `Swarm of delocalised electrons`；
- 原图底部英文长段说明；
- 原图边框之外的空白；
- 任何灰色遮盖块。

然后在新页中：

- 上方保留现有中文标题：`金属键：正离子实 + 离域电子海`；
- 图下方保留中文：`离域电子海`；
- 如需要指向电子云，可使用已有箭头关系，但不要新增多余红框或补丁。

### 禁止的做法

不得继续：

- 用大块白色/灰色矩形盖住原英文；
- 在科学图上放明显遮罩块；
- 把 `Metallic Bonding` 留在图里再在外面重复中文；
- 重画金属键科学关系；
- 调用 image generation；
- 用 Placeholder；
- 把整块原 PDF 再塞回右侧。

目标应该是：

> 一张干净的金属键科学图 + 中文标题 + 中文说明，看不出任何“修补覆盖”痕迹。

---

## 4. 本轮范围必须锁死

### 只允许修改

- 第 16 页中的右下金属键图区域。

### 绝对冻结

- 第 16 页其余区域；
- 第 8–15 页；
- 第 17–24 页；
- 第 1–7 页；
- 第 25–52 页。

如果下一轮除了第 16 页金属键图区之外又发生布局变化，视为扩大任务范围，直接失败。

---

## 5. 提交前强制视觉检查

生成最终 `page_16.png` 后，必须真正打开 PNG 肉眼检查，不得只看 XML/assert/build report。

必须确认：

1. 右下金属键科学图中没有任何大块灰色/白色遮盖矩形；
2. 不再可见原图英文标题 `Metallic Bonding`；
3. 不再可见 `Swarm of delocalised electrons`；
4. 不再有英文长段图注；
5. 原科学图中左侧离域电子、正离子实、中间箭头、右侧电子云/正离子实均完整；
6. 中文标题 `金属键：正离子实 + 离域电子海` 清楚；
7. 中文 `离域电子海` 清楚；
8. 三个 `ΔE` 标签仍完整；
9. `每个键由两个电子共享` 仍完整；
10. 没有新遮挡、重叠、出界、残片。

只有 10 项全部满足，才允许提交“完成”。

---

## 6. 交付要求

下一轮生成：

1. 第二阶段 ROUND5 PPTX；
2. 第 16 页高清 PNG；
3. 第 16 页 `Original PDF vs New Page` 对照图；
4. ROUND5 contact sheet（如现有 workflow 统一生成则保留）；
5. ROUND5 build report；
6. generation commit SHA；
7. packaging / trigger commit SHA（如有）；
8. current branch HEAD。

不得进入最终合并阶段。

必须等待 supervisor visual acceptance。

---

## 7. Worker 最终回复格式：上一轮不合格，下一轮必须恢复完整报告

ROUND4 worker 的聊天回复只给了：

- “已完成第16页 ROUND4返修”
- generation commit SHA
- Current branch HEAD
- 邮件 ID

这不符合之前已锁定的交付原则，因为它没有告诉用户：

- 最终 PPT 完整路径；
- 渲染图路径；
- comparison 路径；
- contact sheet 路径；
- build report 路径；
- packaging / trigger commit；
- 冻结页确认；
- 等待 supervisor 检查的主文件到底是哪一个。

下一轮最终回复必须逐项完整报告，不允许再次缩写成 3–4 行。

必须严格使用：

```text
本轮任务状态：
已完成 / 未完成

本轮实际修改页面：
第 16 页（仅右下金属键图区）

冻结且确认未修改页面：
第 8–15、17–24 页；第 1–7、25–52 页

本轮生成的 PPT 文件：
`l5/完整ROUND5文件名.pptx`

高清渲染图：
`l5/.../page_16.png`

Original PDF vs New Page 对照图：
`l5/.../page_16_original_pdf_vs_new_round5.jpg`

Contact sheet：
`完整路径`
如没有则写：`无`

Build report：
`l5/完整文件路径.md`

真正生成 PPT 的 generation commit SHA：
`40位完整 SHA`

Packaging / trigger commit SHA：
`40位完整 SHA`
如没有则写：`无`

Current branch HEAD：
`40位完整 SHA`

等待 supervisor 检查的主文件就是：
`l5/完整ROUND5文件名.pptx`

视觉自检结果：
- 灰/白遮盖块：无
- `Metallic Bonding`：不可见
- `Swarm of delocalised electrons`：不可见
- 中文 `离域电子海`：可见
- 三个 ΔE 标签：完整
- 其他页面：未修改
```

---

## 8. 完成后邮件通知

GitHub 交付物、commit 和真实 PNG 视觉自检全部完成以后，若当前环境有已连接且已授权的 Gmail / Email 工具，必须向：

`849812169@qq.com`

发送邮件。

建议主题：

`ECE340 L5 第二阶段 ROUND5 返修完成，等待监工验收`

邮件正文至少包含：

- ROUND5 已完成；
- 本轮只改第 16 页右下金属键图；
- 最终 PPT 的完整 GitHub 路径；
- generation commit SHA；
- current branch HEAD；
- 等待 supervisor visual acceptance。

发送成功后，最终聊天回复必须同时写出邮件发送 ID。

如没有邮件发送工具，不得假装发送，也不得要求用户提供 QQ 邮箱授权码。
