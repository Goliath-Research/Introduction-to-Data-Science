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

    - Build a list with `[expression for item in sequence]`.
    - Keep some items with `if`, and choose between two expressions with `if` and `else`.
    - Read a nested comprehension as an outer list built from an inner list.

    ## Background

    A list comprehension builds a list in one expression. It is a shorter way to write a `for` loop that appends to a list. The loop version and the comprehension version produce the same list. Keep a comprehension short enough to read. A long chain of conditions is easier to follow as a `for` loop.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The same list, two ways

    This cell walks the string `"Data Science"` and appends each character.
    """)
    return


@app.cell
def _():
    letters_from_loop = []
    for character in "Data Science":
        letters_from_loop.append(character)
    print(letters_from_loop)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This cell does the same work in one line. The form is `[expression for item in sequence]`.
    """)
    return


@app.cell
def _():
    letters = [character for character in "Data Science"]
    print(letters)
    return (letters,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression before `for` is evaluated once for each item. `number ** 2` squares each number.
    """)
    return


@app.cell
def _():
    print([number ** 2 for number in [1, -5, 10, 11, -15, -20]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `number ** 3` cubes each integer from `range(5)`, which is `0` through `4`.
    """)
    return


@app.cell
def _():
    print([number ** 3 for number in range(5)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A method can be the expression. `lower()` converts each character.
    """)
    return


@app.cell
def _(letters):
    print([character.lower() for character in letters])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `upper()` converts each character to uppercase.
    """)
    return


@app.cell
def _(letters):
    print([character.upper() for character in letters])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `character * 2` repeats each character.
    """)
    return


@app.cell
def _(letters):
    print([character * 2 for character in letters])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Keeping some items

    A comprehension may end with `if condition`. The new list includes an item only when the condition is `True`. This one keeps the positive numbers.
    """)
    return


@app.cell
def _():
    print([number for number in [1, -5, 10, 11, -20] if number > 0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `isdigit()` keeps the characters that are digits. The parentheses, spaces, and dash are left out.
    """)
    return


@app.cell
def _():
    phone = "Phone: (123) 456-7890"
    print([character for character in phone if character.isdigit()])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This comprehension keeps the vowels. `upper()` makes the test ignore capitalization.
    """)
    return


@app.cell
def _():
    print([character for character in "Data Science" if character.upper() in "AEIOU"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression itself can be a function call. The parentheses after the `lambda` call it on the current number. Even numbers are squared. Odd numbers are cubed. The `if` at the end drops the negative numbers before that function runs.
    """)
    return


@app.cell
def _():
    print(
        [
            (lambda x: x ** 2 if x % 2 == 0 else x ** 3)(number)
            for number in [1, -5, 10, 11, -20]
            if number > 0
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Choosing a value with if and else

    `value_if_true if condition else value_if_false` sits in the expression, before `for`. It runs for every item. This is different from the `if` at the end, which decides whether the item is included at all.

    Positive numbers become `1`. The other numbers become `-1`.
    """)
    return


@app.cell
def _():
    samples = [1, -5, 10, 11, -20]
    print([1 if number > 0 else -1 for number in samples])
    return (samples,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Positive numbers are squared. The other numbers become `-1`.
    """)
    return


@app.cell
def _(samples):
    print([number ** 2 if number > 0 else -1 for number in samples])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Each number is labeled `"Even"` or `"Odd"`.
    """)
    return


@app.cell
def _(samples):
    print(["Even" if number % 2 == 0 else "Odd" for number in samples])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Vowels stay. Every other character becomes a space.
    """)
    return


@app.cell
def _():
    print([character if character.upper() in "AEIOU" else " " for character in "Data Science"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The test can be reversed: vowels become spaces, and the other characters stay.
    """)
    return


@app.cell
def _():
    print([" " if character.upper() in "AEIOU" else character for character in "Data Science"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Several `if` and `else` expressions can be nested. Read this one from left to right: the first true condition chooses the letter.

    | Letter | Numerical grade |
    |---|---|
    | A | grade >= 90 |
    | B | 80 <= grade < 90 |
    | C | 70 <= grade < 80 |
    | D | 60 <= grade < 70 |
    | F | grade < 60 |

    These are the grades.
    """)
    return


@app.cell
def _():
    grades = [88, 70, 62, 55, 90, 86, 54, 85]
    print(grades)
    return (grades,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The boundary for D is `60`. A grade of `55` is an F.
    """)
    return


@app.cell
def _(grades):
    print(
        [
            "A"
            if grade >= 90
            else "B"
            if grade >= 80
            else "C"
            if grade >= 70
            else "D"
            if grade >= 60
            else "F"
            for grade in grades
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Moving the D boundary to `55` changes the letter for `55` from F to D. The other grades keep their letters.
    """)
    return


@app.cell
def _(grades):
    print(
        [
            "A"
            if grade >= 90
            else "B"
            if grade >= 80
            else "C"
            if grade >= 70
            else "D"
            if grade >= 55
            else "F"
            for grade in grades
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nested comprehensions

    Two `for` clauses visit every pair. The second `for` is the inner loop. `if die_a <= die_b` keeps the pairs in which the first die is less than or equal to the second. The printed numbers are one greater than the `range` values, so each die shows `1` through `6`.
    """)
    return


@app.cell
def _():
    print(
        [
            (die_a + 1, die_b + 1)
            for die_a in range(6)
            for die_b in range(6)
            if die_a <= die_b
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A matrix written as a list of rows can be transposed: each new row is one column of the original. The inner comprehension walks the rows and takes item `column`. The outer comprehension does that once for each column. This version assumes a square matrix, so the number of columns equals the number of rows.
    """)
    return


@app.cell
def _():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    transpose = [[row[column] for row in matrix] for column in range(len(matrix))]
    print(transpose)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `practice` and predict the new list before you run the cell.
    """)
    return


@app.cell
def _():
    practice = [1, 2, 3, 4, 5]
    print([number * 10 for number in practice if number > 2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Build the list of positive numbers from `[-1, 2, -3, 4]`. Replace `None` with your code. Which numbers are left out, and why?
    """)
    return


@app.cell
def _():
    student_positive = None
    print(student_positive)
    return (student_positive,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_positive = [number for number in [-1, 2, -3, 4] if number > 0]
```
`-1` and `-3` are left out. The `if` at the end keeps an item only when the condition is true.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `[expression for item in sequence]` builds the list that a `for` loop would build with `append`.
    - `if` at the end keeps only the items that pass the test.
    - `if` and `else` before `for` choose the value that goes into the list.
    - A second `for`, or a comprehension inside the expression, handles nested sequences.
    - A comprehension that is hard to read should be written as a loop.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What does a list comprehension build?
    2. Where is the value that goes into the new list written?
    3. What does `if` at the end of a comprehension do?
    4. What does `if` and `else` before `for` do?
    5. Which integers does `range(5)` give a comprehension?
    6. What does a second `for` clause do?
    7. When should you write a loop instead of a comprehension?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **A new list:** It is a shorter way to write a loop that appends.
2. **Before `for`:** That expression runs once for each item that is kept.
3. **It keeps some items:** An item is included only when the condition is true.
4. **It chooses the value:** Every item is included, and the condition picks which expression is used.
5. **`0` through `4`:** The stop value is excluded.
6. **It visits pairs:** The second `for` is the inner loop.
7. **When it is hard to read:** A long chain of conditions is easier to follow as a `for` loop.
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
