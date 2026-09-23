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
    # Python Lists

    ## Objectives

    - Create a list, including an empty list, a list with repeated values, and a list that mixes types.
    - Read one item or a slice with positive indexes and with negative indexes.
    - Add, remove, reverse, and sort items with list methods.
    - Use a list as a stack and as a queue.

    ## Background

    A list is a mutable, ordered sequence. Mutable means the list can change after you create it: you can add, remove, and replace items. Ordered means each item has a position, and that position stays put until you change the list. Each value in the list is an item. Lists are written with square brackets `[]`.

    ## Datasets Used

    This notebook does not use external datasets. The examples are short lists written in the code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating lists

    An empty list is `[]`. A list may hold numbers, text, and other values, and the same value may appear more than once.
    """)
    return


@app.cell
def _():
    empty_list = []
    print("empty:", empty_list, "->", type(empty_list))

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("numbers:", numbers, "->", type(numbers))
    print("first item:", numbers[0], "->", type(numbers[0]))
    print()

    # The same value may appear more than once.
    repeated_numbers = [0, 1, 2, 2, 2, 2]
    print("duplicates:", repeated_numbers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `str()` turns one number into text. A later lesson, List Comprehension, shows how to build a whole new list by applying `str()` to every item. This lesson writes those text values directly, because that lesson has not been introduced yet.
    """)
    return


@app.cell
def _():
    number_text = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(number_text)
    print("first item:", number_text[0], "->", type(number_text[0]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A list can hold items of different types, including another list. Because a variable can refer to any type, the items do not have to match.
    """)
    return


@app.cell
def _():
    mixed_list = [0, 1, 2, ["a", "b", "c"], 3, 4]
    print(mixed_list)
    print("item 0:", mixed_list[0], "->", type(mixed_list[0]))
    print("item 3:", mixed_list[3], "->", type(mixed_list[3]))
    # mixed_list[3] is itself a list, so a second index reads one of its items.
    print("item 3, then item 0:", mixed_list[3][0])
    print()

    mixed_values = [True, "2", 3.3, 4]
    print(mixed_values)
    print("item 0:", mixed_values[0], "->", type(mixed_values[0]))
    print("item 1:", mixed_values[1], "->", type(mixed_values[1]))
    print("item 2:", mixed_values[2], "->", type(mixed_values[2]))
    print("item 3:", mixed_values[3], "->", type(mixed_values[3]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Indexing and slicing

    The first index is `0`. A slice `list[start:stop]` includes the item at `start` and stops before `stop`. Omit `start` to begin at the first item. Omit `stop` to continue through the last item.
    """)
    return


@app.cell
def _():
    values = [True, "2", 3.3, 4]
    print("list:", values)
    print("first two:", values[:2])
    print("from index 2:", values[2:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Negative indexes

    A negative index counts from the end. `-1` is the last item, and `-2` is the item before that.

    | | **True** | **"2"** | **3.3** | **4** |
    |---|---:|---:|---:|---:|
    | index | 0 | 1 | 2 | 3 |
    | negative index | -4 | -3 | -2 | -1 |
    """)
    return


@app.cell
def _():
    indexed_values = [True, "2", 3.3, 4]
    print("last item:", indexed_values[-1])
    print("item before the last:", indexed_values[-2])
    print("last three:", indexed_values[-3:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An index must refer to an item that exists. Run the next cell to see the error raised by an index past the end of the list.
    """)
    return


@app.cell
def _():
    short_list = [True, "2", 3.3, 4]
    short_list[10]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `practice_list` and the indexes, then run the cell. Predict the printed items before you run it.
    """)
    return


@app.cell
def _():
    practice_list = ["red", "green", "blue", "yellow"]
    print(practice_list[0])
    print(practice_list[-1])
    print(practice_list[1:3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## List methods

    These methods change the list they are called on. `len()` is not a list method: it works on any sequence and returns how many items the list holds.

    `append()` adds one item at the end. `count()` returns how many times a value appears. `remove()` deletes the first matching value. `insert()` places an item at an index and shifts the later items right. `pop()` removes the item at an index and returns that item. `reverse()` reverses the order. `sort()` orders the items.
    """)
    return


@app.cell
def _():
    items = [0, 1, 2, ["a", "b", "c"], 3, 4]
    print("length:", len(items))
    print("count of 5:", items.count(5))

    items.append(5)
    print("after append 5:", items)
    print("count of 5:", items.count(5))

    items.remove(5)
    print("after remove 5:", items)

    items.insert(3, "five")
    print("after insert:", items)

    # pop(4) removes the nested list, which is now at index 4.
    removed_list = items.pop(4)
    print("pop(4) removed", removed_list)
    print("list is now:", items)

    items.reverse()
    print("after reverse:", items)

    # Index 2 is the text "five". sort() cannot order text and numbers together.
    removed_text = items.pop(2)
    print("pop(2) removed", repr(removed_text))
    print("list is now:", items)

    items.sort()
    print("after sort:", items)

    items.sort(reverse=True)
    print("after sort(reverse=True):", items)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `+` builds a new list from two lists. It does not change either original list.
    """)
    return


@app.cell
def _():
    left = [4, 3, 2, 1, 0]
    right = [0, 1, 2, 2, 2, 2]
    print(left + right)

    words = ["0", "1", "2"]
    other = [True, "2", 3.3, 4]
    print(words + other)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lists as stacks

    A stack adds and removes items at the same end. The last item added is the first item removed. That order is called last in, first out (LIFO). `append()` adds to the end, and `pop()` with no index removes from the end.
    """)
    return


@app.cell
def _():
    stack = [2, 3, 4]
    stack.append(5)
    print("after append 5:", stack)

    print("pop:", stack.pop())
    print("pop:", stack.pop())
    print("stack is now:", stack)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lists as queues

    A queue adds items at the back and removes items from the front. The first item added is the first item removed. That order is called first in, first out (FIFO). `pop(0)` removes the front item. You must pass `0`. A `pop()` with no index would remove the last item instead.
    """)
    return


@app.cell
def _():
    queue = ["John", "Mary", "Anna"]
    queue.append("Peter")
    print("after append:", queue)

    person = queue.pop(0)
    print("left the queue:", person)
    print("queue is now:", queue)

    person = queue.pop(0)
    print("left the queue:", person)
    print("queue is now:", queue)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `append()` at the end of a list is fast. `pop(0)` is slow, because every remaining item has to shift one position left. `collections.deque` is a sequence made for fast adds and removals at both ends. `popleft()` removes the front item.
    """)
    return


@app.cell
def _():
    from collections import deque

    waiting = deque(["John", "Mary", "Anna"])
    waiting.append("Peter")
    print("after append:", waiting)

    next_person = waiting.popleft()
    print("left the queue:", next_person)
    print("queue is now:", waiting)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A list is an ordered, mutable sequence written with square brackets.
    - Indexes start at 0. Negative indexes start at the last item. A slice includes the start and excludes the stop.
    - `append`, `insert`, `remove`, `pop`, `reverse`, and `sort` change the list. `+` builds a new list.
    - `append` and `pop` use a list as a stack. `append` and `pop(0)` use a list as a queue. `deque.popleft()` removes the front item without shifting every remaining item.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
