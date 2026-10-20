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
    # Introduction to NumPy

    ## Objectives

    - Introduce NumPy, a Python library for numerical computing.
    - Create and inspect arrays of different dimensions.
    - Compare the ways NumPy can build arrays: from sequences, constants, random values, and ranges.

    ## Background

    NumPy (Numerical Python) is the foundational package for scientific computing in Python. It provides a multidimensional array object. Unlike Python lists, NumPy arrays are compact, and mathematical operations run over the whole array.

    ## Datasets Used

    This notebook does not use external datasets. Examples use values created with NumPy.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The NumPy library

    NumPy works with arrays and matrices of numbers. It is usually imported as `np`, so the package is referred to by that short name.

    The main tools live in `numpy` itself. Other parts of the library handle specialized work:

    - `fft` computes the discrete Fourier transform.
    - `linalg` handles linear algebra, including the dot product and matrix multiplication.
    - `polynomial` works with polynomials.
    - `random` draws samples from several distributions.
    - `strings` operates on arrays of text.
    - `testing` provides checks used in NumPy's own tests.
    - `typing` exposes type names such as `ArrayLike` and `DTypeLike`.

    This lesson uses the main array tools and `random`.
    """)
    return


@app.cell
def _(np):
    print("NumPy version:", np.__version__)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The array

    An array is similar to a list, except every element has the same type, usually a number such as `int` or `float`. Arrays are much faster than lists for whole-array math when the data is large and numeric.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dimensions

    A 0-D array is a scalar: one single value.
    """)
    return


@app.cell
def _(np):
    scalar_array = np.array(5)
    print(scalar_array)
    return (scalar_array,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A 1-D array is a sequence of values.
    """)
    return


@app.cell
def _(np):
    vector = np.array([1, 2, 3, 4, 5, 6])
    print(vector)
    return (vector,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A 2-D array is a table. It is written as a list of rows. This one has 2 rows and 3 columns.
    """)
    return


@app.cell
def _(np):
    table = np.array([[1, 2, 3], [4, 5, 6]])
    print(table)
    return (table,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A 3-D array is a stack of tables. This one has 2 tables, and each table has 2 rows and 3 columns.
    """)
    return


@app.cell
def _(np):
    cube = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
    print(cube)
    return (cube,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Structured arrays

    A **structured array** stores one record in each element. A record is a group of named **fields**, and those fields may have different types. The example below has a text field, `student`, and a float field, `grade`.
    """)
    return


@app.cell
def _(np):
    # A structured dtype names each field and gives it a type.
    student_type = np.dtype([("student", np.str_, 32), ("grade", np.float64)])
    records = np.array([("Sarah", 8.0), ("John", 6.0)], dtype=student_type)
    print(records)
    return (records,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `records[0]` is the first record. It holds both fields.
    """)
    return


@app.cell
def _(records):
    print(records[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A field name selects one value from the record. This is the name of the first student.
    """)
    return


@app.cell
def _(records):
    print(records[0]["student"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And this is the grade of the first student.
    """)
    return


@app.cell
def _(records):
    print(records[0]["grade"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Array attributes

    All of these values are `numpy.ndarray` objects. `ndim` is the number of axes, `shape` is the length of each axis, `size` is the total number of elements, and `dtype` is the type of the elements.

    The cell prints one line per array, so you can compare them.
    """)
    return


@app.cell
def _(cube, records, scalar_array, table, vector):
    samples = {
        "scalar": scalar_array,
        "vector": vector,
        "table": table,
        "cube": cube,
        "records": records,
    }
    for label, sample in samples.items():
        print(
            f"{label:8} type={type(sample).__name__:8} "
            f"ndim={sample.ndim} shape={sample.shape} "
            f"size={sample.size:2} dtype={sample.dtype}"
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the numbers in `your_vector`, then print its dimension, shape, size, and dtype.
    """)
    return


@app.cell
def _(np):
    your_vector = np.array([10, 20, 30])

    print(your_vector)
    print("ndim:", your_vector.ndim)
    print("shape:", your_vector.shape)
    print("size:", your_vector.size)
    print("dtype:", your_vector.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Build a 2-D array with 2 rows and 4 columns, using any numbers you like. Replace each `None` with your code. What are its `shape` and its `size`?
    """)
    return


@app.cell
def _():
    student_table = None
    student_shape = None
    student_size = None
    print(student_table)
    print(student_shape)
    print(student_size)
    return student_shape, student_size, student_table


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_table = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
student_shape = student_table.shape
student_size = student_table.size
```
The shape is `(2, 4)`: 2 rows and 4 columns. The size is 8, because 2 × 4 = 8 elements.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ways to create an array

    You can build an array from a list. `dtype` can force a type. Here the numbers are whole, but `dtype="float"` stores them as floats.
    """)
    return


@app.cell
def _(np):
    from_list = np.array([[1, 2, 3], [4, 5, 6]], dtype="float")
    print(from_list, from_list.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A tuple works too. These values are whole numbers, so the type is an integer.
    """)
    return


@app.cell
def _(np):
    from_tuple = np.array((1, 2, 3, 4, 5))
    print(from_tuple, from_tuple.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If any value is a float, the whole array becomes floating-point. One value, `5.4`, is enough.
    """)
    return


@app.cell
def _(np):
    from_mixed_tuple = np.array((1, 2, 3, 4, 5.4))
    print(from_mixed_tuple, from_mixed_tuple.dtype)
    return (from_mixed_tuple,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `astype` converts to another dtype. Converting to int drops the fractional part, so `5.4` becomes `5`.
    """)
    return


@app.cell
def _(from_mixed_tuple):
    print(from_mixed_tuple.astype(int))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Constant arrays

    Constant arrays fill every element with the same value. `zeros`, `ones`, and `full` take the shape as a tuple. `zeros((3, 3))` is a 3 × 3 table of zeros.
    """)
    return


@app.cell
def _(np):
    print(np.zeros((3, 3)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `ones` fills the table with ones.
    """)
    return


@app.cell
def _(np):
    print(np.ones((3, 3)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `full` fills the table with the value you choose. Here it is 5.
    """)
    return


@app.cell
def _(np):
    print(np.full((3, 3), 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `eye(3)` is the 3 × 3 identity matrix: ones on the diagonal and zeros everywhere else.
    """)
    return


@app.cell
def _(np):
    print(np.eye(3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Random arrays

    Random constructors draw a new array of the requested shape. Each cell below sets the seed first, so it shows the same values every time it runs. Newer code uses `rng = np.random.default_rng(0)`, then `rng.integers(...)` and `rng.random(...)`.

    `random` is uniform from 0 up to, but not including, 1. The values are rounded to 3 decimals to keep the output short.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    print(np.round(np.random.random((3, 3)), 3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `randint(high, size=...)` draws integers from 0 up to, but not including, `high`. With `high=11`, the values go from 0 to 10.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    print(np.random.randint(11, size=(3, 3)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With `high=10` and `size=(2, 3)`, the values go from 0 to 9, in 2 rows and 3 columns.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    print(np.random.randint(10, size=(2, 3)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `normal(mean, std, shape)` draws from a normal distribution. With mean 0 and standard deviation 1, most values are between -2 and 2.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    print(np.round(np.random.normal(0, 1, (2, 3)), 3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With mean 10 and standard deviation 5, the values are centered around 10.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    print(np.round(np.random.normal(10, 5, (3, 3)), 3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ranges

    `linspace(start, stop, count)` returns `count` evenly spaced values and **includes** both ends. Eleven points from 0 to 5 are 0.5 apart.
    """)
    return


@app.cell
def _(np):
    print(np.linspace(0, 5, 11))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Six points from 0 to 5 are 1 apart.
    """)
    return


@app.cell
def _(np):
    print(np.linspace(0, 5, 6))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `arange(start, stop, step)` starts at `start`, steps by `step`, and **stops before** `stop`. With stop 20, the last value is 18.
    """)
    return


@app.cell
def _(np):
    print(np.arange(0, 20, 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To include 20, the stop has to be larger than 20. Here it is 21.
    """)
    return


@app.cell
def _(np):
    print(np.arange(0, 21, 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With a step of 5 and stop 21, the values are 0, 5, 10, 15, and 20.
    """)
    return


@app.cell
def _(np):
    print(np.arange(0, 21, 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With stop 28, the next value, 25, also fits. 30 does not, because it is past the stop.
    """)
    return


@app.cell
def _(np):
    print(np.arange(0, 28, 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `indices` builds one coordinate array per axis. With `sparse=False`, each array has the full requested shape. The first table holds the row number of each position, and the second table holds the column number.
    """)
    return


@app.cell
def _(np):
    # One dense 3x3 coordinate array per axis, stored as integers.
    print(np.indices((3, 3), dtype=int, sparse=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `start`, `stop`, and `step`, then compare `arange` with `linspace`.
    """)
    return


@app.cell
def _(np):
    start = 0
    stop = 10
    step = 2

    print(np.arange(start, stop, step))
    print(np.linspace(start, stop, 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Use `arange` to build the values 5, 10, 15, ..., 50, including 50. Replace `None` with your code. Why can the stop value not be 50?
    """)
    return


@app.cell
def _():
    student_range = None
    print(student_range)
    return (student_range,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_range = np.arange(5, 51, 5)
```
`arange` stops before the stop value. With stop 50, the last value would be 45. Any stop above 50, up to 55, includes 50.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A NumPy array is an `ndarray`. Every element shares one dtype. `astype` converts to another dtype.
    - An array can have 0, 1, 2, 3, or more dimensions. A structured array stores named fields in each element.
    - `ndim`, `shape`, `size`, and `dtype` describe the array.
    - `zeros`, `ones`, `full`, `eye`, `random`, `linspace`, and `arange` build arrays without typing every value.
    - `linspace` includes the stop value. `arange` stops before it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What is the main difference between a NumPy array and a Python list?
    2. What does `shape` tell you about a 2-D array?
    3. What is the dtype of `np.array([1, 2, 3.5])`?
    4. What does `np.full((2, 2), 7)` return?
    5. Why does each random cell in this lesson call `np.random.seed(0)` first?
    6. Does `np.arange(0, 10, 2)` include 10?
    7. Does `np.linspace(0, 10, 5)` include 10?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **One type for all elements:** Every element of an array has the same dtype. That makes arrays compact and fast for numbers.
2. **Rows and columns:** `shape` is a tuple with the number of rows, then the number of columns. In general it is one number per axis.
3. **`float64`:** One float value is enough to make the whole array floating-point.
4. **A 2 × 2 table of sevens:** `full` fills every element with the value you pass.
5. **To repeat the same values:** With the same seed, the random values are the same every time the cell runs.
6. **No:** `arange` stops before the stop value. The last value is 8.
7. **Yes:** `linspace` includes both ends. The values are 0, 2.5, 5, 7.5, and 10.
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
