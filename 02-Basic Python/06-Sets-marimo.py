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
    # Python Sets

    ## Objectives

    - Create a set and test whether a value belongs to it.
    - Add and remove items, including the difference between `remove` and `discard`.
    - Combine sets with union, intersection, difference, and symmetric difference.

    ## Background

    A set is an unordered collection written with curly brackets. Items cannot be selected by index or key. A set does not keep duplicate values. You can add or remove items, but you cannot change an item in place.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating a set

    Printing a set may show the items in a different order. Use `in` to test membership.
    """)
    return


@app.cell
def _():
    fruit = {"apple", "banana", "cherry"}
    print(fruit)
    print(type(fruit))
    print("banana" in fruit)
    print("mango" in fruit)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Create a set of three colors and check whether `"blue"` is in it.
    """)
    return


@app.cell
def _():
    your_colors = {"red", "green", "blue"}
    print("blue" in your_colors)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Adding and removing items

    `add` inserts one item. `update` inserts several. Adding a value that is already present leaves the set unchanged. `remove` raises `KeyError` when the item is missing. `discard` does not. `clear` empties the set, and `del` deletes the name.
    """)
    return


@app.cell
def _():
    basket = {"apple", "banana", "cherry"}
    basket.add("mango")
    basket.update(["orange", "grapes"])
    print("after update:", basket)

    basket.add("mango")
    print("mango added again:", basket)
    print("length:", len(basket))

    basket.remove("banana")
    print("after remove:", basket)

    try:
        basket.remove("banana")
    except KeyError as error:
        print("KeyError:", error)

    basket.discard("banana")
    basket.discard("mango")
    print("after discard:", basket)

    basket.clear()
    print("cleared:", basket)
    return


@app.cell
def _():
    temporary_fruit = {"orange", "banana", "grapes"}
    del temporary_fruit

    try:
        print(temporary_fruit)
    except NameError as missing_name:
        print("NameError:", missing_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A set can hold values of different types.
    """)
    return


@app.cell
def _():
    mixed_set = {"John", 20, True, 30.33, "male"}
    print(mixed_set)
    print(type(mixed_set))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Set operations

    - **union**: items that belong to either set
    - **intersection**: items that belong to both sets
    - **difference**: items in the first set that are not in the second
    - **symmetric difference**: items that belong to one set but not both
    """)
    return


@app.cell
def _():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    print("union:", set1.union(set2))
    print("intersection:", set1.intersection(set2))
    print("difference:", set1.difference(set2))
    print("symmetric difference:", set1.symmetric_difference(set2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the two sets, then print their intersection and their difference.
    """)
    return


@app.cell
def _():
    left_set = {"a", "b", "c"}
    right_set = {"b", "c", "d"}

    print(left_set.intersection(right_set))
    print(left_set.difference(right_set))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A set is unordered, does not allow duplicates, and is written with `{}`.
    - `add` and `update` insert items. Adding an existing item does not create a duplicate.
    - `remove` raises an error for a missing item. `discard` does not.
    - Union, intersection, difference, and symmetric difference compare two sets.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
