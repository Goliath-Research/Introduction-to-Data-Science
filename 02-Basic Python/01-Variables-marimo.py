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
    # Python Variables

    ## Objectives

    - Understand what variables are in the context of Python programming.
    - Learn how to define and use variables of different types (integers, floating-point numbers, booleans, and strings).
    - Grasp Python's dynamic typing through variable type changes.
    - Practice basic arithmetic operations and their shorthand notations.
    - Convert values with `int()`, `float()`, and `str()`.

    ## Background

    Variables are fundamental to any programming language, acting as placeholders for data that can change over time. In Python, names are not bound to a type. A name can refer to an integer and later to a string. The value's type is checked at run time.

    ## Datasets Used

    This notebook does not use external datasets. It focuses on variable assignment and manipulation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Variable Definition

    A variable is a name that refers to a value stored in memory.

    A Python variable is created the moment you first assign a value to it. Variables do not need to be declared with a particular type; they receive the type of their value.

    `integer_value` holds a whole number. `type()` reports `int`.
    """)
    return


@app.cell
def _():
    integer_value = 320
    print(integer_value, "->", type(integer_value))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `float_value` holds a number with a decimal point. Its type is `float`.
    """)
    return


@app.cell
def _():
    float_value = 2.5
    print(float_value, "->", type(float_value))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dynamic typing

    A variable can refer to values of different types at different moments. These three lines use one name. Each assignment replaces the previous value, and the type changes with it.
    """)
    return


@app.cell
def _():
    value = 340
    print(value, "->", type(value))

    value = 3.3
    print(value, "->", type(value))

    value = "No"
    print(value, "->", type(value))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Boolean and string variables

    `False` is a boolean. The other boolean value is `True`.
    """)
    return


@app.cell
def _():
    condition_example = False
    print(condition_example, "->", type(condition_example))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Text in quotes is a string.
    """)
    return


@app.cell
def _():
    character_name_example = "John"
    print(character_name_example, "->", type(character_name_example))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Variable names

    A variable name may contain letters, digits, and underscores (`_`), but it cannot begin with a digit. Variable names are case-sensitive, so `age` and `Age` are different variables.

    This sentence places the two ages into the text with commas.
    """)
    return


@app.cell
def _():
    age_person = 20
    age_mother = 40
    print("Laura is", age_person, "years old. Her mother is", age_mother)
    return age_mother, age_person


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An f-string does the same job. The names inside `{}` are replaced by their values.
    """)
    return


@app.cell
def _(age_mother, age_person):
    print(f"Laura is {age_person} years old. Her mother is {age_mother}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Multiple assignment

    You can assign values to multiple variables in one line. The names and the values are matched from left to right.
    """)
    return


@app.cell
def _():
    student_name, student_age, student_grade = "John", 20, 97.7
    print(student_name, student_age, student_grade)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Edit the values in the next cell and watch the output update. Try a different name, age, and grade.
    """)
    return


@app.cell
def _():
    your_name = "John"
    your_age = 20
    your_grade = 97.7
    print(f"{your_name} is {your_age} years old and has a grade of {your_grade}.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Literals

    A literal is a value written directly in the source code. `404` is an integer.
    """)
    return


@app.cell
def _():
    literal_number = 404
    print(literal_number, "->", type(literal_number))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `"404"` looks similar, but the quotes make it a string.
    """)
    return


@app.cell
def _():
    literal_text_number = "404"
    print(literal_text_number, "->", type(literal_text_number))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `5.5` is a float.
    """)
    return


@app.cell
def _():
    literal_float = 5.5
    print(literal_float, "->", type(literal_float))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `"Python"` is a string.
    """)
    return


@app.cell
def _():
    literal_word = "Python"
    print(literal_word, "->", type(literal_word))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `False` is a boolean.
    """)
    return


@app.cell
def _():
    literal_flag = False
    print(literal_flag, "->", type(literal_flag))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the values below and observe their types.
    """)
    return


@app.cell
def _():
    example_a = 25
    example_b = 3.14
    example_c = "25"
    example_d = True
    print(type(example_a))
    print(type(example_b))
    print(type(example_c))
    print(type(example_d))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Converting types

    `int()`, `float()`, and `str()` build a new value of that type. The quotes around `"404"` make a string. `int("404")` reads those digits as an integer.
    """)
    return


@app.cell
def _():
    converted_int = int("404")
    converted_float = float("2.5")
    converted_text = str(404)
    print(converted_int, "->", type(converted_int))
    print(converted_float, "->", type(converted_float))
    print(converted_text, "->", type(converted_text))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `int()` needs a whole number. `int("2.5")` raises an error. Convert to `float` first when the text has a decimal point. `str(2.5)` turns a number into text, which is what `+` needs when you join a number to a string.
    """)
    return


@app.cell
def _():
    print(int(float("2.5")))
    print("Answer: " + str(2.5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Comments and `print`

    A `#` starts a comment. Python ignores the rest of that line. `print` separates values with `sep` and finishes the line with `end`. The default separator is a space, and the default end is a new line.
    """)
    return


@app.cell
def _():
    # The next line converts text to an integer.
    commented_value = int("15")
    print("A", "B", "C", sep="-")
    print("same line", end=" ")
    print("continues")
    print(commented_value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Python Arithmetic Operators

    | Operator | Name |
    |:---:|---|
    | `+` | addition |
    | `-` | subtraction |
    | `*` | multiplication |
    | `/` | division |
    | `//` | floor division |
    | `%` | modulus (remainder) |
    | `**` | exponentiation |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Division and floor division

    Division (`/`) returns the quotient as a floating-point number. `5 / 2` is `2.5`.
    """)
    return


@app.cell
def _():
    print(5 / 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Floor division (`//`) rounds the quotient down to the nearest integer. `5 // 2` is `2`.
    """)
    return


@app.cell
def _():
    print(5 // 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same pair of operators with `5` and `3`. Division keeps the fraction.
    """)
    return


@app.cell
def _():
    print(5 / 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Floor division drops the fraction. `5 // 3` is `1`.
    """)
    return


@app.cell
def _():
    print(5 // 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modulus

    `m % n` is the remainder after the floor division `m // n`. `5 % 3` is `2`, because `3 * 1 + 2 = 5`.
    """)
    return


@app.cell
def _():
    dividend = 5
    divisor = 3
    print(dividend % divisor)
    return dividend, divisor


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The check: divisor times the floor quotient, plus the remainder, equals the dividend.
    """)
    return


@app.cell
def _(dividend, divisor):
    print(divisor * (dividend // divisor) + (dividend % divisor))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exponentiation

    `m**2` means **m to the power of 2**.
    """)
    return


@app.cell
def _():
    power_base = 5
    print(power_base**2)
    return (power_base,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `5` to the power of `3`.
    """)
    return


@app.cell
def _(power_base):
    print(power_base**3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `5` to the power of `4`.
    """)
    return


@app.cell
def _(power_base):
    print(power_base**4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A negative exponent gives a fraction. `5 ** -1` is `1/5`, which is `0.2`.
    """)
    return


@app.cell
def _(power_base):
    print(power_base**-1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Assigning one name to another

    Assigning one variable to another makes both names refer to the same value. After `number_n = number_x`, both names refer to `2.5`. For a number this behaves like a copy, because a number cannot be changed in place. A later lesson shows that the same kind of assignment does not copy a dictionary: both names then refer to one dictionary.
    """)
    return


@app.cell
def _():
    number_x = 2.5
    number_n = number_x
    print(number_n, "->", type(number_n))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Boolean `not`

    `not` is not an arithmetic operator. It reverses a boolean. `not False` is `True`.
    """)
    return


@app.cell
def _():
    original_condition = False
    opposite_condition = not original_condition
    print(opposite_condition)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Joining strings

    `+` joins two strings when both values are text. That is concatenation, not addition.
    """)
    return


@app.cell
def _():
    first_name = "John"
    full_name = first_name + " Doe"
    print(full_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Use floor division and the remainder for `17` and `5`. Replace each `None` with your code. What is `17 % 5`, and why?
    """)
    return


@app.cell
def _():
    student_floor = None
    student_remainder = None
    print(student_floor)
    print(student_remainder)
    return student_floor, student_remainder


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_floor = 17 // 5
student_remainder = 17 % 5
```
The remainder is `2`. `5` goes into `17` three times, and `17 - 15 = 2`.
''')}, lazy=True)
    return


@app.cell
def _(mo):
    operator_m = mo.ui.number(start=-12, stop=20, step=1, value=5, label="m")
    operator_n = mo.ui.number(start=-5, stop=8, step=1, value=3, label="n")
    mo.vstack(
        [
            mo.md("### Explore arithmetic operators"),
            mo.md(
                "Change either value. The results update automatically. "
                "`m` and `n` stay in a small range so the power stays readable."
            ),
            mo.hstack([operator_m, operator_n], justify="start", gap=2),
        ]
    )
    return operator_m, operator_n


@app.cell
def _(mo, operator_m, operator_n):
    if operator_m.value is None or operator_n.value is None:
        operator_table = mo.md("Enter a number for both `m` and `n`.")
    else:
        m_value = int(operator_m.value)
        n_value = int(operator_n.value)

        if n_value == 0:
            division_result = "undefined (division by zero)"
            floor_result = "undefined (division by zero)"
            remainder_result = "undefined (division by zero)"
        else:
            division_result = m_value / n_value
            floor_result = m_value // n_value
            remainder_result = m_value % n_value

        if m_value == 0 and n_value < 0:
            power_result = "undefined (zero to a negative power)"
        else:
            power_result = m_value ** n_value

        operator_table = mo.md(
            f"""
            | Expression | Result |
            |---|---:|
            | `m + n` | {m_value + n_value} |
            | `m - n` | {m_value - n_value} |
            | `m * n` | {m_value * n_value} |
            | `m / n` | {division_result} |
            | `m // n` | {floor_result} |
            | `m % n` | {remainder_result} |
            | `m ** n` | {power_result} |
            """
        )
    operator_table
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Python Assignment Operators

    | Operator | Example | Same as |
    |:---:|---|---|
    | `=` | `x = 5` | `x = 5` |
    | `+=` | `x += 5` | `x = x + 5` |
    | `-=` | `x -= 5` | `x = x - 5` |
    | `*=` | `x *= 5` | `x = x * 5` |
    | `/=` | `x /= 5` | `x = x / 5` |
    | `%=` | `x %= 5` | `x = x % 5` |
    | `//=` | `x //= 5` | `x = x // 5` |
    | `**=` | `x **= 5` | `x = x ** 5` |

    The sequence begins with `5`. The type is `int`.
    """)
    return


@app.cell
def _():
    assignment_start = 5
    print(assignment_start, type(assignment_start))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `+= 10` adds `10` to a variable that starts at `5`. The value is now `15`, still an integer. The next cell starts again from a literal, because this lesson does not reuse the same name in a later cell.
    """)
    return


@app.cell
def _():
    after_add = 5
    after_add += 10
    print(after_add, type(after_add))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `-= 3` starts again from `15` and subtracts `3`. The value is `12`.
    """)
    return


@app.cell
def _():
    after_subtract = 15
    after_subtract -= 3
    print(after_subtract, type(after_subtract))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `/= 4` divides by `4`. Ordinary division produces a float, even when the result is a whole number. `12 / 4` is `3.0`.
    """)
    return


@app.cell
def _():
    after_divide = 12
    after_divide /= 4
    print(after_divide, type(after_divide))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md("Notice that ordinary division with `/` produces a `float`, even when the result is a whole number."),
        kind="info",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Start from `8` and apply `*= 3`. Replace `None` with your code. What is the value, and what is its type?
    """)
    return


@app.cell
def _():
    student_scaled = None
    student_scaled_type = None
    print(student_scaled)
    print(student_scaled_type)
    return student_scaled, student_scaled_type


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_scaled = 8
student_scaled *= 3
student_scaled_type = type(student_scaled)
```
The value is `24`. Multiplying two integers keeps the type `int`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - Variables in Python are created by assignment and do not require explicit declaration.
    - Python supports dynamic typing, allowing a variable to refer to values of different types.
    - The `type()` function reports the data type of a value.
    - Common built-in types include integers (`int`), floating-point numbers (`float`), booleans (`bool`), and strings (`str`).
    - Arithmetic operators calculate new values, while shorthand assignment operators calculate and update a variable at the same time.
    - `/` returns a float. `//` drops the fraction, and `%` returns the remainder.
    - `int()`, `float()`, and `str()` convert a value. A comment starts with `#`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. When is a Python variable created?
    2. What does `type(3.3)` report?
    3. What is the type of `"404"`?
    4. Are `age` and `Age` the same variable?
    5. What is `5 // 2`?
    6. What is `5 % 2`?
    7. What type does `x /= 4` produce when `x` was an integer?
    8. What does `int("404")` return?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **At the first assignment:** Python does not require a separate declaration.
2. **`float`:** A decimal point makes the value a floating-point number.
3. **`str`:** The quotes make it text, even though the characters are digits.
4. **No:** Names are case-sensitive.
5. **`2`:** Floor division drops the fraction.
6. **`1`:** `2` goes into `5` twice, and the remainder is `1`.
7. **`float`:** `/` always returns a floating-point number.
8. **The integer `404`:** `int()` reads the digits. The quotes are not part of the number.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - [The Python Tutorial: An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
    - [Built-in functions `int`, `float`, `str`, and `print`](https://docs.python.org/3/library/functions.html)
    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
