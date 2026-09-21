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
    # Python Lambda

    ## Objectives

    - Write a one-expression function with `lambda`.
    - Compare a `lambda` with a function created by `def`.
    - Pass several arguments to a `lambda`.
    - Return a `lambda` from another function.

    ## Background

    A lambda is a small anonymous function. It can take any number of arguments, and its body is a single expression.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The identity function

    The identity function returns its argument unchanged. The `lambda` version is one expression.
    """)
    return


@app.cell
def _():
    def identity(value):
        return value

    identity_lambda = lambda value: value

    print(identity(1))
    print(identity_lambda(1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## One or more arguments

    `lambda a: a + 100` adds 100 to its argument. Separate additional parameters with commas.
    """)
    return


@app.cell
def _():
    add_100 = lambda amount: amount + 100
    print(add_100(5))
    print(add_100(1000))

    add2 = lambda left, right: left + right
    print(add2(4, 6))
    print(add2(10, 20))

    add3 = lambda first, second, third: first + second + third
    print(add3(10, 20, 30))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the operation inside the lambda, then call it with a new number.
    """)
    return


@app.cell
def _():
    add_five = lambda number: number + 5
    print(add_five(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Returning a lambda

    A lambda is useful as an anonymous function returned by another function. `myfunc(n)` returns a new function that multiplies its argument by `n`.
    """)
    return


@app.cell
def _():
    def multiplier(factor):
        return lambda amount: amount * factor

    doubler = multiplier(2)
    tripler = multiplier(3)

    print("double 10:", doubler(10))
    print("double 2:", doubler(2))
    print("triple 10:", tripler(10))
    print("triple 2:", tripler(2))
    print("double 2 times triple 2:", doubler(2) * tripler(2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the factor from 4 to another number.
    """)
    return


@app.cell
def _():
    def practice_multiplier(factor):
        return lambda amount: amount * factor

    times_four = practice_multiplier(4)
    print(times_four(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## When to use lambda

    - A lambda can contain only one expression.
    - Use it for short code whose behavior is obvious.
    - If one call needs several lambdas, a named function is clearer.
    - If the same function is used in several places, define it with `def` instead of repeating the lambda.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `lambda arguments: expression` creates a small function.
    - A lambda may take one argument or several, and it returns the value of its expression.
    - A function can return a lambda when the caller should receive a new function.
    - Prefer `def` when the function is long or used in many places.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
