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
    - Loop over the elements or the rows of an array.
    - Concatenate and split arrays along rows or columns.
    - Search for values with `where` and sort with `sort`.

    ## Background

    These tools rearrange an array. `reshape` returns a new shape and leaves the original array's shape unchanged. The new shape must hold the same number of elements. Later sections join arrays, cut them apart, find values, and sort them.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reshape and flatten

    `reshape` gives an array a new shape. The number of elements must stay the same, and the original array keeps its shape. The reshaped array shares that data when it can (it is a view). `flatten` returns a 1-D copy.

    The examples use `grid`, which has 3 rows and 4 columns.
    """)
    return


@app.cell
def _(np):
    grid = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(grid)
    return (grid,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Its shape is `(3, 4)`, so it has 3 × 4 = 12 elements.
    """)
    return


@app.cell
def _(grid):
    print("shape", grid.shape, "ndim", grid.ndim, "size", grid.size)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same 12 values in 4 rows and 3 columns. The values are read row by row and refilled row by row.
    """)
    return


@app.cell
def _(grid):
    print(grid.reshape(4, 3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    2 rows and 6 columns.
    """)
    return


@app.cell
def _(grid):
    print(grid.reshape(2, 6))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1 row and 12 columns. The result is still 2-D, so it has two pairs of brackets.
    """)
    return


@app.cell
def _(grid):
    print(grid.reshape(1, 12))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    12 rows and 1 column.
    """)
    return


@app.cell
def _(grid):
    print(grid.reshape(12, 1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `reshape` returned new arrays, but they share data with `grid` (they are views). `grid` keeps its shape. To change a reshaped array safely, call `.copy()`.
    """)
    return


@app.cell
def _(grid):
    print(grid.shape)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The new shape has to contain the same number of elements. This array has 12 elements. A shape of `(2, 5)` has 10, so the next cell raises a `ValueError` on purpose.
    """)
    return


@app.cell
def _(grid):
    grid.reshape(2, 5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `reshape(12)` gives a 1-D array with shape `(12,)`.
    """)
    return


@app.cell
def _(grid):
    flat_reshape = grid.reshape(12)
    print(flat_reshape, flat_reshape.shape)
    return (flat_reshape,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `flatten()` gives the same values and the same shape. Unlike `reshape`, it always returns a copy, so changing it never changes `grid`.
    """)
    return


@app.cell
def _(grid):
    flat_copy = grid.flatten()
    print(flat_copy, flat_copy.shape)
    return


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
    ### Try it yourself

    Reshape `np.arange(6)` into 3 rows and 2 columns. Replace `None` with your code. Which values are in the last row?
    """)
    return


@app.cell
def _():
    student_reshaped = None
    print(student_reshaped)
    return (student_reshaped,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_reshaped = np.arange(6).reshape(3, 2)
```
The last row is `[4, 5]`. The values 0 to 5 fill the rows in order: `[0, 1]`, `[2, 3]`, `[4, 5]`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Iterating

    A loop over a 1-D array yields one element at a time.
    """)
    return


@app.cell
def _(flat_reshape):
    for item in flat_reshape:
        print(item)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A loop over a 2-D array yields one row at a time. Here `grid` is reshaped into 2 rows of 6, so the loop runs twice.
    """)
    return


@app.cell
def _(grid):
    for row in grid.reshape(2, 6):
        print(row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concatenation

    `concatenate` joins arrays. `+` adds them element by element; it does not join them. The two examples use these arrays.
    """)
    return


@app.cell
def _(np):
    ones_vector = np.array([1, 1, 1])
    twos_vector = np.array([2, 2, 2])
    print(ones_vector, twos_vector)
    return ones_vector, twos_vector


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `concatenate` places the second array after the first. The result has 6 elements. In NumPy 2, `np.concat` is another name for `np.concatenate`.
    """)
    return


@app.cell
def _(np, ones_vector, twos_vector):
    print(np.concatenate([ones_vector, twos_vector]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `+` adds each pair of elements. The result has 3 elements.
    """)
    return


@app.cell
def _(ones_vector, twos_vector):
    print(ones_vector + twos_vector)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Choosing the axis

    A 2-D array has rows and columns, so you choose the axis. `axis=0` stacks rows. That is also the default. `axis=1` stacks columns. The examples join a 2 × 2 block of zeros and a 2 × 2 block of ones.

    With the default axis, the ones are added as extra rows. The result is 4 × 2.
    """)
    return


@app.cell
def _(np):
    zeros_block = np.zeros((2, 2))
    ones_block = np.ones((2, 2))
    print(np.concatenate([zeros_block, ones_block]))
    return ones_block, zeros_block


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `axis=0` gives the same result, because it is the default.
    """)
    return


@app.cell
def _(np, ones_block, zeros_block):
    print(np.concatenate([zeros_block, ones_block], axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `axis=1` adds the ones as extra columns. The result is 2 × 4.
    """)
    return


@app.cell
def _(np, ones_block, zeros_block):
    print(np.concatenate([zeros_block, ones_block], axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `vstack` can put a 1-D row on top of a 2-D array. `hstack` needs the new column written as a 2-D column, `[[8], [8]]`.
    """)
    return


@app.cell
def _(np):
    top_row = np.array([1, 2, 3])
    lower_rows = np.array([[4, 4, 4], [5, 5, 5]])
    print(np.vstack([top_row, lower_rows]))
    return (lower_rows,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `hstack` places a column on the right of the array. The column is written as 2 rows of 1 value.
    """)
    return


@app.cell
def _(lower_rows, np):
    extra_column = np.array([[8], [8]])
    print(np.hstack([lower_rows, extra_column]))
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
    ## Splitting

    `split` is the reverse of concatenation. An integer divides the array into equal parts. A list of indexes gives the cut positions. `vsplit` cuts rows and `hsplit` cuts columns.

    The examples start with the numbers 0 to 8.
    """)
    return


@app.cell
def _(np):
    sequence = np.arange(9)
    print(sequence)
    return (sequence,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `split(sequence, 3)` gives 3 equal parts of 3 values.
    """)
    return


@app.cell
def _(np, sequence):
    left, middle, right = np.split(sequence, 3)
    print(left, middle, right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `split(sequence, [2, 6])` cuts before position 2 and before position 6. The parts have 2, 4, and 3 values.
    """)
    return


@app.cell
def _(np, sequence):
    first, second, third = np.split(sequence, [2, 6])
    print(first, second, third)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The 2-D examples use a 4 × 4 block with the numbers 0 to 15.
    """)
    return


@app.cell
def _(np):
    block = np.arange(16).reshape((4, 4))
    print(block)
    return (block,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `vsplit(block, 2)` cuts the rows in half. `upper` is the first two rows.
    """)
    return


@app.cell
def _(block, np):
    upper, lower = np.vsplit(block, 2)
    print(upper)
    return (lower,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `lower` is the last two rows.
    """)
    return


@app.cell
def _(lower):
    print(lower)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `hsplit(block, 2)` cuts the columns in half. `left_half` is the first two columns.
    """)
    return


@app.cell
def _(block, np):
    left_half, right_half = np.hsplit(block, 2)
    print(left_half)
    return (right_half,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `right_half` is the last two columns.
    """)
    return


@app.cell
def _(right_half):
    print(right_half)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Split `np.arange(10)` at positions 3 and 7. Replace `None` with your code. How many parts do you get, and how many values are in each part?
    """)
    return


@app.cell
def _():
    student_parts = None
    print(student_parts)
    return (student_parts,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_parts = np.split(np.arange(10), [3, 7])
```
Two cut positions give three parts: `[0, 1, 2]`, `[3, 4, 5, 6]`, and `[7, 8, 9]`. They have 3, 4, and 3 values.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Search

    `where(condition)` returns a tuple. The first item is the array of indexes where the condition is true. An empty index array means there was no match.

    The examples search this array.
    """)
    return


@app.cell
def _(np):
    values = np.array([-5, 6, 4, 4, 1, 0, -6])
    print(values)
    return (values,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `where(values == 1)` returns a tuple that holds one array of indexes.
    """)
    return


@app.cell
def _(np, values):
    index_one = np.where(values == 1)
    print(index_one)
    return (index_one,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[0]` takes that array out of the tuple. The value 1 is at position 4.
    """)
    return


@app.cell
def _(index_one):
    print(index_one[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A loop over the index array prints each match with its value.
    """)
    return


@app.cell
def _(index_one, values):
    for position_one in index_one[0]:
        print("index:", position_one, "value:", values[position_one])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The value 4 appears twice, at positions 2 and 3.
    """)
    return


@app.cell
def _(np, values):
    for position_four in np.where(values == 4)[0]:
        print("index:", position_four, "value:", values[position_four])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The value 9 is not in the array, so the index array is empty.
    """)
    return


@app.cell
def _(np, values):
    print(np.where(values == 9)[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%` is the remainder after floor division. `%` with 2 gives 1 for every odd integer, negative ones too (`-5 % 2` is 1). The odd values here are -5 and 1.
    """)
    return


@app.cell
def _(np, values):
    # An odd integer leaves a remainder of 1 when divided by 2.
    for position_odd in np.where(values % 2 == 1)[0]:
        print("index:", position_odd, "value:", values[position_odd])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `values > 0` finds the positive values. 0 is not positive, so it is not included.
    """)
    return


@app.cell
def _(np, values):
    for position_positive in np.where(values > 0)[0]:
        print("index:", position_positive, "value:", values[position_positive])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sort

    `np.sort` returns a sorted copy. The original array stays unchanged. The default is `axis=-1`, the last axis, which is the rows for 2-D. `axis=0` sorts each column. `np.sort` has no descending option; use `np.sort(x)[::-1]`.

    The first example sorts 10 random integers.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    random_values = np.random.randint(10, size=10)
    print(random_values)
    return (random_values,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The sorted copy, from smallest to largest.
    """)
    return


@app.cell
def _(np, random_values):
    print(np.sort(random_values))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[::-1]` reverses that sorted copy, so the largest value comes first.
    """)
    return


@app.cell
def _(np, random_values):
    print(np.sort(random_values)[::-1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The original array is still in its first order.
    """)
    return


@app.cell
def _(random_values):
    print(random_values)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For a 2-D array, `np.sort` sorts each row on its own.
    """)
    return


@app.cell
def _(np):
    paired_rows = np.array([[3, 2, 5], [7, 0, 1]])
    print(np.sort(paired_rows))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next examples use this 3 × 3 array.
    """)
    return


@app.cell
def _(np):
    column_major = np.array([[1, 0, 2], [5, 6, 4], [3, -1, 6]])
    print(column_major)
    return (column_major,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The default is the last axis, so this sorts each row.
    """)
    return


@app.cell
def _(column_major, np):
    print(np.sort(column_major))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `axis=0` sorts each column, from top to bottom.
    """)
    return


@app.cell
def _(column_major, np):
    print(np.sort(column_major, axis=0))
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
    ### Try it yourself

    Sort each column of `np.array([[4, 1], [2, 3]])`. Replace `None` with your code. Which value ends up at the top of the first column?
    """)
    return


@app.cell
def _():
    student_sorted = None
    print(student_sorted)
    return (student_sorted,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_sorted = np.sort(np.array([[4, 1], [2, 3]]), axis=0)
```
The result is `[[2, 1], [4, 3]]`. The first column was 4 and 2, so 2 moves to the top. The second column, 1 and 3, was already sorted.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `reshape` keeps the same values and requires a compatible size. It is a view when it can. `flatten` returns a 1-D copy.
    - A loop over a 1-D array yields elements. A loop over a 2-D array yields rows.
    - `concatenate` joins arrays. `+` adds them. `axis=0` adds rows and `axis=1` adds columns.
    - `split`, `vsplit`, and `hsplit` cut an array into parts.
    - `where` finds indexes. `np.sort` returns a new sorted array. The default axis is the last one. Reverse the result with `[::-1]` for descending order.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. Can an array with 12 elements be reshaped to `(5, 2)`?
    2. Does `reshape` change the shape of the original array?
    3. What is the difference between `np.concatenate([a, b])` and `a + b`?
    4. Which axis adds the second array as extra columns?
    5. What does `np.split(np.arange(8), 4)` return?
    6. What does `np.where(values == 9)[0]` return when 9 is not in `values`?
    7. Does `np.sort(x)` change `x`?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **No:** `(5, 2)` holds 10 elements, not 12. NumPy raises a `ValueError`.
2. **No:** It returns an array with the new shape. That array is a view when it can, so it shares data with the original. The original keeps its shape.
3. **Joining versus adding:** `concatenate` places `b` after `a`. `+` adds each pair of elements.
4. **`axis=1`:** `axis=0`, the default, adds extra rows.
5. **Four parts of two values:** `[0, 1]`, `[2, 3]`, `[4, 5]`, and `[6, 7]`.
6. **An empty array:** There are no positions where the condition is true.
7. **No:** `np.sort` returns a sorted copy. The original keeps its order.
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
