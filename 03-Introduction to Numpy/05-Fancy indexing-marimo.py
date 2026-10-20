import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np

    return mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fancy Indexing

    ## Objectives

    - Select several elements at once by passing an array of indexes.
    - Combine fancy indexes with ordinary slices.
    - Filter with a Boolean array, and find unique values with `np.unique`.

    ## Background

    Fancy indexing passes a list or an array of positions instead of one position. A Boolean array used as an index keeps the elements marked `True`. `np.unique` finds the distinct values in an array.

    ## Datasets Used

    This notebook does not use external datasets. The random example uses a fixed seed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Selecting by a list of indexes

    `array[[3, 6, 9, 4]]` returns those four elements in that order. The example uses 10 random integers from 0 to 99.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    sample = np.random.randint(100, size=10)
    print(sample)
    return (sample,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Without fancy indexing, you read the positions one at a time.
    """)
    return


@app.cell
def _(sample):
    print([sample[3], sample[6], sample[9], sample[4]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With fancy indexing, one list of positions gives the same values, as an array.
    """)
    return


@app.cell
def _(sample):
    positions = [3, 6, 9, 4]
    print(sample[positions])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Two dimensions

    The same idea works in two dimensions: one array chooses the rows and another chooses the columns, pair by pair. The examples use this 3 × 4 grid.
    """)
    return


@app.cell
def _(np):
    grid = np.arange(12).reshape((3, 4))
    print(grid)
    return (grid,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `rows` and `columns` are read in pairs: (0, 2), (2, 1), and (1, 3).
    """)
    return


@app.cell
def _(grid, np):
    rows = np.array([0, 2, 1])
    columns = np.array([2, 1, 3])
    print(grid[rows, columns])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Reading the same three pairs one at a time gives the same values.
    """)
    return


@app.cell
def _(grid):
    print([grid[0, 2], grid[2, 1], grid[1, 3]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A single row index can be combined with a list of columns. This is row 2, with the columns in the order 2, 0, 1.
    """)
    return


@app.cell
def _(grid):
    print(grid[2, [2, 0, 1]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A slice of rows can also be combined with a list of columns. This is every row from 1 on, with the same three columns.
    """)
    return


@app.cell
def _(grid):
    print(grid[1:, [2, 0, 1]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `chosen` to another list of indexes, then print those elements.
    """)
    return


@app.cell
def _(np):
    your_values = np.array([10, 20, 30, 40, 50])
    chosen = [0, 2, 4]
    print(your_values[chosen])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    From `grid`, select the elements at (0, 0), (1, 2), and (2, 3) with one fancy index. Replace `None` with your code. Which values do you get?
    """)
    return


@app.cell
def _():
    student_pairs = None
    print(student_pairs)
    return (student_pairs,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_pairs = grid[[0, 1, 2], [0, 2, 3]]
```
The values are `[0, 6, 11]`. The first list holds the rows and the second list holds the columns. They are read in pairs.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Changing selected elements

    Assigning to a fancy index writes into those positions. `+=` and `-=` update the same positions. Each step below works on a copy of the step before, so you can see every result.

    The start is the numbers 0 to 9, and the positions to change are 0, 3, and 7.
    """)
    return


@app.cell
def _(np):
    start_values = np.arange(10)
    selected = np.array([0, 3, 7])
    print(start_values)
    return selected, start_values


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Assign 100 to the selected positions.
    """)
    return


@app.cell
def _(selected, start_values):
    assigned = start_values.copy()
    assigned[selected] = 100
    print(assigned)
    return (assigned,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Add 20 to the same positions. 100 becomes 120. If an index is repeated, `+=` still adds only once.
    """)
    return


@app.cell
def _(assigned, selected):
    plus_twenty = assigned.copy()
    plus_twenty[selected] += 20
    print(plus_twenty)
    return (plus_twenty,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Subtract 125 from the same positions. 120 becomes -5. This array, `values`, is used in the next section.
    """)
    return


@app.cell
def _(plus_twenty, selected):
    values = plus_twenty.copy()
    values[selected] -= 125
    print(values)
    return (values,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Reading with a fancy index returns a copy, unlike a slice. `picked` is a copy of the selected values. Setting its first element to -1 does not change `start_values`.
    """)
    return


@app.cell
def _(selected, start_values):
    picked = start_values[selected]
    picked[0] = -1
    print(start_values)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Boolean filters

    A Boolean list or array used as an index keeps the elements where the mask is `True`. This loop builds the mask by hand: `True` for an even value and `False` for an odd one.
    """)
    return


@app.cell
def _(values):
    even_mask = []
    for item in values:
        if item % 2 == 0:  # the value is even
            even_mask.append(True)
        else:
            even_mask.append(False)
    print(even_mask)
    return (even_mask,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using the mask as an index keeps only the even values.
    """)
    return


@app.cell
def _(even_mask, values):
    print(values[even_mask])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `values > 5` builds a mask in one expression, without a loop.
    """)
    return


@app.cell
def _(values):
    greater_than_five = values > 5
    print(greater_than_five)
    return (greater_than_five,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That mask keeps the values greater than 5.
    """)
    return


@app.cell
def _(greater_than_five, values):
    print(values[greater_than_five])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A mask works on a 2-D array too. The result is a 1-D array of the matching values of `grid`.
    """)
    return


@app.cell
def _(grid):
    print(grid[grid > 4])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Keep only the negative values of `values`. Replace `None` with your code. How many are there?
    """)
    return


@app.cell
def _():
    student_negative = None
    print(student_negative)
    return (student_negative,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_negative = values[values < 0]
```
There are three: `[-5, -5, -5]`. They are the three positions changed in the previous section.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Unique values

    `np.unique` returns the sorted distinct values. The examples use this array of letters.
    """)
    return


@app.cell
def _(np):
    letters = np.array(["d", "a", "b", "d", "c", "c", "b", "a", "b", "a"])
    print(letters)
    return (letters,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The distinct letters, in sorted order.
    """)
    return


@app.cell
def _(letters, np):
    print(np.unique(letters))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `return_counts=True` adds how often each value appears. `zip` pairs each letter with its count.
    """)
    return


@app.cell
def _(letters, np):
    _distinct, counts = np.unique(letters, return_counts=True)
    print(dict(zip(_distinct.tolist(), counts.tolist())))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `return_index=True` adds the first position of each value. `a` first appears at position 1.
    """)
    return


@app.cell
def _(letters, np):
    _distinct, first_positions = np.unique(letters, return_index=True)
    print(dict(zip(_distinct.tolist(), first_positions.tolist())))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `return_inverse=True` adds one index per element. Each index points to that element's letter in the unique array: 0 is `a`, 1 is `b`, and so on.
    """)
    return


@app.cell
def _(letters, np):
    inverse_labels, inverse = np.unique(letters, return_inverse=True)
    print(inverse)
    return inverse, inverse_labels


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using `inverse` as a fancy index on the unique letters rebuilds the original array.
    """)
    return


@app.cell
def _(inverse, inverse_labels):
    print(inverse_labels[inverse])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Print the unique values in `your_letters` and how many times each one appears.
    """)
    return


@app.cell
def _(np):
    your_letters = np.array(["a", "b", "a", "c", "b", "a"])
    labels, times = np.unique(your_letters, return_counts=True)
    print(dict(zip(labels.tolist(), times.tolist())))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A list of indexes selects many elements in the order you give.
    - In two dimensions, a list of rows and a list of columns are read in pairs.
    - Assignment through those indexes changes the original array. Reading with a fancy index returns a copy.
    - A Boolean mask keeps elements that meet a condition.
    - `np.unique` can also return counts, first positions, and a way to rebuild the array.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What does `x[[2, 0]]` return?
    2. In `grid[[0, 1], [2, 3]]`, which elements are selected?
    3. What does `x[[1, 3]] = 0` do to `x`?
    4. What does `x[x > 5]` return?
    5. Can a Boolean mask select values from a 2-D array?
    6. Is the result of `np.unique` sorted?
    7. What does `return_counts=True` add?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **The elements at positions 2 and 0, in that order:** Fancy indexing follows the order of the list.
2. **(0, 2) and (1, 3):** The row list and the column list are read in pairs.
3. **It sets those positions to 0:** The original array changes.
4. **The values greater than 5:** The mask keeps the elements where the condition is `True`.
5. **Yes:** The result is a 1-D array of the matching values.
6. **Yes:** The distinct values come back in sorted order.
7. **How many times each value appears:** It returns a second array with one count per distinct value.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 2.
    """)
    return


if __name__ == "__main__":
    app.run()
