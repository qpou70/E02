# ECE340 L5 Final QA：Supervisor 视觉复核 ROUND2

## 1. 检查对象

本轮检查文件：

`l5/ECE340_L5_S18_Posted_中文忠实重建_最终候选版_R1_第8-24页.pptx`

对应 generation commit：

`890e59a18d0fc92e992e02134cea8ead49b21870`

Supervisor 已从 GitHub Actions artifact 只读取得并实际打开：

- 第 8–24 页全部 17 张高清 PNG；
- 17 张 Original PDF vs Final Candidate R1 对照图；
- contact sheet；
- Final QA R1 Build Report；
- Final Candidate R1 PPTX。

同时实际读取了第 8–24 页 notes 文本。

## 2. 本轮结论

Final Candidate R1 **仍不能获得最终视觉验收**，但问题已经收敛到 **第 18 页一处视觉中文化遗漏**。

上一轮要求修改的第 13、15、20、21 页本轮均已通过：

- 第 13 页：原页页码已删除，图片说明已中文化；
- 第 15 页：大型英文主标题已改为中文，页码已删除；
- 第 20 页：四条 sp³ 公式、正负号、109.5° 和轨道关系保持正确，可翻译教学文字已中文化；
- 第 21 页：大型 `Energy Bands` 已改为中文 `能带`，页码已删除。

Notes QA 本轮也可以通过：第 8–24 页均已有连续中文课堂讲稿和 `[Sources]`，上一轮发现的制作/返修元说明已清除；第 20 页讲稿有效中文汉字数为 412。

因此本轮**不要再修改 notes**。

## 3. 唯一剩余视觉问题：第 18 页

第 18 页标题 `硅的芯层电子与价电子` 正确，科学图本体完整。

但是页面底部仍保留了一整段英文图注：

`Figure 2.8 Electronic structure and energy levels in a Si atom: (a) The orbital model of a Si atom showing the 10 core electrons (n = 1 and 2), and the 4 valence electrons (n = 3); (b) energy levels in the coulombic potential of the nucleus are also shown schematically.`

这段英文不是不可替代的科学符号或高风险图内标签，而是一段完整教学说明，且在页面中占据较明显视觉面积。对于中文忠实重建，继续保留这整段英文不合格。

### 第 18 页只允许做以下定点修改

1. **科学图内部全部保持不动。**
   - 不重画原子轨道图；
   - 不重画右侧势阱/能级图；
   - 不改 `1s / 2s / 2p / 3s / 3p`；
   - 不改 `+14`；
   - 不改曲线、箭头、能级线；
   - 不在图内部增加中文贴纸。

2. **只处理底部完整英文图注。**

将：

`Figure 2.8 ...`

替换为简洁中文图注，例如：

`图 2.8　Si 原子的电子结构与能级示意：（a）轨道模型显示 10 个芯层电子（n = 1、2）和 4 个价电子（n = 3）；（b）示意给出原子核库仑势中的电子能级。`

3. 图注排版要求：
   - 黑色或与当前正文一致的深色文字；
   - 字号明显小于页面主标题；
   - 不遮挡科学图；
   - 不使用大块灰/白补丁造成明显修补感；
   - 不新增第二套英文说明。

4. 页面右上小号英文辅助标题 `Silicon Core and Valence Electrons` 可以保留，不作为本轮问题。

## 4. 冻结范围

本轮视觉只允许修改：

- 第 18 页底部图注区域。

以下全部冻结：

- 第 8–17 页；
- 第 19–24 页；
- 第 1–7 页；
- 第 25–52 页；
- 第 8–24 页全部 notes。

如果除第 18 页底部图注外任何页面内容或 notes 发生变化，本轮视为失败。

## 5. Worker 角色边界

Worker **不负责最终验收**。

Worker 只负责：

1. 按上述范围修改第 18 页；
2. 在 GitHub 生成新的 PPT；
3. 生成 `page_18.png`；
4. 生成 Original PDF vs New Page 18 对照图；
5. 提交 commit；
6. 停止并等待 supervisor。

Worker 不得自行宣布：

- `visual passed`；
- `final acceptance passed`；
- `最终验收通过`。

最终视觉结论只能由 supervisor 给出。

## 6. 交付物

建议新文件：

`l5/ECE340_L5_S18_Posted_中文忠实重建_最终候选版_R2_第8-24页.pptx`

必须同时生成：

- 第 18 页高清 PNG；
- 第 18 页 Original PDF vs Final Candidate R2 对照图；
- 简洁 build report，记录只修改第 18 页底部图注；
- generation commit SHA；
- current branch HEAD。

完成后停止，不要继续下一轮。

## 7. 邮件通知

当上述证据已经真实写入 GitHub 并成功提交后，如果当前环境具有已连接且已授权的邮件工具，发送邮件到：

`849812169@qq.com`

邮件主题：

`ECE340 L5 Final QA R2 证据已提交，等待 supervisor 检查`

邮件只能表述“证据已提交、等待 supervisor”，不得写“最终验收通过”。
