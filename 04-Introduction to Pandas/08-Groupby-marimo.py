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
def _(mo, pd):
    data = {
        'Team': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'A', 'D', 'D', 'A'],
        'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
        'Year': [2018, 2019, 2018, 2019, 2018, 2019, 2020, 2021, 2020, 2018, 2019, 2021],
        'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690],
    }
    df = pd.DataFrame(data)
    mo.Html(df.to_html())
    return df, data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `groupby('Team')` splits the rows by the team label. The result is a groupby object, not a DataFrame yet.
    """)
    return


@app.cell
def _(df):
    df.groupby('Team')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `groups` shows the row labels in each team. Team `A` has the rows 0, 1, 8, and 11.
    """)
    return


@app.cell
def _(df):
    df.groupby('Team').groups
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `size` counts the rows in each team.
    """)
    return


@app.cell
def _(df):
    df.groupby('Team').size()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `ngroups` is the number of teams.
    """)
    return


@app.cell
def _(df):
    df.groupby('Team').ngroups
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `groups.keys()` is the team labels.
    """)
    return


@app.cell
def _(df):
    df.groupby('Team').groups.keys()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Grouping by `Team` and `Year` together makes a finer split: one group for each pair. Each team has at most one row per year, so every group here has one row.
    """)
    return


@app.cell
def _(df):
    df.groupby(['Team', 'Year']).groups
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are 12 pairs, one for each row of `df`.
    """)
    return


@app.cell
def _(df):
    df.groupby(['Team', 'Year']).ngroups
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The group names are now `(Team, Year)` tuples.
    """)
    return


@app.cell
def _(df):
    df.groupby(['Team', 'Year']).groups.keys()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A groupby object can be looped over. Each step gives the group name and the rows in that group. The object `t` is reused by the aggregation, transformation, and filter cells below.
    """)
    return


@app.cell
def _(df, mo):
    t = df.groupby('Team')
    mo.vstack([
        mo.vstack([mo.md(f'`{name}`'), mo.Html(group.to_html())])
        for name, group in t
    ])
    return (t,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `get_group` selects one group by its name. These are the rows of team `A`:
    """)
    return


@app.cell
def _(mo, t):
    mo.Html(t.get_group('A').to_html())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the rows of team `D`:
    """)
    return


@app.cell
def _(mo, t):
    mo.Html(t.get_group('D').to_html())
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
def _(mo, t):
    mo.Html(t[['Rank', 'Points']].agg(['size', 'mean', 'sum']).to_html())
    return


@app.cell
def _(t):
    t['Points'].agg(['size', 'mean', 'std'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The shortcuts give one summary each. `sum` adds the values of each team:
    """)
    return


@app.cell
def _(t):
    t[['Rank', 'Points']].sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `mean` is the same result as `agg('mean')` above:
    """)
    return


@app.cell
def _(t):
    t[['Rank', 'Points']].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `median` is the middle value of each team. A team with an even number of rows uses the average of its two middle values.
    """)
    return


@app.cell
def _(t):
    t[['Rank', 'Points']].median()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Compute the sum of `Points` for each group in `t`. Replace `None` with your code. Does the result have one row per original row, or one row per team?
    """)
    return


@app.cell
def _():
    student_team_points = None
    student_team_points
    return (student_team_points,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_team_points = t['Points'].sum()
```
One row per team. `t` is already grouped by `Team`, and `sum` reduces each group to one number.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Transformation

    `transform` returns a DataFrame with the same shape and the same index as the numeric columns it receives. The function `score` turns each group into a standardized value: the distance from that group's mean, divided by that group's standard deviation.

    `Team` is the group label, so it is not part of the result. `transform` standardizes `Rank`, `Year`, and `Points`.

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
    ### Try it yourself

    Use `transform` to write each team's mean `Points` onto every row of that team. Replace `None` with your code. Does the result have the same number of rows as the original table?
    """)
    return


@app.cell
def _():
    student_team_means = None
    student_team_means
    return (student_team_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_team_means = t['Points'].transform(lambda x: x.mean())
```
Yes. `transform` keeps the original rows. Every row of a team shows that team's mean, so teammates share one number.
''')}, lazy=True)
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
def _(mo, t):
    mo.Html(t.filter(lambda x: len(x) == 2).to_html())
    return


@app.cell
def _(mo, t):
    mo.Html(t.filter(lambda x: x['Points'].min() > 700).to_html())
    return


@app.cell
def _(mo, t):
    mo.Html(t.filter(lambda x: x['Rank'].max() == 4).to_html())
    return


@app.cell
def _(mo, t):
    filtered = t.filter(lambda x: x['Year'].count() == 2)
    mo.Html(filtered.to_html())
    return (filtered,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Use `filter` to keep the teams that have exactly two rows. Replace `None` with your code. Are the dropped teams removed one row at a time, or as a whole group?
    """)
    return


@app.cell
def _():
    student_two_years = None
    student_two_years
    return (student_two_years,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_two_years = t.filter(lambda x: len(x) == 2)
```
As a whole group. A team with any other number of rows is dropped entirely. The rows that remain keep their original columns.
''')}, lazy=True)
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
    return (practice,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `groupby` splits the rows. `groups`, `size`, `ngroups`, and `get_group` describe those groups.
    - Aggregation (`agg`, `sum`, `mean`, `median`) reduces each group to a summary.
    - `transform` keeps the original rows and index, and fills them with a group calculation.
    - `filter` keeps or drops entire groups. The rows that remain still have their original columns.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What are the three steps of a groupby operation?
    2. What does an aggregation return for each group?
    3. What is the difference between `sum` and `transform`?
    4. Does `transform` keep the original index?
    5. What does `filter` drop: selected rows inside a group, or a whole group?
    6. What do `size` and `ngroups` report?
    7. What does `get_group` return?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **Split, apply, combine:** The rows are split into groups, a function is applied to each group, and the results are combined.
2. **One summary:** `agg`, `sum`, `mean`, and `median` reduce a group to a summary instead of keeping its rows.
3. **One value per group, or one value per row:** `sum` returns one number per team. `transform` writes a result back onto every original row.
4. **Yes:** The result lines up with the rows that went in.
5. **A whole group:** Every row of a group that fails the test is dropped. The rows that remain keep their original columns.
6. **Rows in each group, and the number of groups:** `size` counts the rows. `ngroups` counts the groups.
7. **One group:** You pass the group name, such as `'A'`, and get the rows in that group.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 3.
    """)
    return


if __name__ == "__main__":
    app.run()
