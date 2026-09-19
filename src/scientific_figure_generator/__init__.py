"""
Scientific Figure Generator - Publication-quality figure generation for research papers.

Integrates best practices from:
- K-Dense-AI/scientific-agent-skills (matplotlib, infographics, visualization)
- Imbad0202/academic-research-skills (academic-paper visualization, quality gates)
- molecular-visualization skill (molecule structures, orbitals, electron clouds)

Supports: Nature/Science/Cell/ACS/RSC/Elsevier journal styles,
colorblind-safe palettes, vector output, multi-panel figures,
quality checking, molecule structure panels, mechanism diagrams.
"""

__version__ = "1.0.0"
__author__ = "U235-beta"
__license__ = "MIT"

from .style_config import (
    apply_journal_style, get_figure_size, create_figure, save_figure,
    add_panel_label, OKABE_ITO, JOURNAL_STYLES, mm_to_inch,
)
from .data_plots import (
    plot_line, plot_bar, plot_scatter, plot_heatmap,
    plot_boxplot, plot_violin, plot_histogram,
)
from .mechanism_diagrams import (
    causal_chain, layered_framework, process_flow,
    comparison_diagram, uncertainty_propagation_chain,
)
from .figure_generator import FigureGenerator, generate_figure_from_spec
from .quality_checker import FigureQualityChecker, check_and_save

__all__ = [
    "apply_journal_style", "get_figure_size", "create_figure", "save_figure",
    "add_panel_label", "OKABE_ITO", "JOURNAL_STYLES", "mm_to_inch",
    "plot_line", "plot_bar", "plot_scatter", "plot_heatmap",
    "plot_boxplot", "plot_violin", "plot_histogram",
    "causal_chain", "layered_framework", "process_flow",
    "comparison_diagram", "uncertainty_propagation_chain",
    "FigureGenerator", "generate_figure_from_spec",
    "FigureQualityChecker", "check_and_save",
]
