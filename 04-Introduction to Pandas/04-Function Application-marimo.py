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
    # Function Application

    ## Objectives

    - Apply a function to a whole DataFrame with `pipe()`.
    - Apply a function to each column or each row with `apply()`.
    - Apply a function to every element with `map()`.
    - Walk through a DataFrame with `items`, `iterrows`, and `itertuples`.
    - Sort by the index and by column values.

    ## Background

    The method you choose depends on what the function expects:

    - `pipe()` passes the whole DataFrame to the function.
    - `apply()` passes one column, or one row, at a time.
    - `map()` passes one element at a time. Older versions of Pandas called the DataFrame version of this method `applymap()`.

    None of these methods change the original DataFrame. They return a new one.

    ## Datasets Used

    This lesson does not use an external dataset. The tables are written in the cells. Two columns are filled with random numbers, so those values change each time the cell runs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Function application

    `add2` adds its two arguments. Used with `pipe`, the first argument is the DataFrame and the second is the number you pass.
    """)
    return


@app.cell
def _():
    def add2(elem1, elem2):
        '''
        Add two numbers
        '''
        return elem1 + elem2

    return (add2,)


@app.cell
def _(pd):
    df = pd.DataFrame({'Col1': [1, 1, 1, 1], 'Col2': [1, 2, 3, 4], 'Col3': [-1, 0, 1, 2]})
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Table-wise function application

    `pipe` performs the operation on the whole DataFrame. `df.pipe(add2, 5)` adds 5 to every value. The original `df` is unchanged. Assign the result if you want to keep it.
    """)
    return


@app.cell
def _(add2, df):
    df.pipe(add2, 5)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(add2, df):
    df2 = df.pipe(add2, 10)
    df2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Row or column wise function application

    `apply` runs the function on each column. That is `axis=0`, and it is the default.

    `axis=1` runs the function on each row.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The mean of each column, first with `apply` and then with `mean`:
    """)
    return


@app.cell
def _(df, np):
    df.apply(np.mean)
    return


@app.cell
def _(df):
    df.mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sum_squares` adds the squares of the values it receives. With the default axis, those values are one column. With `axis=1`, they are one row.
    """)
    return


@app.cell
def _():
    def sum_squares(l):
        '''
        Return the sum of squares of the list
        '''
        return sum(x**2 for x in l)

    return (sum_squares,)


@app.cell
def _(df, sum_squares):
    print(df.apply(sum_squares))
    print(df.apply(sum_squares, axis=0))
    df.apply(sum_squares, axis=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A lambda is a small function written in one line. Here the argument is a column, or a row when `axis=1`. The result is the range, `max - min`.
    """)
    return


@app.cell
def _(df):
    print(df)
    print('\nRange of each column')
    print(df.apply(lambda x: x.max() - x.min()))
    print('\nRange of each row')
    df.apply(lambda x: x.max() - x.min(), axis=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Element wise function application

    `map` runs the function on every element and returns a new DataFrame. The lambda below multiplies each element by 100.

    You can chain calls. `map` first, then `apply`, computes the mean of those new values. `map` on one column, `Col1`, returns a Series. `pipe` can multiply the whole DataFrame by 100 as well.

    After all of these calls, `df` still holds the original numbers.
    """)
    return


@app.cell
def _(df):
    print(df)
    df.map(lambda x: x * 100)
    return


@app.cell
def _(df, np):
    df.map(lambda x: x * 100).apply(np.mean)
    return


@app.cell
def _(df):
    print(df.Col1)
    df.Col1.map(lambda x: x * 100)
    return


@app.cell
def _(df):
    df.pipe(lambda x: x * 100)
    return


@app.cell
def _(df):
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Iterations

    Iterating a Series produces its values. Iterating a DataFrame produces its column names, the same way iterating a dictionary produces its keys.

    To walk through the rows, use one of these:

    - `items()` yields each column name and that column as a Series.
    - `iterrows()` yields each index and that row as a Series.
    - `itertuples()` yields a named tuple for each row. The first field is the index. The other fields are the row values. `itertuples` keeps the original data types, so it is the better choice when the types matter.

    The first table is only an example of building a DataFrame with dates and random numbers. The loops use the second table.
    """)
    return


@app.cell
def _():
    N = 3
    return (N,)


@app.cell
def _(N, np, pd):
    draft = pd.DataFrame({
        'A': pd.date_range(start='2021-02-15', periods=N, freq='D'),
        'B': np.linspace(0, stop=N - 1, num=N),
        'C': np.random.rand(N),
        'D': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
        'E': np.random.normal(100, 10, size=(N)).tolist(),
    })
    draft.head()
    return


@app.cell
def _(N, np, pd):
    dfi = pd.DataFrame({
        'Date': pd.date_range(start='2022-05-15', periods=N, freq='D'),
        'Values': np.linspace(0, stop=N - 1, num=N),
        'Categ': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    })
    dfi.head()
    return (dfi,)


@app.cell
def _(dfi):
    # Getting the names of the columns
    for col in dfi:
        print(col)
    return


@app.cell
def _(dfi):
    # Getting the values of the columns
    # Key will be the column name
    # Values will be the column values
    for key, values in dfi.items():
        print('Key=', key)
        print('Values=')
        for value in values:
            print(value)
    return


@app.cell
def _(dfi):
    for index, series in dfi.iterrows():
        print(index, series['Date'], series['Values'], series['Categ'])
    return


@app.cell
def _(dfi):
    for row in dfi.itertuples():
        print(row, '\n')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sorting

    Pandas sorts in two ways: by the labels, and by the values.

    `sort_index` sorts the row labels. `axis=1` sorts the column names instead. `ascending=False` reverses the order.

    `sort_values` sorts by one column, or by a list of columns. The first name in the list is the main sort. The later names break ties.

    Sorting returns a new DataFrame. `unsorted_df` stays in its original order.
    """)
    return


@app.cell
def _(np, pd):
    unsorted_df = pd.DataFrame({
        'Z': np.random.randint(0, 5, size=10),
        'A': np.random.randint(2, 5, size=10),
        'K': np.random.randint(1, 8, size=10),
    }, index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7])
    unsorted_df
    return (unsorted_df,)


@app.cell
def _(unsorted_df):
    unsorted_df.sort_index()
    return


@app.cell
def _(unsorted_df):
    unsorted_df.sort_index(ascending=False)
    return


@app.cell
def _(unsorted_df):
    unsorted_df.sort_index(axis=1)
    return


@app.cell
def _(unsorted_df):
    unsorted_df.sort_index(axis=1, ascending=False)
    return


@app.cell
def _(unsorted_df):
    unsorted_df.sort_values(by='Z')
    return


@app.cell
def _(unsorted_df):
    unsorted_df.sort_values(by=['Z', 'A'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the lambda so that it adds the two columns instead of subtracting them.
    """)
    return


@app.cell
def _(pd):
    practice = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    practice.apply(lambda column: column.max() - column.min())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `pipe` applies a function to the whole DataFrame. Extra arguments follow the function.
    - `apply` works down each column by default. `axis=1` works across each row.
    - `map` works on one element at a time, on a DataFrame or on a Series.
    - These methods return a new object. The original DataFrame stays as it was.
    - A DataFrame loop yields column names. `items`, `iterrows`, and `itertuples` yield the contents.
    - `sort_index` orders labels. `sort_values` orders rows by one or more columns.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 3.
    """)
    return


if __name__ == "__main__":
    app.run()
