# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "matplotlib",
#     "numpy",
#     "seaborn",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns

    # A lesson draws many figures. This stops the warning about how many are open.
    plt.rcParams["figure.max_open_warning"] = 0

    return mo, np, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Categorical Plots in Seaborn

    ## Objectives

    - Place a numeric column against a category with a strip plot and a swarm plot.
    - Compare the distribution in each category with a box plot, a boxen plot, and a violin plot.
    - Summarize a category with a count, a point and its uncertainty, or a bar of the mean, the median, or the sum.
    - Split a categorical chart by a second category with `hue`, `col`, `row`, and `split`.

    ## Background

    `catplot` is the general function for a categorical chart. `kind` chooses the chart. The same charts have shorter names: `stripplot`, `swarmplot`, `boxplot`, `boxenplot`, `violinplot`, `countplot`, `pointplot`, and `barplot`. Those shorter functions draw on one axes. `catplot` builds the figure, including extra panels from `col` and `row`.

    ## Datasets Used

    The examples use Seaborn's **tips** dataset. `sns.load_dataset` downloads it, so this lesson needs a network connection. `day` is the category used most often. `total_bill` is the numeric column.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Loading the tips dataset
    """)
    return


@app.cell
def _(sns):
    tips = sns.load_dataset("tips")
    return (tips,)


@app.cell
def _(mo, tips):
    mo.Html(tips.head().to_html())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Strip plot

    A strip plot is a scatter plot whose horizontal axis is a category. Points that share a day would sit on one vertical line, so Seaborn shifts them sideways by a small random amount. That shift is the jitter. It does not change the data. It only makes the points easier to see.

    `kind='strip'` is the default, so the first two calls are the same chart. `stripplot` is the axes-level version of that call.
    """)
    return


@app.cell
def _(sns, tips):
    sns.catplot(data=tips, x="day", y="total_bill")


@app.cell
def _(sns, tips):
    sns.catplot(data=tips, x="day", y="total_bill", kind="strip")


@app.cell
def _(plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.stripplot(data=tips, x="day", y="total_bill", ax=_axes)
    _axes.set_title("stripplot")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Category order

    `order` is the list of categories from left to right. Values not in the list are left out. `set(title=...)` writes the title on the chart that `catplot` returns.

    `jitter=False` turns the sideways shift off, so every bill on a given day shares one vertical line.
    """)
    return


@app.cell
def _(sns, tips):
    category_order = ["Sat", "Sun", "Thur", "Fri"]
    print(category_order)
    return (category_order,)


@app.cell
def _(category_order, sns, tips):
    sns.catplot(data=tips, x="day", y="total_bill", order=category_order)


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, x="day", y="total_bill", order=category_order
    ).set(title="Total Bill by Day")


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="strip",
        order=category_order,
        jitter=False,
    ).set(title="Total Bill by Day, jitter off")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Reorder `your_order`. The days in the list are drawn, and they are drawn in that sequence.
    """)
    return


@app.cell
def _(sns, tips):
    your_order = ["Fri", "Thur", "Sat", "Sun"]
    sns.catplot(
        data=tips, x="day", y="total_bill", order=your_order
    ).set(title="Your order")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Draw a strip plot of `tip` by `time`, with `"Dinner"` first and `"Lunch"` second, and the jitter turned off. Title it "Tip by time". Replace `None` with your code. Does turning the jitter off change the data?
    """)
    return


@app.cell
def _():
    student_time_strip = None
    student_time_strip
    return (student_time_strip,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_time_strip = sns.catplot(
    data=tips, x="time", y="tip", order=["Dinner", "Lunch"], jitter=False
).set(title="Tip by time")
```
No. The jitter only moves points sideways for display. With it off, tips of the same amount sit on top of each other and are harder to count.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Swarm plot

    A swarm plot also puts points on a category axis. Instead of a random shift, it nudges points apart until they do not overlap. The width of the swarm shows how many bills sit near that amount. A wide swarm is a dense part of the data.

    `swarmplot` is the axes-level version. Swapping `x` and `y` lays the categories on the vertical axis.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, x="day", y="total_bill", kind="swarm", order=category_order
    ).set(title="Total Bill by Day")


@app.cell
def _(category_order, plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.swarmplot(
        x="day", y="total_bill", data=tips, order=category_order, ax=_axes
    )
    _axes.set_title("swarmplot")
    return _figure


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, y="day", x="total_bill", kind="swarm", order=category_order
    ).set(title="Total Bill by Day")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Box plot

    `kind='box'` draws the quartiles. The line in the box is the median. The ends of the box are the 25% and 75% points. The black dots are points far from the rest of that day's bills.

    `boxplot` is the same chart on one axes.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, x="day", y="total_bill", kind="box", order=category_order
    ).set(title="Total Bill by Day")


@app.cell
def _(category_order, plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.boxplot(
        x="day", y="total_bill", data=tips, order=category_order, ax=_axes
    ).set(title="Total Bill by Day")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Boxen plot

    A boxen plot is a box plot with more quantiles drawn, so the shape of the distribution is visible further into the tails. It is still a summary, not the individual points.

    `showfliers=False` hides the outlier dots. `boxenplot` is the axes-level version.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, x="day", y="total_bill", kind="boxen", order=category_order
    ).set(title="Total Bill by Day")


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="boxen",
        order=category_order,
        showfliers=False,
    ).set(title="Total Bill by Day, outliers hidden")


@app.cell
def _(category_order, plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.boxenplot(
        x="day",
        y="total_bill",
        data=tips,
        order=category_order,
        showfliers=False,
        ax=_axes,
    ).set(title="Total Bill by Day")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Violin plot

    A violin plot uses the same categories as a box plot and adds a density curve on each side. The width at a bill amount is the estimated density of bills near that amount.

    `inner` chooses what is drawn inside the violin:

    - `'box'` draws a small box plot. This is the default.
    - `'quartiles'` draws the quartile lines.
    - `'point'` draws a point for each observation.
    - `'stick'` draws a short line for each observation.
    - `None` draws only the outline.

    `violinplot` is the axes-level version, with the default inner box.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="violin",
        inner="box",
        order=category_order,
    ).set(title="Total Bill by Day, inner='box'")


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="violin",
        inner="quartiles",
        order=category_order,
    ).set(title="Total Bill by Day, inner='quartiles'")


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="violin",
        inner="point",
        order=category_order,
    ).set(title="Total Bill by Day, inner='point'")


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="violin",
        inner="stick",
        order=category_order,
    ).set(title="Total Bill by Day, inner='stick'")


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="violin",
        inner=None,
        order=category_order,
    ).set(title="Total Bill by Day, inner=None")


@app.cell
def _(category_order, plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.violinplot(
        x="day", y="total_bill", data=tips, order=category_order, ax=_axes
    ).set(title="violinplot")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Draw a violin plot of `tip` by `day`, using `category_order`, with the quartile lines inside. Title it "Tip by Day". Replace `None` with your code. What does the width of a violin at one tip amount represent?
    """)
    return


@app.cell
def _():
    student_tip_violin = None
    student_tip_violin
    return (student_tip_violin,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_tip_violin = sns.catplot(
    data=tips,
    x="day",
    y="tip",
    kind="violin",
    inner="quartiles",
    order=category_order,
).set(title="Tip by Day")
```
The width is the estimated density of tips near that amount on that day. A wide part means many tips close to that value.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Count plot

    `kind='count'` drops `y`. There is nothing to measure except how many rows fall in each category. The bar height is that count. Putting the category on `y` makes the bars horizontal. `countplot` is the axes-level version.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, x="day", kind="count", order=category_order
    ).set(title="Number of Days")


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, y="day", kind="count", order=category_order
    ).set(title="Number of Days")


@app.cell
def _(category_order, plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.countplot(x="day", data=tips, order=category_order, ax=_axes).set(
        title="Number of Days"
    )
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Point plot

    `kind='point'` marks one estimate per category and draws a bar for the uncertainty around it. The default estimate is the mean, `np.mean`. `estimator` replaces that function. `np.median` marks the middle bill instead of the average.

    The points are joined by a line. `linestyle='--'` makes that line dashed. `linestyle='none'` removes it. Swapping `x` and `y` runs the categories down the side. `pointplot` is the axes-level version.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, x="day", y="total_bill", kind="point", order=category_order
    ).set(title="Mean, the default")


@app.cell
def _(category_order, np, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="point",
        estimator=np.mean,
        order=category_order,
    ).set(title="Mean of Total Bill by Day")


@app.cell
def _(category_order, np, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="point",
        estimator=np.median,
        order=category_order,
    ).set(title="Median of Total Bill by Day")


@app.cell
def _(category_order, np, sns, tips):
    sns.catplot(
        data=tips,
        y="day",
        x="total_bill",
        kind="point",
        estimator=np.median,
        order=category_order,
    ).set(title="Median of Total Bill by Day")


@app.cell
def _(category_order, np, sns, tips):
    sns.catplot(
        data=tips,
        y="day",
        x="total_bill",
        kind="point",
        estimator=np.median,
        linestyle="--",
        order=category_order,
    ).set(title="Median of Total Bill by Day")


@app.cell
def _(category_order, np, sns, tips):
    sns.catplot(
        data=tips,
        y="day",
        x="total_bill",
        kind="point",
        estimator=np.median,
        linestyle="none",
        order=category_order,
    ).set(title="Median of Total Bill by Day")


@app.cell
def _(category_order, np, plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.pointplot(
        x="day",
        y="total_bill",
        data=tips,
        estimator=np.median,
        order=category_order,
        ax=_axes,
    ).set(title="Median of Total Bill by Day")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Draw a point plot of the median `tip` for each `day`, using `category_order`, with no line joining the points. Title it "Median of Tip by Day". Replace `None` with your code. Does a point show one bill or a summary of many bills?
    """)
    return


@app.cell
def _():
    student_median_tip_points = None
    student_median_tip_points
    return (student_median_tip_points,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_median_tip_points = sns.catplot(
    data=tips,
    x="day",
    y="tip",
    kind="point",
    estimator=np.median,
    linestyle="none",
    order=category_order,
).set(title="Median of Tip by Day")
```
A summary of many bills. Each point is the median tip of every bill on that day. The bar around it shows the uncertainty of that median.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bar plot

    `kind='bar'` draws the mean of `total_bill` for each day. The black line at the top of a bar is a 95% confidence interval for that mean. `errorbar=None` removes those lines.

    `estimator` changes what the bar measures. `np.median` uses the middle bill. `np.sum` uses the total of the bills that day, so a busy day looks taller even when a typical bill does not. `barplot` is the axes-level version of the mean bar.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, x="day", y="total_bill", kind="bar", order=category_order
    ).set(title="Mean of Total Bill by Day")


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="bar",
        errorbar=None,
        order=category_order,
    ).set(title="Mean of Total Bill by Day")


@app.cell
def _(category_order, np, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="bar",
        estimator=np.median,
        order=category_order,
    ).set(title="Median of Total Bill by Day")


@app.cell
def _(category_order, np, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="bar",
        estimator=np.sum,
        order=category_order,
    ).set(title="Sum of Total Bill by Day")


@app.cell
def _(category_order, plt, sns, tips):
    _figure, _axes = plt.subplots()
    sns.barplot(
        x="day", y="total_bill", data=tips, order=category_order, ax=_axes
    ).set(title="Mean of Total Bill by Day")
    return _figure


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Draw a bar plot of the sum of `tip` for each `day`, using `category_order`, with no error bars. Title it "Sum of Tip by Day". Replace `None` with your code. Why can a day have a tall bar even when its typical tip is small?
    """)
    return


@app.cell
def _():
    student_tip_sum_bars = None
    student_tip_sum_bars
    return (student_tip_sum_bars,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_tip_sum_bars = sns.catplot(
    data=tips,
    x="day",
    y="tip",
    kind="bar",
    estimator=np.sum,
    errorbar=None,
    order=category_order,
).set(title="Sum of Tip by Day")
```
A sum grows with the number of bills. A busy day adds up many tips, so its bar is tall even when each tip is ordinary.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A second category

    `hue` assigns a color to each value of another category. The strip and the swarm then show smokers and non-smokers side by side within each day.

    `col` adds a panel for each value of `time`, so lunch and dinner are separate charts. `row` adds a panel for each value of `sex`.

    On a violin, `split=True` uses one half of the violin for each hue instead of two full violins. `inner='stick'` draws a line for each bill inside those halves. The last chart turns the categories onto the vertical axis.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips, x="day", y="total_bill", order=category_order, hue="smoker"
    )


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="swarm",
        order=category_order,
        hue="smoker",
    )


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="box",
        order=category_order,
        hue="smoker",
        col="time",
    )


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="boxen",
        order=category_order,
        hue="smoker",
        col="time",
    )


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="violin",
        order=category_order,
        hue="smoker",
        col="time",
        row="sex",
    )


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind="violin",
        order=category_order,
        hue="smoker",
        inner="stick",
        split=True,
    )


@app.cell
def _(category_order, sns, tips):
    sns.catplot(
        data=tips,
        y="day",
        x="total_bill",
        kind="violin",
        order=category_order,
        hue="smoker",
        inner="stick",
        split=True,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `kind` to `"box"`, `"violin"`, `"bar"`, or `"point"`.
    """)
    return


@app.cell
def _(category_order, sns, tips):
    kind = "swarm"
    sns.catplot(
        data=tips,
        x="day",
        y="total_bill",
        kind=kind,
        order=category_order,
        hue="smoker",
    ).set(title=kind)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Draw a box plot of `tip` by `day`, using `category_order`, split by `sex` with `hue`, and with one panel per `time`. Replace `None` with your code. Why are some days empty in the Lunch panel?
    """)
    return


@app.cell
def _():
    student_tip_boxes = None
    student_tip_boxes
    return (student_tip_boxes,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_tip_boxes = sns.catplot(
    data=tips,
    x="day",
    y="tip",
    kind="box",
    order=category_order,
    hue="sex",
    col="time",
)
```
The table has no lunch bills on Saturday or Sunday. A panel can only draw a box where there are rows.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    - `catplot` chooses the chart with `kind`. The matching function, such as `boxplot` or `barplot`, draws that one chart on an axes.
    - A strip plot jitters points so they can be seen. A swarm plot places the same points so they do not overlap.
    - A box plot marks the quartiles. A boxen plot adds more quantiles. A violin plot adds the density, and `inner` chooses what sits inside it.
    - A count is how many rows. A point or a bar is a summary of the numbers, by default the mean. `estimator` can replace that summary with the median or the sum.
    - `hue`, `col`, and `row` split the chart by more categories. `split=True` gives each hue one half of a violin.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 4.
    - [seaborn.catplot](https://seaborn.pydata.org/generated/seaborn.catplot.html)
    """)
    return


if __name__ == "__main__":
    app.run()
