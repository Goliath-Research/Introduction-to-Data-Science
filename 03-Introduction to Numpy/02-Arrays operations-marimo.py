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
    # Array Operations

    ## Objectives

    - Create 1-D, 2-D, and 3-D arrays and read their dimensions.
    - Access and replace individual elements.
    - Slice arrays, and see the difference between a view and a copy.

    ## Background

    NumPy arrays support vectorized operations. Slices of an array are usually views of the same data, not independent copies. Changing a view changes the original array.

    ## Datasets Used

    This notebook does not use external datasets. Random examples use a fixed seed so the values stay the same each time you run a cell.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating arrays

    `randint(10, size=...)` draws integers from 0 through 9. The seed is set in this cell so these three arrays are reproducible.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    vector = np.random.randint(10, size=8)
    table = np.random.randint(10, size=(2, 4))
    cube = np.random.randint(10, size=(2, 2, 2))

    print("vector:", vector, "ndim", vector.ndim, "shape", vector.shape, "size", vector.size)
    print("table:\n", table, "\nndim", table.ndim, "shape", table.shape, "size", table.size)
    print("cube:\n", cube, "\nndim", cube.ndim, "shape", cube.shape, "size", cube.size)
    return cube, table, vector


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Accessing elements

    Index `0` is the first element and `-1` is the last. For two or more dimensions, separate the indexes with commas: `array[row, column]`.
    """)
    return


@app.cell
def _(cube, table, vector):
    print("vector:", vector)
    print("first:", vector[0], "last:", vector[-1])

    print("table:\n", table)
    print("first:", table[0, 0], "also", table[0][0])
    print("last:", table[-1, -1], "also", table[-1][-1])

    print("cube:\n", cube)
    print("first:", cube[0, 0, 0], "last:", cube[-1, -1, -1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can replace an element. An integer array cannot store a float: NumPy truncates the value instead of changing the dtype.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    editable_cube = np.random.randint(10, size=(2, 2, 2))
    editable_cube[-1, -1, -1] = 20
    print("after assigning 20:\n", editable_cube)

    editable_cube[-1, -1, -1] = 3.1415
    print("after assigning 3.1415:\n", editable_cube)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Replace one element of `your_table`, then print the table.
    """)
    return


@app.cell
def _(np):
    your_table = np.array([[1, 2], [3, 4]])
    your_table[0, 1] = 9
    print(your_table)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Slicing

    A slice is `[start:stop:step]`. The start is included and the stop is excluded. The defaults are the beginning, the end, and a step of 1. A negative step reverses the array.
    """)
    return


@app.cell
def _(vector):
    print("vector:", vector)
    print("first three:", vector[:3])
    print("from index 3:", vector[3:])
    return


@app.cell
def _():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("list:", numbers)
    print("first three:", numbers[:3])
    print("from index 3:", numbers[3:])
    print("indexes 2 and 3:", numbers[2:4])
    print("2 to 5, step 2:", numbers[2:5:2])
    print("start to 5, step 2:", numbers[:5:2])
    print("2 to the end, step 2:", numbers[2::2])
    print("reversed:", numbers[::-1])
    print("reversed step 2:", numbers[::-2])
    print("from index 4, reversed step 2:", numbers[4::-2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For a 2-D array, the slice before the comma selects rows and the slice after the comma selects columns. `array[0]` is the first row. `array[:, 0]` is the first column.
    """)
    return


@app.cell
def _(np):
    matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(matrix)
    print("first column:", matrix[:, 0])
    print("first row:", matrix[0, :])
    print("first two rows and columns:\n", matrix[:2, :2])
    print("first two rows, three columns:\n", matrix[:2, :3])
    print("first two rows, columns 1 and 2:\n", matrix[:2, 1:3])
    return (matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Views and copies

    A NumPy slice is a **view**: it looks at the same data as the original array. Changing the slice changes the original. A Python list slice is a copy. Call `.copy()` when the slice must be independent.
    """)
    return


@app.cell
def _(matrix):
    view = matrix[:2, :2]
    print("view before:\n", view)
    view[0, 0] = 100
    print("view after:\n", view)
    print("original changed too:\n", matrix)

    independent = matrix[:2, :2].copy()
    independent[0, 0] = 1
    print("copy after the change:\n", independent)
    print("original is unchanged by the copy:\n", matrix)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Slice the first row. Change one item in the slice, then print both the slice and the original array.
    """)
    return


@app.cell
def _(np):
    your_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    first_row = your_matrix[0, :]
    first_row[0] = 99
    print("slice:", first_row)
    print("original:\n", your_matrix)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - Comma indexing reads one element. Slices read a range.
    - An integer array truncates a float assigned into it.
    - A slice is a view. `.copy()` makes a separate array.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 2.
    """)
    return


if __name__ == "__main__":
    app.run()
