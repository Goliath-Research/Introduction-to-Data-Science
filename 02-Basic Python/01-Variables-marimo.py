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

    ## Background

    Variables are fundamental to any programming language, acting as placeholders for data that can change over time. In Python, variables are dynamically typed: the type is inferred at runtime and can change as the program executes.

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
    """)
    return


@app.cell
def _():
    integer_value = 320       # int
    float_value = 2.5       # float

    print("integer_value =", integer_value, "->", type(integer_value))
    print("float_value   =", float_value, "->", type(float_value))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dynamic typing

    A variable can refer to values of different types at different moments. This demonstration is intentionally kept in one cell so you can see the sequence clearly.
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
    mo.md("""
    ### Boolean and string variables
    """)
    return


@app.cell
def _():
    condition_example = False
    print(condition_example, "->", type(condition_example))

    character_name_example = "John"
    print(character_name_example, " ->", type(character_name_example))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Variable names

    A variable name may contain letters, digits, and underscores (`_`), but it cannot begin with a digit. Variable names are case-sensitive, so `age` and `Age` are different variables.
    """)
    return


@app.cell
def _():
    age_person = 20
    age_mother = 40

    print("Laura is", age_person, "years old. Her mother is", age_mother)
    
    # Using Python's f-string formatting
    print(f"Laura is {age_person} years old. Her mother is {age_mother}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Multiple assignment

    You can assign values to multiple variables in one line.
    """)
    return


@app.cell
def _():
    student_name, student_age, student_grade = "John", 20, 97.7

    print("Name  =", student_name)
    print("Age   =", student_age)
    print("Grade =", student_grade)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Edit the values in the next cell, then run it. Try a different name, age, and grade.
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

    A literal is a value written directly in the source code. Notice that `404` and `"404"` look similar but have different types.
    """)
    return


@app.cell
def _():

    literal_example = 404
    print(literal_example, "->", type(literal_example))

    literal_example = "404"
    print(literal_example, "->", type(literal_example))

    literal_example = 5.5
    print(literal_example, "->", type(literal_example))

    literal_example = "Python"
    print(literal_example, "->", type(literal_example))

    literal_example = False
    print(literal_example, "->", type(literal_example))
   
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


@app.cell
def _():
    number_x = 2.5
    number_n = "No"

    print("\nBefore assignment:")
    print("number_x =", number_x, type(number_x))
    print("number_n =", number_n, type(number_n))

    number_n = number_x
    print("\nAfter number_n = number_x:")
    print("number_n =", number_n, type(number_n))
    return


@app.cell
def _():
    original_condition = False
    opposite_condition = not original_condition
    print("condition     =", original_condition)
    print("not condition =", opposite_condition)

    first_name = "John"
    full_name = first_name + " Doe"
    print("full name     =", full_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Division and floor division

    Division (`/`) returns the quotient as a floating-point number. Floor division (`//`) rounds the quotient down to the nearest integer.
    """)
    return


@app.cell
def _():
    division_value = 5
    print("5 / 2  =", division_value / 2)
    print("5 // 2 =", division_value // 2)
    print("\n5 / 3  =", 5 / 3)
    print("5 // 3 =", 5 // 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modulus

    `m % n` is the remainder after the floor division `m // n`.
    """)
    return


@app.cell
def _():
    dividend = 5
    divisor = 3

    print("Floor division:", dividend, "//", divisor, "=", dividend // divisor)
    print("Remainder:     ", dividend, "%", divisor, "=", dividend % divisor)
    print("Verification:  ", divisor, "*", dividend // divisor, "+", dividend % divisor,
          "=", divisor * (dividend // divisor) + (dividend % divisor))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exponentiation

    `m**2` means **m to the power of 2**. Exponents may also be negative.
    """)
    return


@app.cell
def _():
    power_base = 5

    print(power_base, "to the power of 2: ", power_base**2)
    print(power_base, "to the power of 3: ", power_base**3)
    print(power_base, "to the power of 4: ", power_base**4)
    print(power_base, "to the power of -1:", power_base**-1)
    return


@app.cell
def _(mo):
    operator_m = mo.ui.number(value=5, label="m")
    operator_n = mo.ui.number(value=3, label="n")
    mo.vstack(
        [
            mo.md("### Explore arithmetic operators"),
            mo.md("Change either value. The results update automatically."),
            mo.hstack([operator_m, operator_n], justify="start", gap=2),
        ]
    )
    return operator_m, operator_n


@app.cell
def _(mo, operator_m, operator_n):
    m_value = operator_m.value
    n_value = operator_n.value

    if n_value == 0:
        division_result = "undefined (division by zero)"
        floor_result = "undefined (division by zero)"
        remainder_result = "undefined (division by zero)"
    else:
        division_result = m_value / n_value
        floor_result = m_value // n_value
        remainder_result = m_value % n_value

    mo.md(
        f"""
        | Expression | Result |
        |---|---:|
        | `m + n` | {m_value + n_value} |
        | `m - n` | {m_value - n_value} |
        | `m * n` | {m_value * n_value} |
        | `m / n` | {division_result} |
        | `m // n` | {floor_result} |
        | `m % n` | {remainder_result} |
        | `m ** n` | {m_value ** n_value} |
        """
    )
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

    The following sequence begins with `m = 5`, adds 10, subtracts 3, and divides by 4.
    """)
    return


@app.cell
def _():
    assignment_value = 5
    print("Initial value:", assignment_value, type(assignment_value))

    assignment_value += 10
    print("After += 10: ", assignment_value, type(assignment_value))

    assignment_value -= 3
    print("After -= 3:  ", assignment_value, type(assignment_value))

    assignment_value /= 4
    print("After /= 4:  ", assignment_value, type(assignment_value))
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
    ## Conclusions

    **Key takeaways:**

    - Variables in Python are created by assignment and do not require explicit declaration.
    - Python supports dynamic typing, allowing a variable to refer to values of different types.
    - The `type()` function reports the data type of a value.
    - Common built-in types include integers (`int`), floating-point numbers (`float`), booleans (`bool`), and strings (`str`).
    - Arithmetic operators calculate new values, while shorthand assignment operators calculate and update a variable at the same time.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
