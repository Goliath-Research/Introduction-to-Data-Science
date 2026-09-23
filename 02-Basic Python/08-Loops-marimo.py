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

    - Repeat a block with `while` while a condition stays `True`.
    - Repeat a block with `for` once for each item in a sequence.
    - Stop a loop with `break`, skip one pass with `continue`, and write an empty body with `pass`.
    - Use `range()` and `enumerate()`, and loop over the keys and values of a dictionary.

    ## Background

    A loop runs the same indented block more than once. A `while` loop checks a condition before each pass. A `for` loop takes the next item from a sequence on each pass. Sequences you already know, such as lists, tuples, strings, and dictionaries, can be used in a `for` loop.

    ## Datasets Used

    This notebook does not use external datasets. The examples loop over short sequences written in the code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## while

    The indented block runs while the condition is `True`. This loop prints the integers below `5`. The name `counter` must change on each pass. If it never changes, the condition stays `True` and the loop never ends.
    """)
    return


@app.cell
def _():
    counter = 0
    limit_n = 5
    while counter < limit_n:
        print(counter)
        counter += 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A `while` loop can also walk a list until it finds a value. The walrus operator `:=` assigns and tests in the same expression. `found := (search_seq[search_i] == 3)` stores whether the current item is `3`, and that stored result is what `if not` tests.
    """)
    return


@app.cell
def _():
    search_i = 0
    search_seq = [1, 2, 3, 4, 5]
    found = False
    while not found and (search_i < len(search_seq)):
        if not (found := (search_seq[search_i] == 3)):
            search_i += 1
    if found:
        print(f"Found at index {search_i} with value: {search_seq[search_i]}")
    else:
        print("Not found!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `break` leaves the loop immediately, even when the `while` condition is still `True`. Here `not_done` stays `True` when `break` runs, because the walrus assignment happened before the body. After the loop, that tells us the value was found. If the loop ends because `i < len(seq)` becomes `False`, `not_done` is `False` and the value was not found.
    """)
    return


@app.cell
def _():
    break_i = 0
    break_seq = [1, 2, 3, 4, 5]
    while not_done := break_i < len(break_seq):
        if break_seq[break_i] == 3:
            break
        break_i += 1
    if not_done:
        print(f"Found at index {break_i} with value: {break_seq[break_i]}")
    else:
        print("Not found!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `continue` skips the rest of the current pass and starts the next one. `isinstance(current, int)` is `True` when `current` is an integer. Text items are skipped, and the smallest integer is kept.
    """)
    return


@app.cell
def _():
    min_i = 0
    mixed_seq = [1, "2", 3, "4", 5]
    min_val = None
    while min_i < len(mixed_seq):
        current = mixed_seq[min_i]
        min_i += 1
        if not isinstance(current, int):
            continue
        if min_val is None or current < min_val:
            min_val = current
            print(f"New min_val = {min_val}")
    print(f"Final min_val = {min_val}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `else` block on a `while` loop runs once when the condition becomes `False`. It also runs when the condition is `False` before the first pass. It does not run when the loop exits with `break`.
    """)
    return


@app.cell
def _():
    else_i = 0
    while else_i < 5:
        print(else_i)
        else_i += 1
    else:
        print(f"i = {else_i} is no longer less than 5")
    return


@app.cell
def _():
    skipped_i = 1
    while skipped_i > 5:
        print(f"{skipped_i} in loop")
        skipped_i += 1
    else:
        print(f"{skipped_i} in else")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## for

    A `for` loop assigns the next item to the name before `in`, then runs the indented block. It stops after the last item.

    ```python
    for element in sequence:
        pass
    ```
    """)
    return


@app.cell
def _():
    students = ["John", "Mary", "Anna"]
    for student in students:
        print(student)
    return


@app.cell
def _():
    fruits = ("guava", "mango", "cherry", "pear")
    for fruit in fruits:
        print(fruit)
    print()

    # range(len(fruits)) produces the indexes 0, 1, 2, and 3.
    for position in range(len(fruits)):
        print(position, fruits[position])
    print()

    # enumerate() produces each index together with the item.
    for position, fruit in enumerate(fruits):
        print(position, fruit)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A string is a sequence of characters, so a `for` loop can visit one character at a time.
    """)
    return


@app.cell
def _():
    for character in "string":
        print(character)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `break` stops the loop before the remaining items. `continue` skips one item and keeps going. In the second cell, every name is printed except `Mary`.
    """)
    return


@app.cell
def _():
    break_students = ["John", "Rose", "Mary", "Anna"]
    for person in break_students:
        if person == "Mary":
            break
        print(person)
    return


@app.cell
def _():
    continue_students = ["John", "Rose", "Mary", "Anna"]
    for skipped_person in continue_students:
        if skipped_person == "Mary":
            continue
        print(skipped_person)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `number % 2 == 0` is `True` for an even integer. `continue` skips those numbers, and the cell adds the odd integers from `0` through `9`. The name `odd_total` is used so this cell does not replace Python's built-in `sum` function.
    """)
    return


@app.cell
def _():
    odd_total = 0
    for number in range(10):
        if number % 2 == 0:
            continue
        print(number)
        odd_total += number
    print("Sum =", odd_total)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `range(stop)` produces `0, 1, ..., stop - 1`. `range(start, stop)` starts at `start` and still excludes `stop`. `range(start, stop, step)` adds `step` each time. `step` may be negative, which counts down. The stop value is still excluded.
    """)
    return


@app.cell
def _():
    print("range(5)")
    for value in range(5):
        print(value)
    print("range(2, 5)")
    for value in range(2, 5):
        print(value)
    print("range(2, 10, 2)")
    for value in range(2, 10, 2):
        print(value)
    print("range(3, 45, 10)")
    for value in range(3, 45, 10):
        print(value)
    print("range(20, 10, -2)")
    for value in range(20, 10, -2):
        print(value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `else` block of a `for` loop runs when the loop finishes the sequence. Python keeps the last value of the loop name after the loop ends.
    """)
    return


@app.cell
def _():
    for finished in range(6):
        print(finished)
    else:
        print("Finally done!")

    for kept in range(5):
        print(kept)
    else:
        print("else:", kept)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Nested loops

    A loop may contain another loop. The inner loop runs all of its passes for each pass of the outer loop. The first cell adds every item in a list of lists. The second cell prints every pair from two dice.
    """)
    return


@app.cell
def _():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    print(f"The sum of all elements in the matrix is: {total_sum}")
    return


@app.cell
def _():
    for die_a in range(6):
        for die_b in range(6):
            print((die_a + 1, die_b + 1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A `for` body cannot be empty. `pass` makes the body valid and does nothing.
    """)
    return


@app.cell
def _():
    for ignored in [0, 1, "h"]:
        pass
    print("The loop finished. pass printed nothing.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Looping over a dictionary

    A `for` loop over a dictionary assigns the keys, not the values. Use the key to read the value, or loop over `keys()` and `values()` directly.
    """)
    return


@app.cell
def _():
    codes = {1: "a", 2: "b", 3: "c"}
    print(type(codes))
    print("keys from the dictionary:")
    for key in codes:
        print(key)
    print("values looked up by key:")
    for key in codes:
        print(codes[key])
    print("keys():")
    for key in codes.keys():
        print(key)
    print("values():")
    for key in codes.values():
        print(key)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `limit` and predict the printed numbers before you run the cell.
    """)
    return


@app.cell
def _():
    practice_i = 0
    limit = 4
    while practice_i < limit:
        print(practice_i)
        practice_i += 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `while` repeats as long as its condition is `True`. Update the value that the condition tests, or the loop will not end.
    - `for` repeats once for each item. `range()` produces a sequence of integers, and `enumerate()` produces each index with its item.
    - `break` leaves the loop. `continue` skips the rest of the current pass. `pass` is an empty body.
    - `else` on a loop runs when the loop ends without `break`.
    - Looping over a dictionary visits the keys. A loop may contain another loop.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
