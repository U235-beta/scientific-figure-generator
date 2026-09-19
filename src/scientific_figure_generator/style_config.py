"""
Publication-quality style configuration for scientific figures.

Supports: Nature/Science/Cell/ACS/RSC/Elsevier journal styles,
colorblind-safe palettes, vector output, 600+ DPI raster output.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OKABE_ITO = [
    "#E69F00", "#56B4E9", "#009E73", "#F0E442",
    "#0072B2", "#D55E00", "#CC79A7", "#000000",
]

COLORBREWER_QUAL = {
    "set1": ["#E41A1C", "#377EB8", "#4DAF4A", "#984EA3", "#FF7F00", "#FFFF33", "#A65628", "#F781BF"],
    "set2": ["#66C2A5", "#FC8D62", "#8DA0CB", "#E78AC3", "#A6D854", "#FFD92F", "#E5C494", "#B3B3B3"],
    "set3": ["#8DD3C7", "#FFFFB3", "#BEBADA", "#FB8072", "#80B1D3", "#FDB462", "#B3DE69", "#FCCDE5"],
    "paired": ["#A6CEE3", "#1F78B4", "#B2DF8A", "#33A02C", "#FB9A99", "#E31A1C", "#FDBF6F", "#FF7F00"],
}

JOURNAL_STYLES = {
    "nature": {"figure_width": 89.0, "figure_width_double": 183.0, "font_size": 7, "font_family": "sans-serif", "sans_serif": ["Arial", "Helvetica", "DejaVu Sans"], "line_width": 0.6, "marker_size": 4, "dpi": 600, "title_size": 8, "label_size": 7, "tick_size": 6, "legend_size": 6, "spines_top": False, "spines_right": False},
    "science": {"figure_width": 58.0, "figure_width_double": 120.0, "font_size": 6, "font_family": "sans-serif", "sans_serif": ["Arial", "Helvetica", "DejaVu Sans"], "line_width": 0.5, "marker_size": 3, "dpi": 600, "title_size": 7, "label_size": 6, "tick_size": 5, "legend_size": 5, "spines_top": False, "spines_right": False},
    "cell": {"figure_width": 85.0, "figure_width_double": 174.0, "font_size": 8, "font_family": "sans-serif", "sans_serif": ["Arial", "Helvetica", "DejaVu Sans"], "line_width": 0.8, "marker_size": 5, "dpi": 600, "title_size": 9, "label_size": 8, "tick_size": 7, "legend_size": 7, "spines_top": True, "spines_right": True},
    "acs": {"figure_width": 82.0, "figure_width_double": 172.0, "font_size": 8, "font_family": "sans-serif", "sans_serif": ["Arial", "Helvetica", "DejaVu Sans"], "line_width": 0.7, "marker_size": 5, "dpi": 300, "title_size": 9, "label_size": 8, "tick_size": 7, "legend_size": 7, "spines_top": False, "spines_right": False},
    "rsc": {"figure_width": 82.0, "figure_width_double": 170.0, "font_size": 7, "font_family": "sans-serif", "sans_serif": ["Arial", "Helvetica", "DejaVu Sans"], "line_width": 0.6, "marker_size": 4, "dpi": 600, "title_size": 8, "label_size": 7, "tick_size": 6, "legend_size": 6, "spines_top": False, "spines_right": False},
    "elsevier": {"figure_width": 90.0, "figure_width_double": 190.0, "font_size": 8, "font_family": "sans-serif", "sans_serif": ["Arial", "Helvetica", "DejaVu Sans"], "line_width": 0.7, "marker_size": 5, "dpi": 300, "title_size": 9, "label_size": 8, "tick_size": 7, "legend_size": 7, "spines_top": True, "spines_right": True},
    "default": {"figure_width": 120.0, "figure_width_double": 240.0, "font_size": 10, "font_family": "sans-serif", "sans_serif": ["DejaVu Sans", "Arial", "Helvetica"], "line_width": 1.0, "marker_size": 6, "dpi": 300, "title_size": 12, "label_size": 10, "tick_size": 9, "legend_size": 9, "spines_top": False, "spines_right": False},
}

def mm_to_inch(mm):
    return mm / 25.4

def apply_journal_style(journal="nature", custom=None):
    style = JOURNAL_STYLES.get(journal, JOURNAL_STYLES["default"]).copy()
    if custom:
        style.update(custom)
    plt.rcParams.update({
        "font.family": style["font_family"],
        "font.sans-serif": style["sans_serif"],
        "font.size": style["font_size"],
        "axes.titlesize": style["title_size"],
        "axes.labelsize": style["label_size"],
        "xtick.labelsize": style["tick_size"],
        "ytick.labelsize": style["tick_size"],
        "legend.fontsize": style["legend_size"],
        "axes.linewidth": style["line_width"],
        "lines.linewidth": style["line_width"],
        "lines.markersize": style["marker_size"],
        "figure.dpi": style["dpi"],
        "savefig.dpi": style["dpi"],
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "axes.spines.top": style["spines_top"],
        "axes.spines.right": style["spines_right"],
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "axes.unicode_minus": False,
        "xtick.direction": "out",
        "ytick.direction": "out",
    })
    return style

def get_figure_size(width_mm=None, height_mm=None, aspect=1.0, journal="nature", double=False):
    style = JOURNAL_STYLES.get(journal, JOURNAL_STYLES["default"])
    if width_mm is None:
        width_mm = style["figure_width_double"] if double else style["figure_width"]
    if height_mm is None:
        height_mm = width_mm * aspect
    return (mm_to_inch(width_mm), mm_to_inch(height_mm))

def create_figure(width_mm=None, height_mm=None, aspect=1.0, journal="nature",
                  double=False, nrows=1, ncols=1, **fig_kwargs):
    apply_journal_style(journal)
    w, h = get_figure_size(width_mm, height_mm, aspect, journal, double)
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(w, h), **fig_kwargs)
    return fig, axes

def save_figure(fig, path, formats=("pdf", "png"), dpi=None, **kwargs):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    for fmt in formats:
        out = path.with_suffix(f".{fmt}")
        save_kwargs = dict(kwargs)
        if fmt in ("png", "jpg", "jpeg", "tiff") and dpi:
            save_kwargs["dpi"] = dpi
        fig.savefig(out, **save_kwargs)
    return [str(path.with_suffix(f".{f}")) for f in formats]

def add_panel_label(ax, label, position="upper left", fontsize=None, fontweight="bold",
                    offset=(0.02, 0.98), **kwargs):
    pos_map = {
        "upper left": (offset[0], offset[1]),
        "upper right": (1 - offset[0], offset[1]),
        "lower left": (offset[0], 1 - offset[1]),
        "lower right": (1 - offset[0], 1 - offset[1]),
    }
    x, y = pos_map.get(position, offset)
    ha = "left" if "left" in position else "right"
    va = "top" if "upper" in position else "bottom"
    fs = fontsize or plt.rcParams.get("axes.titlesize", 10)
    ax.text(x, y, label, transform=ax.transAxes, fontsize=fs,
            fontweight=fontweight, ha=ha, va=va, **kwargs)
