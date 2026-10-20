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

    - Understand what a Series adds to a NumPy array: a label for each value.
    - Create a Series from an array, a dictionary, and a scalar.
    - Choose a data type with `dtype` and convert it with `astype`.
    - Retrieve values with positions and with labels.
    - Summarize a Series with methods such as `mean`, `agg`, and `value_counts`.

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

    Create an empty Series. The printed Series is empty, and its last line is the data type.
    """)
    return


@app.cell
def _(pd):
    empty_series = pd.Series(dtype='int')
    print(empty_series)
    return (empty_series,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a Series from an ndarray.

    No index was passed, so Pandas assigns the positions `0` through `len(data) - 1`. The left column of the printed Series is that index. The right column is the values.
    """)
    return


@app.cell
def _(np, pd):
    data = np.array([10, 20, 30, 40])
    from_array = pd.Series(data)
    print(from_array)
    return data, from_array


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Indexes can be letters, words, or any other type. Here the same four values are labeled `a` through `d`.
    """)
    return


@app.cell
def _(data, pd):
    letter_index = pd.Series(data, index=['a', 'b', 'c', 'd'])
    print(letter_index)
    return (letter_index,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The labels can also be words. The values are the same. Only the labels change.
    """)
    return


@app.cell
def _(data, pd):
    color_index = pd.Series(data, index=['blue', 'red', 'pink', 'green'])
    print(color_index)
    return (color_index,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Creating a Series from a dictionary: the dictionary keys become the index, and the dictionary values become the values.
    """)
    return


@app.cell
def _(pd):
    d1 = {'a': 5, 'b': 10, 'c': 15, 'd': 20}
    from_dictionary = pd.Series(d1)
    print(from_dictionary)
    return d1, from_dictionary


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Defining an index that is not in the dictionary

    The index order you pass is kept. A label that is not a key in the dictionary is filled with `NaN` (`NaN` means *not a number*).

    There is no entry `a` here, because `a` is not in the index. The index includes `f`, and `f` is not a key of `d1`, so that entry is `NaN`. The values become `float64`, because `NaN` is a float.
    """)
    return


@app.cell
def _(d1, pd):
    missing_index = pd.Series(d1, index=['b', 'c', 'd', 'f'])
    print(missing_index)
    return (missing_index,)


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
    return (from_scalar,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    The cell builds a Series from `practice` with the index `['b', 'a', 'z']`. Run it, then change the index and run it again. Which label becomes `NaN`, and what happens to the key `'c'`?
    """)
    return


@app.cell
def _(pd):
    practice = {'a': 5, 'b': 10, 'c': 15}
    yours = pd.Series(practice, index=['b', 'a', 'z'])
    print(yours)
    return practice, yours


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
`'z'` becomes `NaN`, because it is not a key of `practice`. The key `'c'` is left out, because it is not in the index. The values are listed in the order of the index, so `'b'` comes before `'a'`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data types

    When you construct a Series, Pandas chooses a data type. These values are whole numbers, so the type is `int64`.
    """)
    return


@app.cell
def _(pd):
    print(pd.Series([1, 2, 3, 4, 5]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can set another type with `dtype`. The values have to fit that type. With `dtype='float'`, the same numbers are stored as `1.0`, `2.0`, and so on.
    """)
    return


@app.cell
def _(pd):
    print(pd.Series([1, 2, 3, 4, 5], dtype='float'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This Series is float because one of the values, `3.14`, is float. Every value is stored with the same type, so the whole numbers become floats too.
    """)
    return


@app.cell
def _(pd):
    s2 = pd.Series([1, 2, 3.14, 4, 5])
    print(s2)
    return (s2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `astype('int')` converts the Series to integer. The fractional part is truncated, not rounded: `3.14` becomes `3`.
    """)
    return


@app.cell
def _(s2):
    s3 = s2.astype('int')
    print(s3)
    return (s3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `astype('object')` keeps the same numbers but stores them as general Python objects. The values look the same. The type in the last line changes.
    """)
    return


@app.cell
def _(s3):
    s3_object = s3.astype('object')
    print(s3_object)
    return (s3_object,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A Series of letters is stored as `object` (in pandas 3.0 the type is shown as `str`).
    """)
    return


@app.cell
def _(pd):
    s4 = pd.Series(['a', 'b', 'c', 'd', 'e'])
    print(s4)
    return (s4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `s3_object` holds numbers stored as `object`. `s4` holds text, stored as `object` (shown as `str` in pandas 3.0). Only one of them can become integer.

    - `s3_object` can be converted, because its values are numbers.
    - `s4` cannot be converted, because its values are letters.

    The next cell converts `s3_object`.
    """)
    return


@app.cell
def _(s3_object):
    s3_object.astype('int')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This cell tries to convert `s4`. Letters cannot become integers, so it raises a `ValueError` on purpose. The cells after it still run.
    """)
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
    ### Try it yourself

    Build a Series from `[1.9, 2.1, 3.8]` and convert it to integer with `astype`. Replace `None` with your code. Is `1.9` rounded to 2, or is the fractional part dropped?
    """)
    return


@app.cell
def _():
    student_integers = None
    print(student_integers)
    return (student_integers,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_integers = pd.Series([1.9, 2.1, 3.8]).astype('int')
```
The fractional part is dropped. `1.9` becomes `1`, not `2`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Accessing data

    `iloc` selects by position, starting at 0. A label selects by the index name. A slice written with labels includes the stop label. A slice written with positions does not include the stop position.

    The examples use this Series:
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
    Retrieve the first element using `iloc`. Position `0` is the first element.
    """)
    return


@app.cell
def _(s):
    s.iloc[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Retrieve the same element using its index label.
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
    Retrieve the last three elements by position. A negative position counts from the end.
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
    Retrieve several elements by passing a list of positions to `iloc`.
    """)
    return


@app.cell
def _(s):
    s.iloc[[0, 2, 3]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same elements, selected with a list of labels.
    """)
    return


@app.cell
def _(s):
    s[['a', 'c', 'd']]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If a label is not in the index, Pandas raises an exception. The next cell asks for the label `'f'`, which is not in the index, so it raises a `KeyError` on purpose.
    """)
    return


@app.cell
def _(s):
    s['f']  # This will raise an error
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    From the Series `s`, select the labels `'a'` through `'c'` with a label slice. Replace `None` with your code. Does the slice include `'c'`?
    """)
    return


@app.cell
def _():
    student_label_slice = None
    print(student_label_slice)
    return (student_label_slice,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_label_slice = s[:'c']
```
Yes. A slice written with labels includes the stop label, so `'c'` is included.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    From the Series `s`, select the positions `0` and `2` with `iloc`. Replace `None` with your code. Which labels do those positions have?
    """)
    return


@app.cell
def _():
    student_positions = None
    print(student_positions)
    return (student_positions,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_positions = s.iloc[[0, 2]]
```
Position `0` is the label `'a'`, and position `2` is the label `'c'`. The result keeps those labels.
''')}, lazy=True)
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
    `index` is the labels. No index was passed, so the labels are the positions 0 through 5.
    """)
    return


@app.cell
def _(numbers):
    numbers.index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `values` is the data as a NumPy array, without the labels.
    """)
    return


@app.cell
def _(numbers):
    numbers.values
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `size` is the number of elements. The missing value is counted.
    """)
    return


@app.cell
def _(numbers):
    numbers.size
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `shape` is the same count written as a tuple. A Series has one dimension, so the tuple has one number.
    """)
    return


@app.cell
def _(numbers):
    numbers.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `nunique` is the number of distinct values. It leaves the missing value out, so the distinct values are 1, 2, and 3.
    """)
    return


@app.cell
def _(numbers):
    numbers.nunique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `unique` lists the distinct values in the order they first appear. Unlike `nunique`, it includes `nan`.
    """)
    return


@app.cell
def _(numbers):
    numbers.unique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `mean` skips the missing value. It adds the five values that are present and divides by 5: (1 + 2 + 3 + 1 + 3) / 5 = 2.
    """)
    return


@app.cell
def _(numbers):
    numbers.mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `agg` computes several summaries in one call. The result is a Series with one row per summary. `count` is the number of values that are present, so it is 5, not 6.
    """)
    return


@app.cell
def _(numbers):
    numbers.agg(['min', 'max', 'mean', 'median', 'sum', 'count'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `nsmallest(2)` returns the two smallest values, with their labels. The value `1` appears at labels 0 and 3.
    """)
    return


@app.cell
def _(numbers):
    print(numbers.nsmallest(2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `nlargest(2)` returns the two largest values. The value `3` appears at labels 2 and 4.
    """)
    return


@app.cell
def _(numbers):
    print(numbers.nlargest(2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `value_counts` counts how many times each value occurs. The most frequent values come first. The missing value is not counted.
    """)
    return


@app.cell
def _(numbers):
    numbers.value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Use `agg` on `numbers` to compute `min`, `max`, and `count` in one call. Replace `None` with your code. Does `count` include the missing value?
    """)
    return


@app.cell
def _():
    student_summaries = None
    print(student_summaries)
    return (student_summaries,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_summaries = numbers.agg(['min', 'max', 'count'])
```
No. `count` is the number of non-missing values. The `NaN` in `numbers` is left out, so the count is 5 rather than 6.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the numbers in `scores`, then run the cell. `value_counts` lists the most frequent value first.
    """)
    return


@app.cell
def _(pd):
    scores = pd.Series([88, 76, 88, 91, 76, 88])
    scores.value_counts()
    return (scores,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A Series stores one sequence of values and a label for each value.
    - Build it from an array, a dictionary, or a scalar. A label with no matching dictionary key is `NaN`.
    - `dtype` sets the type when the Series is created. `astype` converts it later. A float converted to integer is truncated.
    - `iloc` uses positions. A label, or a list of labels, uses the index. A missing label raises an error.
    - `mean`, `agg`, `nunique`, `nsmallest`, `nlargest`, and `value_counts` summarize the values. Most of them skip missing values.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What does a Series have that a NumPy array does not?
    2. What appears in a Series when the index names a key that is not in the dictionary?
    3. What does `astype('int')` do to the fractional part of a float?
    4. What is the difference between `iloc` and a label such as `s['a']`?
    5. Does a slice written with labels include the stop label?
    6. What happens if you select a label that is not in the index?
    7. Does `count` include missing values?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **A label for each value:** A NumPy array is reached by position. A Series is reached by position or by its index label.
2. **`NaN`:** The label is kept, and the value is missing.
3. **It drops it:** The conversion truncates. It does not round.
4. **Position and name:** `iloc` counts from 0. The label uses the index name, whatever position that name has.
5. **Yes:** A slice written with positions does not include the stop position.
6. **`KeyError`:** Pandas does not invent a value for a missing label.
7. **No:** `count` is the number of values that are present.
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
