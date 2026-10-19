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
    # Python Dictionaries

    ## Objectives

    - Create a dictionary of key-value pairs and read a value by its key.
    - Add, change, and remove pairs.
    - Use `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`, and `popitem()`.
    - Copy a dictionary, and read a value from a nested dictionary.

    ## Background

    A dictionary maps each key to one value. You retrieve a value by its key, not by a numeric position. That makes a dictionary a good fit for a record, such as a person's name and age, or for a group of records.

    ## Datasets Used

    This notebook does not use external datasets. The examples are small dictionaries written in the code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating dictionaries

    An empty dictionary is `{}`. Its type is `dict`.

    A dictionary with data is written as `{key: value, ...}`. Keys must be hashable, which means they cannot change. Strings, numbers, and tuples are allowed as keys. Lists and dictionaries are not, because those can change.

    A dictionary keeps the order in which you insert the pairs. Keys are unique: assigning to a key that is already present replaces the value.
    """)
    return


@app.cell
def _():
    empty_dictionary = {}
    print(empty_dictionary, "->", type(empty_dictionary))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This dictionary is a student record. Square brackets read a value by its key.
    """)
    return


@app.cell
def _():
    student = {"name": "John", "last_name": "Doe", "age": 30}
    print(student["name"])
    return (student,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same dictionary, read by the key `"age"`.
    """)
    return


@app.cell
def _(student):
    print(student["age"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `get()` also reads a value by key. `"name"` is present, so the default is not used.
    """)
    return


@app.cell
def _():
    lookup = {"name": "John", "last_name": "Doe", "age": 30}
    print(lookup.get("name", "Unknown"))
    return (lookup,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The second argument is returned when the key is absent. `"middle_name"` is not a key, so the result is `"Unknown"`.
    """)
    return


@app.cell
def _(lookup):
    print(lookup.get("middle_name", "Unknown"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `in` asks whether a key is present.
    """)
    return


@app.cell
def _(lookup):
    print("name" in lookup)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `"middle_name"` is not a key.
    """)
    return


@app.cell
def _(lookup):
    print("middle_name" in lookup)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Assign to a key to change its value. This copy starts from the same three pairs, then `"age"` becomes `33`.
    """)
    return


@app.cell
def _():
    aged = {"name": "John", "last_name": "Doe", "age": 30}
    aged["age"] = 33
    print(aged["age"])
    return (aged,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Assigning to a key that is not there yet adds a pair.
    """)
    return


@app.cell
def _(aged):
    updated_student = aged.copy()
    updated_student["weight"] = 65
    print(updated_student)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A dictionary is not a sequence of positions. A slice does not make sense, and it raises an error. Run the next cell to see that error.
    """)
    return


@app.cell
def _():
    slice_attempt = {"name": "John", "last_name": "Doe", "age": 30}
    slice_attempt["name":"last_name"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dictionary methods

    `len()` returns how many pairs the dictionary holds.
    """)
    return


@app.cell
def _():
    methods_student = {"name": "John", "last_name": "Doe", "age": 33, "weight": 65}
    print(len(methods_student))
    return (methods_student,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `keys()` returns a view of the keys.
    """)
    return


@app.cell
def _(methods_student):
    print(methods_student.keys())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `values()` returns a view of the values.
    """)
    return


@app.cell
def _(methods_student):
    print(methods_student.values())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `items()` returns the pairs. Each pair is a tuple of `(key, value)`.
    """)
    return


@app.cell
def _(methods_student):
    print(methods_student.items())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `update()` adds or replaces pairs from another dictionary.
    """)
    return


@app.cell
def _(methods_student):
    with_height = methods_student.copy()
    with_height.update({"height": 5.8})
    print(with_height)
    return (with_height,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `pop(key)` removes that key and returns its value.
    """)
    return


@app.cell
def _(with_height):
    without_weight = with_height.copy()
    print(without_weight.pop("weight"))
    return (without_weight,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `"weight"` is no longer a key.
    """)
    return


@app.cell
def _(without_weight):
    print(without_weight)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `popitem()` removes and returns the last inserted pair. After the update, that pair is the height.
    """)
    return


@app.cell
def _(without_weight):
    without_last = without_weight.copy()
    print(without_last.popitem())
    return (without_last,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The height pair is gone.
    """)
    return


@app.cell
def _(without_last):
    print(without_last)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Copying a dictionary

    `alias = original` does not copy the dictionary. Both names refer to the same dictionary, so a change through one name is visible through the other.
    """)
    return


@app.cell
def _():
    original = {"name": "John", "last_name": "Doe", "age": 33}
    alias = original
    alias["age"] = 40
    print(original)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `dict()` builds a separate dictionary. Changing the copy does not change the original.
    """)
    return


@app.cell
def _():
    separate = {"name": "John", "last_name": "Doe", "age": 33}
    copied = dict(separate)
    copied["age"] = 40
    print(separate)
    return separate, copied


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The copy has the new age.
    """)
    return


@app.cell
def _(copied):
    print(copied)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `copy()` also builds a separate dictionary. `clear()` removes every pair from that copy.
    """)
    return


@app.cell
def _(separate):
    other_copy = separate.copy()
    other_copy.clear()
    print(other_copy)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The original dictionary is unchanged.
    """)
    return


@app.cell
def _(separate):
    print(separate)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `del` removes one pair.
    """)
    return


@app.cell
def _():
    removable = {"name": "John", "last_name": "Doe", "age": 33}
    del removable["name"]
    print(removable)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `del` can also delete the name. Run the next cell to see the error from using a name after it has been deleted.
    """)
    return


@app.cell
def _():
    deleted_record = {"name": "John", "last_name": "Doe", "age": 33}
    del deleted_record
    print(deleted_record)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nested dictionaries

    A value may itself be a dictionary. The first key selects the inner dictionary.
    """)
    return


@app.cell
def _():
    child1 = {"name": "Hazel", "year": 2001, "gender": "F"}
    child2 = {"name": "Helen", "year": 2003, "gender": "F"}
    child3 = {"name": "Abel", "year": 2006, "gender": "M"}
    child4 = {"name": "Diana", "year": 2012, "gender": "F"}
    family = {
        "child1": child1,
        "child2": child2,
        "child3": child3,
        "child4": child4,
    }
    print(family["child4"])
    return (family,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The second key selects a field inside that dictionary.
    """)
    return


@app.cell
def _(family):
    print(family["child4"]["name"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Add a key to `practice` and print that value.
    """)
    return


@app.cell
def _():
    practice = {"city": "Austin", "year": 2024}
    practice["month"] = "September"
    print(practice["city"])
    print(practice.get("month", "Unknown"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Read a missing key with `get()`, using `"Unknown"` as the default. Replace `None` with your code. What does `get()` return, and does it raise an error?
    """)
    return


@app.cell
def _():
    student_missing = None
    print(student_missing)
    return (student_missing,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_missing = {"city": "Austin"}.get("country", "Unknown")
```
It returns `"Unknown"`. `get()` does not raise an error when the key is absent. Square brackets would raise a `KeyError`.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A dictionary stores key-value pairs. You read and write a value by its key, not by position.
    - Keys must be values that cannot change, such as strings, numbers, and tuples. Keys are unique.
    - `get()` can return a default when the key is missing. Square brackets raise an error instead.
    - `update()`, `pop()`, `popitem()`, and `del` change the pairs. `dict()` and `copy()` make a separate dictionary. A plain assignment does not.
    - A value can be another dictionary. Use one key after another to reach an inner value.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. How do you read a value from a dictionary?
    2. What happens if you assign to a key that is already present?
    3. What does `get("missing", "Unknown")` return when the key is absent?
    4. Can you slice a dictionary?
    5. What does `pop("weight")` return?
    6. What is the difference between `alias = original` and `original.copy()`?
    7. How do you read a field inside a nested dictionary?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **By its key:** `student["name"]` uses the key, not a numeric position.
2. **The value is replaced:** Keys are unique, so the old value is discarded.
3. **`"Unknown"`:** The second argument is the default. No error is raised.
4. **No:** A dictionary is not a sequence of positions. A slice raises an error.
5. **The removed value:** `pop` also deletes that pair.
6. **One dictionary or two:** A plain assignment shares the same dictionary. `copy()` builds a separate one.
7. **One key after another:** `family["child4"]["name"]` selects the inner dictionary, then the field.
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
