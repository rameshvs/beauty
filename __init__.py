from beauty import *

# Parameters that the user can change (see set_* below)
_USE_TEX = True      # whether or not to render *all* text w/latex
_USE_SERIFS = False   # serif vs san-serif font (computer modern)
_LEGEND_FONT_SIZE = _TICK_FONT_SIZE = 9
_TITLE_FONT_SIZE = _LABEL_FONT_SIZE = 10.5

_DPI = 150 # Font size adjustments should scale with this

def _update_matplotlibrc():
    """
    Uses the module variables to update matplotlibrc
    """
    _set_matplotlibrc(_DPI, _USE_TEX, _USE_SERIFS,
        _LEGEND_FONT_SIZE, _TICK_FONT_SIZE, _TITLE_FONT_SIZE, _LABEL_FONT_SIZE)

def _set_matplotlibrc(dpi, use_tex, use_serifs,
        legend_font_size, tick_font_size, title_font_size, label_font_size):
    """
    Sets the appropriate matplotlibrc parameters given the provided config
    """
    matplotlib.rc('savefig', dpi=dpi)
    matplotlib.rc('figure', dpi=dpi, figsize=(2,2))
    # Font
    matplotlib.rc('xtick',labelsize=tick_font_size)
    matplotlib.rc('ytick',labelsize=tick_font_size)
    matplotlib.rc('axes', labelsize=label_font_size, titlesize=title_font_size)
    matplotlib.rc('legend', fontsize=legend_font_size)
    matplotlib.rcParams.update({'text.usetex':use_tex})

    sfmath = r'\usepackage{sfmath}'
    if use_serifs:
        font_args = {'family':'serif', 'serif':['Computer Modern Roman']}
        if sfmath in matplotlib.rcParams['text.latex.preamble']:
            matplotlib.rcParams['text.latex.preamble'].remove(sfmath)
    else:
        font_args = {'family': 'sans-serif',
                     'sans-serif': ['Computer Modern Sans Serif']}
        if use_tex:
            matplotlib.rcParams['text.latex.preamble'].append(sfmath)
    matplotlib.rc('font', **font_args)

_update_matplotlibrc()

def set_serifs(use_serifs):
    """ Change whether or not the plot font has serifs. """
    global _USE_SERIFS
    _USE_SERIFS = use_serifs
    _update_matplotlibrc()

def set_tex(use_tex):
    """
    Change whether or not to parse all text using LaTeX. This makes plot
    generation a little slower, but allows using arbitrary math in labels, etc.
    """
    global _USE_TEX
    _USE_TEX = use_tex
    _update_matplotlibrc()

def set_font_sizes(legend_font_size=None, tick_font_size=None,
        title_font_size=None, label_font_size=None):
    """
    Sets font sizes for legend, tick, title, or label. Any value that isn't
    given (or is given as None) remains the same.
    """
    if legend_font_size is not None:
        global _LEGEND_FONT_SIZE
        _LEGEND_FONT_SIZE = legend_font_size
    if tick_font_size is not None:
        global _TICK_FONT_SIZE
        _TICK_FONT_SIZE = tick_font_size
    if title_font_size is not None:
        global _TITLE_FONT_SIZE
        _TITLE_FONT_SIZE = title_font_size
    if label_font_size is not None:
        global _LABEL_FONT_SIZE
        _LABEL_FONT_SIZE = label_font_size
    _update_matplotlibrc()

# Similar to matlab/matplotlib for the first few, but changes to match
# category10, and avoids using both red and green together too early to help
# color-blind plot viewers
matplotlib.rc('axes',
        color_cycle=[blue, green, orange, cyan, purple, red, yellow, pink])
