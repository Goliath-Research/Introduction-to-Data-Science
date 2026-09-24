import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd

    # A lesson draws many figures. This stops the warning about how many are open.
    plt.rcParams["figure.max_open_warning"] = 0
    return mo, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # DataFrame Visualizations

    ## Objectives

    - Build a chart from a pandas Series or DataFrame with `plot`, and choose the chart with `kind`.
    - Compare categories with vertical bars, horizontal bars, pie charts, and stacked bars.
    - Read the shape of a numeric column from a histogram, a density curve, an area plot, and a box plot.
    - Show how two numeric columns move together with a scatter plot.

    ## Background

    Pandas can draw a chart directly from a table. You choose the column and the kind of chart. Matplotlib does the drawing, so `matplotlib.pyplot` is imported as `plt` and each chart is given its own figure. That keeps one chart from being drawn on top of another when a cell runs again.

    ## Datasets Used

    The examples use the **tips** dataset: 244 restaurant bills. Each row records the total bill, the tip, the size of the party, the sex of the person who paid, whether that person smokes, the day, and the time (lunch or dinner). The file is read from the internet, so this lesson needs a network connection.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Loading the tips dataset

    `read_csv` builds a DataFrame from a CSV file. `info` lists the columns, the type of each column, and how many values are missing. `head` shows the first five rows.
    """)
    return


@app.cell
def _(pd):
    path = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    df = pd.read_csv(path)
    df.info()
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Males and females

    `value_counts` counts the rows in each category. This table has 157 males and 87 females.

    A bar chart draws one rectangle per category. The rectangles have the same width and different heights. `kind='bar'` draws vertical bars. `kind='barh'` draws horizontal bars.

    `rot` is the angle of the tick labels, in degrees. `True` is the number `1`, so `rot=True` turns the labels by one degree. `rot=90` stands the labels upright.

    A pie chart divides a circle into slices. Each slice is one category's share of the total. The `title` argument puts a title on the chart.
    """)
    return


@app.cell
def _(df):
    sex_counts = df.sex.value_counts()
    print(sex_counts)
    return (sex_counts,)


@app.cell
def _(plt, sex_counts):
    _figure, _axes = plt.subplots()
    sex_counts.plot(kind="bar", ax=_axes, title="Sex")
    return


@app.cell
def _(plt, sex_counts):
    _figure, _axes = plt.subplots()
    sex_counts.plot(kind="bar", rot=True, ax=_axes, title="Sex, rot=True")
    return


@app.cell
def _(plt, sex_counts):
    _figure, _axes = plt.subplots()
    sex_counts.plot(kind="bar", rot=45, ax=_axes, title="Sex, rot=45")
    return


@app.cell
def _(plt, sex_counts):
    _figure, _axes = plt.subplots()
    sex_counts.plot(kind="barh", ax=_axes, title="Sex, horizontal bars")
    return


@app.cell
def _(plt, sex_counts):
    _figure, _axes = plt.subplots()
    sex_counts.plot(kind="pie", ax=_axes, title="Sex Distribution")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `category` to `"day"`, `"time"`, or `"smoker"`, then run the cell.
    """)
    return


@app.cell
def _(df, plt):
    category = "time"
    _figure, _axes = plt.subplots()
    df[category].value_counts().plot(kind="bar", ax=_axes, title=category)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Smokers and non-smokers

    The same count-and-pie steps work for any category column. Here the column is `smoker`.
    """)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots()
    df.smoker.value_counts().plot(kind="pie", ax=_axes, title="Smoke Distribution")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Two categories together

    `pd.crosstab` counts every pair of values. The first argument becomes the rows and the second becomes the columns.

    `kind='bar'` draws one group of bars for each row. `stacked=True` puts the columns of a row on top of each other, so the height of a stack is the row total.
    """)
    return


@app.cell
def _(df, pd):
    sex_smoker = pd.crosstab(df.sex, df.smoker)
    print(sex_smoker)
    return (sex_smoker,)


@app.cell
def _(plt, sex_smoker):
    _figure, _axes = plt.subplots()
    sex_smoker.plot(kind="bar", rot=0, ax=_axes, title="Sex and smoker")
    return


@app.cell
def _(plt, sex_smoker):
    _figure, _axes = plt.subplots()
    sex_smoker.plot(kind="bar", rot=0, stacked=True, ax=_axes, title="Sex and smoker, stacked")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day and time

    `day` and `time` are another pair of categories. Lunch and dinner are not spread evenly across the week. Read the table first, then compare the grouped bars with the stacked bars.
    """)
    return


@app.cell
def _(df, pd):
    day_time = pd.crosstab(df.day, df.time)
    print(day_time)
    return (day_time,)


@app.cell
def _(day_time, plt):
    _figure, _axes = plt.subplots()
    day_time.plot(kind="bar", rot=0, ax=_axes, title="Day and time")
    return


@app.cell
def _(day_time, plt):
    _figure, _axes = plt.subplots()
    day_time.plot(kind="bar", rot=0, stacked=True, ax=_axes, title="Day and time, stacked")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Histograms

    A histogram summarizes a numeric column. The range of values is split into adjacent bins. Each bar's height is the number of values that fall in that bin. The bars touch, because the bins cover the number line without gaps. A bar chart does not do this: its bars are separate categories, and the spaces between them are not part of the scale.

    `total_bill` is numeric. `bins` is the number of intervals. More bins show more detail and less of the overall shape. Each choice of `bins` is its own chart.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Default number of bins:
    """)
    return


@app.cell
def _(df, plt):
    default_histogram, _axes = plt.subplots()
    df.total_bill.plot(kind="hist", title="Total Bill", ax=_axes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bins=30`:
    """)
    return


@app.cell
def _(df, plt):
    histogram_30_bins, _axes = plt.subplots()
    df.total_bill.plot(kind="hist", bins=30, title="Total Bill, 30 bins", ax=_axes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bins=50`:
    """)
    return


@app.cell
def _(df, plt):
    histogram_50_bins, _axes = plt.subplots()
    df.total_bill.plot(kind="hist", bins=50, title="Total Bill, 50 bins", ax=_axes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `bins` and run the cell again. Try a small number, such as 5, and a large number, such as 40.
    """)
    return


@app.cell
def _(df, plt):
    bins = 10
    _figure, _axes = plt.subplots()
    df.total_bill.plot(kind="hist", bins=bins, title=f"Total Bill, {bins} bins", ax=_axes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Density curve

    A kernel density estimate draws a smooth curve in place of the histogram bars. The area under the curve represents probability. `kind='density'` asks pandas for that curve.
    """)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots()
    df.total_bill.plot(kind="density", title="Total Bill", ax=_axes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Area and line

    `kind='area'` fills the space under the line. `kind='line'` draws only the line. Both charts use the row order of `total_bill`, not the size of the bill, as the horizontal position. `figsize=(10, 5)` sets the width and height in inches.
    """)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots()
    df.total_bill.plot(kind="area", title="Total Bill", ax=_axes)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots(figsize=(10, 5))
    df.total_bill.plot(kind="area", title="Total Bill, wider figure", ax=_axes)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots(figsize=(10, 5))
    df.total_bill.plot(kind="line", title="Total Bill", ax=_axes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Box plots

    A box plot uses the quartiles of a numeric column. The line inside the box is the median, the 50% point. The bottom and top of the box are the first quartile (25%) and the third quartile (75%). Points far from the box are drawn as separate dots.

    `boxplot` can split that summary by one or more categories. `column` is the numeric column. `by` is the category, or a list of categories.
    """)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots()
    df.total_bill.plot(kind="box", title="Total Bill", ax=_axes)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots(figsize=(10, 5))
    df.boxplot(column=["total_bill"], by=["sex"], ax=_axes)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots(figsize=(10, 5))
    df.boxplot(column=["total_bill"], by=["sex", "smoker"], ax=_axes)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots(figsize=(10, 5))
    df.boxplot(column=["total_bill"], by=["day"], ax=_axes)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots(figsize=(10, 5))
    df.boxplot(column=["total_bill"], by=["time"], ax=_axes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Scatter plot

    A scatter plot places one point per row. The horizontal position is one numeric column and the vertical position is another. Here each point is one bill: `total_bill` across, `tip` up. Bills and tips tend to rise together, and a few large bills sit far to the right.
    """)
    return


@app.cell
def _(df, plt):
    _figure, _axes = plt.subplots()
    df.plot("total_bill", "tip", kind="scatter", ax=_axes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the two column names. `size` is another numeric column.
    """)
    return


@app.cell
def _(df, plt):
    horizontal = "total_bill"
    vertical = "tip"
    _figure, _axes = plt.subplots()
    df.plot(horizontal, vertical, kind="scatter", ax=_axes, title=f"{vertical} and {horizontal}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `Series.plot` and `DataFrame.plot` draw the chart. `kind` selects bars, a pie, a histogram, a density curve, an area, a line, a box, or a scatter.
    - `value_counts` and `crosstab` build the tables those category charts display. `stacked=True` piles the columns of each row into one bar.
    - A histogram counts values in neighboring bins. A density curve smooths that shape. A box plot marks the median and the two quartiles.
    - A scatter plot uses two numeric columns. The pattern of the points is the relationship.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 4.
    """)
    return


if __name__ == "__main__":
    app.run()
