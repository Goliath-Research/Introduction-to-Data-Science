import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import seaborn as sns

    # A lesson draws many figures. This stops the warning about how many are open.
    plt.rcParams["figure.max_open_warning"] = 0

    return mo, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Introduction to Seaborn

    ## Objectives

    - Draw a statistical chart from a DataFrame by naming the columns.
    - Count a category, and split that count with `hue`.
    - Compare one relationship across groups with `col`, `row`, `hue`, and `size`.
    - Read one numeric column with a histogram or a density curve, two columns with a joint plot, and every pair of columns with `pairplot`.

    ## Background

    Seaborn is built on Matplotlib. It is imported as `sns`. A plotting function takes the DataFrame in `data` and the role of each column by name: `x`, `y`, `hue`, `col`, `row`, and `size`. You describe the chart. Seaborn chooses the labels, the legend, and the facets.

    `countplot` draws on an existing axes, so each of those charts gets its own figure. `relplot`, `displot`, `jointplot`, and `pairplot` create the figure themselves.

    ## Datasets Used

    The examples use Seaborn's **tips** dataset, the same restaurant bills as the pandas plotting lesson. `sns.load_dataset` downloads it, so this lesson needs a network connection.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Loading the tips dataset

    Seaborn's advantages for this course are practical. The calls are short. The functions accept a DataFrame. The drawings sit on top of Matplotlib, so a chart Seaborn cannot make can still be made with `plt`.
    """)
    return


@app.cell
def _(sns):
    print("Seaborn version:", sns.__version__)
    tips = sns.load_dataset("tips")
    return (tips,)


@app.cell
def _(tips):
    tips.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Count plots

    `countplot` draws one bar per category. The bar height is how many rows have that value.

    - `x` puts the categories on the horizontal axis, so the bars are vertical.
    - `y` puts the categories on the vertical axis, so the bars are horizontal.
    - `hue` splits each category by a second column and draws one colored bar per group.

    You can pass a column as a Series, `x=tips.sex`, or pass the DataFrame and the column name, `data=tips, y="time"`. The second form is the one used in the rest of this lesson.
    """)
    return


@app.cell
def _(plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.countplot(x=tips.sex, ax=_axes)
    _axes.set_title("Bills by sex")
    return _figure


@app.cell
def _(plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.countplot(y=tips.time, ax=_axes)
    _axes.set_title("Bills by time")
    return _figure


@app.cell
def _(plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.countplot(x=tips.time, hue=tips.sex, ax=_axes)
    _axes.set_title("Time, split by sex")
    return _figure


@app.cell
def _(plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.countplot(data=tips, y="time", hue="sex", ax=_axes)
    _axes.set_title("Same chart, using column names")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `category` to `"day"` or `"smoker"`.
    """)
    return


@app.cell
def _(plt, sns, tips):
    category = "sex"
    _figure, _axes = plt.subplots()
    sns.countplot(data=tips, x=category, ax=_axes)
    _axes.set_title(category)
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Relationship plots

    `relplot` draws the relationship between two numeric columns. The default is a scatter plot: one point per row.

    - `col` makes one panel per value of that column, arranged in a row of panels.
    - `row` makes one panel per value, arranged in a column of panels.
    - `hue` colors the points by a category.
    - `size` scales each point by a numeric column. In this table `size` is the party size.

    The last chart uses all of those roles at once. The function is still one call. The column names say what each role is for.
    """)
    return


@app.cell
def _(sns, tips):
    sns.relplot(data=tips, x="total_bill", y="tip")


@app.cell
def _(sns, tips):
    sns.relplot(data=tips, x="total_bill", y="tip", col="time")


@app.cell
def _(sns, tips):
    sns.relplot(data=tips, x="total_bill", y="tip", row="sex")


@app.cell
def _(sns, tips):
    sns.relplot(data=tips, x="total_bill", y="tip", col="time", row="sex")


@app.cell
def _(sns, tips):
    sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")


@app.cell
def _(sns, tips):
    sns.relplot(
        data=tips,
        x="total_bill",
        y="tip",
        col="time",
        hue="smoker",
        size="size",
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `split_by`. `"sex"` and `"smoker"` are both categories.
    """)
    return


@app.cell
def _(sns, tips):
    split_by = "time"
    sns.relplot(data=tips, x="total_bill", y="tip", col=split_by)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## One numeric column

    `displot` draws a distribution. With one column, `x`, the default is a histogram: values fall into bins, and the bar height is the count.

    `col` and `hue` work here as they did for `relplot`. `kde=True` lays a density curve over the bars. `kind='kde'` drops the bars and keeps the curve. That curve is an estimate of the probability density. `linewidth` is the thickness of the curve.

    `bins` sets how many histogram intervals are used. `rug=True` adds a small tick for every observation along the edge of the panel.
    """)
    return


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill")


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", col="time")


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", col="time", hue="smoker")


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", col="time", hue="smoker", kde=True)


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", kind="kde")


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", kind="kde", linewidth=5)


@app.cell
def _(sns, tips):
    sns.displot(
        data=tips, x="total_bill", col="time", hue="smoker", kde=True, bins=30
    )


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", col="time", hue="smoker", kind="kde")


@app.cell
def _(sns, tips):
    sns.displot(
        data=tips, x="total_bill", col="time", hue="smoker", kind="kde", rug=True
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Two numeric columns

    Passing both `x` and `y` to `displot` bins the plane into rectangles and colors each rectangle by the count. `cbar=True` adds the color scale.    
    """)
    return


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", y="tip")


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", y="tip", cbar=True)


@app.cell
def _(sns, tips):
    sns.displot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")


@app.cell
def _(sns, tips):
    sns.displot(
        data=tips, x="total_bill", y="tip", col="time", row="sex", hue="smoker"
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Joint plot and pair plot

    `jointplot` draws one relationship in the center and the distribution of each column on the margin.

    `pairplot` does that for every pair of numeric columns. The table below keeps `total_bill`, `tip`, and `time`. `hue="time"` colors lunch and dinner. The diagonal panels are the distribution of one column. The other panels are the pairs.
    """)
    return


@app.cell
def _(sns, tips):
    sns.jointplot(data=tips, x="total_bill", y="tip")


@app.cell
def _(sns, tips):
    sns.jointplot(data=tips, x="total_bill", y="tip", hue="time")


@app.cell
def _(sns, tips):
    _pair_data = tips[["total_bill", "tip", "time"]]
    sns.pairplot(data=_pair_data, hue="time")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `column` to `"tip"` or `"size"`.
    """)
    return


@app.cell
def _(sns, tips):
    column = "total_bill"
    sns.displot(data=tips, x=column, kind="kde")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - Pass the DataFrame as `data` and the column names as `x`, `y`, and `hue`. `countplot` then counts a category, and `hue` splits the count.
    - `relplot` scatters two numeric columns. `col` and `row` make a panel per group. `hue` colors the points. `size` scales them.
    - `displot` is a histogram by default, a density curve with `kind='kde'`, and a colored grid when both `x` and `y` are set.
    - `jointplot` adds the two margins of one pair. `pairplot` draws every pair.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 4.
    - Seaborn documentation: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
    """)
    return


if __name__ == "__main__":
    app.run()
