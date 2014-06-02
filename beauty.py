import matplotlib

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

