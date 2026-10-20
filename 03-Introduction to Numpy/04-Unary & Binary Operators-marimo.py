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

    - Summarize an array with `min`, `max`, `sum`, `mean`, and `cumsum`, and locate the largest value with `argmax`.
    - Add, subtract, and multiply arrays element by element, and multiply matrices with `dot` or `@`.
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
    ## Reductions and running totals

    `max`, `min`, `sum`, and `mean` reduce an array to a smaller result. `argmax` returns the position of the largest value. `axis=1` works across each row. `axis=0` works down each column. `cumsum` keeps a running total.

    The examples use this table with 2 rows and 3 columns.
    """)
    return


@app.cell
def _(np):
    values = np.array([[1, 2, 3], [4, 5, 6]])
    print(values)
    return (values,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With no axis, `max` looks at every element and returns one value.
    """)
    return


@app.cell
def _(values):
    print(values.max())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `axis=1` returns the largest value of each row: one result per row.
    """)
    return


@app.cell
def _(values):
    print(values.max(axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `axis=0` returns the largest value of each column: one result per column.
    """)
    return


@app.cell
def _(values):
    print(values.max(axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `min` returns the smallest value of the whole array.
    """)
    return


@app.cell
def _(values):
    print(values.min())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sum` adds every element: 1 + 2 + 3 + 4 + 5 + 6 = 21.
    """)
    return


@app.cell
def _(values):
    print(values.sum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sum(axis=1)` adds each row: 1 + 2 + 3 = 6 and 4 + 5 + 6 = 15.
    """)
    return


@app.cell
def _(values):
    print(values.sum(axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `mean` is the average of every element: 21 / 6 = 3.5.
    """)
    return


@app.cell
def _(values):
    print(values.mean())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `mean(axis=0)` returns the average of each column: one result per column.
    """)
    return


@app.cell
def _(values):
    print(values.mean(axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `argmax` returns the position of the largest value. Here that value is 6, at position 5, counting row by row from 0.
    """)
    return


@app.cell
def _(values):
    print(values.argmax())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `cumsum(axis=1)` keeps a running total across each row. The last value in each row is the row sum.
    """)
    return


@app.cell
def _(values):
    print(values.cumsum(axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `cumsum(axis=0)` keeps a running total down each column.
    """)
    return


@app.cell
def _(values):
    print(values.cumsum(axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With no axis, `cumsum` reads the elements row by row and returns a 1-D running total.
    """)
    return


@app.cell
def _(values):
    print(values.cumsum())
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
    ### Try it yourself

    Find the smallest value of each row of `np.array([[3, 9, 1], [7, 2, 8]])`. Replace `None` with your code. Which axis did you use, and why?
    """)
    return


@app.cell
def _():
    student_row_min = None
    print(student_row_min)
    return (student_row_min,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_row_min = np.array([[3, 9, 1], [7, 2, 8]]).min(axis=1)
```
The result is `[1, 2]`. `axis=1` works across each row, so there is one result per row. `axis=0` would give one result per column.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Binary operators

    `+`, `-`, and `*` combine arrays element by element. The shapes must either match or be compatible for broadcasting.
    `dot` is matrix multiplication: the number of columns in the first array must equal the number of rows in the second. `@` does the same multiplication.

    The examples use these two 2 × 2 arrays, `left` and `right`.
    """)
    return


@app.cell
def _(np):
    left = np.array([[0, 1], [2, 3]])
    right = np.array([[1, 1], [1, 1]])
    print(left)
    print(right)
    return left, right


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `+` adds each pair of elements.
    """)
    return


@app.cell
def _(left, right):
    print(left + right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `-` subtracts each pair of elements.
    """)
    return


@app.cell
def _(left, right):
    print(left - right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `*` multiplies each pair of elements. Every element of `right` is 1, so the result equals `left`.
    """)
    return


@app.cell
def _(left, right):
    print(left * right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `dot` is matrix multiplication. Each result is a row of `left` times a column of `right`, added up. For example, the first row `[0, 1]` times the first column `[1, 1]` is 0 × 1 + 1 × 1 = 1.
    """)
    return


@app.cell
def _(left, right):
    print(left.dot(right))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `left @ right` gives the same result as `left.dot(right)`.
    """)
    return


@app.cell
def _(left, right):
    print(left @ right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `wider` has 2 rows and 3 columns. `left` has 2 columns, which matches the 2 rows of `wider`, so `dot` works.
    """)
    return


@app.cell
def _(left, np):
    wider = np.array([[1, 1, 1], [2, 2, 2]])
    print(left.shape, wider.shape)
    return (wider,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The result has the rows of `left` and the columns of `wider`: 2 × 3.
    """)
    return


@app.cell
def _(left, wider):
    print(left.dot(wider))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Universal functions

    Applying one operation to every element, instead of writing a Python loop, is called **vectorization**. NumPy does that with universal functions (`ufuncs`). Each arithmetic operator has a ufunc with the same result.

    | Operator | Ufunc | Description |
    |---|---|---|
    | `+` | `np.add` | addition |
    | `-` | `np.subtract` | subtraction |
    | `-` | `np.negative` | unary negation |
    | `*` | `np.multiply` | multiplication |
    | `/` | `np.divide` | division |
    | `//` | `np.floor_divide` | floor division |
    | `**` | `np.power` | exponentiation |
    | `%` | `np.mod` | remainder |
    | `abs()` | `np.absolute` | absolute value |

    `np.add` gives the same result as `left + right`.
    """)
    return


@app.cell
def _(left, np, right):
    print(np.add(left, right))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `np.subtract` gives the same result as `left - right`.
    """)
    return


@app.cell
def _(left, np, right):
    print(np.subtract(left, right))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `np.multiply` gives the same result as `left * right`.
    """)
    return


@app.cell
def _(left, np, right):
    print(np.multiply(left, right))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `np.divide` divides each pair of elements. The result is float, even when the values divide evenly.
    """)
    return


@app.cell
def _(left, np, right):
    print(np.divide(left, right))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `np.add` is a `ufunc` object. `np.subtract`, `np.multiply`, and `np.divide` have the same type.
    """)
    return


@app.cell
def _(np):
    print(type(np.add))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ufuncs also accept Python lists. The next examples use these lists.
    """)
    return


@app.cell
def _():
    bases = [10, 20, 30, 40, 50]
    exponents = [2, 3, 2, 3, 2]
    signed = [-5, 2, -3, -1, 6, 3]
    print(bases, exponents, signed)
    return bases, exponents, signed


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `np.power` raises each base to its exponent: 10² = 100, 20³ = 8000, and so on.
    """)
    return


@app.cell
def _(bases, exponents, np):
    print(np.power(bases, exponents))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `np.mod` is the remainder of each division: 10 % 2 = 0, 20 % 3 = 2, and so on.
    """)
    return


@app.cell
def _(bases, exponents, np):
    print(np.mod(bases, exponents))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `np.remainder` is another name for `np.mod`, so the result is the same.
    """)
    return


@app.cell
def _(bases, exponents, np):
    print(np.remainder(bases, exponents))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `np.absolute` removes the sign of each value.
    """)
    return


@app.cell
def _(np, signed):
    print(np.absolute(signed))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Broadcasting and transpose

    A scalar is a 0-D array. NumPy repeats it across a larger array so the operation is element by element. The examples use the numbers 0 to 5.
    """)
    return


@app.cell
def _(np):
    sequence = np.arange(6)
    print(sequence)
    return (sequence,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `+ 5` adds 5 to every element.
    """)
    return


@app.cell
def _(sequence):
    print(sequence + 5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `- 1` subtracts 1 from every element.
    """)
    return


@app.cell
def _(sequence):
    print(sequence - 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `* 10` multiplies every element by 10.
    """)
    return


@app.cell
def _(sequence):
    print(sequence * 10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `** 2` squares every element.
    """)
    return


@app.cell
def _(sequence):
    print(sequence ** 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A 1-D array of 3 values is added to each row of the 2 × 3 table `values`, because the last sizes match.
    """)
    return


@app.cell
def _(np, values):
    print(values + np.array([10, 20, 30]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `.T` swaps rows and columns. This array has 2 rows and 3 columns.
    """)
    return


@app.cell
def _(np):
    rectangular = np.array([[1, 2, 3], [4, 5, 6]])
    print(rectangular)
    return (rectangular,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Its transpose has 3 rows and 2 columns. The first row became the first column.
    """)
    return


@app.cell
def _(rectangular):
    print(rectangular.T)
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
    ### Try it yourself

    Multiply `rectangular` by its transpose with `dot`. Replace `None` with your code. What is the shape of the result, and why?
    """)
    return


@app.cell
def _():
    student_product = None
    print(student_product)
    return (student_product,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_product = rectangular.dot(rectangular.T)
```
The shape is `(2, 2)`. `rectangular` is 2 × 3 and its transpose is 3 × 2. The 3 columns match the 3 rows, and the result keeps the 2 rows of the first array and the 2 columns of the second. The values are `[[14, 32], [32, 77]]`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Trigonometry and logarithms

    `sin` and `cos` expect radians. The examples use the angles 0, π/2, and π. The results are rounded to 5 decimals, because the computer stores π only approximately.
    """)
    return


@app.cell
def _(np):
    angles = np.array([0, np.pi / 2, np.pi])
    print(np.round(np.sin(angles), 5))
    return (angles,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The cosine of the same angles.
    """)
    return


@app.cell
def _(angles, np):
    print(np.round(np.cos(angles), 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `trunc` drops the fractional part. The tiny value of `sin(π)` becomes 0.
    """)
    return


@app.cell
def _(angles, np):
    print(np.trunc(np.sin(angles)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same for the cosine.
    """)
    return


@app.cell
def _(angles, np):
    print(np.trunc(np.cos(angles)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `log2`, `log`, and `log10` use bases 2, e, and 10. The examples use these values.
    """)
    return


@app.cell
def _(np):
    log_inputs = np.array([1, 2, 10, 100])
    print(log_inputs)
    return (log_inputs,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `log2` asks: 2 to which power gives the value? log2(2) = 1.
    """)
    return


@app.cell
def _(log_inputs, np):
    print(np.round(np.log2(log_inputs), 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `log` is the natural logarithm, with base e.
    """)
    return


@app.cell
def _(log_inputs, np):
    print(np.round(np.log(log_inputs), 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `log10` uses base 10: log10(10) = 1 and log10(100) = 2.
    """)
    return


@app.cell
def _(log_inputs, np):
    print(np.round(np.log10(log_inputs), 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `axis` chooses whether a reduction runs across rows or down columns. `mean` is an average. `argmax` returns the position of the largest value.
    - `+` and `*` are element by element. `dot` and `@` are matrix multiplication.
    - Ufuncs and broadcasting apply one operation to a whole array. A 1-D array can be added to each row when the last sizes match.
    - `.T` transposes an array. `sin`, `cos`, and `log` are element-wise too.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What does `values.sum(axis=0)` return for a table with 2 rows and 3 columns?
    2. What is the last value of `np.array([1, 2, 3]).cumsum()`?
    3. What is the difference between `a * b` and `a.dot(b)`?
    4. When can `a.dot(b)` be computed?
    5. What does `np.arange(4) + 10` return?
    6. What is the shape of the transpose of a 2 × 5 array?
    7. Do `np.sin` and `np.cos` expect degrees or radians?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **Three sums, one per column:** `axis=0` works down each column.
2. **6:** The running total ends with the sum of all elements, 1 + 2 + 3.
3. **Element by element versus matrix multiplication:** `*` multiplies each pair of elements. `dot` adds the products of rows and columns.
4. **When the inner sizes match:** The number of columns of `a` must equal the number of rows of `b`.
5. **`[10, 11, 12, 13]`:** Broadcasting adds 10 to every element.
6. **`(5, 2)`:** The transpose swaps rows and columns.
7. **Radians:** For example, π/2 radians is 90 degrees.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - [NumPy universal functions](https://numpy.org/doc/stable/reference/ufuncs.html)
    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 2.
    """)
    return


if __name__ == "__main__":
    app.run()
