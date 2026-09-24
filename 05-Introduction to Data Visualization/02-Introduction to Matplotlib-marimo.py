import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np

    # A lesson draws many figures. This stops the warning about how many are open.
    plt.rcParams["figure.max_open_warning"] = 0

    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Introduction to Matplotlib

    ## Objectives

    - Create a figure and an axes, then draw a line on those axes.
    - See how the number of points changes a curve, and draw more than one line on the same axes.
    - Set the color, the line style, the axis limits, a title, and a legend.
    - Show uncertainty with error bars, and compare several distributions with histograms.

    ## Background

    Matplotlib is a library for charts, built on NumPy arrays. A figure is the whole picture. An axes is the region inside it where the data is drawn. One figure can hold one axes or several.

    In this lesson each chart starts a new figure, so running a cell again does not draw the new lines on top of the old ones.

    ## Datasets Used

    This lesson does not read a file. The arrays are built with NumPy. Random samples use a seed, so the same cell produces the same numbers each time it runs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A figure and an axes

    Every chart in this lesson starts from these two objects. `plt.figure` creates the picture. `plt.axes` creates the plotting region. The cell below is that empty picture.
    """)
    return


@app.cell
def _(plt):
    _figure = plt.figure()
    plt.axes()
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How many points

    `np.linspace(0, 10, n)` returns `n` evenly spaced numbers from 0 to 10, including both ends. The three charts plot `sin` of those numbers for 10, 50, and 1000 points. More points turn the broken line into a smooth curve.
    """)
    return


@app.cell
def _(np, plt):
    _figure, _axes = plt.subplots()
    _x = np.linspace(0, 10, 10)
    _axes.plot(_x, np.sin(_x))
    _axes.set_title("10 points")
    return _figure


@app.cell
def _(np, plt):
    _figure, _axes = plt.subplots()
    _x = np.linspace(0, 10, 50)
    _axes.plot(_x, np.sin(_x))
    _axes.set_title("50 points")
    return _figure


@app.cell
def _(np, plt):
    _figure, _axes = plt.subplots()
    _x = np.linspace(0, 10, 1000)
    _axes.plot(_x, np.sin(_x))
    _axes.set_title("1000 points")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `count`, then run the cell. A small count looks jagged. A large count looks smooth.
    """)
    return


@app.cell
def _(np, plt):
    count = 20
    _figure, _axes = plt.subplots()
    _x = np.linspace(0, 10, count)
    _axes.plot(_x, np.sin(_x))
    _axes.set_title(f"sin(x) with {count} points")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Two lines, a legend, and a style

    Call `plot` once for each line. The second call draws on the same axes.

    `label` names a line. `plt.legend` draws the box that matches each name to its line.

    `color` and `linestyle` can be passed separately. They can also be packed into one format string:

    - `'-g'` is a solid green line
    - `'--c'` is a dashed cyan line
    - `'-.k'` is a dash-dot black line
    - `':r'` is a dotted red line
    """)
    return


@app.cell
def _(np, plt):
    _figure, _axes = plt.subplots()
    _x = np.linspace(0, 10, 1000)
    _axes.plot(_x, np.sin(_x))
    _axes.plot(_x, np.cos(_x))
    _axes.set_title("sin and cos")
    return _figure


@app.cell
def _(np, plt):
    _figure, _axes = plt.subplots()
    _x = np.linspace(0, 10, 1000)
    _axes.plot(_x, np.sin(_x), label="sin(x)")
    _axes.plot(_x, np.cos(_x), label="cos(x)")
    _axes.legend()
    _axes.set_title("With a legend")
    return _figure


@app.cell
def _(np, plt):
    _figure, _axes = plt.subplots()
    _x = np.linspace(0, 10, 1000)
    _axes.plot(_x, np.sin(_x), color="green", linestyle="dashed", label="dashed green")
    _axes.plot(_x, np.cos(_x), color="red", linestyle="dotted", label="dotted red")
    _axes.legend()
    return _figure


@app.cell
def _(np, plt):
    _figure, _axes = plt.subplots()
    _x = np.linspace(0, 10, 1000)
    _axes.plot(_x, np.sin(_x), "-g", label="solid green")
    _axes.plot(_x, np.cos(_x), "--c", label="dashed cyan")
    _axes.plot(_x, np.sin(_x + 1), "-.k", label="dash-dot black")
    _axes.plot(_x, np.cos(_x + 1), ":r", label="dotted red")
    _axes.legend()
    _axes.set_title("Format strings")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Limits, title, and a shorter call

    `plt.xlim` and `plt.ylim` set the visible range of each axis. `plt.axis([xmin, xmax, ymin, ymax])` sets both at once. `plt.title` adds the title.

    The last chart skips the explicit `figure` and `axes` lines. `plt.plot` creates them when they do not already exist. That cell still starts with `plt.figure()` so the chart has a picture of its own.
    """)
    return


@app.cell
def _(np, plt):
    _figure = plt.figure()
    _x = np.linspace(0, 10, 1000)
    plt.plot(_x, np.sin(_x), "--g")
    plt.xlim(-1, 11)
    plt.ylim(-1.5, 1.5)
    plt.title("xlim and ylim")
    return _figure


@app.cell
def _(np, plt):
    _figure = plt.figure()
    _x = np.linspace(0, 10, 1000)
    plt.plot(_x, np.sin(_x), "--g")
    plt.axis([-1, 11, -1.2, 1.2])
    plt.title("A Sine Curve")
    return _figure


@app.cell
def _(np, plt):
    _figure = plt.figure()
    _x = np.linspace(0, 10, 1000)
    plt.title("A Sine and Cosine Curves")
    plt.plot(_x, np.sin(_x), "--g", label="sin(x)")
    plt.plot(_x, np.cos(_x), ":r", label="cos(x)")
    plt.legend()
    plt.axis([-1, 11, -1.2, 1.2])
    return _figure


@app.cell
def _(np, plt):
    _figure = plt.figure()
    _x = np.linspace(0, 2 * np.pi, 50)
    plt.plot(_x, np.sin(_x), label="sin(x)")
    plt.plot(_x, np.cos(_x), label="cos(x)")
    plt.legend()
    plt.title("From 0 to 2 pi, in one call each")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Error bars

    A measurement is usually a value plus some uncertainty. Here `x` is 50 evenly spaced numbers from 0 to 10. `y` is `sin(x)` plus a random shift. `dy` is the size of that shift, and it is also the length of the error bar.

    `plt.errorbar` draws the points and a bar of length `yerr` around each one. It returns an `ErrorbarContainer` with three pieces:

    - `plotline` is the `Line2D` of the data.
    - `caplines` are the `Line2D` caps at the ends of the bars. With the default size, that list is often empty. `capsize` gives the caps a length.
    - `barlinecols` are the `LineCollection` objects that hold the bars. One collection is vertical and one is horizontal. Each point has a segment. The cell prints the first segment.

    In Jupyter, a semicolon at the end of the line hides that container and leaves the chart. This notebook shows the chart by returning the figure.

    `fmt` is a format string for the line and the markers. `'r'` is a red line. `'ro'` is red circles. `color` colors the points, and `ecolor` colors the bars, so the two can differ.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    x = np.linspace(0, 10, 50)
    dy = 0.6
    y = np.sin(x) + dy * np.random.rand(50)
    print("First 5 values of x:", x[:5])
    print("First 5 values of y:", y[:5])
    return dy, x, y


@app.cell
def _(dy, plt, x, y):
    _figure = plt.figure()
    plt.errorbar(x, y, yerr=dy)
    plt.title("Error bars")
    return _figure


@app.cell
def _(dy, plt, x, y):
    _figure = plt.figure()
    _container = plt.errorbar(x, y, yerr=dy)
    _plotline, _caplines, _barlinecols = _container
    print("Data line, first 5 x:", _plotline.get_xdata()[:5])
    print("Data line, first 5 y:", _plotline.get_ydata()[:5])
    print("Number of cap lines:", len(_caplines))
    for _index, _capline in enumerate(_caplines):
        print(f"Cap line {_index + 1} X data:", _capline.get_xdata()[:5])
        print(f"Cap line {_index + 1} Y data:", _capline.get_ydata()[:5])
    for _index, _barlinecol in enumerate(_barlinecols):
        _segments = _barlinecol.get_segments()
        print(f"Bar line collection {_index + 1} has {len(_segments)} segments")
        print("First segment:")
        print(_segments[0])
    return _figure


@app.cell
def _(dy, plt, x, y):
    _figure = plt.figure()
    plt.errorbar(x, y, yerr=dy, fmt="r")
    plt.title("fmt='r'")
    return _figure


@app.cell
def _(dy, plt, x, y):
    _figure = plt.figure()
    plt.errorbar(x, y, yerr=dy, fmt="ro")
    plt.title("fmt='ro'")
    return _figure


@app.cell
def _(dy, plt, x, y):
    _figure = plt.figure()
    plt.errorbar(x, y, yerr=dy, fmt="o", color="black", ecolor="lightgray")
    plt.title("Black points, light gray bars")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Histograms

    `plt.hist` splits the values into bins and draws one bar per bin. It returns three things:

    - the count in each bin
    - the edges of the bins
    - the `Rectangle` patches that form the bars

    A semicolon in Jupyter hides that tuple. The chart is the same either way. The next cell prints the tuple and draws that histogram once.
    """)
    return


@app.cell
def _(np):
    np.random.seed(1)
    data = np.random.randn(1000)
    return (data,)


@app.cell
def _(data, plt):
    _figure = plt.figure()
    _values, _edges, _patches = plt.hist(data)
    print("Values:", _values)
    print("Edges:", _edges)
    for _index, _patch in enumerate(_patches):
        print(f"Patch {_index + 1}:")
        print("  Height (Frequency):", _patch.get_height())
        print("  Width (Bin size):", _patch.get_width())
        print("  X (Bin start):", _patch.get_x())
        print("  Y (Bottom of the bar):", _patch.get_y())
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bins` is the number of intervals, or a list of the edges. `color` sets the bar color. `alpha` is the opacity, from 0 (invisible) to 1 (solid). `density=True` rescales the heights so the bars represent probability. The shape stays the same. The vertical scale changes. Each of these settings is its own chart.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Default number of bins:
    """)
    return


@app.cell
def _(data, plt):
    default_histogram = plt.figure()
    plt.hist(data)
    plt.title("Default histogram")
    return default_histogram


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bins=30`:
    """)
    return


@app.cell
def _(data, plt):
    histogram_30_bins = plt.figure()
    plt.hist(data, bins=30, color="red")
    plt.title("30 bins")
    return histogram_30_bins


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bins=30` and `alpha=0.5`:
    """)
    return


@app.cell
def _(data, plt):
    histogram_30_bins_faint = plt.figure()
    plt.hist(data, bins=30, color="red", alpha=0.5)
    plt.title("alpha=0.5")
    return histogram_30_bins_faint


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bins=50` and `density=True`:
    """)
    return


@app.cell
def _(data, plt):
    histogram_50_bins = plt.figure()
    plt.hist(data, bins=50, color="red", density=True, alpha=0.5)
    plt.title("density=True")
    return histogram_50_bins


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `bins` and `opacity`, then run the cell.
    """)
    return


@app.cell
def _(data, plt):
    bins = 20
    opacity = 0.7
    _figure = plt.figure()
    plt.hist(data, bins=bins, color="red", alpha=opacity)
    plt.title(f"bins={bins}, alpha={opacity}")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Several histograms

    `np.random.normal(center, spread, count)` draws `count` values from a bell curve. The three samples below have different centers and different spreads.

    Drawing them on separate axes shows each one alone. Drawing them on one axes, with `alpha` below 1, shows how they overlap. A dictionary of shared settings can be unpacked with `**kwargs`.
    """)
    return


@app.cell
def _(np):
    np.random.seed(2)
    x1 = np.random.normal(0, 0.8, 1000)
    x2 = np.random.normal(-2, 1, 1000)
    x3 = np.random.normal(3, 2, 1000)
    return x1, x2, x3


@app.cell
def _(plt, x1):
    _figure = plt.figure()
    plt.hist(x1, alpha=0.5)
    plt.title("x1")
    return _figure


@app.cell
def _(plt, x2):
    _figure = plt.figure()
    plt.hist(x2, alpha=0.5)
    plt.title("x2")
    return _figure


@app.cell
def _(plt, x3):
    _figure = plt.figure()
    plt.hist(x3, alpha=0.5)
    plt.title("x3")
    return _figure


@app.cell
def _(plt, x1, x2, x3):
    _figure = plt.figure()
    _kwargs = dict(alpha=0.3, density=True, bins=40)
    plt.hist(x1, **_kwargs)
    plt.hist(x2, **_kwargs)
    plt.hist(x3, **_kwargs)
    plt.title("Same bins, no legend")
    return _figure


@app.cell
def _(plt, x1, x2, x3):
    _figure = plt.figure()
    _kwargs = dict(alpha=0.3, density=True, bins=40)
    plt.hist(x1, **_kwargs, label="x1")
    plt.hist(x2, **_kwargs, label="x2")
    plt.hist(x3, **_kwargs, label="x3")
    plt.legend()
    plt.title("Same bins, with a legend")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A figure holds the picture. An axes is where `plot` draws. One axes can hold several lines.
    - `color`, `linestyle`, and a format string such as `'--g'` change the look of a line. `legend`, `title`, `xlim`, `ylim`, and `axis` describe and frame it.
    - `errorbar` draws a point and a bar. The returned container holds the data line, the caps, and the bar collections. `fmt`, `color`, and `ecolor` style those pieces separately.
    - `hist` returns the counts, the edges, and the patches. `bins`, `alpha`, and `density` change the bars. Several samples can share one axes when the bars are partly transparent.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 4.
    """)
    return


if __name__ == "__main__":
    app.run()
