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

    `set()` builds an empty set. Its type is `set`.
    """)
    return


@app.cell
def _():
    empty_set = set()
    print(empty_set, "->", type(empty_set))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A set with items is written as `{value, value, ...}`. The printed order may differ from the order you wrote. For strings it can also differ between runs, because Python randomizes string hashes. That is why a set of words may not print in the order you typed.
    """)
    return


@app.cell
def _():
    numbers = {1, 2, 3}
    print(numbers, "->", type(numbers))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `{}` does not build an empty set. Those brackets build an empty dictionary.
    """)
    return


@app.cell
def _():
    empty_braces = {}
    print(empty_braces, "->", type(empty_braces))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `in` asks whether a value is in the set. `"banana"` is present.
    """)
    return


@app.cell
def _():
    fruit = {"guava", "banana", "cherry"}
    print("banana" in fruit)
    return (fruit,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `"mango"` is not present.
    """)
    return


@app.cell
def _(fruit):
    print("mango" in fruit)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Adding and removing items

    `add()` inserts one item. You cannot change an item by index, because a set has no indexes.
    """)
    return


@app.cell
def _():
    basket = {"guava", "banana", "cherry"}
    with_mango = basket.copy()
    with_mango.add("mango")
    print(with_mango)
    return (with_mango,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `update()` inserts every item from another collection.
    """)
    return


@app.cell
def _(with_mango):
    with_more = with_mango.copy()
    with_more.update(["orange", "grapes"])
    print(with_more)
    return (with_more,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Adding a value that is already present leaves the set unchanged.
    """)
    return


@app.cell
def _(with_more):
    still_once = with_more.copy()
    still_once.add("mango")
    print(still_once)
    return (still_once,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `len()` returns how many items the set holds.
    """)
    return


@app.cell
def _(still_once):
    print(len(still_once))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `remove()` deletes an item.
    """)
    return


@app.cell
def _(still_once):
    without_banana = still_once.copy()
    without_banana.remove("banana")
    print(without_banana)
    return (without_banana,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `discard()` deletes an item and does nothing if the item is absent. `"banana"` is already gone, so the set stays the same.
    """)
    return


@app.cell
def _(without_banana):
    after_discard = without_banana.copy()
    after_discard.discard("banana")
    print(after_discard)
    return (after_discard,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `discard("mango")` removes mango, because it is present.
    """)
    return


@app.cell
def _(after_discard):
    without_mango = after_discard.copy()
    without_mango.discard("mango")
    print(without_mango)
    return (without_mango,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `clear()` removes every item.
    """)
    return


@app.cell
def _(without_mango):
    cleared = without_mango.copy()
    cleared.clear()
    print(cleared)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `remove()` raises a `KeyError` if the item is absent, so the next cell raises that error on purpose.
    """)
    return


@app.cell
def _():
    # This cell raises KeyError on purpose.
    remove_target = {"guava", "cherry"}
    remove_target.remove("banana")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `del` deletes the name. The next cell uses that name afterward, so it raises a `NameError` on purpose.
    """)
    return


@app.cell
def _():
    # This cell raises NameError on purpose.
    deleted_name = {"guava", "cherry"}
    del deleted_name
    print(deleted_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sets drop duplicates

    A set may hold different types. This set includes `True`. In Python, `True == 1`, so `{1, True}` has a single item. There is no `1` here, so `True` stays.
    """)
    return


@app.cell
def _():
    mixed = {"John", 20, True, 30.33, "male"}
    print(mixed, "->", type(mixed))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `{1, True}` keeps one item, because `True` equals `1`.
    """)
    return


@app.cell
def _():
    print({1, True})
    print(len({1, True}))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Building a set from a list keeps each value once, so the repeated `3` appears only once.
    """)
    return


@app.cell
def _():
    number_list = [2, 3, 3, 4.0, "Peter"]
    print(set(number_list))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same conversion works for a tuple.
    """)
    return


@app.cell
def _():
    number_tuple = (2, 3, 3, 4.0, "Peter")
    print(set(number_tuple))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A set cannot contain an unhashable item such as a list or a dictionary, so the next cell raises a `TypeError` on purpose.
    """)
    return


@app.cell
def _():
    # This cell raises TypeError on purpose.
    list_target = {"John", 20, True, 30.33, "male"}
    list_target.add([2, 3, 3, 4.0, "Peter"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A tuple is allowed as long as everything inside it is hashable. A tuple of numbers and strings is fine. A tuple that contains a list, such as `(1, [2])`, is not.
    """)
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

    `union()` returns the items that appear in either set. The examples use `{1, 2, 3}` and `{3, 4, 5}`.
    """)
    return


@app.cell
def _():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union = set1.union(set2)
    print(union)
    return set1, set2, union


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Union gives the same items if you swap the two sets.
    """)
    return


@app.cell
def _(set1, set2):
    print(set2.union(set1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `intersection()` returns the items that appear in both. The only shared item is `3`.
    """)
    return


@app.cell
def _(set1, set2):
    intersection = set1.intersection(set2)
    print(intersection)
    return (intersection,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Swapping the sets does not change the intersection.
    """)
    return


@app.cell
def _(set1, set2):
    print(set2.intersection(set1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `difference()` returns the items that appear in the first set and not in the second. `set1 - set2` is `{1, 2}`.
    """)
    return


@app.cell
def _(set1, set2):
    print(set1.difference(set2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Difference depends on the order. `set2 - set1` is `{4, 5}`.
    """)
    return


@app.cell
def _(set1, set2):
    print(set2.difference(set1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `symmetric_difference()` returns the items that appear in one set but not in both.
    """)
    return


@app.cell
def _(set1, set2):
    print(set1.symmetric_difference(set2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Swapping the sets gives the same items.
    """)
    return


@app.cell
def _(set1, set2):
    print(set2.symmetric_difference(set1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The symmetric difference is the union minus the intersection.
    """)
    return


@app.cell
def _(intersection, union):
    print(union.difference(intersection))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The operator `-` is another way to write `difference()`.
    """)
    return


@app.cell
def _(intersection, union):
    print(union - intersection)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `|` is another way to write union. `&` is intersection. `^` is symmetric difference.
    """)
    return


@app.cell
def _(set1, set2):
    print(set1 | set2)
    print(set1 & set2)
    print(set1 ^ set2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `issubset()` asks whether every item of the first set is also in the second. `<=` is the same test.
    """)
    return


@app.cell
def _(set1):
    print({1, 2}.issubset(set1))
    print({1, 2} <= set1)
    print(set1 <= {1, 2})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next exercise lists `"Lima"` twice. A set keeps that city once.
    """)
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
    ### Try it yourself

    Build a set from `[1, 1, 2, 3, 3]` and store how many items it has. Replace each `None` with your code. Why is the length smaller than 5?
    """)
    return


@app.cell
def _():
    student_unique = None
    student_count = None
    print(student_unique)
    print(student_count)
    return student_count, student_unique


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_unique = set([1, 1, 2, 3, 3])
student_count = len(student_unique)
```
The length is `3`. A set keeps each value only once, so the repeated `1` and the repeated `3` do not create extra items.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A set is an unordered collection of unique items. `set()` is an empty set. `{}` is an empty dictionary.
    - `add()` and `update()` insert items. A duplicate does not create a second copy.
    - `remove()` raises an error when the item is missing. `discard()` does not.
    - A set cannot hold a list. It can hold a tuple when everything inside that tuple is hashable. `set()` applied to a list or tuple drops duplicates.
    - Union, intersection, difference, and symmetric difference combine two sets. `|`, `&`, `-`, and `^` are the operator forms. `<=` tests whether one set is a subset. Difference depends on which set comes first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What is the difference between `set()` and `{}`?
    2. Can you read a set item with an index?
    3. What happens when you add a value that is already in the set?
    4. How does `discard()` differ from `remove()` when the item is absent?
    5. What does `set([1, 1, 2])` contain?
    6. Can a set contain a list?
    7. Is `A.difference(B)` the same as `B.difference(A)`?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **A set and a dictionary:** `set()` is an empty set. `{}` is an empty dictionary.
2. **No:** A set is unordered, so it has no indexes.
3. **Nothing:** The set keeps that value only once.
4. **`discard()` does nothing:** `remove()` raises an error.
5. **`{1, 2}`:** The repeated `1` is dropped.
6. **No:** A list is unhashable. A tuple can be an item when everything inside it is hashable.
7. **No:** Difference keeps items from the first set only. The order matters.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - [The Python Tutorial: Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
    - [Set types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
