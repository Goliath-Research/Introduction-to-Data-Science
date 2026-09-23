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
    # Python datetime

    ## Objectives

    - Create `datetime`, `date`, and `time` objects.
    - Read the year, month, day, hour, minute, second, and microsecond.
    - Format a datetime as text with `strftime()`.
    - Subtract two dates to get the number of days between them.

    ## Background

    A date or a time is not one of Python's built-in types such as `int` or `str`. The `datetime` module provides objects for a calendar date, a time of day, and a date with a time. Those objects can be formatted as text and combined with arithmetic.

    ## Datasets Used

    This notebook does not use external datasets. `datetime.now()` and `date.today()` read the computer's clock.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The current date and time

    `datetime.now()` returns the current date and time. The object holds the year, month, day, hour, minute, second, and microsecond.
    """)
    return


@app.cell
def _():
    import datetime as dt

    current = dt.datetime.now()
    print(current)
    print(type(current))
    print("year:", current.year)
    print("month:", current.month)
    print("day:", current.day)
    print("hour:", current.hour)
    print("minute:", current.minute)
    print("second:", current.second)
    print("microsecond:", current.microsecond)
    return (current, dt)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## strftime

    `strftime(format)` turns a datetime into text. The format string uses codes that start with `%`.

    | Code | Meaning |
    |---|---|
    | `%Y` | Year, four digits |
    | `%y` | Year, two digits |
    | `%B` | Month name |
    | `%b` | Month name, short |
    | `%m` | Month number, 01-12 |
    | `%A` | Weekday name |
    | `%a` | Weekday name, short |
    | `%w` | Weekday number, 0 for Sunday |
    | `%j` | Day of the year, 001-366 |
    | `%H` | Hour, 00-23 |
    | `%I` | Hour, 01-12 |
    | `%p` | AM or PM |
    | `%M` | Minute, 00-59 |
    | `%S` | Second, 00-59 |
    | `%f` | Microsecond, 000000-999999 |
    """)
    return


@app.cell
def _(current):
    print("year:", current.strftime("%Y"))
    print("year, short:", current.strftime("%y"))
    print("month name:", current.strftime("%B"))
    print("month, short:", current.strftime("%b"))
    print("month number:", current.strftime("%m"))
    print("weekday:", current.strftime("%A"))
    print("weekday, short:", current.strftime("%a"))
    print("weekday number:", current.strftime("%w"))
    print("day of year:", current.strftime("%j"))
    print("hour 00-23:", current.strftime("%H"))
    print("hour 01-12:", current.strftime("%I"))
    print("AM/PM:", current.strftime("%p"))
    print("minute:", current.strftime("%M"))
    print("second:", current.strftime("%S"))
    print("microsecond:", current.strftime("%f"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating a date or a time

    `datetime(year, month, day)` builds a datetime. The time defaults to midnight. `date(year, month, day)` builds a date with no time. `time(hour, minute, second)` builds a time with no date.
    """)
    return


@app.cell
def _(dt):
    print(dt.datetime(2022, 1, 1))
    print(dt.date(2022, 4, 4))
    print(dt.time(5, 20, 21))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Subtracting two `date` objects returns the time between them. `.days` is that interval as a number of days.
    """)
    return


@app.cell
def _(dt):
    day1 = dt.date(2022, 5, 5)
    today = dt.date.today()
    print("day1:", day1)
    print("today:", today)
    print("Number of days elapsed from May 5, 2022:", (today - day1).days)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `birthday` to a date you choose, then run the cell.
    """)
    return


@app.cell
def _(dt):
    birthday = dt.date(2001, 3, 14)
    print(birthday.strftime("%A"))
    print(birthday.strftime("%B %d, %Y"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - Import `datetime` to work with dates and times. `datetime.now()` and `date.today()` read the current clock.
    - A datetime object stores the year, month, day, hour, minute, second, and microsecond as separate attributes.
    - `strftime()` formats those parts as text. Each `%` code selects one part.
    - `datetime()`, `date()`, and `time()` build objects from numbers you choose. Subtracting two dates gives the days between them.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
