# ECE340 L5：第二阶段视觉验收通过 + 最终综合 QA 指令

## 1. Supervisor 结论

当前检查文件：

`l5/ECE340_L5_S18_Posted_中文忠实重建_第二阶段视觉返修ROUND5_第16页.pptx`

对应 generation commit：

`21591dee5cbb6088e7df243c9c761a33ffa28fdf`

本轮 supervisor 已从 GitHub Actions artifact 只读取得并实际打开：

- `l5/stage2_visual_review_round5/rendered/page_16.png`
- `l5/stage2_visual_review_round5/comparison/page_16_original_pdf_vs_new_round5.jpg`
- ROUND5 contact sheet
- ROUND5 build report
- ROUND5 PPTX

并以最终高清渲染图为第一验收标准，与 Original PDF 第 16 页并排检查。

**结论：ROUND5 第 16 页通过 supervisor visual acceptance。第二阶段视觉返修通过。**

第 16 页右下金属键图区目前已经达到本轮要求：

- ROUND4 中明显的大块灰/白遮盖补丁已消失；
- 原图英文标题 `Metallic Bonding` 不再出现在科学图区；
- `Swarm of delocalised electrons` 不再可见；
- 金属键科学关系完整：左侧正离子实与橙色离域电子、中央箭头、右侧电子云中的正离子实均保留；
- 中文标题 `金属键：正离子实 + 离域电子海` 清楚；
- 中文 `离域电子海` 清楚；
- 三个 `ΔE` 标签完整：
  - `ΔE = 0（共价键）`
  - `ΔE 中等（极性共价键）`
  - `ΔE 较大（离子键）`
- `每个键由两个电子共享` 完整；
- 未发现明显文字重叠、出界、残片或新遮挡。

因此：**第 16 页冻结，不得再返修。**

---

## 2. 第 8–24 页当前冻结状态

经过前序多轮 supervisor 逐页视觉检查，目前第 8–24 页全部进入冻结状态：

- 第 8 页：通过，冻结
- 第 9 页：通过，冻结
- 第 10 页：通过，冻结
- 第 11 页：通过，冻结
- 第 12 页：通过，冻结
- 第 13 页：通过，冻结
- 第 14 页：通过，冻结
- 第 15 页：通过，冻结
- 第 16 页：ROUND5 通过，冻结
- 第 17 页：通过，冻结
- 第 18 页：通过，冻结
- 第 19 页：通过，冻结
- 第 20 页：通过，冻结
- 第 21 页：通过，冻结
- 第 22 页：通过，冻结
- 第 23 页：通过，冻结
- 第 24 页：通过，冻结

**从现在开始不得再重新设计、重新翻译、重新裁图、重新排版或“顺手优化”第 8–24 页。**

---

## 3. 下一阶段不是继续返修，而是“最终综合 QA / Final Candidate Packaging”

下一阶段只做验证、打包和回归检查。

不得修改已经通过的页面内容。

以当前 ROUND5 PPT 为唯一基准：

`l5/ECE340_L5_S18_Posted_中文忠实重建_第二阶段视觉返修ROUND5_第16页.pptx`

不得退回 ROUND4、ROUND3 或更早版本。

### 允许做的事情

- 将当前 ROUND5 文件复制/另存为“最终候选版”文件名；
- 重新导出 PDF；
- 重新渲染第 8–24 页高清 PNG；
- 生成第 8–24 页 Original PDF vs Final Candidate 对照图；
- 生成 8–24 页 contact sheet；
- 检查 notes / `[Sources]`；
- 做 slide XML 回归检查；
- 做字体、图片、公式、页面边界回归检查；
- 如存在真实 Microsoft PowerPoint 环境，做 PowerPoint 桌面版实际打开检查。

### 禁止做的事情

- 改第 8–24 页内容；
- 改第 8–24 页布局；
- 替换已经通过的图片；
- 调整已经通过的公式；
- 重写已通过中文文字；
- 调整第 16 页金属键图；
- 调用 Canvas / Work / Writing Block / image generation；
- 创建 Placeholder；
- 因为“看起来还能更好”而重新设计。

---

## 4. 最终候选版文件

建议生成：

`l5/ECE340_L5_S18_Posted_中文忠实重建_最终候选版_第8-24页.pptx`

这个文件必须以 ROUND5 文件为基础复制/打包。

第 8–24 页 slide XML 与 ROUND5 基准应保持一致；如果为了文件打包而出现非内容型 metadata 变化，可以记录，但不得出现视觉或文本内容变化。

---

## 5. 最终综合视觉 QA

必须重新生成第 8–24 页全部 17 张高清渲染 PNG：

- page_08.png
- page_09.png
- page_10.png
- page_11.png
- page_12.png
- page_13.png
- page_14.png
- page_15.png
- page_16.png
- page_17.png
- page_18.png
- page_19.png
- page_20.png
- page_21.png
- page_22.png
- page_23.png
- page_24.png

并逐页真正打开肉眼检查。

如果 GitHub connector 不能直接显示二进制图片：

允许通过 GitHub Actions artifact 只读下载到临时 sandbox，使用模型自身视觉能力查看；但任何工程修改只能回 GitHub 执行。

### 每一页都必须检查

1. 无文字互相重叠；
2. 无文字出界；
3. 无图片拉伸；
4. 无源 PDF 标题条残片；
5. 无残留页码；
6. 无重复网址；
7. 无 Placeholder；
8. 无施工说明；
9. 无红框贴纸式重复翻译；
10. 无大段英文重新承担主要教学内容；
11. 无公式改变；
12. 无科学关系丢失；
13. 无上一轮已经清理掉的问题回归；
14. 页面标题与原页主题一致；
15. 图、表、公式、箭头和状态数与 Original PDF 对应关系正确。

如果任意一页回归失败：

不要自行大范围返修。

只报告“最终综合 QA 发现回归页 X”，等待 supervisor 决定是否允许解冻该页。

---

## 6. Original PDF vs Final Candidate 对照证据

必须为第 8–24 页生成 17 张真正的：

`Original PDF vs Final Candidate`

左边必须是原始 PDF 对应页面，而不是旧中文返修版。

右边必须是最终候选版对应页面。

必须同时生成一张第 8–24 页 contact sheet，方便 supervisor 总览。

---

## 7. Notes / Sources 最终检查

最终候选版必须检查第 8–24 页 notes。

要求：

- 每页应保留 `[Sources]`；
- notes 不得出现“教师应当”“本页建议”“讲授顺序”等施工/元说明；
- notes 应是可以直接授课朗读的连续课堂语言；
- 第 20 页等复杂公式页的讲稿不得因最终打包而丢失；
- 不得因为复制/另存为最终候选版而丢 notes。

本阶段原则上**只检查，不重写**。

如发现 notes 回归丢失或损坏，先报告 supervisor，不得自行改写已验收内容。

---

## 8. Microsoft PowerPoint 实机门槛

GitHub Linux runner / LibreOffice 导出成功不等于 Microsoft PowerPoint 实机验收。

如果当前执行环境能真正访问 Microsoft PowerPoint 桌面版：

必须实际打开最终候选版，并检查：

- 字体替换；
- 文本换行；
- 数学公式；
- 图片裁剪；
- 图层遮挡；
- 第 8–24 页是否出现与 LibreOffice 渲染不同的布局问题。

如果当前环境**没有真实 Microsoft PowerPoint 桌面版能力**：

不得声称“PowerPoint 实机检查通过”。

Build Report 必须明确写：

`Microsoft PowerPoint actual open check: not performed / pending`

此时最终候选版只能叫：

`Final Candidate / 最终候选版`

不能叫：

`最终验收版`

---

## 9. 最终阶段必须生成的交付物

必须真实写入 GitHub：

1. 最终候选版 PPTX；
2. 第 8–24 页 17 张高清 PNG；
3. 第 8–24 页 17 张 Original PDF vs Final Candidate 对照图；
4. 第 8–24 页总 contact sheet；
5. Final QA Build Report；
6. generation / packaging commit SHA；
7. current branch HEAD。

建议目录：

`l5/final_qa_08_24/`

建议报告：

`l5/BUILD_REPORT_FINAL_QA_08_24.md`

---

## 10. Worker 最终回复格式：必须完整，不允许再次缩写

最终回复必须逐项包含：

```text
本轮任务状态：
已完成 / 未完成

本轮性质：
最终综合 QA / Final Candidate Packaging

本轮实际修改页面内容：
无

冻结且确认未修改页面：
第 8–24 页

最终候选 PPT 文件：
`l5/完整文件名.pptx`

第 8–24 页高清渲染图目录：
`l5/.../rendered/`

Original PDF vs Final Candidate 对照图目录：
`l5/.../comparison/`

Contact sheet：
`l5/.../完整文件名.jpg`

Final QA Build report：
`l5/BUILD_REPORT_FINAL_QA_08_24.md`

真正生成/打包最终候选版的 commit SHA：
`完整40位SHA`

Packaging / trigger commit SHA：
`完整40位SHA`
如没有：`无`

Current branch HEAD：
`完整40位SHA`

等待 supervisor 最终检查的主文件就是：
`l5/完整最终候选版文件名.pptx`

第 8–24 页视觉回归检查：
17/17 通过 / 发现回归（列页码）

Notes / [Sources] 检查：
通过 / 发现问题（列页码）

Microsoft PowerPoint actual open check：
passed / not performed / pending
```

不得只回复 SHA。

不得只回复“已完成”。

不得省略主 PPT 文件路径。

---

## 11. 工作完全完成后的邮件通知

只有当以下内容全部真实完成：

- 最终候选版 PPT 已写入 GitHub；
- 17 张高清 PNG 已生成；
- 17 张 Original PDF vs Final Candidate 已生成；
- contact sheet 已生成；
- Final QA report 已生成；
- commit 已成功；
- 17 张 PNG 已实际逐页查看；
- notes / Sources 已检查；

才允许发送邮件。

如果当前环境存在已连接且已授权的 Gmail / Email 工具，必须向：

`849812169@qq.com`

发送邮件。

建议主题：

`ECE340 L5 第8–24页最终候选版 QA 完成，等待 supervisor 最终验收`

正文至少包含：

- 最终综合 QA 已完成；
- 第 8–24 页视觉回归结果；
- 最终候选 PPT 的完整 GitHub 路径；
- commit SHA；
- current branch HEAD；
- Microsoft PowerPoint actual open check 状态。

发送成功后最终聊天回复必须包含：

```text
邮件通知：
已发送至 849812169@qq.com

邮件发送 ID：
`实际邮件 ID`
```

如果当前环境无已连接且已授权邮件工具：

不得假装发送。

必须写：

`邮件通知未发送：当前环境无已连接且已授权的邮件发送工具。`

不得要求用户再次提供 QQ 邮箱授权码。

---

## 12. 当前 supervisor 状态

- 第二阶段视觉返修：**通过**。
- 第 8–24 页逐页冻结：**是**。
- 当前基准主文件：ROUND5。
- 下一步：**最终综合 QA / Final Candidate Packaging**。
- 在最终综合 QA 完成前，不得重新打开任何已冻结页面做内容返修。
