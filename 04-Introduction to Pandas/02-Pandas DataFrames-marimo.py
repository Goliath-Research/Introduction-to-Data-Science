import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Pandas DataFrames

    ## Objectives

    - Understand a DataFrame as a table with labeled rows and columns.
    - Create DataFrames from a list, a dictionary, and a list of dictionaries.
    - Add, delete, and rename columns.
    - Inspect a DataFrame with `head`, `tail`, `describe`, and the summary methods.

    ## Background

    A DataFrame is a two-dimensional table. Data is arranged in rows and columns.

    - Columns may have different types.
    - The size can change: you can add and remove rows and columns.
    - Rows and columns have labels.
    - You can calculate with rows and columns.

    You can think of it as an SQL table or a spreadsheet.

    ## Datasets Used

    This lesson does not use an external dataset. The tables are written in the cells.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Introducing the Pandas DataFrame

    Create an empty DataFrame:
    """)
    return


@app.cell
def _(pd):
    empty_frame = pd.DataFrame()
    print(empty_frame)
    return (empty_frame,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a DataFrame from a list. The column name is assigned automatically as `0`.
    """)
    return


@app.cell
def _(pd):
    data = [10, 20, 30, 40, 50]
    from_list = pd.DataFrame(data)
    print(from_list)
    return data, from_list


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pass the column names as a list to name that column.
    """)
    return


@app.cell
def _(data, pd):
    named_column = pd.DataFrame(data, columns=['data'])
    print(named_column)
    return (named_column,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a DataFrame from a list of lists. Each inner list is one row. The `columns` list names the columns.
    """)
    return


@app.cell
def _(pd):
    students_rows = [['John', 18], ['Anna', 17], ['Peter', 19]]
    from_rows = pd.DataFrame(students_rows, columns=['Name', 'Age'])
    from_rows
    return students_rows, from_rows


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create a DataFrame from a dictionary of lists

    - The lists must have the same length. If you pass an index, it must have that same length.
    - If you do not pass an index, the index is `0, 1, 2, ...`.
    """)
    return


@app.cell
def _(pd):
    # with index
    students = {'Name': ['John', 'Jane', 'Emma'], 'Age': [18, 17, 19]}
    with_index = pd.DataFrame(students, index=['a', 'b', 'c'])
    with_index
    return students, with_index


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same dictionary without an index:
    """)
    return


@app.cell
def _(pd, students):
    # without index
    without_index = pd.DataFrame(students)
    without_index
    return (without_index,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a DataFrame from a list of dictionaries. Each dictionary is one row.

    The first dictionary has no key `'c'`, so that entry is `NaN`. The third dictionary has no key `'b'`, so that entry is `NaN` as well. With no index argument, the rows are numbered from 0 to 4.
    """)
    return


@app.cell
def _(pd):
    records = [
        {'a': 5, 'b': 20},
        {'a': 5, 'b': 20, 'c': 10},
        {'a': 4, 'c': 10},
        {'a': 3, 'b': 19},
        {'a': 2, 'b': 18},
    ]
    pd.DataFrame(records)
    return (records,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Basic operations on DataFrames

    A new column is added by name. The calculation is done row by row.

    `df['a'] + df['b']` is `NaN` in a row where `b` is missing. Any arithmetic with `NaN` gives `NaN`.

    These steps change `df` in order: add `d`, add `e`, add the scalar column `f`, delete `f`, pop `e`, then drop `d`. `drop` without `inplace=True` returns a new DataFrame and leaves `df` unchanged. `inplace=True` changes `df` itself. `rename` changes the column names.
    """)
    return


@app.cell
def _(pd, records):
    df = pd.DataFrame(records)
    print('Add d = a + b')
    df['d'] = df['a'] + df['b']
    print(df)

    print('\nAdd e = a - c. Arithmetic with NaN is NaN.')
    df['e'] = df['a'] - df['c']
    print(df)

    print('\nAdd a scalar column f')
    df['f'] = 5
    print(df)

    print('\nDelete column f')
    del(df['f'])
    print(df)

    print('\nPop column e. pop returns the deleted column.')
    print(df.pop('e'))
    print(df)

    print("\ndrop returns another DataFrame without column 'd'.")
    print(df.drop(columns=['d']))
    print('\ndf itself is unchanged:')
    print(df)

    print('\ndrop with inplace=True changes df.')
    df.drop(columns=['d'], inplace=True)
    print(df)

    df.rename(columns={'a': 'A', 'b': 'B', 'c': 'C'}, inplace=True)
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inspecting data

    The columns are now `A`, `B`, and `C`. Missing values stay missing. Summary methods skip `NaN` unless a method says otherwise.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `df.head(n)` shows the first `n` rows. If `n` is omitted, the first five rows are shown.
    """)
    return


@app.cell
def _(df):
    df.head(2)
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `df.tail(n)` shows the last `n` rows. If `n` is omitted, the last five rows are shown.
    """)
    return


@app.cell
def _(df):
    df.tail(2)
    return


@app.cell
def _(df):
    df.tail()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `shape` is the number of rows and the number of columns. `info` reports the index, the column types, and the memory use. `describe` summarizes the numeric columns.
    """)
    return


@app.cell
def _(df):
    print(df.shape)
    df.info()
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These methods return one result for each column:

    - `count`: the number of non-null values
    - `min` and `max`: the lowest and highest values
    - `mean` and `median`: the average and the middle value
    - `mode`: the value that occurs most often
    - `std`: the standard deviation
    """)
    return


@app.cell
def _(df):
    print('mean')
    print(df.mean())
    print('\ncount')
    print(df.count())
    print('\nmin')
    print(df.min())
    print('\nmax')
    print(df.max())
    print('\nmedian')
    print(df.median())
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.mode()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `round` rounds a number to the given number of decimals. The default number of decimals is 0, so the result is the nearest integer.
    """)
    return


@app.cell
def _(df):
    print(df.std())
    print(round(df.std(), 2))
    round(df.std())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sum` adds the values in each column. `cumsum` is the cumulative sum: each row includes the rows above it. `prod` multiplies the values in each column.
    """)
    return


@app.cell
def _(df):
    print(df)
    print('\nsum')
    print(df.sum())
    print('\ncumulative sum')
    print(df.cumsum())
    print('\nproduct')
    df.prod()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Add a column `NextYear` equal to `Age + 1`, then show the table.
    """)
    return


@app.cell
def _(pd):
    practice = pd.DataFrame({'Name': ['John', 'Anna', 'Peter'], 'Age': [18, 17, 19]})
    practice['NextYear'] = practice['Age'] + 1
    practice
    return (practice,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A DataFrame is a labeled table. Columns may have different types.
    - Build one from a list, a list of lists, a dictionary of lists, or a list of dictionaries. A missing key becomes `NaN`.
    - Assign a column by name. `del` and `pop` remove a column immediately. `drop` returns a new DataFrame unless you pass `inplace=True`.
    - Arithmetic with `NaN` produces `NaN`.
    - `head`, `tail`, `shape`, `info`, and `describe` show what the table contains. `mean`, `min`, `max`, `sum`, `cumsum`, and `prod` summarize the columns.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 3.
    """)
    return


if __name__ == "__main__":
    app.run()
