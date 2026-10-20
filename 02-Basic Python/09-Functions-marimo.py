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
    # Python Functions

    ## Objectives

    - Define a function and call it by name.
    - Pass values as positional arguments, keyword arguments, `*args`, and `**kwargs`.
    - Give a parameter a default value, pass a list, and return one or more values.
    - Write a function that calls itself.

    ## Background

    A function is a named block of code that runs when you call it. You can pass data in through parameters and send a result back with `return`. A function lets you write a task once and use it in more than one place.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Defining and calling

    `def` starts a function. The indented lines are the body. They do not run at `def`. They run when you call the function: the name, followed by parentheses.
    """)
    return


@app.cell
def _():
    def first_function():
        print("Hello world!")

    first_function()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A parameter is a name in the parentheses. A call must pass one value for each parameter, unless that parameter has a default. The value you pass is an argument.
    """)
    return


@app.cell
def _():
    def hello(name):
        print("Hello", name)

    hello("John")
    return (hello,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same function works with a different argument.
    """)
    return


@app.cell
def _(hello):
    hello("Mary")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Passing too many arguments raises a `TypeError`. `hello` has one parameter, so the next cell raises that error on purpose.
    """)
    return


@app.cell
def _(hello):
    # This cell raises TypeError on purpose.
    hello("Mary", "John")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ways to pass arguments

    `*kids` collects any number of positional arguments into a tuple. The function below treats the first item as the youngest, so the caller must pass the names in that order. `*args` is the name often used for this pattern in documentation.
    """)
    return


@app.cell
def _():
    def youngest_of(*kids):
        print("The youngest child is", kids[0])

    youngest_of("John", "Mary", "Anna")
    return (youngest_of,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Extra arguments are still collected. The first one is still the value the function prints.
    """)
    return


@app.cell
def _(youngest_of):
    youngest_of("John", "Mary", "Anna", "Raul")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The order matters. Passing `"Anna"` first makes Anna the youngest in this call.
    """)
    return


@app.cell
def _(youngest_of):
    youngest_of("Anna", "John", "Mary", "Raul")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A typical `*args` function adds every number the caller passes. The order does not change the result.
    """)
    return


@app.cell
def _():
    def add_all(*numbers):
        return sum(numbers)

    print(add_all(1, 2, 3, 4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Keyword arguments use `name=value`. The order of those arguments does not matter, and they must come after positional arguments. This function prints the parameter named `child1`.
    """)
    return


@app.cell
def _():
    def youngest_by_name(child3, child2, child1):
        print("The youngest child is", child1)

    youngest_by_name(child1="John", child2="Mary", child3="Anna")
    return (youngest_by_name,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same names in a different order still print John, because each value is tied to a parameter name.
    """)
    return


@app.cell
def _(youngest_by_name):
    youngest_by_name(child2="Mary", child3="Anna", child1="John")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `**named_kids` collects keyword arguments into a dictionary. `**kwargs` is the usual name for that pattern. The function reads the key `"child1"`.
    """)
    return


@app.cell
def _():
    def youngest_from_keywords(**named_kids):
        print("The youngest child is", named_kids["child1"])

    youngest_from_keywords(child1="Mary", child3="Anna")
    return (youngest_from_keywords,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    More keyword arguments can be passed. The function still reads `"child1"`.
    """)
    return


@app.cell
def _(youngest_from_keywords):
    youngest_from_keywords(child2="Mary", child3="Anna", child1="John")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A default value is used when the call leaves that argument out. This call passes `"Colombia"`.
    """)
    return


@app.cell
def _():
    def my_country(country="USA"):
        print("I am from", country)

    my_country("Colombia")
    return (my_country,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A call with no argument uses the default, `"USA"`.
    """)
    return


@app.cell
def _(my_country):
    my_country()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A list is one argument. The function can loop over that list.
    """)
    return


@app.cell
def _():
    def my_food(food):
        for item in food:
            print(item)

    meals = ["rice", "beans", "eggs", "potato"]
    my_food(meals)
    return (my_food,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same function works for any list you pass.
    """)
    return


@app.cell
def _(my_food):
    fruits = ["orange", "apple", "grapes", "banana"]
    my_food(fruits)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `return` sends a value back to the caller. `mult_by_10(5)` returns `50`.
    """)
    return


@app.cell
def _():
    def mult_by_10(x):
        return 10 * x

    print(mult_by_10(5))
    return (mult_by_10,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function can return more than one value. Python packs those values into a tuple.
    """)
    return


@app.cell
def _():
    def swap(a, b):
        return b, a

    print(swap(1, 2))
    return (swap,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same function swaps two strings.
    """)
    return


@app.cell
def _(swap):
    print(swap("Anna", "John"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The caller can unpack that tuple into names. The number of names must match the number of returned values.
    """)
    return


@app.cell
def _(swap):
    swapped_left, swapped_right = swap(1, 2)
    print(swapped_left, swapped_right)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function with no `return` returns `None`. `print` displays a value. It does not send that value back to the caller. The next cell prints `10`, then prints the returned value, which is `None`.
    """)
    return


@app.cell
def _():
    def announced(number):
        print(number * 2)

    printed_result = announced(5)
    print("returned:", printed_result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A string on the first line of the body is a docstring. It documents the function. `help()` and `.__doc__` can read it.
    """)
    return


@app.cell
def _():
    def square(number):
        """Return the square of number."""
        return number * number

    print(square(4))
    print(square.__doc__)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A name assigned inside a function is local. The assignment does not change a variable of the same name outside the function.
    """)
    return


@app.cell
def _():
    course_name = "Python"

    def rename_course():
        course_name = "Data"
        return course_name

    print(rename_course())
    print(course_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A default value is created once, when the function is defined. A list used as a default is shared by later calls, so the second call still sees the first item. Use `None` as the default and create a new list inside the function.
    """)
    return


@app.cell
def _():
    def append_item(item, items=[]):
        items.append(item)
        return items

    print(append_item("a"))
    print(append_item("b"))

    def append_fresh(item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items

    print(append_fresh("a"))
    print(append_fresh("b"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Recursion

    A function may call itself. This factorial function multiplies `n` by `factorial(n - 1)`. The calls stop when `n` is not greater than `1`: that call returns `1` and does not call the function again. That stopping case is required. Without it, the function would call itself forever. Python also stops a chain of calls around 1000 deep, so `factorial(5000)` would raise `RecursionError`.

    `3!` is `3 * 2 * 1 = 6`.
    """)
    return


@app.cell
def _():
    def factorial(n):
        if n > 1:
            result = n * factorial(n - 1)
        else:
            result = 1
        return result

    print(factorial(3))
    return (factorial,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The stopping case returns `1`. `factorial(0)` does not call itself.
    """)
    return


@app.cell
def _(factorial):
    print(factorial(0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `10!` is `3,628,800`.
    """)
    return


@app.cell
def _(factorial):
    print(factorial(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `your_name`, then run the cell.
    """)
    return


@app.cell
def _():
    def greet(name):
        return "Hello " + name

    your_name = "Ana"
    print(greet(your_name))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Write a function that returns twice its argument, and call it with `6`. Replace `None` with your code. What does the function return?
    """)
    return


@app.cell
def _():
    student_doubled = None
    print(student_doubled)
    return (student_doubled,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
def student_double(number):
    return number * 2

student_doubled = student_double(6)
```
The function returns `12`. `return` sends that value back to the caller. The `def` line does not run the body.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `def` creates a function. The body runs only when you call the function.
    - A call needs one argument per parameter, unless the parameter has a default.
    - `*args` collects extra positional arguments into a tuple. `**kwargs` collects keyword arguments into a dictionary.
    - `return` sends a value back. A function with no `return` returns `None`. `print` shows a value and does not send it back. Several returned values arrive as a tuple, which the caller can unpack.
    - Names assigned inside a function are local. A mutable default argument is shared by later calls, so use `None` and create the list inside the function.
    - A recursive function must have a case that stops the calls.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. When does the body of a function run?
    2. What is the difference between a parameter and an argument?
    3. What happens if you pass more positional arguments than the function has parameters?
    4. Does the order of keyword arguments matter?
    5. What does a default value do?
    6. What does `return` send back when a function returns two values?
    7. Why does a recursive function need a stopping case?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **When you call it:** `def` stores the function. The call, with parentheses, runs the body.
2. **Name and value:** A parameter is the name in the definition. An argument is the value you pass in the call.
3. **An error:** The call must match the parameters, unless the function collects extras with `*args`.
4. **No:** Each value is tied to a parameter name.
5. **It fills a missing argument:** The call can leave that argument out.
6. **A tuple:** Python packs the values into one tuple.
7. **Otherwise the calls never stop:** The stopping case returns without calling the function again.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - [The Python Tutorial: Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
