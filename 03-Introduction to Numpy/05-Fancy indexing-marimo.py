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

    `array[[3, 6, 9, 4]]` returns those four elements in that order. The same idea works in two dimensions: one array chooses the rows and another chooses the columns, pair by pair.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    sample = np.random.randint(100, size=10)
    positions = [3, 6, 9, 4]
    print("sample:", sample)
    print("one at a time:", [sample[3], sample[6], sample[9], sample[4]])
    print("fancy index:  ", sample[positions])
    return


@app.cell
def _(np):
    grid = np.arange(12).reshape((3, 4))
    rows = np.array([0, 2, 1])
    columns = np.array([2, 1, 3])
    print(grid)
    print("pairs:", grid[rows, columns])
    print("one at a time:", [grid[0, 2], grid[2, 1], grid[1, 3]])
    print("row 2, selected columns:", grid[2, [2, 0, 1]])
    print("rows from 1, selected columns:\n", grid[1:, [2, 0, 1]])
    return (grid,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Changing selected elements

    Assigning to a fancy index writes into those positions. `+=` and `-=` update the same positions. This sequence is kept in one cell so you can follow the array.
    """)
    return


@app.cell
def _(np):
    values = np.arange(10)
    selected = np.array([0, 3, 7])
    print("start:     ", values)

    values[selected] = 100
    print("assign 100:", values)

    values[selected] += 20
    print("plus 20:   ", values)

    values[selected] -= 125
    print("minus 125: ", values)
    return (values,)


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
    ## Boolean filters

    A Boolean list or array used as an index keeps the elements where the mask is `True`. `values > 5` builds that mask in one expression.
    """)
    return


@app.cell
def _(grid, values):
    even_mask = []
    for item in values:
        if item % 2 == 0:  # the value is even
            even_mask.append(True)
        else:
            even_mask.append(False)
    print("values:", values)
    print("even mask:", even_mask)
    print("even values:", values[even_mask])

    greater_than_five = values > 5
    print("greater than 5:", greater_than_five)
    print(values[greater_than_five])

    print("grid:\n", grid)
    print("grid entries greater than 4:", grid[grid > 4])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Unique values

    `np.unique` returns the sorted distinct values. `return_counts` adds how often each value appears. `return_index` adds the first position of each value. `return_inverse` adds the indexes needed to rebuild the original array.
    """)
    return


@app.cell
def _(np):
    letters = np.array(["d", "a", "b", "d", "c", "c", "b", "a", "b", "a"])
    print("unique:", np.unique(letters))

    distinct, counts = np.unique(letters, return_counts=True)
    print("counts:", dict(zip(distinct, counts)))

    distinct, first_positions = np.unique(letters, return_index=True)
    print("first positions:", dict(zip(distinct, first_positions)))

    distinct, inverse = np.unique(letters, return_inverse=True)
    print("inverse:", inverse)
    print("rebuilt:", distinct[inverse])
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
    print(dict(zip(labels, times)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A list of indexes selects many elements in the order you give.
    - Assignment through those indexes changes the original array.
    - A Boolean mask keeps elements that meet a condition.
    - `np.unique` can also return counts, first positions, and a way to rebuild the array.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 2.
    """)
    return


if __name__ == "__main__":
    app.run()
