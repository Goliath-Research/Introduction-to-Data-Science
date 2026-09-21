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

    - Store and read values with keys.
    - Add, update, and remove key-value pairs.
    - Copy a dictionary so the copy is independent.
    - Nest dictionaries inside another dictionary.

    ## Background

    A dictionary is an ordered, changeable collection of key-value pairs. Each key maps to one value. Dictionaries do not allow duplicate keys, and they are read by key rather than by position.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating and reading dictionaries

    An empty dictionary is `{}`. Read a value with `dictionary[key]` or `dictionary.get(key)`.
    """)
    return


@app.cell
def _():
    empty_dictionary = {}
    print(type(empty_dictionary))

    student = {"name": "John", "last_name": "Doe", "age": 30}
    print(student)
    print(student["name"])
    print(student.get("name"))

    student["age"] = 33
    print(student)
    print("name" in student)
    print("middle_name" in student)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Slicing uses positions. A dictionary is organized by keys, so a slice raises `TypeError`.
    """)
    return


@app.cell
def _():
    record = {"name": "John", "last_name": "Doe", "age": 33}

    try:
        print(record["name":"last_name"])
    except KeyError as error:
        print("KeyError:", error)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the keys and values, then print one value and check whether another key exists.
    """)
    return


@app.cell
def _():
    your_profile = {"name": "Ana", "city": "Madrid"}

    print(your_profile["name"])
    print("city" in your_profile)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dictionary methods

    Add a pair by assigning a new key. `update` adds or replaces pairs. `items`, `keys`, and `values` show the contents. `pop` removes a named key. `popitem` removes the last inserted pair.
    """)
    return


@app.cell
def _():
    profile = {"name": "John", "last_name": "Doe", "age": 33}
    print("length:", len(profile))

    profile["weight"] = 65
    profile.update({"height": 5.8})
    print(profile)
    print("items:", list(profile.items()))
    print("keys:", list(profile.keys()))
    print("values:", list(profile.values()))

    profile.pop("weight")
    print("after pop:", profile)
    print("popitem removed:", profile.popitem())
    print("remaining:", profile)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Copying and deleting

    `alias = original` makes both names refer to the same dictionary. `dict(original)` and `copy()` make a separate dictionary. `clear` empties a dictionary. `del` can remove one key or the whole dictionary.
    """)
    return


@app.cell
def _():
    person = {"last_name": "Doe", "age": 33}
    copied = dict(person)
    copied_again = person.copy()
    print("copy:", copied_again)

    copied_again.clear()
    print("cleared copy:", copied_again)
    print("original:", person)

    del person["last_name"]
    print("after del key:", person)

    removed = person
    del removed
    try:
        print(removed)
    except NameError as missing_name:
        print("NameError:", missing_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Copy `scores`, add a new subject, and print both dictionaries. The original should stay unchanged.
    """)
    return


@app.cell
def _():
    scores = {"math": 90, "history": 85}
    scores_copy = scores.copy()
    scores_copy["science"] = 88

    print("original:", scores)
    print("copy:", scores_copy)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nested dictionaries

    A value may itself be a dictionary. The outer keys select a record, and the inner keys select a field.
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
    print(family["child1"])
    print(family["child3"]["name"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A dictionary maps each key to one value.
    - Read values with `dictionary[key]` or `get`. Test keys with `in`.
    - Assign a new key to add a pair. `pop` and `del` remove pairs.
    - Copy with `copy()` or `dict()` when the new dictionary must be independent.
    - Dictionaries can contain other dictionaries.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
