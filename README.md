# Scientific Figure Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.5+-green.svg)](https://matplotlib.org/)

> Publication-quality figure generation for scientific research papers. Journal-ready styling, colorblind-safe palettes, multi-panel figures, molecule structures, mechanism diagrams, and automated quality checking.

## Features

- 7+ data plot types - line, bar, scatter, heatmap, boxplot, violin, histogram
- 6 journal styles - Nature, Science, Cell, ACS, RSC, Elsevier
- Colorblind-safe - Okabe-Ito, viridis family, ColorBrewer palettes
- Multi-panel figures - Figure 1-5 style composite layouts
- Molecule panels - integrates with molecular-visualization skill
- Mechanism diagrams - causal chains, process flows, layered frameworks
- Quality checking - automated pre-submission quality gates
- Vector output - PDF/SVG with editable text (TrueType fonts)
- Specification-based - generate figures from JSON/YAML specs

## Installation

```bash
git clone https://github.com/U235-beta/scientific-figure-generator.git
cd scientific-figure-generator
pip install -r requirements.txt
pip install -e .
```

## Quick Start

```python
from scientific_figure_generator import FigureGenerator

gen = FigureGenerator(journal="nature", double=True, aspect=0.8)
fig, axes = gen.create_figure(layout="2x2")

gen.add_line_plot(axes[0], x, [y1, y2], labels=["Control", "Treatment"])
gen.add_bar_plot(axes[1], ["PET", "PS", "PVC"], [values])
gen.add_mechanism_chain(axes[2], ["Pure polymer", "+ Additives", "+ Aging"])
gen.add_text_panel(axes[3], "Key finding: additives dominate fluorescence", title="Summary")

gen.save("Figure1")
```

## Project Structure

```
scientific-figure-generator/
├── SKILL.md              # Skill definition and usage guide
├── README.md             # This file
├── plugin.json           # Agent Plugin manifest
├── pyproject.toml        # Python package configuration
├── requirements.txt      # Python dependencies
├── src/
│   └── scientific_figure_generator/
│       ├── __init__.py       # Package init, re-exports
│       ├── style_config.py   # Journal styles, color palettes, sizing
│       ├── data_plots.py     # Line, bar, scatter, heatmap, etc.
│       ├── mechanism_diagrams.py  # Causal chains, process flows
│       ├── figure_generator.py    # Multi-panel figure generator
│       └── quality_checker.py     # Automated quality checking
├── examples/
│   └── example_figure.py # Example usage script
├── tests/
│   └── test_basic.py     # Basic unit tests
└── templates/
    └── figure_spec.json  # Figure specification template
```

## Integration

This skill integrates with:
- molecular-visualization - molecule structure panels with ball-and-stick models, orbitals, electron clouds
- K-Dense-AI/scientific-agent-skills - matplotlib and visualization best practices
- Imbad0202/academic-research-skills - academic paper visualization workflow

## License

MIT License - see LICENSE for details.

## Citation

```bibtex
@software{scientific_figure_generator,
  author = {U235-beta},
  title = {Scientific Figure Generator},
  year = {2026},
  url = {https://github.com/U235-beta/scientific-figure-generator}
}
```
