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
    A parameter is a name in the parentheses. A call must pass one value for each parameter, unless that parameter has a default. The value you pass is an argument. Run the last cell in this section to see the error from passing too many arguments.
    """)
    return


@app.cell
def _():
    def hello(name):
        print("Hello", name)

    hello("John")
    hello("Mary")
    return (hello,)


@app.cell
def _(hello):
    hello("Mary", "John")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ways to pass arguments

    `*kids` collects any number of positional arguments into a tuple. The function below treats the first item as the youngest, so the caller must pass the names in that order. `*args` is the name often used for this pattern in documentation.

    Keyword arguments use `name=value`. The order of those arguments does not matter, and they must come after positional arguments.

    `**kid` collects keyword arguments into a dictionary. `**kwargs` is the usual name for that pattern. The function below reads the key `"child1"`.
    """)
    return


@app.cell
def _():
    def youngest_of(*kids):
        print("The youngest child is", kids[0])

    youngest_of("John", "Mary", "Anna")
    youngest_of("John", "Mary", "Anna", "Raul")
    youngest_of("Anna", "John", "Mary", "Raul")
    return


@app.cell
def _():
    def youngest_by_name(child3, child2, child1):
        print("The youngest child is", child1)

    youngest_by_name(child1="John", child2="Mary", child3="Anna")
    youngest_by_name(child2="Mary", child3="Anna", child1="John")
    return


@app.cell
def _():
    def youngest_from_keywords(**kid):
        print("The youngest child is", kid["child1"])

    youngest_from_keywords(child1="Mary", child3="Anna")
    youngest_from_keywords(child1="John", child2="Mary", child3="Anna")
    youngest_from_keywords(child2="Mary", child3="Anna", child1="John")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A default value is used when the call leaves that argument out.
    """)
    return


@app.cell
def _():
    def my_country(country="USA"):
        print("I am from", country)

    my_country("Colombia")
    my_country("Spain")
    my_country()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A list is one argument. The function can loop over that list. The same function works for any list you pass.
    """)
    return


@app.cell
def _():
    def my_food(food):
        for item in food:
            print(item)

    meals = ["rice", "beans", "eggs", "patata"]
    my_food(meals)
    print()
    fruits = ["orange", "apple", "grapes", "banana"]
    my_food(fruits)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `return` sends a value back to the caller. A function can return more than one value. Python packs those values into a tuple.
    """)
    return


@app.cell
def _():
    def mult_by_10(x):
        return 10 * x

    print("0 multiply by 10 is", mult_by_10(0))
    print("1 multiply by 10 is", mult_by_10(1))
    print("5 multiply by 10 is", mult_by_10(5))
    print("8 multiply by 10 is", mult_by_10(8))
    return


@app.cell
def _():
    def swap(a, b):
        return b, a

    print(swap(1, 2))
    print(swap("Anna", "John"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Recursion

    A function may call itself. This factorial function multiplies `n` by `factorial(n - 1)`. The calls stop when `n` is not greater than `1`: that call returns `1` and does not call the function again. That stopping case is required. Without it, the function would call itself forever.
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

    print("3! =", factorial(3))
    print("0! =", factorial(0))
    print("10! =", factorial(10))
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
    ## Conclusions

    **Key takeaways:**

    - `def` creates a function. The body runs only when you call the function.
    - A call needs one argument per parameter, unless the parameter has a default.
    - `*args` collects extra positional arguments into a tuple. `**kwargs` collects keyword arguments into a dictionary.
    - `return` sends a value back. Several returned values arrive as a tuple.
    - A recursive function must have a case that stops the calls.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
