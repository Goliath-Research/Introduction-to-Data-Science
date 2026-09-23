import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd

    return mo, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Working with Text Data

    ## Objectives

    - Clean and change the case of text in a Series.
    - Split, join, replace, and repeat strings.
    - Test and search text with boolean methods, `find`, and `findall`.
    - Turn categories into indicator columns with `get_dummies`.

    ## Background

    String methods on a Series are reached through `.str`. A method such as `lower` does not change the original Series. It returns a new one. A missing value stays missing, and the result for that entry is `NaN`.

    ## Datasets Used

    This lesson uses small Series written in the cells, including one missing value and one number stored beside the text.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Text operations in a Pandas Series

    This Series mixes ordinary words, extra spaces, a newline, a missing value, digits stored as text, and the number `34`.
    """)
    return


@app.cell
def _(np, pd):
    text = pd.Series([
        'Tommy   ',
        'William Scott',
        'John\n',
        'ALBERT@',
        np.nan,
        '5678',
        'PeterSmith',
        34,
    ])
    text
    return (text,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `lower` converts each string to lower case. `upper` converts each string to upper case. `swapcase` exchanges lower case and upper case.
    """)
    return


@app.cell
def _(text):
    print(text.str.lower())
    print(text.str.upper())
    text.str.swapcase()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `islower` is `True` when every character in the string is lower case. `isupper` checks for upper case. `isnumeric` is `True` when every character is a digit.

    Calling `lower` first, then `islower`, makes the alphabetic strings report `True`. The original Series is unchanged.
    """)
    return


@app.cell
def _(text):
    print(text.str.islower())
    print(text.str.lower().str.islower())
    print(text)
    print(text.str.isupper())
    text.str.isnumeric()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `len` is the number of characters. Spaces and the newline count.

    `strip` removes whitespace from both ends, including the newline. `'John\n'` becomes `'John'`.

    `split(' ')` breaks each string at spaces. The result in each row is a list.
    """)
    return


@app.cell
def _(text):
    print(text.str.len())
    print(text.str.strip())
    text.str.split(' ')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next Series is a new one. `cat(sep='_')` joins its elements into a single string, with `_` between them.
    """)
    return


@app.cell
def _(pd):
    names = pd.Series(['Tom ', ' John', 'Will Smith', '123'])
    names.str.cat(sep='_')
    return (names,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `contains` is `True` when the pattern occurs in the element. `replace` substitutes one substring for another. `repeat` repeats each element the given number of times. The Series still has the same number of rows. What changes is the length of each element.
    """)
    return


@app.cell
def _(names):
    print(names.str.contains(' '))
    print(names.str.replace(' ', '_'))
    print(names.str.repeat(2))
    print(names.str.repeat(5))
    print(len(names))
    print(len(names.str.repeat(5)))
    print(len(names[0]))
    print(len(names.str.repeat(5)[0]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `count` is how many times the pattern appears in each element.

    `startswith` is `True` when the element begins with the pattern. The check is case sensitive: `'w'` and `'W'` are different. `lower` followed by `startswith('w')` ignores that difference.

    `endswith` is `True` when the element ends with the pattern.
    """)
    return


@app.cell
def _(names):
    print(names.str.count('o'))
    print(names.str.startswith(' '))
    print(names.str.startswith('w'))
    print(names.str.startswith('W'))
    print(names.str.lower().str.startswith('w'))
    names.str.endswith(' ')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `find` returns the position of the first match. Positions start at 0. If the pattern is absent, `find` returns `-1`.

    `findall` returns a list of every match in that element.
    """)
    return


@app.cell
def _(names):
    print(names.str.find('2'))
    print(names.str.find('ll'))
    names.str.findall('ll')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same three methods on a Series of color names. `find('e')` is the first `'e'`. `findall('e')` collects every `'e'`. `endswith('e')` asks whether the name ends in `'e'`.
    """)
    return


@app.cell
def _(pd):
    colors = pd.Series(['red', 'orange', 'yellow', 'green', 'blue'])
    print(colors)
    # return the index of the first occurrence of the pattern
    print(colors.str.find('e'))
    # return all the 'e's
    print(colors.str.findall('e'))
    colors.str.endswith('e')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `get_dummies` builds one column per distinct value. A row has `1` in the column that matches its value and `0` in the others. This is also called one-hot encoding.
    """)
    return


@app.cell
def _(pd):
    country = pd.Series([
        'USA',
        'Colombia',
        'Ecuador',
        'Rep. Dominicana',
        'Puerto Rico',
    ])
    country.str.get_dummies()
    return


@app.cell
def _(pd):
    sex = pd.Series(['Male', 'Female'])
    sex.str.get_dummies()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Strip the spaces, make the letters lower case, then replace the space inside `'blue bird'`.
    """)
    return


@app.cell
def _(pd):
    practice = pd.Series(['  Cat', 'DOG  ', 'Blue Bird'])
    practice.str.strip().str.lower().str.replace(' ', '_')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - String methods live under `.str` and return a new Series.
    - `lower`, `upper`, and `swapcase` change case. `islower`, `isupper`, and `isnumeric` test each element.
    - `strip` removes whitespace from both ends. `split` breaks a string into a list. `cat` joins the Series into one string.
    - `contains`, `startswith`, and `endswith` answer a yes-or-no question. `count`, `find`, and `findall` locate a pattern.
    - `replace` substitutes text. `repeat` repeats each element without adding rows.
    - `get_dummies` turns each distinct string into its own indicator column.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 3.
    """)
    return


if __name__ == "__main__":
    app.run()
