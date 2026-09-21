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

    - Define a function and call it.
    - Pass positional arguments, `*args`, keyword arguments, and `**kwargs`.
    - Give a parameter a default value and pass a list.
    - Return a value, including a function that calls itself.

    ## Background

    A function is a block of code that runs when you call it. Parameters receive the data you pass in. A function can return a result.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Defining and calling a function

    `def` creates the function. The function does not run until a later line calls it.
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
    ## Arguments

    Arguments go inside the parentheses, separated by commas. The call must pass the number of arguments the definition expects.
    """)
    return


@app.cell
def _():
    def hello(name):
        print("Hello", name)

    hello("John")
    hello("Mary")

    try:
        hello("Mary", "John")
    except TypeError as error:
        print("TypeError:", error)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the name passed to `greet`, then run the cell.
    """)
    return


@app.cell
def _():
    def greet(name):
        print("Welcome,", name)

    greet("Ana")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Arbitrary arguments

    `*kids` collects any number of positional arguments into a tuple. This version treats the first argument as the youngest child, so the call is expected to list children from youngest to oldest.
    """)
    return


@app.cell
def _():
    def youngest_from_args(*kids):
        print("The youngest child is", kids[0])

    youngest_from_args("John", "Mary", "Anna")
    youngest_from_args("John", "Mary", "Anna", "Raul")
    youngest_from_args("Anna", "John", "Mary", "Raul")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Keyword arguments

    `name=value` assigns an argument by parameter name, so the order in the call does not matter.
    """)
    return


@app.cell
def _():
    def youngest_from_keywords(child3, child2, child1):
        print("The youngest child is", child1)

    youngest_from_keywords(child1="John", child2="Mary", child3="Anna")
    youngest_from_keywords(child2="Mary", child3="Anna", child1="John")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `**kid` collects keyword arguments into a dictionary. The function then reads the keys it needs.
    """)
    return


@app.cell
def _():
    def youngest_from_kwargs(**kid):
        print("The youngest child is", kid["child1"])

    youngest_from_kwargs(child1="Mary", child3="Anna")
    youngest_from_kwargs(child1="John", child2="Mary", child4="Anna")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Default values and lists

    A default value is used when the caller omits that argument. A list can be passed as one argument and then visited inside the function.
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


@app.cell
def _():
    def my_food(food):
        for item in food:
            print(item)

    foods = ["orange", "apple", "grapes", "patata"]
    my_food(foods)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Add another food to the list, or change the default country in a copy of the function above.
    """)
    return


@app.cell
def _():
    def describe_meal(country="USA", foods=None):
        if foods is None:
            foods = ["rice"]
        print("I am from", country)
        print("Foods:", ", ".join(foods))

    describe_meal("Mexico", ["beans", "corn"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Return values

    `return` sends a value back to the caller. A function may also call itself. `factorial` keeps multiplying until it reaches the base case.
    """)
    return


@app.cell
def _():
    def mult_by_5(value):
        return 5 * value

    print("0 multiply by 5 is", mult_by_5(0))
    print("1 multiply by 5 is", mult_by_5(1))
    print("5 multiply by 5 is", mult_by_5(5))
    print("8 multiply by 5 is", mult_by_5(8))
    return


@app.cell
def _():
    def factorial(number):
        if number > 1:
            result = number * factorial(number - 1)
        else:
            result = 1
        return result

    print("3! =", factorial(3))
    print("0! =", factorial(0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `your_number`. The function returns that number squared.
    """)
    return


@app.cell
def _():
    def square(number):
        return number * number

    your_number = 6
    print(square(your_number))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `def` creates a function. A call runs it.
    - A call must match the parameters, unless the definition uses defaults, `*args`, or `**kwargs`.
    - Keyword arguments assign values by name.
    - `return` gives a value back. A function can call itself when a base case stops the chain.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
