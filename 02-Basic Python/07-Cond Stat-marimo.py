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

    The examples use `a = 2` and `b = 5`. `==` asks whether the values are equal.
    """)
    return


@app.cell
def _():
    a = 2
    b = 5
    print(a == b)
    return a, b


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `!=` asks whether the values are different.
    """)
    return


@app.cell
def _(a, b):
    print(a != b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `<` asks whether the first value is smaller.
    """)
    return


@app.cell
def _(a, b):
    print(a < b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `<=` is also true when the values are equal. Here `2` is smaller, so it is true.
    """)
    return


@app.cell
def _(a, b):
    print(a <= b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `>` asks whether the first value is larger. `2` is not larger than `5`.
    """)
    return


@app.cell
def _(a, b):
    print(a > b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `>=` is false for the same reason.
    """)
    return


@app.cell
def _(a, b):
    print(a >= b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Logical operators

    `and` is `True` only when both sides are `True`. These examples use `1`, `2`, and `10`. Both comparisons are true.
    """)
    return


@app.cell
def _():
    left = 1
    middle = 2
    right = 10
    print(left < right and middle < right)
    return left, middle, right


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One false side makes `and` false.
    """)
    return


@app.cell
def _(left, middle, right):
    print(left < right and middle > right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `or` is `True` when at least one side is `True`.
    """)
    return


@app.cell
def _(left, middle, right):
    print(left < right or middle > right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `or` is false only when both sides are false.
    """)
    return


@app.cell
def _(left, middle, right):
    print(left > right or middle > right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `not` reverses a boolean. `not False` is `True`.
    """)
    return


@app.cell
def _():
    print(not False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `not` also reverses a comparison. `1 < 10` is true, so `not` makes it false.
    """)
    return


@app.cell
def _(left, right):
    print(not (left < right))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## if, elif, and else

    The indented lines under `if` run only when the condition is `True`.
    """)
    return


@app.cell
def _():
    larger = 20
    smaller = 10
    if larger > smaller:
        print("The condition is True")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When the condition is `False`, the indented lines are skipped. A line that is not indented always runs.
    """)
    return


@app.cell
def _():
    first = 10
    second = 20
    if second < first:
        print("The condition is False")
    print("This line is not indented, so it always runs.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python uses indentation to decide which lines belong to the `if`. The next block is not valid Python, because the `print` line is not indented under the `if`. A notebook cell has to be valid Python, so this version is shown here rather than run:

    ```python
    if second > first:
    print("The condition is True")
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `else` runs when the `if` condition is `False`.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `elif` tries another condition when the earlier condition was `False`. Here the values are equal, so the first test fails and the second test runs.
    """)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `else` runs when none of the conditions were `True`. You may write several `elif` branches. If you write `else`, it must be last, and there can be only one.
    """)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A chain of `elif` branches can match one name. `"Anna"` matches the third test, so the later tests are not tried.
    """)
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `"Julia"` matches none of the names, so `else` runs.
    """)
    return


@app.cell
def _():
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
    `input()` pauses and reads a line that you type. It always returns text.
    """)
    return


@app.cell
def _():
    username = input("Enter username:")
    print("Your name is", username)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `int()` converts that text to an integer so it can be compared with `18`.
    """)
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
    An `if` may contain another `if`. The inner test runs only when the outer condition is `True`. `14` is above `10`, but it is not above `20`.
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `35` passes both tests.
    """)
    return


@app.cell
def _():
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
    An `if` body cannot be empty. `pass` is a statement that does nothing, so the branch is valid and no error is raised. The condition is true, so `else` does not run.
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

    `match` compares one value with several `case` patterns. `_` matches anything that the earlier cases did not match.

    `match` requires Python 3.10 or newer. This value is `404`, so the matching case prints `Not Found`.
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
        case _:
            print("Unknown error")
    return (http_error_code,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `case 401 | 403 | 404` matches any one of those three values. `404` now prints `Not allowed`.
    """)
    return


@app.cell
def _(http_error_code):
    match http_error_code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 401 | 403 | 404:
            print("Not allowed")
        case _ as error_code:
            print(f"Unknown error {error_code}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `match` can also unpack a tuple. `(1, 2)` does not match the origin or an axis, so the case `(x, y)` stores the two numbers.
    """)
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
    ### Try it yourself

    Store the results of `(1 < 10) and (2 > 10)` and of `(1 < 10) or (2 > 10)`. Replace each `None` with your code. Why do the two results differ?
    """)
    return


@app.cell
def _():
    student_and = None
    student_or = None
    print(student_and)
    print(student_or)
    return student_and, student_or


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_and = (1 < 10) and (2 > 10)
student_or = (1 < 10) or (2 > 10)
```
`and` is `False` because one side is false. `or` is `True` because one side is true. `and` needs both sides. `or` needs only one.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A comparison or a logical expression is `True` or `False`.
    - `and` needs both sides to be true. `or` needs one side. `not` reverses the value.
    - Indented lines under `if` run only when that condition is `True`. `elif` tries the next condition. `else` runs when none of the conditions were `True`.
    - `input()` returns text. Convert it with `int()` before a numeric comparison.
    - `pass` fills a branch that should do nothing. `match` selects a `case` from one value, including several values written with `|` and values unpacked from a tuple.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What does `==` compare?
    2. When is `and` true?
    3. When is `or` false?
    4. Which lines belong to an `if`?
    5. When does `else` run?
    6. What does `input()` return?
    7. What does `_` match in a `match` statement?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **Equality:** It asks whether two values are equal. `=` assigns a value. `==` compares.
2. **When both sides are true:** One false side makes the whole expression false.
3. **When both sides are false:** One true side is enough to make `or` true.
4. **The indented lines:** A line that is not indented is not part of the branch.
5. **When no earlier condition was true:** It must be the last branch.
6. **Text:** Use `int()` before comparing the answer with a number.
7. **Anything left over:** It is the case that runs when the earlier cases did not match.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
