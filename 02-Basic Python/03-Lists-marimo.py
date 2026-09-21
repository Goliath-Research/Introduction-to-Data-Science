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

    - Create ordered lists, including lists with repeated or mixed values.
    - Read items with positive indexes, slices, and negative indexes.
    - Add, remove, reverse, and sort items with list methods.
    - Use a list as a stack and as a queue.

    ## Background

    A list is a mutable, ordered sequence. Each value in the list is an item. Lists are written with square brackets.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating lists

    An empty list is `[]`. A list may contain numbers, strings, and other types in the same sequence. Repeated values are allowed.
    """)
    return


@app.cell
def _():
    empty_list = []
    print("empty:", empty_list)

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers)
    print(type(numbers))
    print(type(numbers[0]))

    repeated_numbers = [0, 1, 2, 2, 2, 2]
    print("duplicates:", repeated_numbers)

    number_text = [str(item) for item in numbers]
    print(number_text)
    print(type(number_text), type(number_text[0]))

    mixed_values = [True, "2", 3.3, 4]
    print(mixed_values)
    print([type(item) for item in mixed_values])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Indexing and slicing

    `list[0]` is the first item. A slice such as `list[:2]` includes the start and excludes the stop. Negative indexes count from the end: `-1` is the last item.
    """)
    return


@app.cell
def _():
    indexed_values = [True, "2", 3.3, 4]

    print("first two:", indexed_values[:2])
    print("from index 2:", indexed_values[2:])
    print("last:", indexed_values[-1])
    print("second last:", indexed_values[-2])
    print("last three:", indexed_values[-3:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An index past the end of the list raises `IndexError`.
    """)
    return


@app.cell
def _():
    bounded_values = [True, "2", 3.3, 4]

    try:
        print(bounded_values[10])
    except IndexError as error:
        print("IndexError:", error)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Replace the items, then print the first item, the last item, and a slice.
    """)
    return


@app.cell
def _():
    your_items = ["red", "green", "blue"]

    print(your_items[0])
    print(your_items[-1])
    print(your_items[:2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## List methods

    These methods change the list itself. This sequence is kept in one cell so you can follow each change.
    """)
    return


@app.cell
def _():
    samples = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("length:", len(samples))
    print("count of 5:", samples.count(5))

    samples.append(5)
    print("after append:", samples)
    print("count of 5:", samples.count(5))

    samples.remove(5)
    print("after remove:", samples)

    samples.insert(3, "five")
    print("after insert:", samples)

    samples.pop(3)
    print("after pop:", samples)

    samples.reverse()
    print("after reverse:", samples)

    samples.sort()
    print("after sort:", samples)

    samples.sort(reverse=True)
    print("after reverse sort:", samples)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Start with the list below. Append one item, insert one item at index 1, then print the list.
    """)
    return


@app.cell
def _():
    practice_list = ["a", "b", "c"]

    practice_list.append("d")
    practice_list.insert(1, "aa")
    print(practice_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lists as stacks

    A stack is last in, first out. `append` puts an item on top. `pop()` removes that same item.
    """)
    return


@app.cell
def _():
    stack = [2, 3, 4]
    stack.append(5)
    print("after append:", stack)

    print("popped:", stack.pop())
    print("popped:", stack.pop())
    print("remaining:", stack)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lists as queues

    A queue is first in, first out. `append` adds to the end. `pop(0)` removes the first item.
    """)
    return


@app.cell
def _():
    queue = ["John", "Mary", "Anna"]
    queue.append("Peter")
    print("after append:", queue)

    print("left:", queue.pop(0))
    print("left:", queue.pop(0))
    print("remaining:", queue)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Add one name to the queue, then remove the person who has been waiting the longest.
    """)
    return


@app.cell
def _():
    your_queue = ["Luis", "Mei"]

    your_queue.append("Sofia")
    print("next:", your_queue.pop(0))
    print("still waiting:", your_queue)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - A list is an ordered, mutable sequence written with `[]`.
    - Indexes start at 0. Negative indexes start at the last item.
    - `append`, `insert`, `remove`, `pop`, `reverse`, and `sort` change the list.
    - `append` plus `pop()` models a stack. `append` plus `pop(0)` models a queue.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
