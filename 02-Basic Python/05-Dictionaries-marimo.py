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

    An empty dictionary is `{}`. A dictionary with data is written as `{key: value, ...}`. Keys must be hashable, which means they cannot change. Strings, numbers, and tuples are allowed as keys. Lists and dictionaries are not, because those can change.

    A dictionary keeps the order in which you insert the pairs. Keys are unique: assigning to a key that is already present replaces the value.
    """)
    return


@app.cell
def _():
    empty_dictionary = {}
    print("empty:", empty_dictionary, "->", type(empty_dictionary))

    student = {"name": "John", "last_name": "Doe", "age": 30}
    print(student)
    print("name:", student["name"])
    print("last_name:", student["last_name"])
    print("age:", student["age"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `get()` also reads a value by key. The second argument is returned when the key is absent, so a missing key does not raise an error. Square brackets raise an error when the key is absent.
    """)
    return


@app.cell
def _():
    lookup = {"name": "John", "last_name": "Doe", "age": 30}
    print(lookup.get("name", "Unknown"))
    print(lookup.get("middle_name", "Unknown"))
    print("name" in lookup)
    print("middle_name" in lookup)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Assign to a key to change its value, or to add a key that is not there yet.
    """)
    return


@app.cell
def _():
    updated_student = {"name": "John", "last_name": "Doe", "age": 30}
    updated_student["age"] = 33
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

    `len()` returns how many pairs the dictionary holds. `keys()`, `values()`, and `items()` return views of the keys, the values, and the pairs. Each pair from `items()` is a tuple of `(key, value)`.

    `update()` adds or replaces pairs from another dictionary. `pop(key)` removes that key and returns its value. `popitem()` removes and returns the last inserted pair.
    """)
    return


@app.cell
def _():
    methods_student = {"name": "John", "last_name": "Doe", "age": 33, "weight": 65}
    print("length:", len(methods_student))
    print("keys:", methods_student.keys())
    print("values:", methods_student.values())
    print("items:", methods_student.items())
    print()

    methods_student.update({"height": 5.8})
    print("after update:", methods_student)

    print("pop weight:", methods_student.pop("weight"))
    print("after pop:", methods_student)

    print("popitem:", methods_student.popitem())
    print("after popitem:", methods_student)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Copying a dictionary

    `alias = student` does not copy the dictionary. Both names refer to the same dictionary, so a change through one name is visible through the other. `dict()` and `copy()` each build a separate dictionary.
    """)
    return


@app.cell
def _():
    original = {"name": "John", "last_name": "Doe", "age": 33}
    alias = original
    alias["age"] = 40
    print("same dictionary:", original)

    separate = {"name": "John", "last_name": "Doe", "age": 33}
    copied = dict(separate)
    copied["age"] = 40
    print("original:", separate)
    print("dict() copy:", copied)

    other_copy = separate.copy()
    other_copy.clear()
    print("cleared copy:", other_copy)
    print("original is unchanged:", separate)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `del` removes one pair. `del` can also delete the name. Run the next cell to see the error from using a name after it has been deleted.
    """)
    return


@app.cell
def _():
    removable = {"name": "John", "last_name": "Doe", "age": 33}
    del removable["name"]
    print("after del name:", removable)

    del removable
    print(removable)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nested dictionaries

    A value may itself be a dictionary. The first key selects the inner dictionary. The second key selects a field inside it.
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
    ## Conclusions

    **Key takeaways:**

    - A dictionary stores key-value pairs. You read and write a value by its key, not by position.
    - Keys must be values that cannot change, such as strings, numbers, and tuples. Keys are unique.
    - `get()` can return a default when the key is missing. Square brackets raise an error instead.
    - `update()`, `pop()`, `popitem()`, and `del` change the pairs. `dict()` and `copy()` make a separate dictionary.
    - A value can be another dictionary. Use one key after another to reach an inner value.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
