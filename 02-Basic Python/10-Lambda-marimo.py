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

    The identity function returns the value it receives. This version is written with `def`.
    """)
    return


@app.cell
def _():
    def identity(x):
        return x

    print(identity(1))
    return (identity,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `lambda x: x` means "a function that takes `x` and returns `x`." It does the same job.
    """)
    return


@app.cell
def _():
    identity_lambda = lambda x: x
    print(identity_lambda(1))
    return (identity_lambda,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same lambda returns whatever value it receives.
    """)
    return


@app.cell
def _(identity_lambda):
    print(identity_lambda(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A `lambda` can take one argument. The expression after the colon is the returned value. `a + 100` adds `100`.
    """)
    return


@app.cell
def _():
    add_100 = lambda a: a + 100
    print(add_100(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Two parameters are written before the colon, separated by a comma.
    """)
    return


@app.cell
def _():
    add2 = lambda a, b: a + b
    print(add2(4, 6))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Three parameters work the same way.
    """)
    return


@app.cell
def _():
    add3 = lambda a, b, c: a + b + c
    print(add3(10, 20, 30))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function can return a `lambda`. `mult_by(2)` returns a function that multiplies by `2`. The returned function remembers the value of `n`.
    """)
    return


@app.cell
def _():
    def mult_by(n):
        return lambda x: x * n

    mydoubler = mult_by(2)
    print(mydoubler(10))
    return mult_by, mydoubler


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `mult_by(3)` returns a different function that multiplies by `3`.
    """)
    return


@app.cell
def _(mult_by):
    mytripler = mult_by(3)
    print(mytripler(10))
    return (mytripler,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The two returned functions can be used in one expression. `mydoubler(2)` is `4`, and `mytripler(2)` is `6`, so the product is `24`.
    """)
    return


@app.cell
def _(mydoubler, mytripler):
    print(mydoubler(2) * mytripler(2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A condition inside a lambda

    The expression may use `value_if_true if condition else value_if_false`. This function returns the text `"Even"` or `"Odd"`. `2` is even.
    """)
    return


@app.cell
def _():
    check = lambda x: "Even" if x % 2 == 0 else "Odd"
    print(check(2))
    return (check,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `21` is odd.
    """)
    return


@app.cell
def _(check):
    print(check(21))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A recursive lambda

    A `lambda` can call the name it was assigned to. This one computes a factorial. The expression stops calling itself when `n` is not greater than `1`, and then the value is `1`.

    `factorial(3)` is `3 * 2 * 1 = 6`.
    """)
    return


@app.cell
def _():
    factorial = lambda n: n * factorial(n - 1) if n > 1 else 1
    print(factorial(3))
    return (factorial,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `factorial(1)` uses the stopping case and returns `1`.
    """)
    return


@app.cell
def _(factorial):
    print(factorial(1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## filter

    `filter(function, items)` keeps the items for which `function` returns `True`. `list()` turns that result into a list. This lambda keeps the positive numbers.
    """)
    return


@app.cell
def _():
    positive = lambda x: x > 0
    samples = [1, -3, 0, 5, -2, -5, 0, 7, -9]
    print(list(filter(positive, samples)))
    return (samples,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can pass a `lambda` directly, without giving it a name first. This one keeps the zeros.
    """)
    return


@app.cell
def _(samples):
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
    ### Try it yourself

    Use a lambda to add `3` and `4`. Replace `None` with your code. What does the lambda return?
    """)
    return


@app.cell
def _():
    student_sum = None
    print(student_sum)
    return (student_sum,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_sum = (lambda a, b: a + b)(3, 4)
```
The lambda returns `7`. The expression after the colon is the returned value. The parentheses at the end call the lambda with `3` and `4`.
''')}, lazy=True)
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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. How many expressions can a `lambda` body contain?
    2. What does `lambda x: x` return?
    3. Where is the returned value written?
    4. What does a function such as `mult_by(2)` return?
    5. How does a `lambda` choose between two values?
    6. What stops a recursive factorial lambda?
    7. What does `filter` keep?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **One:** The body is a single expression. A longer task belongs in a `def` function.
2. **Its argument:** It is an identity function.
3. **After the colon:** That expression is the value the lambda returns.
4. **Another function:** The returned lambda remembers `2` and multiplies by it.
5. **`value if condition else other`:** Both results are part of the one expression.
6. **The case `n` is not greater than 1:** That case returns `1` and does not call the lambda again.
7. **Items for which the function returns true:** `list()` turns the kept items into a list.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
