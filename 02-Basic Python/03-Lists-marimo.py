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

    An empty list is `[]`. Its type is `list`.
    """)
    return


@app.cell
def _():
    empty_list = []
    print(empty_list, "->", type(empty_list))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A list of numbers. The first item is at index `0`.
    """)
    return


@app.cell
def _():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers[0], "->", type(numbers[0]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same value may appear more than once.
    """)
    return


@app.cell
def _():
    repeated_numbers = [0, 1, 2, 2, 2, 2]
    print(repeated_numbers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `str()` turns one number into text. A later lesson, List Comprehension, shows how to build a whole new list by applying `str()` to every item. This lesson writes those text values directly, because that lesson has not been introduced yet.

    The first item looks like a number, but it is a string.
    """)
    return


@app.cell
def _():
    number_text = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(number_text[0], "->", type(number_text[0]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A list can hold items of different types, including another list. Item 3 is itself a list.
    """)
    return


@app.cell
def _():
    mixed_list = [0, 1, 2, ["a", "b", "c"], 3, 4]
    print(mixed_list[3], "->", type(mixed_list[3]))
    return (mixed_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second index reads one item of that nested list.
    """)
    return


@app.cell
def _(mixed_list):
    print(mixed_list[3][0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These four items have four types: `bool`, `str`, `float`, and `int`. This is the boolean.
    """)
    return


@app.cell
def _():
    mixed_values = [True, "2", 3.3, 4]
    print(mixed_values[0], "->", type(mixed_values[0]))
    return (mixed_values,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The second item is text.
    """)
    return


@app.cell
def _(mixed_values):
    print(mixed_values[1], "->", type(mixed_values[1]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The third item is a float.
    """)
    return


@app.cell
def _(mixed_values):
    print(mixed_values[2], "->", type(mixed_values[2]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The fourth item is an integer.
    """)
    return


@app.cell
def _(mixed_values):
    print(mixed_values[3], "->", type(mixed_values[3]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Indexing and slicing

    The first index is `0`. A slice `list[start:stop]` includes the item at `start` and stops before `stop`.

    `values[:2]` is the first two items.
    """)
    return


@app.cell
def _():
    values = [True, "2", 3.3, 4]
    print(values[:2])
    return (values,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Omit the stop to continue through the last item. `values[2:]` starts at index 2.
    """)
    return


@app.cell
def _(values):
    print(values[2:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Negative indexes

    A negative index counts from the end. `-1` is the last item.

    | | **True** | **"2"** | **3.3** | **4** |
    |---|---:|---:|---:|---:|
    | index | 0 | 1 | 2 | 3 |
    | negative index | -4 | -3 | -2 | -1 |
    """)
    return


@app.cell
def _():
    indexed_values = [True, "2", 3.3, 4]
    print(indexed_values[-1])
    return (indexed_values,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `-2` is the item before the last.
    """)
    return


@app.cell
def _(indexed_values):
    print(indexed_values[-2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `[-3:]` starts three items from the end and continues through the last item.
    """)
    return


@app.cell
def _(indexed_values):
    print(indexed_values[-3:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An index must refer to an item that exists. The next cell uses an index past the end of the list, so it raises an `IndexError` on purpose.
    """)
    return


@app.cell
def _():
    # This cell raises IndexError on purpose.
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
    ### Try it yourself

    From `["red", "green", "blue", "yellow"]`, take the last two items with a slice. Replace `None` with your code. Which index is excluded?
    """)
    return


@app.cell
def _():
    student_colors = None
    print(student_colors)
    return (student_colors,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_colors = ["red", "green", "blue", "yellow"][-2:]
```
The stop is omitted, so nothing at the end is excluded. The slice starts at index `-2`, which is `"blue"`. `["red", "green", "blue", "yellow"][2:4]` gives the same two items, and index `4` is excluded because it is past the end.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## List methods

    Most list methods (`append`, `insert`, `remove`, `pop`, `reverse`, `sort`) change the list in place. `count()` only reads it. `len()` is not a list method. It works on any collection, including lists, strings, tuples, dictionaries, and sets. Here it returns how many items the list holds.
    """)
    return


@app.cell
def _():
    items = [0, 1, 2, ["a", "b", "c"], 3, 4]
    print(len(items))
    return (items,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `count()` returns how many times a value appears. `5` is not in the list yet.
    """)
    return


@app.cell
def _(items):
    print(items.count(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `append()` adds one item at the end.

    Each step below copies the list and uses a new name. Marimo does not allow two cells to define the same name, so this lesson cannot call `append` on `items` in a later cell and still show the earlier list. `.copy()` gives each step its own list. You do not need `.copy()` before every `append` in an ordinary Python script. There, `items.append(5)` changes `items` itself.
    """)
    return


@app.cell
def _(items):
    items_appended = items.copy()
    items_appended.append(5)
    print(items_appended)
    return (items_appended,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `5` now appears once.
    """)
    return


@app.cell
def _(items_appended):
    print(items_appended.count(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `remove()` deletes the first matching value.
    """)
    return


@app.cell
def _(items_appended):
    items_removed = items_appended.copy()
    items_removed.remove(5)
    print(items_removed)
    return (items_removed,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `insert()` places an item at an index and shifts the later items right. `"five"` is placed at index 3.
    """)
    return


@app.cell
def _(items_removed):
    items_inserted = items_removed.copy()
    items_inserted.insert(3, "five")
    print(items_inserted)
    return (items_inserted,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `pop(4)` removes the item at index 4 and returns that item. After the insert, index 4 is the nested list.
    """)
    return


@app.cell
def _(items_inserted):
    items_popped = items_inserted.copy()
    removed_list = items_popped.pop(4)
    print(removed_list)
    return (items_popped,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The nested list is no longer in the list.
    """)
    return


@app.cell
def _(items_popped):
    print(items_popped)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `reverse()` reverses the order.
    """)
    return


@app.cell
def _(items_popped):
    items_reversed = items_popped.copy()
    items_reversed.reverse()
    print(items_reversed)
    return (items_reversed,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Index 2 of the reversed list is the text `"five"`. `sort()` cannot order text and numbers together, so that item is removed first. `pop()` returns the removed item.
    """)
    return


@app.cell
def _(items_reversed):
    items_numbers = items_reversed.copy()
    removed_text = items_numbers.pop(2)
    print(removed_text)
    return (items_numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sort()` orders the remaining numbers from smallest to largest.
    """)
    return


@app.cell
def _(items_numbers):
    items_sorted = items_numbers.copy()
    items_sorted.sort()
    print(items_sorted)
    return (items_sorted,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sort(reverse=True)` orders them from largest to smallest.
    """)
    return


@app.cell
def _(items_sorted):
    items_descending = items_sorted.copy()
    items_descending.sort(reverse=True)
    print(items_descending)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### More ways to change a list

    You can replace the item at an index. That is the main way a list is mutable. This cell starts from a copy so the earlier list stays as it was.
    """)
    return


@app.cell
def _(indexed_values):
    replaced_values = indexed_values.copy()
    replaced_values[0] = False
    print(replaced_values)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `in` asks whether a value is an item. `index()` returns the first position of a value.
    """)
    return


@app.cell
def _():
    tools = ["pen", "pencil", "pen"]
    print("pencil" in tools)
    print(tools.index("pen"))
    return (tools,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `extend()` adds every item from another list. It changes the list. `del` removes the item at an index and does not return that item. `pop()` removes an item and returns it.
    """)
    return


@app.cell
def _(tools):
    tools_extended = tools.copy()
    tools_extended.extend(["eraser", "ruler"])
    del tools_extended[1]
    print(tools_extended)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sorted()` returns a new list and leaves the original in place. `sort()` changes the list and returns `None`. Saving that return value is a common mistake: the name then refers to `None`, not to the sorted list.
    """)
    return


@app.cell
def _():
    sort_source = [3, 1, 2]
    print(sorted(sort_source))
    print(sort_source)
    sort_result = sort_source.copy()
    print(sort_result.sort())
    print(sort_result)
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The two lists do not have to hold the same types.
    """)
    return


@app.cell
def _():
    words = ["0", "1", "2"]
    other = [True, "2", 3.3, 4]
    print(words + other)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lists as stacks

    A stack adds and removes items at the same end. The last item added is the first item removed. That order is called last in, first out (LIFO). `append()` adds to the end.
    """)
    return


@app.cell
def _():
    stack = [2, 3, 4]
    stack_pushed = stack.copy()
    stack_pushed.append(5)
    print(stack_pushed)
    return (stack_pushed,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `pop()` with no index removes the last item and returns it.
    """)
    return


@app.cell
def _(stack_pushed):
    stack_once = stack_pushed.copy()
    print(stack_once.pop())
    return (stack_once,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second `pop()` removes the new last item.
    """)
    return


@app.cell
def _(stack_once):
    stack_twice = stack_once.copy()
    print(stack_twice.pop())
    return (stack_twice,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Two items remain. They were the first two items of the original stack.
    """)
    return


@app.cell
def _(stack_twice):
    print(stack_twice)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lists as queues

    A queue adds items at the back and removes items from the front. The first item added is the first item removed. That order is called first in, first out (FIFO). `append()` adds Peter at the back.
    """)
    return


@app.cell
def _():
    queue = ["John", "Mary", "Anna"]
    queue_with_peter = queue.copy()
    queue_with_peter.append("Peter")
    print(queue_with_peter)
    return (queue_with_peter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `pop(0)` removes the front item. You must pass `0`. A `pop()` with no index would remove the last item instead.
    """)
    return


@app.cell
def _(queue_with_peter):
    queue_after_john = queue_with_peter.copy()
    print(queue_after_john.pop(0))
    return (queue_after_john,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    John has left. Mary is now at the front.
    """)
    return


@app.cell
def _(queue_after_john):
    print(queue_after_john)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next `pop(0)` removes Mary.
    """)
    return


@app.cell
def _(queue_after_john):
    queue_after_mary = queue_after_john.copy()
    print(queue_after_mary.pop(0))
    return (queue_after_mary,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Anna and Peter remain, in that order.
    """)
    return


@app.cell
def _(queue_after_mary):
    print(queue_after_mary)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `append()` at the end of a list is fast. `pop(0)` is slow, because every remaining item has to shift one position left. `collections.deque` is a sequence made for fast adds and removals at both ends. `append()` still adds at the back.
    """)
    return


@app.cell
def _():
    from collections import deque

    waiting = deque(["John", "Mary", "Anna"])
    waiting.append("Peter")
    print(waiting)
    return (deque, waiting)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `popleft()` removes the front item without shifting every remaining item.
    """)
    return


@app.cell
def _(deque, waiting):
    waiting_after = deque(waiting)
    print(waiting_after.popleft())
    return (waiting_after,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The remaining people stay in the order they arrived.
    """)
    return


@app.cell
def _(waiting_after):
    print(waiting_after)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A list is an ordered, mutable sequence written with square brackets.
    - Indexes start at 0. Negative indexes start at the last item. A slice includes the start and excludes the stop.
    - `append`, `insert`, `remove`, `pop`, `extend`, `reverse`, and `sort` change the list. `sort()` returns `None`. `sorted()` returns a new list. `+` builds a new list.
    - You can replace the item at an index. `in` tests membership, and `index()` returns the first position.
    - `append` and `pop` use a list as a stack. `append` and `pop(0)` use a list as a queue. `deque.popleft()` removes the front item without shifting every remaining item.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What does mutable mean for a list?
    2. Which index is the first item?
    3. What does `items[:2]` include?
    4. Which item does `-1` select?
    5. What does `append()` change?
    6. What does `pop()` return?
    7. Why is `pop(0)` slower than `deque.popleft()`?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **It can change:** You can add, remove, and replace items after the list is created.
2. **`0`:** Positions start at the beginning.
3. **The first two items:** The slice includes the start and stops before index 2.
4. **The last item:** Negative indexes count from the end.
5. **The same list:** It adds one item at the end. It does not build a new list.
6. **The removed item:** With no index, that item is the last one.
7. **The remaining items must shift:** `pop(0)` moves every later item one place left. `popleft()` does not.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - [The Python Tutorial: Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
    - [Data structures: more on lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
