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
    # DataFrame Basic Functionalities

    ## Objectives

    - Create a DataFrame and inspect its rows, shape, and types.
    - Transpose a table and read or replace its index.
    - Select columns and rows with `[]`, `loc`, and `iloc`.

    ## Background

    This lesson walks through the basic tools for looking at a DataFrame and taking a subset of it. `loc` selects by label. `iloc` selects by position. A slice of positions does not include the stop position. A slice of labels does include the stop label.

    ## Datasets Used

    This lesson does not use an external dataset. The student table is written in the cells.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Basic operations with DataFrames

    Anna has no age. That missing age is `np.nan`.
    """)
    return


@app.cell
def _(np, pd):
    students = {
        'Name': pd.Series(['John', 'Anna', 'Tom', 'Mary', 'Steve', 'Peter', 'Joe']),
        'Age': pd.Series([20, np.nan, 22, 22, 20, 23, 18]),
        'GPA': pd.Series([3.3, 3.6, 3.5, 3.7, 3.0, 2.8, 2.95]),
    }
    df = pd.DataFrame(students)
    df.head(3)
    return df, students


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The last three rows, three random rows, and the shape `(rows, columns)`:
    """)
    return


@app.cell
def _(df):
    print(df.tail(3))
    print('\nThree random rows')
    print(df.sample(3))
    df.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `df.T` transposes the table: rows become columns and columns become rows.

    `df.axes` returns the row labels and the column labels. `df.index` is only the row labels.
    """)
    return


@app.cell
def _(df):
    df.T
    return


@app.cell
def _(df):
    print(df)
    df.axes
    return


@app.cell
def _(df):
    df.index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Assigning to `.index` replaces the row labels. This cell copies `df` first, so the original table keeps its numeric index.
    """)
    return


@app.cell
def _(df):
    labeled = df.copy()
    labeled.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    labeled
    return (labeled,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `set_index` uses an existing column as the row index. Passing a list of columns builds an index with more than one level.

    These calls do not use `inplace=True`, so `labeled` stays as it was. The result is a new DataFrame.
    """)
    return


@app.cell
def _(labeled):
    labeled.set_index('Age')
    return


@app.cell
def _(labeled):
    labeled.set_index(['Name', 'Age'])
    return


@app.cell
def _(labeled):
    labeled
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Use `set_index` to make `Name` the index of `labeled`. Do not pass `inplace=True`. Replace `None` with your code. Does `labeled` itself now use `Name` as its index?
    """)
    return


@app.cell
def _():
    student_by_name = None
    student_by_name
    return (student_by_name,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_by_name = labeled.set_index('Name')
```
No. Without `inplace=True`, `set_index` returns a new DataFrame. `labeled` still has the index `a` through `g`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `reset_index` puts the current index back into a column and uses the default index `0, 1, 2, ...`.

    `drop=True` discards the old index instead of saving it as a column. `inplace=True` changes that DataFrame. The copy below is changed. `labeled` is not.
    """)
    return


@app.cell
def _(labeled):
    labeled.reset_index()
    return


@app.cell
def _(labeled):
    restored = labeled.copy()
    restored.reset_index(drop=True, inplace=True)
    restored
    return (restored,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `columns` is the column names. `dtypes` is the type of each column. `empty` is `True` only when the object has no elements. `size` is the number of elements, rows times columns. `values` is the data as a NumPy array.
    """)
    return


@app.cell
def _(df):
    print(df.columns)
    print(df.dtypes)
    print('empty =', df.empty)
    print('size  =', df.size)
    print('shape =', df.shape)
    return


@app.cell
def _(df):
    v = df.values
    print(type(v))
    print(v)
    v.flatten()
    return (v,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `value_counts` counts how many times each distinct value appears in a column. By default it does not count missing values. `dropna=False` includes them.
    """)
    return


@app.cell
def _(df):
    print(df.Age.value_counts())
    print('\nIncluding missing values')
    df.Age.value_counts(dropna=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Count the distinct values of `df['Age']`, including the missing age. Replace `None` with your code. Does the default `value_counts` count that missing age?
    """)
    return


@app.cell
def _():
    student_age_counts = None
    student_age_counts
    return (student_age_counts,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_age_counts = df['Age'].value_counts(dropna=False)
```
No. The default leaves missing values out. `dropna=False` adds a count for `NaN`. Anna is that one missing age.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Indexing and selecting data

    `[]` and `.` reach a column by name. They are convenient, and they are enough for many selections.

    - `loc` selects by label. A label slice includes the stop label.
    - `iloc` selects by integer position, starting at 0. A position slice includes the start and excludes the end.

    The selection examples use `labeled`, whose index is `a` through `g`.
    """)
    return


@app.cell
def _(labeled):
    labeled
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Select one column, or a list of columns:
    """)
    return


@app.cell
def _(labeled):
    labeled['Age']
    return


@app.cell
def _(labeled):
    labeled[['Age', 'GPA']]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `iloc[:, [1, 2]]` keeps every row and the columns at positions 1 and 2. Those columns are `Age` and `GPA`.
    """)
    return


@app.cell
def _(labeled):
    labeled.iloc[:, [1, 2]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Select rows. `labeled[:'d']` and `labeled.loc[:'d']` keep the labels `a` through `d`, including `d`. `iloc[:4]` keeps the first four positions, which are those same rows.
    """)
    return


@app.cell
def _(labeled):
    labeled[:'d']
    return


@app.cell
def _(labeled):
    labeled.loc[:'d']
    return


@app.cell
def _(labeled):
    labeled.iloc[:4]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Select rows and columns together.

    - `labeled[:3][['Age', 'GPA']]` takes the first three positions, then those two columns.
    - `loc[:'c']` takes labels `a` through `c`, including `c`.
    - `iloc[:3, [1, 2]]` takes the first three positions and the columns at positions 1 and 2.
    """)
    return


@app.cell
def _(labeled):
    labeled[:3][['Age', 'GPA']]
    return


@app.cell
def _(labeled):
    labeled.loc[:'c'][['Age', 'GPA']]
    return


@app.cell
def _(labeled):
    labeled.iloc[:3, [1, 2]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    From `labeled`, keep the labels `'a'` through `'c'` and the columns `Age` and `GPA`, using `loc`. Replace `None` with your code. Is the row labeled `'c'` included?
    """)
    return


@app.cell
def _():
    student_first_students = None
    student_first_students
    return (student_first_students,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_first_students = labeled.loc[:'c', ['Age', 'GPA']]
```
Yes. A label slice includes the stop label. The matching position slice, `iloc[:3, [1, 2]]`, also keeps three rows, but it stops before position 3.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the stop label in `loc` and the stop position in `iloc`. Include `City` in the column list and run the cell again.
    """)
    return


@app.cell
def _(pd):
    practice = pd.DataFrame(
        {'City': ['Rome', 'Oslo', 'Lima', 'Accra'], 'Temp': [18, 7, 22, 29]},
        index=['w', 'x', 'y', 'z'],
    )
    print(practice.loc[:'y', ['City', 'Temp']])
    practice.iloc[:2, [1]]
    return (practice,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `head`, `tail`, `sample`, `shape`, `axes`, `index`, `columns`, `dtypes`, `empty`, `size`, and `values` describe the table.
    - `T` swaps rows and columns.
    - Assigning to `.index` replaces the row labels. `set_index` uses a column as the index. `reset_index` restores a default index. Without `inplace=True`, the original DataFrame is unchanged.
    - `value_counts` counts distinct values. `dropna=False` also counts missing values.
    - `[]` selects columns by name. `loc` selects by label and includes the stop label. `iloc` selects by position and excludes the stop position.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What does `T` exchange?
    2. Does assigning to `.index` change the values in the columns?
    3. What does `set_index` do when `inplace` is not `True`?
    4. What does `value_counts` leave out unless you pass `dropna=False`?
    5. Does a slice of labels include the stop label?
    6. Does a slice of positions include the stop position?
    7. What do `size` and `shape` report?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **Rows and columns:** After the transpose, the old column names are the row labels.
2. **No:** It replaces the row labels. The column values stay in the same order.
3. **It returns a new DataFrame:** The original table keeps its index.
4. **Missing values:** The default counts only values that are present.
5. **Yes:** `loc[:'c']` keeps the row labeled `'c'`.
6. **No:** `iloc[:3]` keeps positions 0, 1, and 2.
7. **Elements, and rows by columns:** `size` is the number of elements. `shape` is the pair `(rows, columns)`.
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
