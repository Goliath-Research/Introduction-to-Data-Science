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
    # Operators and Universal Functions

    ## Objectives

    - Summarize an array with `min`, `max`, `sum`, and `cumsum`.
    - Add, subtract, and multiply arrays element by element, and multiply matrices with `dot`.
    - Use universal functions and broadcasting, including trigonometry and logarithms.

    ## Background

    A universal function, or ufunc, applies one operation to every element. That is faster than a Python loop. Broadcasting stretches a smaller array so it can combine with a larger one.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Unary reductions

    `max`, `min`, and `sum` reduce an array to a smaller result. `axis=1` works across each row. `axis=0` works down each column. `cumsum` keeps a running total.
    """)
    return


@app.cell
def _(np):
    values = np.array([[1, 2, 3], [4, 5, 6]])
    print(values)
    print("max:", values.max())
    print("max of each row:", values.max(axis=1))
    print("max of each column:", values.max(axis=0))
    print("min:", values.min())
    print("sum:", values.sum())
    print("sum of each row:", values.sum(axis=1))
    print("cumsum of each row:\n", values.cumsum(axis=1))
    print("cumsum of each column:\n", values.cumsum(axis=0))
    print("cumsum of the whole array:", values.cumsum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the table, then print the sum of each column.
    """)
    return


@app.cell
def _(np):
    your_table = np.array([[2, 4], [6, 8]])
    print(your_table.sum(axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Binary operators

    `+`, `-`, and `*` combine arrays element by element, so the shapes must match. `dot` is matrix multiplication: the number of columns in the first array must equal the number of rows in the second.
    """)
    return


@app.cell
def _(np):
    left = np.array([[0, 1], [2, 3]])
    right = np.array([[1, 1], [1, 1]])
    wider = np.array([[1, 1, 1], [2, 2, 2]])

    print("sum:\n", left + right)
    print("difference:\n", left - right)
    print("element product:\n", left * right)
    print("dot of the square arrays:\n", left.dot(right))
    print("shapes", left.shape, wider.shape)
    print("dot with the wider array:\n", left.dot(wider))
    return left, right


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Universal functions

    Each arithmetic operator has a ufunc with the same result.

    | Operator | Ufunc | Description |
    |---|---|---|
    | `+` | `np.add` | addition |
    | `-` | `np.subtract` | subtraction |
    | `-` | `np.negative` | unary negation |
    | `*` | `np.multiply` | multiplication |
    | `/` | `np.divide` | division |
    | `**` | `np.power` | exponentiation |
    | `%` | `np.mod` | remainder |
    """)
    return


@app.cell
def _(left, np, right):
    print("add:\n", np.add(left, right))
    print("subtract:\n", np.subtract(left, right))
    print("multiply:\n", np.multiply(left, right))
    print("divide:\n", np.divide(left, right))
    print(type(np.add), type(np.subtract), type(np.multiply), type(np.divide))
    return


@app.cell
def _(np):
    bases = [10, 20, 30, 40, 50]
    exponents = [2, 3, 2, 3, 2]
    signed = [-5, 2, -3, -1, 6, 3]
    print("power:", np.power(bases, exponents))
    print("mod:", np.mod(bases, exponents))
    print("remainder:", np.remainder(bases, exponents))
    print("absolute:", np.absolute(signed))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Broadcasting and transpose

    A scalar is a 0-D array. NumPy repeats it across a larger array so the operation is element by element. `.T` swaps rows and columns.
    """)
    return


@app.cell
def _(np):
    sequence = np.arange(6)
    print("original: ", sequence)
    print("plus 5:   ", sequence + 5)
    print("minus 1:  ", sequence - 1)
    print("times 10: ", sequence * 10)
    print("squared:  ", sequence ** 2)

    rectangular = np.array([[1, 2, 3], [4, 5, 6]])
    print("transposed:\n", rectangular.T)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `factor`. Every element is multiplied by it.
    """)
    return


@app.cell
def _(np):
    your_values = np.array([1, 2, 3, 4])
    factor = 3
    print(your_values * factor)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Trigonometry and logarithms

    `sin` and `cos` expect radians. `trunc` drops the fractional part. `log2`, `log`, and `log10` use bases 2, e, and 10.
    """)
    return


@app.cell
def _(np):
    angles = np.array([0, np.pi / 2, np.pi])
    print("sin:", np.round(np.sin(angles), 5))
    print("cos:", np.round(np.cos(angles), 5))
    print("truncated sin:", np.trunc(np.sin(angles)))
    print("truncated cos:", np.trunc(np.cos(angles)))

    powers_of_ten = np.array([1, 2, 10, 100])
    print("log2: ", np.round(np.log2(powers_of_ten), 2))
    print("log:  ", np.round(np.log(powers_of_ten), 2))
    print("log10:", np.round(np.log10(powers_of_ten), 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `axis` chooses whether a reduction runs across rows or down columns.
    - `+` and `*` are element by element. `dot` is matrix multiplication.
    - Ufuncs and broadcasting apply one operation to a whole array.
    - `.T` transposes an array. `sin`, `cos`, and `log` are element-wise too.

    ## References

    - [NumPy universal functions](https://numpy.org/doc/stable/reference/ufuncs.html)
    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 2.
    """)
    return


if __name__ == "__main__":
    app.run()
