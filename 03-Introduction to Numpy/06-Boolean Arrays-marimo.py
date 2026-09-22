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

    Each comparison lines up with the original array. These two arrays are created once, with seed 0, and reused below.
    """)
    return


@app.cell
def _(np):
    np.random.seed(0)
    sample = np.random.randint(-2, 5, size=6)
    table = np.random.randint(-2, 5, size=(3, 4))
    print("sample:", sample)
    print("less than 0:     ", sample < 0)
    print("greater than 0:  ", sample > 0)
    print("at least 1:      ", sample >= 1)
    print("not equal to 1:  ", sample != 1)
    print("equal to 2:      ", sample == 2)
    print("table:\n", table)
    print("table <= 0:\n", table <= 0)
    return sample, table


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Counting matches

    `count_nonzero` counts entries that are not zero. A comparison is 1 where it is true, so counting the comparison counts the matches. `sum` does the same thing. `axis=0` counts down columns and `axis=1` counts across rows. `any` asks whether at least one match exists. `all` asks whether every element matches.
    """)
    return


@app.cell
def _(np, table):
    print("nonzero entries:", np.count_nonzero(table))
    print("negative:", np.count_nonzero(table < 0))
    print("positive:", np.count_nonzero(table > 0))
    print("positive, using sum:", np.sum(table > 0))
    print("positive in each column:", np.sum(table > 0, axis=0))
    print("positive in each row:", np.sum(table > 0, axis=1))
    print("any zero:", np.any(table == 0))
    print("columns with a zero:", np.any(table == 0, axis=0))
    print("rows with a zero:", np.any(table == 0, axis=1))
    print("all equal to 5:", np.all(table == 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Masks

    Putting a Boolean array inside the brackets returns the values where the mask is true. If nothing matches, the result is empty.
    """)
    return


@app.cell
def _(table):
    print("negative:", table[table < 0])
    print("positive:", table[table > 0])
    print("greater than 4:", table[table > 4])
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

    `and` and `or` ask whether a whole object is true. `&` and `|` compare bits, or Boolean elements.

    | Operator | Ufunc |
    |---|---|
    | `&` | `np.bitwise_and` |
    | `\|` | `np.bitwise_or` |
    | `^` | `np.bitwise_xor` |
    | `~` | `np.bitwise_not` |

    For ordinary integers, `and` returns one of the objects. `&` compares their binary digits. `9` is `0b1001` and `10` is `0b1010`, so `9 & 10` is `0b1000`, which is 8.
    """)
    return


@app.cell
def _():
    left = 9
    right = 10
    print("and, left first:", left and right)
    print("and, right first:", right and left)
    print("bitwise and:", left & right)
    print(bin(left), bin(right), bin(left & right))
    return


@app.cell
def _(np):
    np.random.seed(1)
    bits_a = np.random.randint(0, 2, size=10)
    bits_b = np.random.randint(0, 2, size=10)
    print("a:", bits_a)
    print("b:", bits_b)
    print("and:", bits_a & bits_b)
    print("or: ", bits_a | bits_b)

    try:
        print(bits_a and bits_b)
    except ValueError as error:
        print("ValueError:", error)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use `&` inside the brackets to require two conditions. Each condition needs parentheses because `&` binds more tightly than the comparisons.
    """)
    return


@app.cell
def _(sample, table):
    print("sample between -1 and 1:", sample[(sample >= -1) & (sample <= 1)])
    print("table between -1 and 1:", table[(table >= -1) & (table <= 1)])
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
    ## Conclusions

    **Key takeaways:**

    - A comparison returns a Boolean array with one result per element.
    - `sum`, `count_nonzero`, `any`, and `all` summarize that array.
    - Use the Boolean array as an index to keep the matching values.
    - Combine array conditions with `&` and `|`. The keywords `and` and `or` do not work element by element.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 2.
    """)
    return


if __name__ == "__main__":
    app.run()
