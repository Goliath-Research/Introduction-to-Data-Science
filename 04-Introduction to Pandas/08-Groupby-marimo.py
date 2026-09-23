import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd

    return mo, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Pandas Groupby

    ## Objectives

    - Split a DataFrame into groups with `groupby`.
    - Summarize each group with `agg` and with shortcuts such as `mean` and `sum`.
    - Compute a new value for every original row with `transform`.
    - Keep or drop whole groups with `filter`.

    ## Background

    A groupby operation has three steps:

    1. Split the rows into groups.
    2. Apply a function to each group on its own.
    3. Combine the results.

    The function can do one of three jobs:

    1. **Aggregation** returns one summary for each group.
    2. **Transformation** returns a new value for each original row.
    3. **Filtration** keeps or drops whole groups.

    ## Datasets Used

    This lesson does not use an external dataset. The table is a small set of teams, with a rank, a year, and a points total.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The groupby method
    """)
    return


@app.cell
def _(pd):
    data = {
        'Team': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'A', 'D', 'D', 'A'],
        'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
        'Year': [2018, 2019, 2018, 2019, 2018, 2019, 2020, 2021, 2020, 2018, 2019, 2021],
        'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690],
    }
    df = pd.DataFrame(data)
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `groupby('Team')` splits the rows by the team label. The result is a groupby object, not a DataFrame yet. `groups` shows the row positions in each team. `size` counts the rows. `ngroups` is the number of teams. `groups.keys()` is the team labels.

    Grouping by `Team` and `Year` together makes a finer split: one group for each pair.
    """)
    return


@app.cell
def _(df):
    df.groupby('Team')
    return


@app.cell
def _(df):
    print(df.groupby('Team').groups)
    print(df.groupby('Team').size())
    print('Number of teams =', df.groupby('Team').ngroups)
    df.groupby('Team').groups.keys()
    return


@app.cell
def _(df):
    print(df.groupby(['Team', 'Year']).groups)
    print('Number of groups =', df.groupby(['Team', 'Year']).ngroups)
    df.groupby(['Team', 'Year']).groups.keys()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A groupby object can be looped over. Each step gives the group name and the rows in that group. `get_group` selects one group by its name. The object `t` is reused by the aggregation, transformation, and filter cells below.
    """)
    return


@app.cell
def _(df):
    t = df.groupby('Team')
    for name, group in t:
        print(name)
        print(group)
    return (t,)


@app.cell
def _(t):
    print(t.get_group('A'))
    t.get_group('D')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Aggregation

    An aggregation returns one value for each group. `agg` accepts one function name or a list of them. `sum`, `mean`, and `median` are shortcuts for a single summary.

    `Team` is the group label, so these calls summarize `Rank` and `Points` only.
    """)
    return


@app.cell
def _(t):
    t[['Rank', 'Points']].agg('mean')
    return


@app.cell
def _(t):
    t[['Rank', 'Points']].agg(['size', 'mean', 'sum'])
    return


@app.cell
def _(t):
    t['Points'].agg(['size', 'mean', 'std'])
    return


@app.cell
def _(t):
    print(t[['Rank', 'Points']].sum())
    print(t[['Rank', 'Points']].mean())
    t[['Rank', 'Points']].median()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Transformation

    `transform` returns a DataFrame with the same shape and the same index as the numeric columns it receives. The function `score` turns each group into a standardized value: the distance from that group's mean, divided by that group's standard deviation.

    `Team` is text, so `transform` standardizes `Rank`, `Year`, and `Points`.

    The second call writes each team's mean points onto every row of that team. Rows 2 and 3 are team B, and both show `768.0`. The result has one value per original row.
    """)
    return


@app.cell
def _():
    score = lambda x: (x - x.mean()) / x.std()
    return (score,)


@app.cell
def _(t, score):
    t.transform(score)
    return


@app.cell
def _(t):
    t.groups
    return


@app.cell
def _(t):
    t['Points'].transform(lambda x: x.mean())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Filtration

    `filter` keeps every row of a group that passes the test, and drops the other groups.

    - `len(x) == 2` keeps teams with exactly two rows.
    - `x['Points'].min() > 700` keeps teams whose lowest points total is above 700.
    - `x['Rank'].max() == 4` keeps teams that contain the rank 4.
    - `x['Year'].count() == 2` keeps teams with exactly two non-missing years.
    """)
    return


@app.cell
def _(t):
    t.groups
    return


@app.cell
def _(t):
    t.filter(lambda x: len(x) == 2)
    return


@app.cell
def _(t):
    t.filter(lambda x: x['Points'].min() > 700)
    return


@app.cell
def _(t):
    t.filter(lambda x: x['Rank'].max() == 4)
    return


@app.cell
def _(t):
    filtered = t.filter(lambda x: x['Year'].count() == 2)
    filtered
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In summary:

    - Use `aggregate`, or a shortcut such as `mean`, when you want one value for each group.
    - Use `transform` when you want a new value for each original row.
    - Use `filter` when you want a subset of the original rows, chosen by a rule about the whole group.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Group `practice` by `Team` and compute the mean of `Points`.
    """)
    return


@app.cell
def _(pd):
    practice = pd.DataFrame({
        'Team': ['A', 'A', 'B', 'B'],
        'Points': [10, 30, 20, 40],
    })
    practice.groupby('Team')['Points'].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `groupby` splits the rows. `groups`, `size`, `ngroups`, and `get_group` describe those groups.
    - Aggregation (`agg`, `sum`, `mean`, `median`) reduces each group to a summary.
    - `transform` keeps the original rows and index, and fills them with a group calculation.
    - `filter` keeps or drops entire groups. The rows that remain still have their original columns.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 3.
    """)
    return


if __name__ == "__main__":
    app.run()
