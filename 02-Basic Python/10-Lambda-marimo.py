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
    - Compare a `lambda` with a function written with `def`.
    - Return a `lambda` from another function.
    - Use a `lambda` with a condition, with recursion, and with `filter()`.

    ## Background

    A `lambda` is a small function without a name of its own. It can take any number of arguments, and its body is a single expression. The value of that expression is what the function returns. Use it for a short calculation. When the same logic is long, or you need it in several places, write a `def` function instead.

    ## Datasets Used

    This notebook does not use external datasets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A function and a lambda

    The identity function returns the value it receives. The `def` version and the `lambda` version do the same job. `lambda x: x` means "a function that takes `x` and returns `x`."
    """)
    return


@app.cell
def _():
    def identity(x):
        return x

    print(identity(1))
    print(identity(10))

    identity_lambda = lambda x: x
    print(identity_lambda(1))
    print(identity_lambda(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A `lambda` can take one argument or several. The expression after the colon is the returned value.
    """)
    return


@app.cell
def _():
    add_100 = lambda a: a + 100
    print(add_100(5))
    print(add_100(1000))

    add2 = lambda a, b: a + b
    print(add2(4, 6))
    print(add2(10, 20))

    add3 = lambda a, b, c: a + b + c
    print(add3(10, 20, 30))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function can return a `lambda`. `mult_by(2)` returns a function that multiplies by `2`. `mult_by(3)` returns a different function that multiplies by `3`. The returned functions remember the value of `n`.
    """)
    return


@app.cell
def _():
    def mult_by(n):
        return lambda x: x * n

    mydoubler = mult_by(2)
    print(mydoubler(10))
    print(mydoubler(2))

    mytripler = mult_by(3)
    print(mytripler(10))
    print(mytripler(2))

    print(mydoubler(2) * mytripler(2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A condition inside a lambda

    The expression may use `value_if_true if condition else value_if_false`. This function returns the text `"Even"` or `"Odd"`.
    """)
    return


@app.cell
def _():
    check = lambda x: "Even" if x % 2 == 0 else "Odd"
    print(check(2))
    print(check(21))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A recursive lambda

    A `lambda` can call the name it was assigned to. This one computes a factorial. The expression stops calling itself when `n` is not greater than `1`, and then the value is `1`.
    """)
    return


@app.cell
def _():
    factorial = lambda n: n * factorial(n - 1) if n > 1 else 1
    print(factorial(3))
    print(factorial(1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## filter

    `filter(function, items)` keeps the items for which `function` returns `True`. `list()` turns that result into a list. You can pass a `lambda` directly, without giving it a name first.
    """)
    return


@app.cell
def _():
    positive = lambda x: x > 0
    samples = [1, -3, 0, 5, -2, -5, 0, 7, -9]
    print(list(filter(positive, samples)))
    print(list(filter(lambda x: x == 0, samples)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `amount` and predict the result before you run the cell.
    """)
    return


@app.cell
def _():
    add_amount = lambda x: x + 5
    amount = 10
    print(add_amount(amount))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `lambda arguments: expression` is a function whose body is one expression.
    - It can replace a short `def` function. A longer task is easier to read as `def`.
    - A function can return a `lambda` that remembers a value from the outer function.
    - A `lambda` can include `if` and `else`, can call itself, and can be passed to `filter()`.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
