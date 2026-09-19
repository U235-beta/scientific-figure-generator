---
name: scientific-figure-generator
version: 1.0.0
description: "Publication-quality scientific figure generator for research papers. Supports Nature/Science/Cell/ACS/RSC/Elsevier journal styles, colorblind-safe palettes, multi-panel figures, molecule structures, mechanism diagrams, and quality checking. Integrates best practices from K-Dense-AI/scientific-agent-skills and Imbad0202/academic-research-skills."
keywords: [scientific figures, publication quality, matplotlib, journal style, multi-panel, molecule visualization, mechanism diagram, quality control, colorblind-safe]
license: MIT
author: U235-beta
---

# Scientific Figure Generator

Generate publication-quality figures for scientific research papers with journal-appropriate styling, colorblind-safe palettes, vector output, and automated quality checking.

## When to Use

- Generating Figure 1-5 for a research paper, review, or thesis
- Creating multi-panel composite figures with consistent layout
- Producing data plots (line, bar, scatter, heatmap, boxplot, violin, histogram)
- Drawing mechanism diagrams, causal chains, process flows, comparison diagrams
- Adding molecule structure panels (integrates with molecular-visualization skill)
- Quality-checking figures before submission
- Converting rough plots to journal-ready format

## Prerequisites

- Python 3.9+
- matplotlib >= 3.5
- numpy >= 1.21
- Optional: molecular-visualization skill (for molecule structure panels)

## Quick Start

```python
from scientific_figure_generator import FigureGenerator, plot_line

# Create a 2x2 multi-panel figure in Nature style
gen = FigureGenerator(journal="nature", double=True, aspect=0.8)
fig, axes = gen.create_figure(layout="2x2")

# Panel A: Line plot
gen.add_line_plot(axes[0], x, [y1, y2], labels=["Control", "Treatment"])
gen.set_axis_labels(axes[0], "Time (h)", "Fluorescence Intensity (a.u.)")

# Panel B: Bar plot
gen.add_bar_plot(axes[1], ["PET", "PS", "PVC", "PLA"], [values])
gen.set_axis_labels(axes[1], "Polymer", "Autofluorescence (a.u.)")

# Panel C: Mechanism diagram
gen.add_mechanism_chain(axes[2], ["Pure polymer", "+ Additives", "+ Aging", "Mixed signal"])

# Panel D: Key finding text
gen.add_text_panel(axes[3], "Additive fluorescence dominates\nin commercial plastics", title="Key Finding")

# Save as PDF + PNG (600 DPI)
gen.save("Figure1_autofluorescence_mechanism")
```

## Journal Styles

| Journal | Single Column (mm) | Double Column (mm) | Font Size | DPI |
|---------|-------------------|-------------------|-----------|-----|
| Nature | 89 | 183 | 7pt | 600 |
| Science | 58 | 120 | 6pt | 600 |
| Cell | 85 | 174 | 8pt | 600 |
| ACS | 82 | 172 | 8pt | 300 |
| RSC | 82 | 170 | 7pt | 600 |
| Elsevier | 90 | 190 | 8pt | 300 |

## Color Palettes

- **Okabe-Ito** (default, colorblind-safe): 8 distinct colors
- **ColorBrewer**: Set1, Set2, Set3, Paired
- **Viridis family**: viridis, magma, inferno, plasma, cividis (perceptually uniform)
- **Diverging**: coolwarm, RdBu, PiYG

## Quality Checking

```python
from scientific_figure_generator import FigureQualityChecker

checker = FigureQualityChecker(journal="nature")
issues = checker.check(fig)
report = checker.report(issues)
print(report)
```

## API Reference

### Core Modules

- `style_config.py` - Journal styles, color palettes, figure sizing, save helpers
- `data_plots.py` - Line, bar, scatter, heatmap, boxplot, violin, histogram
- `mechanism_diagrams.py` - Causal chains, layered frameworks, process flows, comparisons, uncertainty propagation
- `figure_generator.py` - Multi-panel figure generator, FigureGenerator class, spec-based generation
- `quality_checker.py` - Automated quality checking, quality gates

## Integration with molecular-visualization

When the `molecular-visualization` skill is installed, molecule structure panels are automatically rendered with:
- Ball-and-stick models (RDKit coordinates, CPK coloring)
- sp2/sp3 hybrid orbital visualization
- pi orbital overlap
- Electron cloud density contours
- FRET mechanism diagrams

## Best Practices

1. **Always use vector output** (PDF/SVG) for submission
2. **Use colorblind-safe palettes** - Okabe-Ito or viridis family
3. **Embed fonts as TrueType** (pdf.fonttype=42) for Illustrator compatibility
4. **Add panel labels** (A, B, C...) to multi-panel figures
5. **Quality-check before submission** - run FigureQualityChecker
6. **Match journal column width** - use journal parameter for correct sizing

## References

- K-Dense-AI/scientific-agent-skills - matplotlib and visualization best practices
- Imbad0202/academic-research-skills - academic paper visualization workflow and quality gates
- Okabe & Ito (2008) - Color universal design palette

## License

MIT License
