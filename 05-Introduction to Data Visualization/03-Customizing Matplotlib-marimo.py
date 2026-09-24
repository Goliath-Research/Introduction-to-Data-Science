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
    # Customizing Matplotlib Graphs

    ## Objectives

    - Choose a color and a marker with a format string such as `'ro'`, `'g^'`, or `'ks'`.
    - Place several charts in one figure with `subplot`.
    - Label a histogram, set its bins and its opacity, and write text on the axes, including Greek letters.
    - Read a two-dimensional distribution with `hist2d` and `hexbin`, and point at a feature with `annotate`.

    ## Background

    Almost every piece of a Matplotlib chart can be changed: the marker, the color, the title, the tick labels, and the text written on the axes. Subplots put several of those charts into one figure so they can be compared.

    Each example that is its own chart starts a new figure. Shared data, such as the normal sample `x`, is created once and reused.

    ## Datasets Used

    The numbers are created with NumPy. The normal sample and the two-dimensional sample use a seed, so the charts stay the same when the cell runs again.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Markers and format strings

    `plt.plot` with one list uses the positions `0, 1, 2, ...` as the horizontal coordinates and the list as the heights.

    Passing two lists sets both coordinates. A third argument is a format string: a color letter plus a marker shape.

    - `'ro'` is red circles
    - `'g^'` is green triangles
    - `'ks'` is black squares

    `plt.axis([xmin, xmax, ymin, ymax])` sets the ranges. A line and a marker can be drawn with two `plot` calls. `plt.title` adds the title.
    """)
    return


@app.cell
def _(plt):
    _figure = plt.figure()
    plt.plot([2, 3, 5, 6])
    plt.title("One list: positions 0, 1, 2, 3")
    return _figure


@app.cell
def _(plt):
    _figure = plt.figure()
    plt.plot([0, 1, 2, 3], [2, 3, 5, 6])
    plt.title("Two lists")
    return _figure


@app.cell
def _(plt):
    _figure = plt.figure()
    plt.plot([0, 1, 2, 3], [2, 3, 5, 6], "ro")
    plt.axis([-0.1, 3.1, 0, 6.4])
    plt.title("Red circles")
    return _figure


@app.cell
def _(plt):
    _figure = plt.figure()
    plt.plot([0, 1, 2, 3], [2, 3, 5, 6], "g^")
    plt.axis([-0.1, 3.1, 0, 6.4])
    plt.title("Green triangles")
    return _figure


@app.cell
def _(plt):
    _figure = plt.figure()
    plt.plot([0, 1, 2, 3], [2, 3, 5, 6], "ks")
    plt.axis([-0.1, 3.1, 0, 6.4])
    plt.title("Black squares")
    return _figure


@app.cell
def _(plt):
    _figure = plt.figure()
    plt.plot([0, 1, 2, 3], [2, 3, 5, 6])
    plt.plot([0, 1, 2, 3], [2, 3, 5, 6], "bo")
    plt.axis([-0.1, 3.1, 0, 6.4])
    plt.title("Four Points")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `fmt` to another color and marker. `'bD'` is blue diamonds. `'m*'` is magenta stars.
    """)
    return


@app.cell
def _(plt):
    fmt = "ro"
    _figure = plt.figure()
    plt.plot([0, 1, 2, 3], [2, 3, 5, 6], fmt)
    plt.axis([-0.1, 3.1, 0, 6.4])
    plt.title(fmt)
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Subplots

    `plt.subplot(nrows, ncols, index)` selects one cell of a grid and makes it the current axes.

    - `nrows` is the number of rows.
    - `ncols` is the number of columns.
    - `index` counts from 1, left to right and top to bottom.

    `subplot(1, 4, 1)` is the first cell of a single row of four. `subplot(221)` is the same call written as one number: 2 rows, 2 columns, cell 1.

    The four cells below are a bar chart, a scatter plot, a line, and a pie. `plt.suptitle` titles the whole figure, not one cell. `figsize` is the width and height of that figure, in inches.
    """)
    return


@app.cell
def _():
    names = ["A", "B", "C"]
    values = [5, 10, 30]
    return names, values


@app.cell
def _(names, plt, values):
    _figure = plt.figure(figsize=(15, 3))
    plt.subplot(1, 4, 1)
    plt.bar(names, values, alpha=0.8)
    plt.axis([-1, 3, 0, 31])
    plt.subplot(1, 4, 2)
    plt.scatter(names, values)
    plt.axis([-1, 3, 0, 31])
    plt.subplot(1, 4, 3)
    plt.plot(names, values)
    plt.axis([-1, 3, 0, 31])
    plt.subplot(1, 4, 4)
    plt.pie(values, labels=names)
    plt.suptitle("Bar, Scatter, Line, and Pie Charts")
    return _figure


@app.cell
def _(names, plt, values):
    _figure = plt.figure(figsize=(8, 8))
    plt.subplot(221)
    plt.bar(names, values, alpha=0.8)
    plt.axis([-1, 3, 0, 31])
    plt.subplot(222)
    plt.scatter(names, values)
    plt.axis([-1, 3, 0, 31])
    plt.subplot(223)
    plt.plot(names, values)
    plt.axis([-1, 3, 0, 31])
    plt.subplot(224)
    plt.pie(values, labels=names)
    plt.suptitle("Bar, Scatter, Line, and Pie Charts (2x2 Matrix)")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A histogram and its bins

    `np.random.normal(mu, sigma, 10000)` draws 10,000 values from a bell curve with center `mu` and spread `sigma`. The names use the Greek letters μ and σ.

    A bin is one interval on the horizontal axis. The bar height is the number of values in that interval. `bins=20` uses wider intervals than `bins=50`. `facecolor` is the fill color. `alpha` is the opacity. Each choice of `bins` is its own chart.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    mu, sigma = 100, 10
    x = np.random.normal(mu, sigma, 10000)
    print("mu =", mu, " sigma =", sigma)
    print("First 5 values:", x[:5])
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Default number of bins:
    """)
    return


@app.cell
def _(plt, x):
    default_histogram = plt.figure()
    plt.hist(x, facecolor="r", alpha=0.6)
    plt.title("Default bins")
    return default_histogram


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bins=20`:
    """)
    return


@app.cell
def _(plt, x):
    histogram_20_bins = plt.figure()
    plt.hist(x, bins=20, facecolor="r", alpha=0.6)
    plt.title("bins=20")
    return histogram_20_bins


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bins=50`:
    """)
    return


@app.cell
def _(plt, x):
    histogram_50_bins = plt.figure()
    plt.hist(x, bins=50, facecolor="r", alpha=0.6)
    plt.title("bins=50")
    return histogram_50_bins


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Labels, a title, and text

    `xlabel`, `ylabel`, and `title` write text in the usual three places. `fontweight='bold'` thickens the axis labels.

    `title` also accepts `loc` (`'left'`, `'center'`, or `'right'`) and `fontdict`, a dictionary of font settings: `family`, `size`, `weight`, and `color`.

    `plt.text(x, y, words)` writes `words` at the data coordinates `(x, y)`. A raw string, `r'...'`, lets backslashes through. Matplotlib then renders the LaTeX between dollar signs: `r'$\mu=100,\sigma=10$'` becomes μ and σ. The same letters can be typed directly as Unicode.

    The coordinates `65` and `500` sit on the left side of this histogram, around the height of a mid-sized bar. If you change the sample, those coordinates may need to move.
    """)
    return


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="r", alpha=0.6)
    plt.xlabel("x values")
    plt.ylabel("Frequency")
    return _figure


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="r", alpha=0.6)
    plt.xlabel("x values", fontweight="bold")
    plt.ylabel("Frequency", fontweight="bold")
    plt.title("Histogram")
    return _figure


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="r", alpha=0.6)
    plt.xlabel("x values", fontweight="bold")
    plt.ylabel("Frequency", fontweight="bold")
    plt.title(
        "Histogram",
        loc="center",
        fontdict={"family": "serif", "size": 20, "weight": "normal", "color": "black"},
    )
    return _figure


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="r", alpha=0.6)
    plt.xlabel("x values", fontweight="bold")
    plt.ylabel("Frequency", fontweight="bold")
    plt.title(
        "Histogram",
        loc="center",
        fontdict={"family": "serif", "size": 20, "weight": "normal", "color": "black"},
    )
    plt.text(65, 500, r"$\mu=100,\sigma=10$")
    plt.text(65, 400, "μ= 100, σ= 10")
    return _figure


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="r", alpha=0.6)
    plt.xlabel("x values", fontweight="bold")
    plt.ylabel("Frequency", fontweight="bold")
    plt.title(
        "Histogram",
        loc="center",
        fontdict={"family": "serif", "size": 20, "weight": "normal", "color": "black"},
    )
    plt.text(
        65,
        500,
        "μ= 100, σ= 10",
        fontdict={"size": 12, "weight": "bold", "color": "darkred"},
    )
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Color and opacity

    `facecolor` changes the fill. `alpha` changes how solid that fill is. The charts use green, then blue at `alpha=0.6`, `0.4`, and `0.2`. The text color changes with the bars.
    """)
    return


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="g", alpha=0.6)
    plt.xlabel("x values", fontweight="bold")
    plt.ylabel("Frequency", fontweight="bold")
    plt.title(
        "Histogram",
        loc="center",
        fontdict={"family": "serif", "size": 20, "weight": "normal", "color": "black"},
    )
    plt.text(
        65,
        500,
        "μ= 100, σ= 10",
        fontdict={"size": 12, "weight": "bold", "color": "darkgreen"},
    )
    return _figure


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="b", alpha=0.6)
    plt.xlabel("x values", fontweight="bold")
    plt.ylabel("Frequency", fontweight="bold")
    plt.title(
        "Histogram",
        loc="center",
        fontdict={"family": "serif", "size": 20, "weight": "normal", "color": "black"},
    )
    plt.text(
        65,
        500,
        "μ= 100, σ= 10",
        fontdict={"size": 12, "weight": "bold", "color": "darkblue"},
    )
    return _figure


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="b", alpha=0.4)
    plt.xlabel("x values", fontweight="bold")
    plt.ylabel("Frequency", fontweight="bold")
    plt.title(
        "Histogram",
        loc="center",
        fontdict={"family": "serif", "size": 20, "weight": "normal", "color": "black"},
    )
    plt.text(
        65,
        500,
        "μ= 100, σ= 10",
        fontdict={"size": 12, "weight": "bold", "color": "darkblue"},
    )
    return _figure


@app.cell
def _(plt, x):
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor="b", alpha=0.2)
    plt.xlabel("x values", fontweight="bold")
    plt.ylabel("Frequency", fontweight="bold")
    plt.title(
        "Histogram",
        loc="center",
        fontdict={"family": "serif", "size": 20, "weight": "normal", "color": "black"},
    )
    plt.text(
        65,
        500,
        "μ= 100, σ= 10",
        fontdict={"size": 12, "weight": "bold", "color": "darkblue"},
    )
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `face` and `alpha`. Colors can be names such as `"orange"` or letters such as `"g"`.
    """)
    return


@app.cell
def _(plt, x):
    face = "g"
    alpha = 0.5
    _figure = plt.figure()
    plt.hist(x, bins=50, facecolor=face, alpha=alpha)
    plt.xlabel("x values")
    plt.ylabel("Frequency")
    plt.title(f"facecolor={face}, alpha={alpha}")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Two-dimensional histograms

    `hist2d` and `hexbin` count points in a grid instead of along one line. The color of each cell is the count.

    The sample is 10,000 rows from a multivariate normal. `mean` is the center, `(0, 0)`. `cov` is the covariance, which sets the spread and the tilt. `.T` splits the two columns into `point_x` and `point_y`. Those names are not `x`: `x` is already the one-dimensional normal sample.

    `cmap` chooses the color scale. `'Greens'` and `'Blues'` are two of Matplotlib's maps. `gridsize` is the number of hexagons across the grid. `plt.grid(False)` turns the grid lines off so the colored cells are easier to see.
    """)
    return


@app.cell
def _(np):
    np.random.seed(1)
    _mean = [0, 0]
    _cov = [[1, 1], [1, 2]]
    point_x, point_y = np.random.multivariate_normal(_mean, _cov, 10000).T
    return point_x, point_y


@app.cell
def _(plt, point_x, point_y):
    _figure = plt.figure()
    plt.grid(False)
    plt.hist2d(point_x, point_y, bins=30, cmap="Greens")
    plt.title("hist2d, Greens")
    return _figure


@app.cell
def _(plt, point_x, point_y):
    _figure = plt.figure()
    plt.grid(False)
    plt.hexbin(point_x, point_y, gridsize=30, cmap="Greens")
    plt.title("hexbin, Greens")
    return _figure


@app.cell
def _(plt, point_x, point_y):
    _figure = plt.figure()
    plt.grid(False)
    plt.hexbin(point_x, point_y, gridsize=30, cmap="Blues")
    plt.title("hexbin, Blues")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Annotations with arrows

    `text` only writes words. `annotate` writes words and can draw an arrow from the words to a point.

    This chart is a new example, a sine wave, not the histogram above. `xy` is the point being marked. `xytext` is where the words sit. `arrowprops` describes the arrow. `facecolor` is the arrow color.
    """)
    return


@app.cell
def _(np, plt):
    _figure = plt.figure()
    _wave_x = np.arange(0.0, 6.0, 0.01)
    _wave_y = np.sin(2 * np.pi * _wave_x)
    plt.plot(_wave_x, _wave_y)
    plt.annotate(
        "local max",
        xy=(2.3, 1),
        xytext=(3, 1.5),
        arrowprops=dict(facecolor="darkgreen"),
    )
    plt.annotate(
        "local min",
        xy=(2.8, -1),
        xytext=(3.5, -1.5),
        arrowprops=dict(facecolor="darkred"),
    )
    plt.ylim(-2, 2)
    plt.show()
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A format string sets the color and the marker in one argument. Two `plot` calls can put a line and a marker on the same points.
    - `subplot(nrows, ncols, index)` picks one cell of a grid. `suptitle` names the whole figure.
    - `bins`, `facecolor`, and `alpha` change a histogram. `xlabel`, `ylabel`, `title`, and `text` write on it. A raw string between `$` signs is rendered as LaTeX.
    - `hist2d` and `hexbin` color a grid by how many points fall in each cell. `annotate` points at one place on a chart.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 4.
    """)
    return


if __name__ == "__main__":
    app.run()
