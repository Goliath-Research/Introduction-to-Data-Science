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

    NumPy is usually imported as `np`. The main namespace holds the array tools. Specialized work lives in submodules such as `linalg` (linear algebra), `fft`, `polynomial`, `random`, and `strings`.
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

    An array is similar to a list, except every element has the same type, usually a number. A **structured array** can store named fields of different types in each item. Arrays are much faster than lists for large amounts of numeric data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dimensions

    A 0-D array is a scalar. A 1-D array is a sequence. A 2-D array is a table. A 3-D array is a stack of tables.
    """)
    return


@app.cell
def _(np):
    scalar_array = np.array(5)
    vector = np.array([1, 2, 3, 4, 5, 6])
    table = np.array([[1, 2, 3], [4, 5, 6]])
    cube = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])

    student_type = np.dtype([("student", np.str_, 32), ("grade", np.float64)])
    records = np.array([("Sarah", 8.0), ("John", 6.0)], dtype=student_type)

    print("scalar:", scalar_array)
    print("vector:", vector)
    print("table:\n", table)
    print("cube:\n", cube)
    print("records:", records)
    print("first student:", records[0])
    print("name:", records[0]["student"], "grade:", records[0]["grade"])
    return cube, records, scalar_array, table, vector


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All of these values are `numpy.ndarray` objects. `ndim` is the number of axes, `shape` is the length of each axis, `size` is the total number of elements, and `dtype` is the type of the elements.
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
    ## Ways to create an array

    You can build an array from a list or a tuple. If any value is a float, the whole array becomes floating-point. `dtype` can force a type.
    """)
    return


@app.cell
def _(np):
    from_list = np.array([[1, 2, 3], [4, 5, 6]], dtype="float")
    from_tuple = np.array((1, 2, 3, 4, 5))
    from_mixed_tuple = np.array((1, 2, 3, 4, 5.4))

    print(from_list, from_list.dtype)
    print(from_tuple, from_tuple.dtype)
    print(from_mixed_tuple, from_mixed_tuple.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Constant arrays fill every element with the same value. `zeros`, `ones`, and `full` take the shape as a tuple.
    """)
    return


@app.cell
def _(np):
    print("zeros:\n", np.zeros((3, 3)))
    print("ones:\n", np.ones((3, 3)))
    print("fives:\n", np.full((3, 3), 5))
    print("identity:\n", np.eye(3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Random constructors draw a new array of the requested shape. `random` is uniform between 0 and 1. `randint(high, size=...)` draws integers from 0 up to, but not including, `high`. `normal(mean, std, shape)` draws from a normal distribution.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    print("uniform:\n", np.round(np.random.random((3, 3)), 3))
    print("integers 0-10:\n", np.random.randint(11, size=(3, 3)))
    print("integers 0-9, shape 2x3:\n", np.random.randint(10, size=(2, 3)))
    print("normal mean 0, std 1, shape 2x3:\n", np.round(np.random.normal(0, 1, (2, 3)), 3))
    print("normal mean 10, std 5, shape 3x3:\n", np.round(np.random.normal(10, 5, (3, 3)), 3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `linspace(start, stop, count)` returns `count` evenly spaced values and **includes** both ends. `arange(start, stop, step)` starts at `start`, steps by `step`, and **stops before** `stop`.
    """)
    return


@app.cell
def _(np):
    eleven_points = np.linspace(0, 5, 11)
    print("linspace count:", len(eleven_points))
    print(eleven_points)
    print("linspace 6 points:", np.linspace(0, 5, 6))
    print("arange step 2, stop before 20:", np.arange(0, 20, 2))
    print("arange step 2, include 20:", np.arange(0, 21, 2))
    print("arange step 5, stop before 21:", np.arange(0, 21, 5))
    print("arange step 5, stop before 28:", np.arange(0, 28, 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `indices` builds one coordinate array per axis. With `sparse=False`, each array has the full requested shape.
    """)
    return


@app.cell
def _(np):
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
    ## Conclusions

    **Key takeaways:**

    - A NumPy array is an `ndarray`. Every element shares one dtype.
    - `ndim`, `shape`, `size`, and `dtype` describe the array.
    - `zeros`, `ones`, `full`, `eye`, `random`, `linspace`, and `arange` build arrays without typing every value.
    - `linspace` includes the stop value. `arange` stops before it.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 2.
    """)
    return


if __name__ == "__main__":
    app.run()
