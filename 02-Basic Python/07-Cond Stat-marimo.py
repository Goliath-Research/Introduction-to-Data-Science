import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Conditional Statements in Python

    ## Objectives

    - Compare values with `==`, `!=`, `<`, `<=`, `>`, and `>=`.
    - Combine comparisons with `and`, `or`, and `not`.
    - Choose which lines run with `if`, `elif`, and `else`.
    - Match one value against several cases with `match`.

    ## Background

    A condition is an expression that is either `True` or `False`. A conditional statement uses that result to decide which block of code runs. The lines that belong to a branch are indented.

    ## Datasets Used

    This notebook does not use external datasets. The examples compare small values written in the code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Comparisons

    These operators compare two values and return `True` or `False`.

    | Condition | Expression |
    |---|---|
    | Equal | `a == b` |
    | Not equal | `a != b` |
    | Less than | `a < b` |
    | Less than or equal to | `a <= b` |
    | Greater than | `a > b` |
    | Greater than or equal to | `a >= b` |
    """)
    return


@app.cell
def _():
    a = 2
    b = 5
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a < b:", a < b)
    print("a <= b:", a <= b)
    print("a > b:", a > b)
    print("a >= b:", a >= b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Logical operators

    `and` is `True` only when both sides are `True`. `or` is `True` when at least one side is `True`. `not` reverses a boolean value.
    """)
    return


@app.cell
def _():
    left = 1
    middle = 2
    right = 10
    print("True and True:", left < right and middle < right)
    print("True and False:", left < right and middle > right)
    print("True or False:", left < right or middle > right)
    print("False or True:", left > right or middle < right)
    print("True or True:", left < right or middle < right)
    print("False or False:", left > right or middle > right)
    print("not False:", not False)
    print("not (left < right):", not (left < right))
    print("not (left > right):", not (left > right))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## if, elif, and else

    The indented lines under `if` run only when the condition is `True`. When the condition is `False`, those lines are skipped. `else` runs when the `if` condition is `False`. `elif` tries another condition when the earlier conditions were `False`. You may write several `elif` branches. If you write `else`, it must be last, and there can be only one.
    """)
    return


@app.cell
def _():
    larger = 20
    smaller = 10
    if larger > smaller:
        print("The condition is True")
        print("All these sentences are executed!")
    return


@app.cell
def _():
    first = 10
    second = 20
    if second < first:
        print("The condition is False")
        print("These sentences are NOT executed!")
    print("This line is not indented, so it always runs.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python uses indentation to decide which lines belong to the `if`. The next block is not valid Python, because the `print` lines are not indented under the `if`. A notebook cell has to be valid Python, so this version is shown here rather than run:

    ```python
    if second > first:
    print("The condition is True")
    ```
    """)
    return


@app.cell
def _():
    high = 10
    low = 5
    if high < low:
        print("The condition is True.")
    else:
        print("The condition is False.")
    return


@app.cell
def _():
    equal_left = 3
    equal_right = 3
    if equal_right > equal_left:
        print("b is greater than a")
    elif equal_left == equal_right:
        print("a and b are equal")
    return


@app.cell
def _():
    greater = 6
    lesser = 4
    if lesser > greater:
        print("b is greater than a")
    elif greater == lesser:
        print("a and b are equal")
    else:
        print("a is greater than b")
    return


@app.cell
def _():
    known_name = "Anna"
    if known_name == "Maria":
        print("Hello Maria!")
    elif known_name == "Sarah":
        print("Hello Sarah!")
    elif known_name == "Anna":
        print("Hello Anna!")
    elif known_name == "Sofia":
        print("Hello Sofia!")
    else:
        print("I do not know who you are!")

    unknown_name = "Julia"
    if unknown_name == "Maria":
        print("Hello Maria!")
    elif unknown_name == "Sarah":
        print("Hello Sarah!")
    elif unknown_name == "Anna":
        print("Hello Anna!")
    elif unknown_name == "Sofia":
        print("Hello Sofia!")
    else:
        print("I do not know who you are!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `input()` pauses and reads a line that you type. It always returns text. `int()` converts that text to an integer so it can be compared with `18`.
    """)
    return


@app.cell
def _():
    username = input("Enter username:")
    print("Your name is", username)
    return


@app.cell
def _():
    age_text = input("Enter your age:")
    if int(age_text) < 18:
        print("You are a child!")
    else:
        print("You are an adult!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An `if` may contain another `if`. The inner test runs only when the outer condition is `True`.
    """)
    return


@app.cell
def _():
    fourteen = 14
    if fourteen > 10:
        print("Above 10,")
        if fourteen > 20:
            print("and also above 20.")
        else:
            print("but not above 20.")

    thirty_five = 35
    if thirty_five > 10:
        print("Above 10,")
        if thirty_five > 20:
            print("and also above 20.")
        else:
            print("but not above 20.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An `if` body cannot be empty. `pass` is a statement that does nothing, so the branch is valid and no error is raised.
    """)
    return


@app.cell
def _():
    checked = 33
    limit = 200
    if limit > checked:
        pass
    else:
        print("b <= a")
    print("The cell finished. pass did not print anything.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The match statement

    `match` compares one value with several `case` patterns. It can do the same job as a chain of `elif` branches, and it can also unpack a tuple. `_` matches anything that the earlier cases did not match. `case 401 | 403 | 404` matches any one of those three values. `case _ as error_code` matches anything left and stores it in `error_code`.

    `match` requires Python 3.10 or newer.
    """)
    return


@app.cell
def _():
    http_error_code = 404
    match http_error_code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case 502:
            print("Bad Gateway")
        case 503:
            print("Service Unavailable")
        case 504:
            print("Gateway Timeout")
        case _:
            print("Unknown error")

    print()
    match http_error_code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 401 | 403 | 404:
            print("Not allowed")
        case 500:
            print("Internal Server Error")
        case 502:
            print("Bad Gateway")
        case 503:
            print("Service Unavailable")
        case 504:
            print("Gateway Timeout")
        case _ as error_code:
            print(f"Unknown error {error_code}")
    return


@app.cell
def _():
    point = (1, 2)
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y = {y}")
        case (x, 0):
            print(f"X = {x}")
        case (x, y):
            print(f"X = {x}, Y = {y}")
        case _:
            print("It is not a point")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `score` and predict which message prints before you run the cell.
    """)
    return


@app.cell
def _():
    score = 82
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("Not yet")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A comparison or a logical expression is `True` or `False`.
    - Indented lines under `if` run only when that condition is `True`. `elif` tries the next condition. `else` runs when none of the conditions were `True`.
    - `input()` returns text. Convert it with `int()` before a numeric comparison.
    - `pass` fills a branch that should do nothing. `match` selects a `case` from one value, including several values written with `|` and values unpacked from a tuple.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
