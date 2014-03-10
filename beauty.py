import matplotlib

#### Parameters you can adjust to your liking
USE_TEX = True      # whether or not to render *all* text w/latex
USE_SERIFS = False   # serif vs san-serif font (computer modern)
LEGEND_FONT_SIZE = TICK_FONT_SIZE = 9
TITLE_FONT_SIZE = LABEL_FONT_SIZE = 10.5

DPI = 150 # Font size adjustments should scale with this

#### Automatic parameter setting
# Figure size/scale
matplotlib.rc('savefig', dpi=DPI)
matplotlib.rc('figure', dpi=DPI, figsize=(2,2))
# Font
matplotlib.rc('xtick',labelsize=TICK_FONT_SIZE)
matplotlib.rc('ytick',labelsize=TICK_FONT_SIZE)
matplotlib.rc('axes', labelsize=LABEL_FONT_SIZE, titlesize=TITLE_FONT_SIZE)
matplotlib.rc('legend', fontsize=LEGEND_FONT_SIZE)

if USE_SERIFS:
    matplotlib.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman']})
else:
    matplotlib.rc('font', **{'family':'sans-serif', 'sans-serif':['Computer Modern Sans serif']})
    if USE_TEX:
        matplotlib.rcParams['text.latex.preamble'].append('\usepackage{sfmath}')
matplotlib.rcParams.update({'text.usetex':USE_TEX})

def dim(color, factor):
    """
    Dims a color (in #rrggbb hex form) by the factor given (float from 0-1):
    e.g., dim('#886644', 0.5) returns '#443322'
    """
    r = color[1:3]
    g = color[3:5]
    b = color[5:7]
    out = '#'
    for c in (r,g,b):
        out += '%02x' % int(int(c, 16) * factor)
    return out

### Colors modeled after d3.js's `category10` color scale
### (defined like this so it's easy to use 'beauty.blue' as a color)
blue = '#1f77b4'
darkblue = dim(blue, 0.75)

orange = '#ff7f0e'
darkorange = dim(orange, 0.75)

green =  '#2ca02c'
darkgreen = dim(green, 0.75)

red =  '#d62728'
darkred = dim(red, 0.75)

purple = '#9467bd'
darkpurple = dim(purple, 0.75)

brown = '#8c564b'
darkbrown = dim(brown, 0.75)

pink = '#e377c2'
darkpink = dim(pink, 0.75)

yellow =  '#bcbd22'
darkyellow = dim(yellow, 0.75)

cyan = '#17becf'
darkcyan = dim(cyan, 0.75)

# Same as matlab/matplotlib for the first few, but diverges to match category10
# TODO consider not using green & red so early on (colorblindness)
matplotlib.rc('axes',
        color_cycle=[blue, green, orange, red, cyan, purple, yellow, pink])

def scatter(x, y, **kwargs):
    """ Like plt.scatter, but with nicer default color & transparency """
    import matplotlib.pyplot as plt
    kwargs.setdefault('c', blue)
    kwargs.setdefault('alpha', 0.95)
    kwargs.setdefault('edgecolors', 'none')
    plt.scatter(x, y, **kwargs)

def bar(left, height, **kwargs):
    """ Like plt.bar, but with edge lines off by default """
    kwargs.setdefault('edgecolors', 'none')
    plt.bar(left, height, **kwargs)

def equalize_axes():
    import matplotlib.pyplot as plt
    ax = plt.axis()
    mini = min(ax[0],ax[2])
    maxi = max(ax[1],ax[3])
    bounds = [mini, maxi, mini, maxi]
    plt.axis(bounds)
    return bounds

def change_xlimits(axis, xmin, xmax):
    ax = axis.axis()
    axis.axis([xmin, xmax, ax[2], ax[3]])

def change_ylimits(axis, ymin, ymax):
    ax = axis.axis()
    axis.axis([ax[0], ax[1], ymin, ymax])
def x_axis_only(axis):
    """ Removes the axis lines on the top and right/left sides """
    for (location, spine) in axis.spines.items():
        if location in ['right', 'top', 'left']:
            spine.set_color('none') # don't draw it
    axis.xaxis.set_ticks_position('bottom')
    #axis.yaxis.set_ticks_position('left')

def permute_legend_items(ax, permutation_of_sorted_labels, **kwargs):
    def permute(lst):
        return [lst[i] for i in permutation_of_sorted_labels]
    (handles, labels) = ax.get_legend_handles_labels()
    ax.legend(permute(handles), permute(labels), **kwargs)

def xy_axes_only(axis):
    limit_axes(axis, ['right', 'top'], 'bottom', 'left')

def limit_axes(axis, locations_to_remove, xtick_location='none', ytick_location='none'):
    """
    Removes the axis lines at the specified locations, and puts the x/y ticks
    at the specified locations.
    locations_to_remove: a list or other iterable with a subset of:
                         ['top', 'bottom', 'left', 'right']

    xtick_location: one of 'top', 'bottom', 'left', 'right', 'none'
    """
    for (location, spine) in axis.spines.items():
        if location in locations_to_remove:
            spine.set_color('none') # don't draw it

    axis.xaxis.set_ticks_position(xtick_location)
    axis.yaxis.set_ticks_position(ytick_location)

