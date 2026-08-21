# SUPERVISOR STRICT VISUAL REWORK FEEDBACK 08–24

## Scope and execution rule

This supervisor standard applies to the current L5 visual rework. Stage 1 is restricted to pages **9, 12, 18, 20, 23** only. Pages 8–24 other than those five must remain unchanged from the current latest baseline deck.

Baseline for Stage 1: `l5/ECE340_L5_S18_Posted_中文忠实重建_视觉返修版_第8-24页.pptx`.

## Non-negotiable rules

1. **No placeholders.** Do not use labels such as 原设备照片, 右侧显微图, 原图示意, 待替换图片, 此处保留原图, or any empty frame in place of a real image/diagram/formula. If a source image cannot be faithfully redrawn, preserve and cleanly crop the real source image.
2. **Do not change scientific content.** Preserve formulas, numbers, chemical reactions, method names, energy-level relationships, arrows, state counts, key structures, and teaching logic. Page 20 sp3 formulas must match the source page term by term.
3. **No production notes on student-visible slides.** Text such as 本页已重建, 已删除残留, 保留原始信息, 为避免 PowerPoint 压字, 本页采用中文示意, 右图保留…, 已完成中文化, and any maker-facing explanation is forbidden on slide content. Such notes belong only in build/report records.
4. **No English original figure plus red Chinese sticker boxes.** Either rebuild a complete Chinese/necessary-bilingual figure with labels tied directly to the original objects/arrows, or preserve the complete English source figure without overlaid Chinese boxes and explain it in speaker notes.
5. **Redrawing is not simplification.** If a redraw cannot preserve the full source information relationship, use the original figure instead.

## Page 9

- No red-frame labels.
- No placeholder replacing the real equipment photo; keep the real source equipment photograph.
- The VPE reactor diagram must preserve gas flow, reaction chamber, wafer, susceptor/base, pedestal/support, vent/exhaust, RF heating, and their relationships.
- Chinese labels must correspond directly to the diagram objects.
- Preserve reactions exactly:
  - `SiCl₄ + 2H₂ ⇌ Si + 4HCl`
  - `SiH₄ → Si + 2H₂`

## Page 12

- Title must be fully readable.
- If rebuilding the MBE left diagram, preserve molecular beams, shutters, sources, substrate, and Si / Al / Ga / As / Be relationships.
- No red sticker labels.
- Right micrograph must be the real source image, not a placeholder.
- Preserve visible source information `4×4 / GaAs substrate / 10 nm / <100>`.
- No production-note text such as “右图保留……”.

## Page 18

- No red Chinese boxes on the English source image.
- Preserve complete relationships in both figures: core electrons, valence electrons, valence orbitals, first excited orbital, ionization/zero-energy level, valence levels, etc.
- Preserve `+14` and `1s / 2s / 2p / 3s / 3p`.
- If a complete faithful rebuild is not possible, preserve the English source figures and use Chinese speaker notes.
- Do not reduce the source to a few schematic lines.

## Page 20

- Preserve the four original sp3 hybridization formulas exactly term by term; do not substitute another coefficient convention or expression.
- Preserve the 109.5° tetrahedral geometry relationship.
- Caption, URL/source, and body text must not overlap.
- No content may run outside the slide.
- If the right figure uses the source image, crop it cleanly without source-page title-strip/page-number residue.
- Keep source citation once, preferably in notes under `[Sources]`.

## Page 23

- Priority rebuild.
- Do not leave a large unorganized English paragraph as the primary teaching content.
- Preserve:
  - `H #1: 2 states, 1 electron`
  - `H₂: 4 states, 2 electrons`
  - `Higher Energy / Lower Energy`
  - bonding / antibonding relationship
  - original energy-level and orbital relationship
- Chinese text and arrows/orbitals must correspond one-to-one.
- No broken text, duplicate labels, isolated text, or overflow.
- Do not simplify away the original teaching relationship.

## Stage 1 deliverables

1. New stage PPTX modifying only pages 9, 12, 18, 20, 23.
2. High-resolution single-page renders for those five pages.
3. Original-vs-new comparison images for those five pages.
4. Contact sheet containing only those five pages.
5. Build report listing modified pages, unchanged pages, per-page work, placeholder status, scientific/formula-change status, and render paths.
6. Commit everything to GitHub and record the commit SHA.

## Mandatory pre-commit visual checks

For every target page, inspect the final render for:
- no text overlap;
- no overflow;
- no red sticker boxes;
- no placeholders;
- no production notes;
- no residual source page number/title strip;
- no duplicate URL;
- no formula change;
- no image stretching;
- no loss of key scientific relationships.

Do not proceed to Stage 2 before supervisor acceptance of these five pages.
