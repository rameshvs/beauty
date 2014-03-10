# beauty — make matplotlib beautiful

This module will make your matplotlib plots more beautiful. It also includes
various utility functions for performing common plot-beautifying tasks (such as
removing axes, rescaling axes, etc.).

Most plotting functions (`plot`, `hist`, `errorbar`, `bar`) automatically change
to use the colors specified here, but `scatter` doesn't. For `scatter`, you can
use `beauty.scatter` just like you would `plt.scatter`.

By default, it uses LaTeX to render all text. This typically causes a slowdown
in producing text (labels, titles, etc.), especially for the first figure of a
session. You can prevent this by setting the `USE_TEX` flag at the top to
`False`.

In order to get the most out of your plots (especially when using
subplots), I recommend calling `plt.tight_layout()` to make matplotlib
optimize your plots.

### Demos
For demos (with code samples), see the
[wiki](https://github.com/rameshvs/beauty/wiki).

### Example:
    import beauty
    import matplotlib.pyplot as plt

    plt.figure(figsize=(4,2))
    plt.plot([4, 7, 13], label='Increasing')
    plt.plot([7, 2, 1], label='Decreasing')
    plt.plot([0, 6, 2], label='Up and down')
    plt.legend(loc='upper left')

    plt.figure(figsize=(3, 3))
    beauty.scatter([4,7,13], [7,2,1])
    plt.xlabel('$x$')
    plt.ylabel('$y$')

### Things to adjust

At the top of `beauty.py`, adjust `USE_TEX`, `USE_SERIFS`, and other variables to your liking.
