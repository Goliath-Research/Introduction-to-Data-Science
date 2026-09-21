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
    # List Comprehension

    ## Objectives

    - Build a list with a `for` loop and with a list comprehension.
    - Filter items with a condition.
    - Choose between two expressions with `if` / `else` inside a comprehension.

    ## Background

    A list comprehension creates a list in one expression. The basic form is `[expression for item in iterable]`.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## From a loop to a comprehension

    Both cells collect the characters of the same text. The comprehension does the append inside the brackets.
    """)
    return


@app.cell
def _():
    letters_from_loop = []
    for character in "LIST COMPREHENSION":
        letters_from_loop.append(character)
    print(letters_from_loop)
    return


@app.cell
def _():
    letters_from_comprehension = [character for character in "LIST COMPREHENSION"]
    print(letters_from_comprehension)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same pattern squares each number: `[i ** 2 for i in numbers]`.
    """)
    return


@app.cell
def _():
    squares = [number ** 2 for number in [1, -5, 10, 11, -20]]
    print(squares)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `word` and build a list of its characters.
    """)
    return


@app.cell
def _():
    word = "PYTHON"
    your_letters = [character for character in word]
    print(your_letters)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A condition at the end

    `if` at the end of the comprehension keeps only the items that pass the test.
    """)
    return


@app.cell
def _():
    positive_squares = [number ** 2 for number in [1, -5, 10, 11, -20] if number > 0]
    print(positive_squares)

    vowels = [character for character in "LIST COMPREHENSION" if character in "AEIOU"]
    print(vowels)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## if / else in the expression

    Place `if` / `else` before `for` when every item should produce a value, and the value depends on a test.
    """)
    return


@app.cell
def _():
    signed_squares = [
        number ** 2 if number > 0 else -1
        for number in [1, -5, 10, 11, -20]
    ]
    print(signed_squares)

    vowel_or_space = [
        character if character in "AEIOU" else " "
        for character in "LIST COMPREHENSION"
    ]
    print(vowel_or_space)

    parity = [
        "Even" if number % 2 == 0 else "Odd"
        for number in [1, -5, 10, 11, -20]
    ]
    print(parity)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Keep the numbers that are greater than `cutoff`, and square them.
    """)
    return


@app.cell
def _():
    cutoff = 0
    your_squares = [number ** 2 for number in [1, -5, 10, 11, -20] if number > cutoff]
    print(your_squares)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How to choose

    - A comprehension is a compact way to build a list from another sequence.
    - It is often shorter than the loop it replaces.
    - Keep the expression short enough to read.
    - Every comprehension can be rewritten as a loop. Not every loop can be rewritten as a comprehension.

    ## Conclusions

    **Key takeaways:**

    - `[expression for item in iterable]` builds a list.
    - A trailing `if` filters items.
    - `expression_if if test else expression_else` chooses a value for every item.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
