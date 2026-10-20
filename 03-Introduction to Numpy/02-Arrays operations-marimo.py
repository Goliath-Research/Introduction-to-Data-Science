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

    This lesson reads and changes array elements, then slices them. A slice of a NumPy array is usually a view of the same data, not a separate copy. Changing the view changes the original array. A slice of a Python list is a copy.

    ## Datasets Used

    This notebook does not use external datasets. Random examples use a fixed seed so the values stay the same each time you run a cell.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating arrays

    `randint(10, size=...)` draws integers from 0 through 9. The seed is set in this cell so these three arrays are reproducible. The cells after it show each array.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    vector = np.random.randint(10, size=8)
    table = np.random.randint(10, size=(2, 4))
    cube = np.random.randint(10, size=(2, 2, 2))
    return cube, table, vector


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `vector` is a 1-D array with 8 values.
    """)
    return


@app.cell
def _(vector):
    print(vector)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It has one axis, its shape is `(8,)`, and it has 8 elements.
    """)
    return


@app.cell
def _(vector):
    print("ndim", vector.ndim, "shape", vector.shape, "size", vector.size)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `table` is a 2-D array with 2 rows and 4 columns.
    """)
    return


@app.cell
def _(table):
    print(table)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It has two axes, and its size is 2 × 4 = 8.
    """)
    return


@app.cell
def _(table):
    print("ndim", table.ndim, "shape", table.shape, "size", table.size)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `cube` is a 3-D array: 2 tables, each with 2 rows and 2 columns.
    """)
    return


@app.cell
def _(cube):
    print(cube)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It has three axes, and its size is 2 × 2 × 2 = 8.
    """)
    return


@app.cell
def _(cube):
    print("ndim", cube.ndim, "shape", cube.shape, "size", cube.size)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Accessing elements

    Index `0` is the first element and `-1` is the last. For two or more dimensions, separate the indexes with commas: `array[row, column]`.

    The first element of `vector`:
    """)
    return


@app.cell
def _(vector):
    print(vector[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The last element of `vector`:
    """)
    return


@app.cell
def _(vector):
    print(vector[-1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In `table`, `[0, 0]` is the first row and the first column.
    """)
    return


@app.cell
def _(table):
    print(table[0, 0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `table[0][0]` gives the same value. It first selects row 0, then the first element of that row.
    """)
    return


@app.cell
def _(table):
    print(table[0][0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[-1, -1]` is the last row and the last column.
    """)
    return


@app.cell
def _(table):
    print(table[-1, -1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A 3-D array needs three indexes: table, row, and column. This is the first element of `cube`.
    """)
    return


@app.cell
def _(cube):
    print(cube[0, 0, 0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And this is the last element of `cube`.
    """)
    return


@app.cell
def _(cube):
    print(cube[-1, -1, -1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Replacing an element

    You can replace an element by assigning to its position. These examples change a copy of `cube`, so `cube` itself stays the same. The last element becomes 20.
    """)
    return


@app.cell
def _(cube):
    cube_20 = cube.copy()
    cube_20[-1, -1, -1] = 20
    print(cube_20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An integer array cannot store a float. NumPy truncates the value instead of changing the dtype, so `3.1415` is stored as `3`. Values that cannot be converted, such as `np.nan`, raise an error.
    """)
    return


@app.cell
def _(cube):
    cube_pi = cube.copy()
    cube_pi[-1, -1, -1] = 3.1415
    print(cube_pi)
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
    ### Try it yourself

    Make a copy of `table` and set its first element to `7.9`. Replace `None` with your code. What value is stored, and why?
    """)
    return


@app.cell
def _():
    student_table = None
    print(student_table)
    return (student_table,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_table = table.copy()
student_table[0, 0] = 7.9
```
The value stored is `7`. `table` holds integers, so the fractional part is dropped. It is not rounded to 8.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Slicing

    A slice is `[start:stop:step]`. The start is included and the stop is excluded. The defaults are the beginning, the end, and a step of 1. A negative step reverses the array.

    `vector[:3]` is the first three elements: positions 0, 1, and 2.
    """)
    return


@app.cell
def _(vector):
    print(vector[:3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `vector[3:]` starts at position 3 and goes to the end.
    """)
    return


@app.cell
def _(vector):
    print(vector[3:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python lists use the same slice rules. This list holds the numbers 0 through 8, so each value is also its position.
    """)
    return


@app.cell
def _():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(numbers)
    return (numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[2:4]` is positions 2 and 3. Position 4 is the stop, so it is excluded.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[2:4])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[2:5:2]` starts at 2, takes every second position, and stops before 5.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[2:5:2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[:5:2]` starts at the beginning and takes every second position before 5.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[:5:2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[2::2]` starts at 2 and takes every second position up to the end.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[2::2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[::-1]` uses a step of -1, so it reverses the list.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[::-1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[::-2]` reverses the list and takes every second value.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[::-2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[4::-2]` starts at position 4 and moves backward two positions at a time.
    """)
    return


@app.cell
def _(numbers):
    print(numbers[4::-2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Slicing a 2-D array

    For a 2-D array, the slice before the comma selects rows and the slice after the comma selects columns. The examples use this 3 × 4 matrix.
    """)
    return


@app.cell
def _(np):
    matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(matrix)
    return (matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `matrix[:, 0]` is the first column. The `:` before the comma means every row.
    """)
    return


@app.cell
def _(matrix):
    print(matrix[:, 0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `matrix[0, :]` is the first row. The `:` after the comma means every column.
    """)
    return


@app.cell
def _(matrix):
    print(matrix[0, :])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `matrix[:2, :2]` is the first two rows and the first two columns.
    """)
    return


@app.cell
def _(matrix):
    print(matrix[:2, :2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `matrix[:2, :3]` is the first two rows and the first three columns.
    """)
    return


@app.cell
def _(matrix):
    print(matrix[:2, :3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `matrix[:2, 1:3]` is the first two rows and the columns at positions 1 and 2.
    """)
    return


@app.cell
def _(matrix):
    print(matrix[:2, 1:3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    From `matrix`, select the last two rows and the last two columns. Replace `None` with your code. Which four numbers do you get?
    """)
    return


@app.cell
def _():
    student_corner = None
    print(student_corner)
    return (student_corner,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_corner = matrix[1:, 2:]
```
The result is `[[7, 8], [11, 12]]`. `matrix[-2:, -2:]` gives the same result, because negative positions count from the end.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Views and copies

    A NumPy slice is a **view**: it looks at the same data as the original array. Changing the slice changes the original. That is useful with a large array, because you can work on one piece without copying the whole array. A Python list slice is a copy. Call `.copy()` when the NumPy slice must be independent. The next lesson shows that `reshape` is a view too.

    This section uses its own array, `original`. `view` is its top-left 2 × 2 corner. The first element of the view is set to 100.
    """)
    return


@app.cell
def _(np):
    original = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    view = original[:2, :2]
    view[0, 0] = 100
    print(view)
    return (original,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `original` changed too. The view and the original share the same data.
    """)
    return


@app.cell
def _(original):
    print(original)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `.copy()` makes a separate array. Its first element is set to 1.
    """)
    return


@app.cell
def _(original):
    independent = original[:2, :2].copy()
    independent[0, 0] = 1
    print(independent)
    return (independent,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `original` still has 100 in its first position. Changing the copy did not change it.
    """)
    return


@app.cell
def _(independent, original):
    print(original)
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
    ### Try it yourself

    Take the first column of `matrix` as an independent array, then set its first element to 0. Replace `None` with your code. Does `matrix` change?
    """)
    return


@app.cell
def _():
    student_column = None
    print(student_column)
    return (student_column,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_column = matrix[:, 0].copy()
student_column[0] = 0
```
No. `.copy()` makes a separate array, so `matrix` keeps its first value, 1. Without `.copy()`, the slice would be a view, and `matrix` would change too.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `ndim`, `shape`, and `size` describe an array of any dimension.
    - Comma indexing reads one element. Negative indexes count from the end.
    - An integer array truncates a float assigned into it. Values that cannot be converted, such as `np.nan`, raise an error.
    - Slices read a range: the start is included and the stop is excluded. A negative step reverses.
    - A NumPy slice is a view. `.copy()` makes a separate array.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. Which index selects the last element of a 1-D array?
    2. How do you select the element in row 1, column 2 of a 2-D array?
    3. What happens when you assign `2.7` to an element of an integer array?
    4. In `numbers[2:5]`, which positions are included?
    5. What does `numbers[::-1]` return?
    6. What does `matrix[:, 1]` select?
    7. Why does changing a NumPy slice also change the original array?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **`-1`:** Negative indexes count from the end.
2. **`array[1, 2]`:** The row comes before the comma and the column after it. Positions start at 0.
3. **It is stored as `2`:** The array keeps its integer dtype, so the fractional part is dropped.
4. **2, 3, and 4:** The start is included and the stop, 5, is excluded.
5. **The reversed list:** A step of -1 walks from the end to the beginning.
6. **The second column:** `:` selects every row, and `1` is the column at position 1.
7. **It is a view:** The slice shares data with the original. Use `.copy()` to get an independent array.
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
