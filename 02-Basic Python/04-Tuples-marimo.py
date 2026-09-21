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
    # Python Tuples

    ## Objectives

    - Create tuples, including a one-item tuple.
    - Read items by index and recognize that a tuple cannot be changed.
    - Build a new tuple by converting to a list and back.
    - Use `count`, `index`, concatenation, and nesting.

    ## Background

    A tuple is an ordered collection written with parentheses. Its order does not change. Unlike a list, a tuple is immutable: you cannot replace or append items in place.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating tuples

    A one-item tuple needs a trailing comma. `(4)` is just the number 4 in parentheses.
    """)
    return


@app.cell
def _():
    empty_tuple = ()
    print("empty:", empty_tuple, type(empty_tuple))

    one_item = (4,)
    print("one item:", one_item, type(one_item))

    not_a_tuple = (4)
    print("not a tuple:", not_a_tuple, type(not_a_tuple))

    values = (0, "one", "two", 3, 4, 5.5)
    print(values)
    print("length =", len(values))
    print([type(item) for item in values])
    print("index 2 =", values[2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tuples are immutable

    Assignment and `append` both fail. The cells below catch the error so the rest of the notebook can still run.
    """)
    return


@app.cell
def _():
    fixed_values = (0, "one", "two", 3, 4, 5.5)

    try:
        fixed_values[2] = 2
    except TypeError as error:
        print("TypeError:", error)

    try:
        fixed_values.append(6)
    except AttributeError as error:
        print("AttributeError:", error)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To add an item, convert the tuple to a list, change the list, and convert it back.
    """)
    return


@app.cell
def _():
    original = (0, "one", "two", 3, 4, 5.5)
    as_list = list(original)
    print(as_list, type(as_list))

    as_list.append(6)
    print(as_list)

    extended = tuple(as_list)
    print(extended, type(extended))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Convert `your_tuple` to a list, append one value, and convert it back to a tuple.
    """)
    return


@app.cell
def _():
    your_tuple = ("a", "b")
    your_list = list(your_tuple)
    your_list.append("c")
    your_tuple = tuple(your_list)

    print(your_tuple, type(your_tuple))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tuple operations

    `+` concatenates tuples. `in` tests membership. `count` and `index` search for a value. Tuples may contain other tuples.
    """)
    return


@app.cell
def _():
    first = (4,)
    second = (0, "one", "two", 3, 4, 5.5, 6)
    combined = first + second
    print("combined:", combined)
    print("3 in second:", 3 in second)
    print("10 in second:", 10 in second)
    print("count of 4:", combined.count(4))
    print("index of 3:", combined.index(3))
    print("index of 'one':", combined.index("one"))

    nested = ("123", "hello", combined)
    print(nested)
    print("length:", len(nested))
    print(type(nested[0]), type(nested[2]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Check whether a value is in the tuple, then print how many times it occurs.
    """)
    return


@app.cell
def _():
    practice_tuple = (1, 2, 2, 3)
    target = 2

    print(target in practice_tuple)
    print(practice_tuple.count(target))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A tuple is an ordered, immutable collection written with `()`.
    - A one-item tuple needs a comma: `(4,)`.
    - Items can be read by index, but they cannot be replaced or appended in place.
    - Convert to a list when you need to change the contents, then convert back.
    - `count`, `index`, `in`, and `+` work with tuples.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
