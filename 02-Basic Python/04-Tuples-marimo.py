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
    - Use `count()` and `index()`, read an item inside a nested tuple, and unpack a tuple into names.

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

    Commas make a tuple. Parentheses are usually written around it. An empty tuple is `()`, and it has no items.
    """)
    return


@app.cell
def _():
    empty_tuple = ()
    print(empty_tuple, "->", type(empty_tuple))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A tuple with one item needs a trailing comma.
    """)
    return


@app.cell
def _():
    one_item = (4,)
    print(one_item, "->", type(one_item))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Parentheses without a comma do not make a tuple. `(4)` is just the integer `4`.
    """)
    return


@app.cell
def _():
    not_a_tuple = (4)
    print(not_a_tuple, "->", type(not_a_tuple))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The items in a tuple do not have to share a type. This tuple mixes integers, strings, and a float.
    """)
    return


@app.cell
def _():
    record = (0, "one", "two", 3, 4, 5.5)
    print(record)
    return (record,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Unpacking

    Unpacking assigns each item to its own name. The number of names must match the number of items. This is the usual way to take a pair apart. A later lesson returns two values from a function the same way: the caller unpacks the tuple.
    """)
    return


@app.cell
def _():
    point = (3, 4)
    point_x, point_y = point
    print(point_x, point_y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `len()` returns how many items the tuple holds.
    """)
    return


@app.cell
def _(record):
    print(len(record))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An index reads one item, using the same positions as a list. The item at index 0 is the integer `0`.
    """)
    return


@app.cell
def _(record):
    print(record[0], "->", type(record[0]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Item 1 is a string.
    """)
    return


@app.cell
def _(record):
    print(record[1], "->", type(record[1]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The last item is a float.
    """)
    return


@app.cell
def _(record):
    print(record[5], "->", type(record[5]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tuples are immutable

    You cannot replace an item in a tuple, so the next cell raises a `TypeError` on purpose.
    """)
    return


@app.cell
def _():
    # This cell raises TypeError on purpose.
    assign_target = (0, "one", "two", 3, 4, 5.5)
    assign_target[2] = 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A tuple has no `append()` method, so the next cell raises an `AttributeError` on purpose.
    """)
    return


@app.cell
def _():
    # This cell raises AttributeError on purpose.
    append_target = (0, "one", "two", 3, 4, 5.5)
    append_target.append(6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When a new item is required, convert the tuple to a list. `list()` builds a new list. The tuple itself is unchanged.
    """)
    return


@app.cell
def _():
    source_tuple = (0, "one", "two", 3, 4, 5.5)
    as_list = list(source_tuple)
    print(as_list, "->", type(as_list))
    return (as_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The list can be changed. `append(6)` adds `6` at the end.
    """)
    return


@app.cell
def _(as_list):
    appended_list = as_list.copy()
    appended_list.append(6)
    print(appended_list)
    return (appended_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `tuple()` converts the list back. The result is a new tuple.
    """)
    return


@app.cell
def _(appended_list):
    updated_tuple = tuple(appended_list)
    print(updated_tuple, "->", type(updated_tuple))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Slicing

    A slice uses the same rule as a list or a string. `tuple[start:stop]` includes `start` and excludes `stop`.

    `[1:4]` starts at `"one"` and stops before `3`.
    """)
    return


@app.cell
def _():
    slice_tuple = (0, "one", "two", 3, 4, 5.5, 6)
    print(slice_tuple[1:4])
    return (slice_tuple,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[:3]` is the first three items.
    """)
    return


@app.cell
def _(slice_tuple):
    print(slice_tuple[:3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[4:]` starts at index 4 and continues through the end.
    """)
    return


@app.cell
def _(slice_tuple):
    print(slice_tuple[4:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tuple operations

    `len()` returns the number of items. An empty tuple has length 0.
    """)
    return


@app.cell
def _():
    length_empty = ()
    print(len(length_empty))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A one-item tuple has length 1.
    """)
    return


@app.cell
def _():
    length_one = (4,)
    print(len(length_one))
    return (length_one,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This record has 7 items.
    """)
    return


@app.cell
def _():
    length_record = (0, "one", "two", 3, 4, 5.5, 6)
    print(len(length_record))
    return (length_record,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `+` builds a new tuple and does not change the tuples you add.
    """)
    return


@app.cell
def _(length_one, length_record):
    combined = length_one + length_record
    print(combined)
    return (combined,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `in` asks whether a value is an item. `3` is in the record.
    """)
    return


@app.cell
def _(length_record):
    print(3 in length_record)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `10` is not in the record.
    """)
    return


@app.cell
def _(length_record):
    print(10 in length_record)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `count()` returns how many times a value appears. `4` appears twice in the concatenated tuple: once from the one-item tuple, and once from the record.
    """)
    return


@app.cell
def _(combined):
    print(combined.count(4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `index()` returns the first position of a value. The first `4` is at index 0.
    """)
    return


@app.cell
def _(combined):
    print(combined.index(4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `"one"` is at index 2.
    """)
    return


@app.cell
def _(combined):
    print(combined.index("one"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `index()` raises a `ValueError` when the value is absent, so the next cell raises that error on purpose.
    """)
    return


@app.cell
def _():
    # This cell raises ValueError on purpose.
    index_target = (4, 0, "one", "two", 3, 4, 5.5, 6)
    index_target.index("five")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Nested tuples

    A tuple may contain another tuple. The outer tuple below has three items: two strings, and one tuple.
    """)
    return


@app.cell
def _():
    inner = (4, 0, "one", "two", 3, 4, 5.5, 6)
    nested = ("123", "hello", inner)
    print(nested)
    return (nested,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The length is 3, not the length of the inner tuple.
    """)
    return


@app.cell
def _(nested):
    print(len(nested))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Item 0 is a string.
    """)
    return


@app.cell
def _(nested):
    print(type(nested[0]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Item 2 is the inner tuple.
    """)
    return


@app.cell
def _(nested):
    print(type(nested[2]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second index reads an item inside the inner tuple. Index 3 of the inner tuple is `"two"`.
    """)
    return


@app.cell
def _(nested):
    print(nested[2][3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `-1` still means the last item of the sequence you index. The last item of the inner tuple is `6`.
    """)
    return


@app.cell
def _(nested):
    print(nested[2][-1])
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
    ### Try it yourself

    Build a tuple that contains only the number `7`. Replace `None` with your code. Why is the comma required?
    """)
    return


@app.cell
def _():
    student_one = None
    print(student_one)
    return (student_one,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_one = (7,)
```
Without the comma, `(7)` is the integer `7`. The comma tells Python that the parentheses hold a tuple.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A tuple is an ordered, immutable sequence. Commas create it, and parentheses usually surround it.
    - Unpacking assigns each item to its own name: `x, y = point`.
    - A one-item tuple needs a trailing comma. `(4)` is an integer, not a tuple.
    - Indexes and slices follow the same rules as lists. You cannot assign to an index or call `append()`.
    - To add an item, convert to a list, change the list, and convert back with `tuple()`.
    - `count()` and `index()` search the items. A tuple may contain another tuple.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. How is a tuple different from a list?
    2. What is `(4)`?
    3. What does a trailing comma do in `(4,)`?
    4. Can you assign a new value to `record[0]`?
    5. How do you add an item to the data in a tuple?
    6. What does `index()` do when the value is absent?
    7. What is the length of `("123", "hello", (1, 2))`?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **A tuple cannot be changed:** Both are ordered. A list is mutable, and a tuple is immutable.
2. **The integer `4`:** Parentheses without a comma only group a value.
3. **It makes a one-item tuple:** The comma is what creates the tuple.
4. **No:** Replacing an item raises a `TypeError`.
5. **Convert it to a list:** Change the list, then convert it back with `tuple()`.
6. **It raises an error:** It does not return `-1`.
7. **`3`:** The inner tuple is one item of the outer tuple.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - [The Python Tutorial: Tuples and sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
