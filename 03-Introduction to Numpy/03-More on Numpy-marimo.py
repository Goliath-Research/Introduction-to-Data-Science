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
    # More on NumPy

    ## Objectives

    - Reshape and flatten an array without changing its values.
    - Concatenate and split arrays along rows or columns.
    - Search for values with `where` and sort with `sort`.

    ## Background

    These operations change how an array is arranged. Reshape and many slices share data with the original array. `flatten`, `sort`, and an explicit copy do not.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reshape and flatten

    `reshape` gives an array a new shape. The number of elements must stay the same, and the original array is not replaced. `flatten` returns a 1-D copy.
    """)
    return


@app.cell
def _(np):
    grid = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print("original", grid.shape, "ndim", grid.ndim)
    print(grid)

    as_four_by_three = grid.reshape(4, 3)
    as_two_by_six = grid.reshape(2, 6)
    as_row = grid.reshape(1, 12)
    as_column = grid.reshape(12, 1)
    print("4 x 3:\n", as_four_by_three)
    print("2 x 6:\n", as_two_by_six)
    print("1 x 12:\n", as_row)
    print("12 x 1:\n", as_column)
    print("original is still", grid.shape)

    try:
        grid.reshape(2, 5)
    except ValueError as error:
        print("ValueError:", error)
    return (grid,)


@app.cell
def _(grid):
    flat_reshape = grid.reshape(12)
    flat_copy = grid.flatten()
    print("reshape(12):", flat_reshape, flat_reshape.shape)
    print("flatten():  ", flat_copy, flat_copy.shape)
    return flat_copy, flat_reshape


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `rows` and `columns`. Their product must equal the number of elements.
    """)
    return


@app.cell
def _(np):
    your_values = np.arange(12)
    rows = 3
    columns = 4
    print(your_values.reshape(rows, columns))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Iterating

    A loop over a 1-D array yields elements. A loop over a 2-D array yields rows.
    """)
    return


@app.cell
def _(flat_reshape, grid):
    print("1-D:")
    for item in flat_reshape:
        print(item)

    print("2-D rows:")
    paired = grid.reshape(2, 6)
    for row in paired:
        print(row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concatenation

    `concatenate` joins arrays. `+` adds them element by element; it does not join them. For 2-D arrays, `axis=0` stacks rows and `axis=1` stacks columns. `vstack` and `hstack` do the same when the arrays have different ranks.
    """)
    return


@app.cell
def _(np):
    ones_vector = np.array([1, 1, 1])
    twos_vector = np.array([2, 2, 2])
    print("concatenate:", np.concatenate([ones_vector, twos_vector]))
    print("plus:       ", ones_vector + twos_vector)

    zeros_block = np.zeros((2, 2))
    ones_block = np.ones((2, 2))
    by_rows = np.concatenate([zeros_block, ones_block], axis=0)
    by_columns = np.concatenate([zeros_block, ones_block], axis=1)
    print("axis 0:\n", by_rows, by_rows.shape)
    print("axis 1:\n", by_columns, by_columns.shape)

    top_row = np.array([1, 2, 3])
    lower_rows = np.array([[4, 4, 4], [5, 5, 5]])
    extra_column = np.array([[8], [8]])
    print("vstack:\n", np.vstack([top_row, lower_rows]))
    print("hstack:\n", np.hstack([lower_rows, extra_column]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Splitting

    `split` is the reverse of concatenation. An integer divides the array into equal parts. A list of indexes gives the cut positions. `vsplit` cuts rows and `hsplit` cuts columns.
    """)
    return


@app.cell
def _(np):
    sequence = np.arange(9)
    left, middle, right = np.split(sequence, 3)
    print(sequence)
    print(left, middle, right)

    first, second, third = np.split(sequence, [2, 6])
    print("cuts at 2 and 6:", first, second, third)

    block = np.arange(16).reshape((4, 4))
    upper, lower = np.vsplit(block, 2)
    left_half, right_half = np.hsplit(block, 2)
    print("upper:\n", upper)
    print("lower:\n", lower)
    print("left:\n", left_half)
    print("right:\n", right_half)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Stack `left_part` and `right_part` with `axis=0`, then with `axis=1`.
    """)
    return


@app.cell
def _(np):
    left_part = np.array([[1, 2]])
    right_part = np.array([[3, 4]])
    print(np.concatenate([left_part, right_part], axis=0))
    print(np.concatenate([left_part, right_part], axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Search

    `where(condition)` returns the indexes where the condition is true. An empty index array means there was no match.
    """)
    return


@app.cell
def _(np):
    values = np.array([-5, 6, 4, 4, 1, 0, -6])

    def report(label, indexes):
        positions = indexes[0]
        print(label, positions)
        if positions.size == 0:
            print("  no match")
        for position in positions:
            print(f"  index {position}, value {values[position]}")

    report("equal to 1:", np.where(values == 1))
    report("equal to 4:", np.where(values == 4))
    report("equal to 9:", np.where(values == 9))
    report("odd:", np.where(values % 2 == 1))
    report("positive:", np.where(values > 0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sort

    `np.sort` returns a sorted copy. The original array stays unchanged. The default axis sorts each row. `axis=0` sorts each column.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    random_values = np.random.randint(10, size=10)
    print("original:", random_values)
    print("sorted:  ", np.sort(random_values))
    print("original after sort:", random_values)

    paired_rows = np.array([[3, 2, 5], [7, 0, 1]])
    print("sort rows:\n", np.sort(paired_rows))

    column_major = np.array([[1, 0, 2], [5, 6, 4], [3, -1, 6]])
    print("sort rows:\n", np.sort(column_major))
    print("sort columns:\n", np.sort(column_major, axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `target`. The cell prints every index where the array equals that value.
    """)
    return


@app.cell
def _(np):
    practice = np.array([3, 1, 4, 1, 5])
    target = 1
    print(np.where(practice == target)[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `reshape` keeps the same values and requires a compatible size.
    - `concatenate` joins arrays. `+` adds them.
    - `where` finds indexes. `np.sort` returns a new sorted array.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 2.
    """)
    return


if __name__ == "__main__":
    app.run()
