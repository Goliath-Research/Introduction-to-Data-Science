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
    """)
    return


@app.cell
def _():
    print("Hello World!")
    print("Hello World!")

    greeting = "Hello World!"
    print(greeting)
    print(type(greeting))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Multiline strings

    Assign a multiline string with three quotes.
    """)
    return


@app.cell
def _():
    first_multiline = """This is an
    example of a
    multiline string."""
    print(first_multiline)

    second_multiline = '''This is another
    example of a
    multiline string.'''
    print(second_multiline)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Strings are sequences

    Square brackets read one character. Index `0` is the first character.
    """)
    return


@app.cell
def _():
    indexed_greeting = "Hello World!"
    print(indexed_greeting)
    print(indexed_greeting[0])
    print(indexed_greeting[1])
    print(indexed_greeting[2])
    print(indexed_greeting[3])
    print(indexed_greeting[4])
    print("length =", len(indexed_greeting))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `your_word`, then run the cell. Print the first character, the last character, and the length.
    """)
    return


@app.cell
def _():
    your_word = "Python"

    print(your_word)
    print("first =", your_word[0])
    print("last  =", your_word[-1])
    print("length =", len(your_word))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Slicing

    A slice returns a range of characters. `s[1:5]` includes index 1 and stops before index 5.

    - Omit the start to begin at the first character: `s[:5]`
    - Omit the end to continue through the last character: `s[6:]`
    """)
    return


@app.cell
def _():
    slice_text = "Hello World!"

    print(slice_text[1:5])
    print(slice_text[0:5])
    print(slice_text[:5])
    print(slice_text[6:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Negative indexes

    A negative index counts from the end of the string. The diagram below labels the indexes of `Hello World!`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ![Indexes of Hello World](Hello_World.PNG)
    """)
    return


@app.cell
def _():
    negative_text = "Hello World!"

    print(negative_text[-6:-1])
    print(negative_text[-6:])
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
    ## String methods

    String methods return a new string. They do not change the original value.
    """)
    return


@app.cell
def _():
    spaced_text = "   Hello World!    "
    trimmed_text = spaced_text.strip()
    print("strip:     ", trimmed_text)
    print("lower:     ", trimmed_text.lower())
    print("upper:     ", trimmed_text.upper())
    print("capitalize:", "hello world".capitalize())
    print("replace:   ", trimmed_text.replace("World", "Earth"))
    print("original:  ", repr(spaced_text))
    return


@app.cell
def _():
    search_text = "Hello World!"

    print("find o:  ", search_text.find("o"))
    print("find u:  ", search_text.find("u"))
    print("count u: ", search_text.count("u"))
    print("count l: ", search_text.count("l"))
    print("find l:  ", search_text.find("l"))
    print("rfind l: ", search_text.rfind("l"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `find` returns the first position, or `-1` when the text is absent. `rfind` returns the last position. `count` returns how many times the text occurs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concatenation and format

    `+` joins strings. `format` places values into `{}` placeholders. Numbered placeholders such as `{0}` choose the argument by position.
    """)
    return


@app.cell
def _():
    given_name = "Jane"
    family_name = "Doe"
    print(given_name + " " + family_name)

    age_years = 30
    sentence = "My name is Anna, I am {}"
    print(sentence.format(age_years))

    full_sentence = "My name is {} {}, I am {}"
    print(full_sentence.format("Jane", "Doe", 33))

    indexed_sentence = "My name is {1} {2}, I am {0}"
    print(indexed_sentence.format(33, "Jane", "Doe"))
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
    ## Conclusions

    **Key takeaways:**

    - Strings can be written with single, double, or triple quotes.
    - Indexes start at 0. Negative indexes start at the end.
    - A slice includes the start index and excludes the stop index.
    - String methods return a new string and leave the original unchanged.
    - `+` concatenates strings. `format()` fills placeholders.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
