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
    # Pandas Series

    ## Objectives

    - Understand Pandas Series fundamentals and their advantages over NumPy arrays.
    - Learn to create, manipulate, and access data in Series.
    - Explore data types within Series and methods for data conversion.
    - Retrieve values with positions and with labels.

    ## Background

    A Series is a one-dimensional array of indexed data. Each value has a label. The label can be a number, a letter, or another kind of value. That label is the main difference from a NumPy array, which is reached by position.

    ## Datasets Used

    This lesson does not use an external dataset. The examples use small values written in the cells.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Introducing Pandas Series

    A Pandas Series is a one-dimensional array of indexed data.
    At the basic level, a Pandas Series is a NumPy array whose elements can be identified with labels rather than only with integer positions.

    Create an empty Series:
    """)
    return


@app.cell
def _(pd):
    empty_series = pd.Series(dtype='int')
    print(empty_series)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a Series from an ndarray.

    No index was passed, so Pandas assigns the positions `0` through `len(data) - 1`.
    """)
    return


@app.cell
def _(np, pd):
    data = np.array([10, 20, 30, 40])
    from_array = pd.Series(data)
    print(from_array)
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Indexes can be letters, words, or any other type.
    """)
    return


@app.cell
def _(data, pd):
    letter_index = pd.Series(data, index=['a', 'b', 'c', 'd'])
    print(letter_index)
    return


@app.cell
def _(data, pd):
    color_index = pd.Series(data, index=['blue', 'red', 'pink', 'green'])
    print(color_index)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Creating a Series from a dictionary: the dictionary keys become the index.
    """)
    return


@app.cell
def _(pd):
    d1 = {'a': 5, 'b': 10, 'c': 15, 'd': 20}
    from_dictionary = pd.Series(d1)
    print(from_dictionary)
    return (d1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Defining an index that is not in the dictionary

    The index order you pass is kept. A label that is not a key in the dictionary is filled with `NaN` (`NaN` means *not a number*).

    There is no entry `a` here, because `a` is not in the index. The index includes `f`, and `f` is not a key of `d1`, so that entry is `NaN`.
    """)
    return


@app.cell
def _(d1, pd):
    missing_index = pd.Series(d1, index=['b', 'c', 'd', 'f'])
    print(missing_index)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a Series from a scalar. The same value is repeated once for each index label.
    """)
    return


@app.cell
def _(pd):
    from_scalar = pd.Series(20, index=[1, 2, 3, 4, 5])
    print(from_scalar)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Build a Series from `practice`. Use the index `['b', 'a', 'z']`. Which label becomes `NaN`?
    """)
    return


@app.cell
def _(pd):
    practice = {'a': 5, 'b': 10, 'c': 15}
    yours = pd.Series(practice, index=['b', 'a', 'z'])
    print(yours)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data types

    When you construct a Series, Pandas chooses a data type. You can set another type with `dtype`. The values have to fit that type.
    """)
    return


@app.cell
def _(pd):
    pd.Series([1, 2, 3, 4, 5])
    return


@app.cell
def _(pd):
    pd.Series([1, 2, 3, 4, 5], dtype='float')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Series below is float because one of the values, `3.14`, is float.

    `astype('int')` converts it to integer. The fractional part is truncated, not rounded.
    """)
    return


@app.cell
def _(pd):
    # replacing 3 for 3.14
    s2 = pd.Series([1, 2, 3.14, 4, 5])
    print(s2)
    print(s2.dtype)

    s3 = s2.astype('int')
    print(s3)
    print(s3.dtype)

    s3 = s3.astype('object')
    print(s3)
    print(s3.dtype)
    return (s3,)


@app.cell
def _(pd):
    s4 = pd.Series(['a', 'b', 'c', 'd', 'e'])
    s4
    return (s4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `s3` and `s4` are both stored as `object`.

    - `s3` can be converted to integer because its values are numbers.
    - `s4` cannot be converted to integer because its values are letters.

    The next cell raises an error. The cells after it still run.
    """)
    return


@app.cell
def _(s3):
    s3.astype('int')
    return


@app.cell
def _(s4):
    s4.astype('int')  # This will raise an error
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A Series of `True` and `False` values has dtype `bool`.
    """)
    return


@app.cell
def _(pd):
    pd.Series([True, True, False])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Accessing data

    `iloc` selects by position, starting at 0. A label selects by the index name. A slice written with labels includes the stop label. A slice written with positions does not include the stop position.
    """)
    return


@app.cell
def _(pd):
    s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    s
    return (s,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Retrieve the first element using `iloc`.
    """)
    return


@app.cell
def _(s):
    s.iloc[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Retrieve the first element using its index label.
    """)
    return


@app.cell
def _(s):
    s['a']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Retrieve the first three elements by position. Position 3 is not included.
    """)
    return


@app.cell
def _(s):
    s[:3]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Retrieve the first three elements using labels. The label `'c'` is included.
    """)
    return


@app.cell
def _(s):
    s[:'c']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Retrieve the last three elements by position.
    """)
    return


@app.cell
def _(s):
    s[-3:]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Retrieve the last three elements using labels. The slice starts at `'c'` and continues through the end.
    """)
    return


@app.cell
def _(s):
    s['c':]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Retrieve several elements. Pass a list of positions to `iloc`, or a list of labels to the index.
    """)
    return


@app.cell
def _(s):
    s.iloc[[0, 2, 3]]
    return


@app.cell
def _(s):
    s[['a', 'c', 'd']]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If a label is not in the index, Pandas raises an exception. The next cell raises that error.
    """)
    return


@app.cell
def _(s):
    s['f']  # This will raise an error
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Other useful options

    This Series repeats some values and includes one missing value, `np.nan`.
    """)
    return


@app.cell
def _(np, pd):
    numbers = pd.Series([1, 2, 3, 1, 3, np.nan])
    numbers
    return (numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The index, the values, and the length:
    """)
    return


@app.cell
def _(numbers):
    print(numbers.index)
    print(numbers.values)
    # getting the number of items in the series
    print('size  =', numbers.size)
    print('shape =', numbers.shape)
    return


@app.cell
def _(numbers):
    print('Number of unique elements =', numbers.nunique())
    print('Unique elements =', numbers.unique())
    return


@app.cell
def _(numbers):
    print('Min    =', numbers.min())
    print('Max    =', numbers.max())
    print('Mean   =', numbers.mean())
    print('Median =', numbers.median())
    print('Sum    =', numbers.sum())
    print('Non-missing values =', numbers.count())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `agg` computes the same summaries in one call.
    """)
    return


@app.cell
def _(numbers):
    numbers.agg(['min', 'max', 'mean', 'median', 'sum', 'count'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The two smallest values, the two largest values, and how many times each value occurs:
    """)
    return


@app.cell
def _(numbers):
    # 2 smallest elements
    print(numbers.nsmallest(2))
    # 2 largest elements
    print(numbers.nlargest(2))
    # number of times each element occurs
    numbers.value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the numbers in `scores`, then print the minimum, the maximum, and `value_counts()`.
    """)
    return


@app.cell
def _(pd):
    scores = pd.Series([88, 76, 88, 91, 76])
    print('Min =', scores.min())
    print('Max =', scores.max())
    scores.value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A Series stores one sequence of values and a label for each value.
    - Build it from an array, a dictionary, or a scalar. A label with no matching dictionary key is `NaN`.
    - `dtype` sets the type when the Series is created. `astype` converts it later. A float converted to integer is truncated.
    - `iloc` uses positions. A label, or a list of labels, uses the index. A missing label raises an error.
    - `min`, `max`, `mean`, `agg`, `nsmallest`, `nlargest`, and `value_counts` summarize the values.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 3.
    """)
    return


if __name__ == "__main__":
    app.run()
