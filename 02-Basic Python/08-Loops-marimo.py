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
    # Python Loops

    ## Objectives

    - Repeat code with `while` as long as a condition stays true.
    - Stop or skip an iteration with `break` and `continue`.
    - Iterate over a list, a string, a range, and a dictionary with `for`.
    - Place one loop inside another.

    ## Background

    A loop runs a block more than once. `while` checks a condition before each pass. `for` walks through a sequence. Indentation marks the statements that belong to the loop.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## while

    The loop below prints `i` while `i` is less than 5. The counter must change, or the condition never becomes false.
    """)
    return


@app.cell
def _():
    counter = 0
    while counter < 5:
        print(counter)
        counter += 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `break` leaves the loop immediately. `continue` skips the rest of the current pass and starts the next one. `else` on a `while` runs when the condition becomes false without a `break`.
    """)
    return


@app.cell
def _():
    break_counter = 0
    while break_counter < 5:
        break_counter += 1
        if break_counter == 3:
            break
        print(break_counter)
    print("Outside the loop")
    return


@app.cell
def _():
    continue_counter = 0
    while continue_counter < 5:
        continue_counter += 1
        if continue_counter == 3:
            continue
        print(continue_counter)
    print("Outside the loop")
    return


@app.cell
def _():
    else_counter = 0
    while else_counter < 5:
        print(else_counter)
        else_counter += 1
    else:
        print("i is no longer less than 5")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the limit. Print every number from 1 through that limit.
    """)
    return


@app.cell
def _():
    limit = 4
    practice_counter = 1

    while practice_counter <= limit:
        print(practice_counter)
        practice_counter += 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## for

    A `for` loop visits each item in a list, tuple, set, dictionary, or string.
    """)
    return


@app.cell
def _():
    students = ["John", "Mary", "Anna"]
    for student in students:
        print(student)

    print("---")
    for character in "string":
        print(character)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `break` stops before the remaining items. `continue` skips one item and keeps going. The `continue` example prints every name except Mary.
    """)
    return


@app.cell
def _():
    break_students = ["John", "Rose", "Mary", "Anna"]
    for break_name in break_students:
        if break_name == "Mary":
            break
        print(break_name)
    return


@app.cell
def _():
    continue_students = ["John", "Rose", "Mary", "Anna"]
    for skipped_name in continue_students:
        if skipped_name == "Mary":
            continue
        print(skipped_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## range

    `range(stop)` starts at 0 and stops before `stop`. `range(start, stop)` chooses the start. `range(start, stop, step)` chooses the increment. The `else` block runs when the loop finishes.
    """)
    return


@app.cell
def _():
    print("range(5)")
    for number in range(5):
        print(number)

    print("range(2, 5)")
    for number in range(2, 5):
        print(number)

    print("range(2, 10, 2)")
    for number in range(2, 10, 2):
        print(number)

    print("range(3, 45, 10)")
    for number in range(3, 45, 10):
        print(number)
    return


@app.cell
def _():
    for finished in range(6):
        print(finished)
    else:
        print("Finally finished!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `start`, `stop`, and `step`, then run the cell.
    """)
    return


@app.cell
def _():
    start = 1
    stop = 10
    step = 2

    for practice_number in range(start, stop, step):
        print(practice_number)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nested loops

    The inner loop finishes a full pass for each item of the outer loop. A `for` loop cannot be empty; `pass` is a statement that does nothing.
    """)
    return


@app.cell
def _():
    adjectives = ["smart", "polite"]
    names = ["John", "Mary", "Anna"]

    for adjective in adjectives:
        for name in names:
            print(adjective, name)
    return


@app.cell
def _():
    for row in range(6):
        for column in range(6):
            print("(", row + 1, ",", column + 1, ")")
    return


@app.cell
def _():
    for item in [0, 1, "h"]:
        pass

    print("The loop ran, and pass gave it a body.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Looping through a dictionary

    A `for` loop over a dictionary visits the keys. Use the key to read the value, or loop over `keys()` and `values()` directly.
    """)
    return


@app.cell
def _():
    letters = {1: "a", 2: "b", 3: "c"}
    print(type(letters))

    print("keys from the dictionary:")
    for key in letters:
        print(key)

    print("values looked up by key:")
    for key in letters:
        print(letters[key])

    print("keys():")
    for key in letters.keys():
        print(key)

    print("values():")
    for value in letters.values():
        print(value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `while` repeats until its condition is false. Update the values that the condition uses.
    - `break` leaves the loop. `continue` skips to the next iteration.
    - `for` walks through each item of a sequence. `range` builds a numeric sequence.
    - A nested loop runs its inner loop once for every outer item.
    - Looping over a dictionary yields keys unless you ask for `values()`.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
