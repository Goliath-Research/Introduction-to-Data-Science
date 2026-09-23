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

    - Create a tuple, including an empty tuple and a tuple with one item.
    - Read items and slices with the same index rules used for lists and strings.
    - Explain why a tuple cannot be changed, and how to build a new tuple when a value must be added.
    - Use `count()` and `index()`, and read an item inside a nested tuple.

    ## Background

    A tuple is an ordered sequence, like a list, but it is immutable: after you create it, you cannot replace, add, or remove its items. Use a tuple for values that should stay together and should not change, such as a pair of coordinates or a record of fixed fields.

    ## Datasets Used

    This notebook does not use external datasets. The examples are short tuples written in the code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating tuples

    A tuple is written with parentheses `()`. A tuple with one item needs a trailing comma. Without that comma, the parentheses only group a value, and the result is not a tuple.
    """)
    return


@app.cell
def _():
    empty_tuple = ()
    print("empty:", empty_tuple, "->", type(empty_tuple))

    one_item = (4,)
    print("one item:", one_item, "->", type(one_item))

    # Parentheses without a comma do not make a tuple.
    not_a_tuple = (4)
    print("no comma:", not_a_tuple, "->", type(not_a_tuple))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The items in a tuple do not have to share a type. `len()` returns how many items it holds. An index reads one item, using the same positions as a list: the first item is `0`.
    """)
    return


@app.cell
def _():
    record = (0, "one", "two", 3, 4, 5.5)
    print(record)
    print("type:", type(record))
    print("length:", len(record))
    print("item 0:", record[0], "->", type(record[0]))
    print("item 1:", record[1], "->", type(record[1]))
    print("item 2:", record[2], "->", type(record[2]))
    print("item 5:", record[5], "->", type(record[5]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tuples are immutable

    You cannot replace an item, and a tuple has no `append()` method. Run each of the next two cells to see the error.
    """)
    return


@app.cell
def _():
    assign_target = (0, "one", "two", 3, 4, 5.5)
    assign_target[2] = 2
    return


@app.cell
def _():
    append_target = (0, "one", "two", 3, 4, 5.5)
    append_target.append(6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When a new item is required, convert the tuple to a list, change the list, and convert the list back. `tuple()` and `list()` each build a new sequence. The original tuple is unchanged until you assign the new tuple to the name.
    """)
    return


@app.cell
def _():
    source_tuple = (0, "one", "two", 3, 4, 5.5)
    as_list = list(source_tuple)
    print("as a list:", as_list, "->", type(as_list))

    as_list.append(6)
    print("after append:", as_list)

    updated_tuple = tuple(as_list)
    print("as a tuple:", updated_tuple, "->", type(updated_tuple))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Slicing

    A slice uses the same rule as a list or a string. `tuple[start:stop]` includes `start` and excludes `stop`.
    """)
    return


@app.cell
def _():
    slice_tuple = (0, "one", "two", 3, 4, 5.5, 6)
    print("from 1 to 4:", slice_tuple[1:4])
    print("first three:", slice_tuple[:3])
    print("from index 4:", slice_tuple[4:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tuple operations

    `len()` returns the number of items. `+` builds a new tuple and does not change the tuples you add. `in` asks whether a value is an item. `count()` returns how many times a value appears. `index()` returns the first position of a value, and raises an error when the value is absent.
    """)
    return


@app.cell
def _():
    length_empty = ()
    length_one = (4,)
    length_record = (0, "one", "two", 3, 4, 5.5, 6)

    print("len empty:", len(length_empty))
    print("len one item:", len(length_one))
    print("len record:", len(length_record))
    print()

    combined = length_one + length_record
    print("concatenated:", combined)
    print("3 in record:", 3 in length_record)
    print("10 in record:", 10 in length_record)
    print("count of 4:", combined.count(4))
    print("index of 4:", combined.index(4))
    print("index of 'one':", combined.index("one"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Run the next cell to see the error from `index()` when the value is not in the tuple.
    """)
    return


@app.cell
def _():
    index_target = (4, 0, "one", "two", 3, 4, 5.5, 6)
    index_target.index("five")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Nested tuples

    A tuple may contain another tuple. The outer tuple below has three items: two strings, and one tuple. A second index reads an item inside the inner tuple. `-1` still means the last item of the sequence you index.
    """)
    return


@app.cell
def _():
    inner = (4, 0, "one", "two", 3, 4, 5.5, 6)
    nested = ("123", "hello", inner)
    print(nested)
    print("length:", len(nested))
    print("item 0:", type(nested[0]))
    print("item 1:", type(nested[1]))
    print("item 2:", type(nested[2]))
    print("inner tuple:", nested[2])
    print("item 'two':", nested[2][3])
    print("last inner item:", nested[2][7])
    print("last inner item again:", nested[2][-1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `practice` and the index, then run the cell.
    """)
    return


@app.cell
def _():
    practice = ("Mon", "Tue", "Wed", "Thu", "Fri")
    print("first:", practice[0])
    print("last:", practice[-1])
    print("middle:", practice[1:4])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A tuple is an ordered, immutable sequence written with parentheses.
    - A one-item tuple needs a trailing comma. `(4)` is an integer, not a tuple.
    - Indexes and slices follow the same rules as lists. You cannot assign to an index or call `append()`.
    - To add an item, convert to a list, change the list, and convert back with `tuple()`.
    - `count()` and `index()` search the items. A tuple may contain another tuple.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
