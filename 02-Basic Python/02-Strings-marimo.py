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
    # Python Strings

    ## Objectives

    - Create string literals with single quotes, double quotes, and triple quotes.
    - Read individual characters and slices, including negative indexes.
    - Use common string methods without changing the original string.
    - Combine strings with concatenation and `format()`.

    ## Background

    A string is a sequence of characters. Python does not have a separate character type: a single character is a string of length 1. The first index is 0.

    ## Datasets Used

    This notebook does not use external datasets. It focuses on string values written in the code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## String literals

    String literals are surrounded by single or double quotation marks. `'hello'` is the same as `"hello"`.

    This string uses single quotes.
    """)
    return


@app.cell
def _():
    print('Hello World!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same text, written with double quotes.
    """)
    return


@app.cell
def _():
    print("Hello World!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A variable can hold a string. Its type is `str`.
    """)
    return


@app.cell
def _():
    greeting = "Hello World!"
    print(greeting, "->", type(greeting))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An apostrophe ends a single-quoted string early. Double quotes let the apostrophe sit inside the text.
    """)
    return


@app.cell
def _():
    print("I'm a string")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A single-quoted string can hold an apostrophe if you escape it with `\'`.
    """)
    return


@app.cell
def _():
    print('I\'m a string')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Multiline strings

    Three double quotes hold a string that continues onto the next lines.
    """)
    return


@app.cell
def _():
    first_multiline = """This is an
    example of a
    multiline string."""
    print(first_multiline)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Three single quotes do the same job.
    """)
    return


@app.cell
def _():
    second_multiline = '''This is another
    example of a
    multiline string.'''
    print(second_multiline)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Parentheses next to each other join string pieces into one line. Python concatenates them when the program loads.
    """)
    return


@app.cell
def _():
    third_multiline = (
        "This is a very long string that goes"
        " on and on "
        "with automatic concatenation"
    )
    print(third_multiline)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Strings are sequences

    Square brackets read one character. This is the string used in the next cells.
    """)
    return


@app.cell
def _():
    indexed_greeting = "Hello World!"
    print(indexed_greeting)
    return (indexed_greeting,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Index `0` is the first character.
    """)
    return


@app.cell
def _(indexed_greeting):
    print(indexed_greeting[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Index `1` is the second character.
    """)
    return


@app.cell
def _(indexed_greeting):
    print(indexed_greeting[1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `len()` is the number of characters, including the space and the exclamation mark. This string has 12 characters, so the last index is 11.
    """)
    return


@app.cell
def _(indexed_greeting):
    print(len(indexed_greeting))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `your_word`, then run the cell. Print the first character and the length.
    """)
    return


@app.cell
def _():
    your_word = "Python"
    print(your_word)
    print("first =", your_word[0])
    print("length =", len(your_word))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Slicing

    A slice returns a range of characters. `s[1:5]` includes index 1 and stops before index 5.
    """)
    return


@app.cell
def _():
    slice_text = "Hello World!"
    print(slice_text[1:5])
    return (slice_text,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `s[0:5]` starts at the first character and stops before index 5. The result is `Hello`.
    """)
    return


@app.cell
def _(slice_text):
    print(slice_text[0:5])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Omit the start to begin at the first character. `s[:5]` is the same slice as `s[0:5]`.
    """)
    return


@app.cell
def _(slice_text):
    print(slice_text[:5])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Omit the end to continue through the last character. `s[6:]` is `World!`.
    """)
    return


@app.cell
def _(slice_text):
    print(slice_text[6:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Negative indexes

    A negative index counts from the end of the string.

    | | **H** | **e** | **l** | **l** | **o** | | **W** | **o** | **r** | **l** | **d** | **!** |
    |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
    | index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
    | negative index | -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

    `[-6:-1]` starts at `W` and stops before the last character, so the `!` is left out.
    """)
    return


@app.cell
def _():
    negative_text = "Hello World!"
    print(negative_text[-6:-1])
    return (negative_text,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Omit the stop to include the last character.
    """)
    return


@app.cell
def _(negative_text):
    print(negative_text[-6:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[-12:-7]` is the first word. Index `-7` is the space, and the stop is excluded.
    """)
    return


@app.cell
def _(negative_text):
    print(negative_text[-12:-7])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the slice bounds and predict the printed text before you run the cell.
    """)
    return


@app.cell
def _():
    practice_text = "Hello World!"
    start_index = 0
    stop_index = 5
    print(practice_text[start_index:stop_index])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    From `"Hello World!"`, take the slice that equals `"World"`. Replace `None` with your code. Is the stop index included?
    """)
    return


@app.cell
def _():
    student_world = None
    print(student_world)
    return (student_world,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_world = "Hello World!"[6:11]
```
No. The stop index is excluded. Index 11 is `!`, so the slice stops before it. `"Hello World!"[6:]` also works, and it includes the `!`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## String methods

    String methods return a new string. They do not change the original value.

    `strip()` removes the whitespace from the beginning and the end.
    """)
    return


@app.cell
def _():
    spaced_text = "   Hello World!    "
    trimmed_text = spaced_text.strip()
    print(trimmed_text)
    return spaced_text, trimmed_text


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `lower()` converts the string to lowercase.
    """)
    return


@app.cell
def _(trimmed_text):
    print(trimmed_text.lower())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `upper()` converts the string to uppercase.
    """)
    return


@app.cell
def _(trimmed_text):
    print(trimmed_text.upper())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `capitalize()` converts the first character to uppercase and the rest to lowercase.
    """)
    return


@app.cell
def _(trimmed_text):
    print(trimmed_text.capitalize())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `replace()` returns a new string with one substring replaced by another.
    """)
    return


@app.cell
def _(trimmed_text):
    print(trimmed_text.replace("World", "Earth"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The original string is unchanged. `repr()` shows the spaces that are still at both ends.
    """)
    return


@app.cell
def _(spaced_text):
    print(repr(spaced_text))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `find()` returns the first position of a substring, or `-1` when the text is absent. The first `o` in `"Hello World!"` is at index 4.
    """)
    return


@app.cell
def _():
    search_text = "Hello World!"
    print(search_text.find("o"))
    return (search_text,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There is no `u`, so `find()` returns `-1`.
    """)
    return


@app.cell
def _(search_text):
    print(search_text.find("u"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `count()` returns how many times a substring appears. `u` appears 0 times.
    """)
    return


@app.cell
def _(search_text):
    print(search_text.count("u"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `l` appears 3 times.
    """)
    return


@app.cell
def _(search_text):
    print(search_text.count("l"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `find("l")` returns the first `l`, at index 2.
    """)
    return


@app.cell
def _(search_text):
    print(search_text.find("l"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `rfind("l")` returns the last `l`, at index 9.
    """)
    return


@app.cell
def _(search_text):
    print(search_text.rfind("l"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concatenation and format

    `+` joins strings.
    """)
    return


@app.cell
def _():
    given_name = "Jane"
    family_name = "Doe"
    print(given_name + " " + family_name)
    return family_name, given_name


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `format()` places a value into a `{}` placeholder.
    """)
    return


@app.cell
def _():
    age_years = 30
    sentence = "My name is Anna, I am {}"
    print(sentence.format(age_years))
    return (age_years,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `format()` can take several arguments. They fill the placeholders from left to right.
    """)
    return


@app.cell
def _(age_years, family_name, given_name):
    full_sentence = "My name is {} {}, I am {}"
    print(full_sentence.format(given_name, family_name, age_years))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A number inside the braces chooses the argument by position. `{0}` is the first argument, which is the age.
    """)
    return


@app.cell
def _(age_years, family_name, given_name):
    indexed_sentence = "My name is {1} {2}, I am {0}"
    print(indexed_sentence.format(age_years, given_name, family_name))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `split()` returns a list of the pieces separated by the delimiter. The comma is not kept.
    """)
    return


@app.cell
def _():
    comma_text = "Hello, World!"
    print(comma_text.split(","))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Edit the name and age, then run the cell.
    """)
    return


@app.cell
def _():
    your_name = "Ana"
    your_age = 21
    print("My name is {} and I am {}.".format(your_name, your_age))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Call `upper()` on `"hello"`. Replace each `None` with your code. Does the original string change?
    """)
    return


@app.cell
def _():
    student_original = "hello"
    student_upper = None
    print(student_original)
    print(student_upper)
    return student_original, student_upper


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_original = "hello"
student_upper = student_original.upper()
```
No. `upper()` returns a new string, `"HELLO"`. `student_original` is still `"hello"`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - Strings can be written with single, double, or triple quotes. Escape a matching quote with `\`.
    - Indexes start at 0. Negative indexes start at the end.
    - A slice includes the start index and excludes the stop index.
    - String methods return a new string and leave the original unchanged.
    - `+` concatenates strings. `format()` fills placeholders. `split()` breaks a string into a list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What is the type of a single character such as `"A"`?
    2. Which index is the first character?
    3. What does `"Hello"[1:4]` return?
    4. Which character does a negative index of `-1` select?
    5. What does `find()` return when the substring is absent?
    6. Does `upper()` change the original string?
    7. What does `"a,b".split(",")` return?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **`str`:** Python has no separate character type. One character is a string of length 1.
2. **`0`:** Indexes start at the beginning.
3. **`"ell"`:** The slice includes index 1 and stops before index 4.
4. **The last character:** Negative indexes count backward from the end.
5. **`-1`:** That value means the substring was not found.
6. **No:** It returns a new string.
7. **`["a", "b"]`:** `split` returns a list and leaves the delimiter out.
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
