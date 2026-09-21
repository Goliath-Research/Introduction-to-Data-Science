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
    # Conditional Statements

    ## Objectives

    - Compare values with `==`, `!=`, `<`, `<=`, `>`, and `>=`.
    - Combine Boolean expressions with `and`, `or`, and `not`.
    - Choose code with `if`, `elif`, and `else`.
    - Nest a condition and use `pass` when a branch is intentionally empty.

    ## Background

    A condition is an expression that is `True` or `False`. Python uses indentation to decide which lines belong to a branch.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Comparisons

    | Operator | Meaning |
    |---|---|
    | `==` | equal |
    | `!=` | not equal |
    | `<` | less than |
    | `<=` | less than or equal to |
    | `>` | greater than |
    | `>=` | greater than or equal to |
    """)
    return


@app.cell
def _():
    left = 2
    right = 5

    print("equal:             ", left == right)
    print("not equal:         ", left != right)
    print("less than:         ", left < right)
    print("less or equal:     ", left <= right)
    print("greater than:      ", left > right)
    print("greater or equal:  ", left >= right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Logical operators

    - `and` is true when both parts are true.
    - `or` is true when at least one part is true.
    - `not` reverses a Boolean value.
    """)
    return


@app.cell
def _():
    first = 1
    second = 2
    third = 10

    print("True and True:  ", first < third and second < third)
    print("True and False: ", first < third and second > third)
    print("True or False:  ", first < third or second > third)
    print("False or True:  ", first > third or second < third)
    print("True or True:   ", first < third or second < third)
    print("False or False: ", first > third or second > third)
    print("not False:      ", not False)
    print("not (first < third):", not (first < third))
    print("not (first > third):", not (first > third))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the two numbers and predict each comparison before you run the cell.
    """)
    return


@app.cell
def _():
    your_left = 8
    your_right = 3

    print(your_left == your_right)
    print(your_left > your_right)
    print(your_left < 10 and your_right < 10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## if, elif, and else

    The indented lines run only when the condition is true. `else` runs when the earlier conditions are false. `elif` tries another condition. Only one `else` is allowed, and it must be last.
    """)
    return


@app.cell
def _():
    high = 20
    low = 10

    if high > low:
        print("The condition (high > low) is True, so this sentence runs.")

    if high < low:
        print("This sentence does not run.")
    else:
        print("The condition is False, so else runs.")
    return


@app.cell
def _():
    equal_left = 3
    equal_right = 3

    if equal_right > equal_left:
        print("right is greater than left")
    elif equal_left == equal_right:
        print("the two values are equal")
    return


@app.cell
def _():
    greater_left = 6
    greater_right = 4

    if greater_right > greater_left:
        print("right is greater than left")
    elif greater_left == greater_right:
        print("the two values are equal")
    else:
        print("left is greater than right")
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
    The lines inside `if` must be indented. This cell runs the same statement without indentation and prints the `IndentationError`.
    """)
    return


@app.cell
def _():
    unindented = "if 20 > 10:\nprint('missing indentation')"

    try:
        exec(unindented)
    except IndentationError as error:
        print("IndentationError:", error)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `your_score`. Print `"pass"` when it is at least 60, and `"retry"` otherwise.
    """)
    return


@app.cell
def _():
    your_score = 72

    if your_score >= 60:
        print("pass")
    else:
        print("retry")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nested if and pass

    An `if` inside another `if` tests a second condition only after the first one is true. An empty branch is not allowed; use `pass` when the branch should do nothing.
    """)
    return


@app.cell
def _():
    small_number = 14

    if small_number > 10:
        print("Above 10,")
        if small_number > 20:
            print("and also above 20.")
        else:
            print("but not above 20.")
    return


@app.cell
def _():
    large_number = 35

    if large_number > 10:
        print("Above 10,")
        if large_number > 20:
            print("and also above 20.")
        else:
            print("but not above 20.")
    return


@app.cell
def _():
    pass_left = 33
    pass_right = 200

    if pass_right > pass_left:
        pass
    else:
        print("right is not greater than left")

    print("The empty branch used pass, so execution continued.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interactive check

    Type a name and an age. The results update when you change either value. This replaces `input()`, which would stop the notebook while it waits for the terminal.
    """)
    return


@app.cell
def _(mo):
    name_input = mo.ui.text(value="Ana", label="Name")
    age_input = mo.ui.number(value=21, label="Age", start=0, stop=120)
    mo.hstack([name_input, age_input], justify="start", gap=2)
    return age_input, name_input


@app.cell
def _(age_input, mo, name_input):
    entered_name = name_input.value
    entered_age = age_input.value

    if entered_age < 18:
        age_message = "You are a child."
    else:
        age_message = "You are an adult."

    mo.md(f"**{entered_name}**, age {entered_age}. {age_message}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - Comparison operators produce `True` or `False`.
    - `and`, `or`, and `not` combine Boolean expressions.
    - `if`, `elif`, and `else` choose which block runs. The blocks must be indented.
    - A nested `if` adds a second test. `pass` fills a branch that should do nothing.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
