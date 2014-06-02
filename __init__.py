from beauty import *
#### Parameters I chose arbitrarily
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

gray = '#c7c7c7'

# Similar to matlab/matplotlib for the first few, but diverges to match category10,
# and avoids using both red and green together too early
matplotlib.rc('axes',
        color_cycle=[blue, green, orange, cyan, purple, red, yellow, pink])
