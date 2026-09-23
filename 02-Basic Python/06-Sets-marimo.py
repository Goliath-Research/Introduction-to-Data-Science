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

    - Create a set and tell an empty set apart from an empty dictionary.
    - Add and remove items, and see that a set keeps each value only once.
    - Test membership, and convert a list or a tuple into a set to drop duplicates.
    - Compute union, intersection, difference, and symmetric difference.

    ## Background

    A set is an unordered collection of unique items, written with curly brackets. Unordered means the items have no index: you cannot ask for "the first item." Unique means a value appears at most once. Sets are useful when you need to ask whether a value is present, or when you need to drop duplicates.

    ## Datasets Used

    This notebook does not use external datasets. The examples are small sets written in the code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating sets

    `set()` builds an empty set. `{}` does not: those brackets build an empty dictionary. A set with items is written as `{value, value, ...}`.

    You can add and remove items. You cannot change an item by index, because a set has no indexes. The printed order may differ from the order you wrote.
    """)
    return


@app.cell
def _():
    empty_set = set()
    print("empty set:", empty_set, "->", type(empty_set))

    numbers = {1, 2, 3}
    print("numbers:", numbers, "->", type(numbers))

    empty_braces = {}
    print("empty braces:", empty_braces, "->", type(empty_braces))
    return


@app.cell
def _():
    fruit = {"guava", "banana", "cherry"}
    print(fruit)
    print("banana" in fruit)
    print("mango" in fruit)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Adding and removing items

    `add()` inserts one item. `update()` inserts every item from another collection. Adding a value that is already present leaves the set unchanged. `len()` returns how many items the set holds.

    `remove()` deletes an item and raises an error if the item is absent. `discard()` deletes an item and does nothing if the item is absent. `clear()` removes every item. `del` deletes the name.
    """)
    return


@app.cell
def _():
    basket = {"guava", "banana", "cherry"}
    basket.add("mango")
    print("after add:", basket)

    basket.update(["orange", "grapes"])
    print("after update:", basket)

    basket.add("mango")
    print("mango was already present:", basket)
    print("length:", len(basket))

    basket.remove("banana")
    print("after remove banana:", basket)

    basket.discard("banana")
    print("discard of a missing item:", basket)

    basket.discard("mango")
    print("after discard mango:", basket)

    basket.clear()
    print("after clear:", basket)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Run the next cell to see the error from `remove()` when the item is not in the set.
    """)
    return


@app.cell
def _():
    remove_target = {"guava", "cherry"}
    remove_target.remove("banana")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Run the next cell to see the error from using a name after `del` deletes it.
    """)
    return


@app.cell
def _():
    deleted_name = {"guava", "cherry"}
    del deleted_name
    print(deleted_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sets drop duplicates

    A set may hold different types. Building a set from a list or a tuple keeps each value once, so the repeated `3` appears only once.
    """)
    return


@app.cell
def _():
    mixed = {"John", 20, True, 30.33, "male"}
    print(mixed, "->", type(mixed))

    number_list = [2, 3, 3, 4.0, "Peter"]
    print("from a list:", set(number_list))

    number_tuple = (2, 3, 3, 4.0, "Peter")
    print("from a tuple:", set(number_tuple))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A set cannot contain a mutable item such as a list or a dictionary. A tuple is allowed, because a tuple cannot change. Run the next cell to see the error from adding a list.
    """)
    return


@app.cell
def _():
    list_target = {"John", 20, True, 30.33, "male"}
    list_target.add([2, 3, 3, 4.0, "Peter"])
    return


@app.cell
def _():
    tuple_target = {"John", 20, True, 30.33, "male"}
    tuple_target.add((2, 3, 3, 4.0, "Peter"))
    print(tuple_target)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Set operations

    `union()` returns the items that appear in either set. `intersection()` returns the items that appear in both. `difference()` returns the items that appear in the first set and not in the second. `symmetric_difference()` returns the items that appear in one set but not in both.

    Union, intersection, and symmetric difference give the same items if you swap the two sets. Difference does not: `A - B` is not the same as `B - A`.

    The symmetric difference is the union minus the intersection.
    """)
    return


@app.cell
def _():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    union = set1.union(set2)
    print("union:", union)
    print("union swapped:", set2.union(set1))

    intersection = set1.intersection(set2)
    print("intersection:", intersection)
    print("intersection swapped:", set2.intersection(set1))

    print("set1 - set2:", set1.difference(set2))
    print("set2 - set1:", set2.difference(set1))

    print("symmetric:", set1.symmetric_difference(set2))
    print("symmetric swapped:", set2.symmetric_difference(set1))
    print("union minus intersection:", union.difference(intersection))
    print("same result with - :", union - intersection)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Add another city to `visited`, then print whether `"Paris"` is in the set.
    """)
    return


@app.cell
def _():
    visited = {"Lima", "Paris", "Lima", "Rome"}
    visited.add("Oslo")
    print(visited)
    print("Paris" in visited)
    print("length:", len(visited))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A set is an unordered collection of unique items. `set()` is an empty set. `{}` is an empty dictionary.
    - `add()` and `update()` insert items. A duplicate does not create a second copy.
    - `remove()` raises an error when the item is missing. `discard()` does not.
    - A set cannot hold a list. It can hold a tuple. `set()` applied to a list or tuple drops duplicates.
    - Union, intersection, difference, and symmetric difference combine two sets. Difference depends on which set comes first.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
