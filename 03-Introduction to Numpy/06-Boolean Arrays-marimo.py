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
    # Boolean Arrays

    ## Objectives

    - Compare an array with a number and get a Boolean array.
    - Count matches with `count_nonzero`, `sum`, `any`, and `all`.
    - Use a Boolean array as a mask to keep the matching values.
    - Combine conditions with `&` and `|`, which are bitwise operators, not `and` and `or`.

    ## Background

    A comparison such as `x < 0` does not return one Boolean. It returns an array with one Boolean per element. That array can count matches or select the matching values.

    ## Datasets Used

    This notebook does not use external datasets. Random examples use a fixed seed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Comparisons

    Each comparison lines up with the original array. Two arrays are created once, with seed 0, and reused below: `sample`, with 6 integers from -2 to 4, and `table`, with 3 rows and 4 columns.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    sample = np.random.randint(-2, 5, size=6)
    table = np.random.randint(-2, 5, size=(3, 4))
    print(sample)
    return sample, table


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sample < 0` is `True` where the value is negative.
    """)
    return


@app.cell
def _(sample):
    print(sample < 0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sample > 0` is `True` where the value is positive.
    """)
    return


@app.cell
def _(sample):
    print(sample > 0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sample >= 1` is `True` where the value is at least 1.
    """)
    return


@app.cell
def _(sample):
    print(sample >= 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sample != 1` is `True` where the value is not 1.
    """)
    return


@app.cell
def _(sample):
    print(sample != 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sample == 2` is `True` where the value is exactly 2.
    """)
    return


@app.cell
def _(sample):
    print(sample == 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Comparisons work the same way on a 2-D array. This is `table`.
    """)
    return


@app.cell
def _(table):
    print(table)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `table <= 0` has the same shape as `table`, with one Boolean per element.
    """)
    return


@app.cell
def _(table):
    print(table <= 0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Counting matches

    `count_nonzero` counts entries that are not zero. This is the number of entries of `table` that are not 0.
    """)
    return


@app.cell
def _(np, table):
    print(np.count_nonzero(table))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A comparison is 1 where it is true and 0 where it is false, so counting the comparison counts the matches. This is the number of negative entries.
    """)
    return


@app.cell
def _(np, table):
    print(np.count_nonzero(table < 0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The number of positive entries.
    """)
    return


@app.cell
def _(np, table):
    print(np.count_nonzero(table > 0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sum` does the same thing: it adds the 1s of the comparison.
    """)
    return


@app.cell
def _(np, table):
    print(np.sum(table > 0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `axis=0` counts down columns: one count for each of the 4 columns.
    """)
    return


@app.cell
def _(np, table):
    print(np.sum(table > 0, axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `axis=1` counts across rows: one count for each of the 3 rows.
    """)
    return


@app.cell
def _(np, table):
    print(np.sum(table > 0, axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `any` asks whether at least one match exists. Is there any zero in `table`?
    """)
    return


@app.cell
def _(np, table):
    print(np.any(table == 0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With `axis=0`, `any` answers the question for each column.
    """)
    return


@app.cell
def _(np, table):
    print(np.any(table == 0, axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With `axis=1`, it answers the question for each row.
    """)
    return


@app.cell
def _(np, table):
    print(np.any(table == 0, axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `all` asks whether every element matches. The values of `table` go from -2 to 4, so none of them is 5.
    """)
    return


@app.cell
def _(np, table):
    print(np.all(table == 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Count how many entries of `table` are equal to 0, using `np.sum`. Replace `None` with your code. Why can `sum` count matches?
    """)
    return


@app.cell
def _():
    student_zero_count = None
    print(student_zero_count)
    return (student_zero_count,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_zero_count = np.sum(table == 0)
```
`table == 0` is a Boolean array. `sum` treats `True` as 1 and `False` as 0, so adding the array counts the `True` values.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Masks

    Putting a Boolean array inside the brackets returns the values where the mask is true. These are the negative values of `table`.
    """)
    return


@app.cell
def _(table):
    print(table[table < 0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The positive values of `table`.
    """)
    return


@app.cell
def _(table):
    print(table[table > 0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If nothing matches, the result is empty. No value of `table` is greater than 4.
    """)
    return


@app.cell
def _(table):
    print(table[table > 4])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `cutoff`. The cell prints the values in `practice` that are greater than the cutoff.
    """)
    return


@app.cell
def _(np):
    practice = np.array([1, 4, 2, 8, 3])
    cutoff = 3
    print(practice[practice > cutoff])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bitwise operators

    `and` and `or` ask whether a whole object is true. They follow this table:

    | a | b | a and b | a or b |
    |---|---|---|---|
    | False | False | False | False |
    | False | True | False | True |
    | True | False | False | True |
    | True | True | True | True |

    | a | not a |
    |---|---|
    | False | True |
    | True | False |

    `&` and `|` compare bits, or Boolean elements, one by one.

    | Operator | Ufunc |
    |---|---|
    | `&` | `np.bitwise_and` |
    | `\|` | `np.bitwise_or` |
    | `^` | `np.bitwise_xor` |
    | `~` | `np.bitwise_not` |

    Any integer other than 0 counts as true. `and` returns the last object it had to look at, not the word `True`. Python skips the right-hand side when the left-hand side is already enough to decide.

    The examples use the integers 9 and 10.
    """)
    return


@app.cell
def _():
    left = 9
    right = 10
    return left, right


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `9 and 10` returns `10`. Both are true, so `and` has to look at the right-hand side, and it returns it.
    """)
    return


@app.cell
def _(left, right):
    print(left and right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With the order reversed, `10 and 9` returns `9`.
    """)
    return


@app.cell
def _(left, right):
    print(right and left)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `&` compares the binary digits instead. `9 & 10` is 8.
    """)
    return


@app.cell
def _(left, right):
    print(left & right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `bin` shows why. `9` is `0b1001` and `10` is `0b1010`. Only the first digit is 1 in both, so the result is `0b1000`, which is 8: `1001 & 1010 = 1000`.
    """)
    return


@app.cell
def _(left, right):
    print(bin(left), bin(right), bin(left & right))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Bitwise operators on arrays

    `bits_a` and `bits_b` are two random arrays of 0s and 1s, made with seed 1.
    """)
    return


@app.cell
def _(np):
    np.random.seed(1)
    bits_a = np.random.randint(0, 2, size=10)
    bits_b = np.random.randint(0, 2, size=10)
    print(bits_a)
    print(bits_b)
    return bits_a, bits_b


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `&` is 1 only where both arrays are 1.
    """)
    return


@app.cell
def _(bits_a, bits_b):
    print(bits_a & bits_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `|` is 1 where at least one of the arrays is 1.
    """)
    return


@app.cell
def _(bits_a, bits_b):
    print(bits_a | bits_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The keywords `and` and `or` compare whole objects. They cannot compare two arrays element by element. Run the next cell to see the error.
    """)
    return


@app.cell
def _(bits_a, bits_b):
    bits_a and bits_b
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Combining conditions

    Use `&` inside the brackets to require two conditions. Each condition needs parentheses because `&` is applied before the comparisons. These are the values of `sample` from -1 to 1.
    """)
    return


@app.cell
def _(sample):
    print(sample[(sample >= -1) & (sample <= 1)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same condition on `table`.
    """)
    return


@app.cell
def _(table):
    print(table[(table >= -1) & (table <= 1)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Keep the values that are at least `low` and at most `high`.
    """)
    return


@app.cell
def _(np):
    numbers = np.array([-2, -1, 0, 1, 2, 3])
    low = -1
    high = 1
    print(numbers[(numbers >= low) & (numbers <= high)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    From `sample`, keep the values that are less than 0 **or** greater than 2. Replace `None` with your code. Which operator joins the two conditions?
    """)
    return


@app.cell
def _():
    student_outside = None
    print(student_outside)
    return (student_outside,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_outside = sample[(sample < 0) | (sample > 2)]
```
`|` keeps a value when at least one condition is true. Each condition needs its own parentheses. The keyword `or` raises an error, because it cannot compare arrays element by element.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A comparison returns a Boolean array with one result per element.
    - `sum`, `count_nonzero`, `any`, and `all` summarize that array. `axis` gives one result per column or per row.
    - Use the Boolean array as an index to keep the matching values.
    - Combine array conditions with `&` and `|`. The keywords `and` and `or` do not work element by element.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What does `np.array([1, -2, 3]) > 0` return?
    2. Why does `np.sum(x > 0)` count the positive values?
    3. What is the difference between `np.any` and `np.all`?
    4. What does `x[x < 0]` return when `x` has no negative values?
    5. What is `9 and 10` in Python?
    6. What is `9 & 10`?
    7. Why does `(x > 0) & (x < 5)` need parentheses?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **`[True, False, True]`:** One Boolean per element.
2. **`True` counts as 1:** `sum` adds the 1s, so the total is the number of matches.
3. **At least one versus every one:** `any` is true if one element matches. `all` is true only if every element matches.
4. **An empty array:** The mask has no `True` values.
5. **`10`:** Both values are true, so `and` returns the last object it looked at.
6. **`8`:** `&` compares binary digits: `1001 & 1010 = 1000`.
7. **`&` is applied first:** Without parentheses, Python would compute `0 & x` before the comparisons.
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
