import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import datetime as dt
    import marimo as mo

    return dt, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python datetime

    ## Objectives

    - Create `datetime`, `date`, and `time` objects.
    - Read the year, month, day, hour, minute, second, and microsecond.
    - Format a datetime as text with `strftime()`.
    - Subtract two dates to get a `timedelta`, and read a date from text.

    ## Background

    A date or a time is not one of Python's built-in types such as `int` or `str`. It comes from the standard-library module `datetime`. That module provides objects for a calendar date, a time of day, and a date with a time. Those objects can be formatted as text and combined with arithmetic.

    ## Datasets Used

    This notebook does not use external datasets. `datetime.now()` and `date.today()` read the clock. In the browser version of this lesson, that clock is the browser's clock.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The current date and time

    `datetime.now()` returns the current local date and time. The result is naive: it has no time zone. The object holds the year, month, day, hour, minute, second, and microsecond.
    """)
    return


@app.cell
def _(dt):
    current = dt.datetime.now()
    print(current)
    return (current,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The type is `datetime`.
    """)
    return


@app.cell
def _(current):
    print(type(current))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `year` is the four-digit year.
    """)
    return


@app.cell
def _(current):
    print(current.year)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `month` is a number from 1 to 12.
    """)
    return


@app.cell
def _(current):
    print(current.month)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `day` is the day of the month.
    """)
    return


@app.cell
def _(current):
    print(current.day)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `hour` uses a 24-hour clock.
    """)
    return


@app.cell
def _(current):
    print(current.hour)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `minute` and `second` are the rest of the time. This is the minute.
    """)
    return


@app.cell
def _(current):
    print(current.minute)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is the second.
    """)
    return


@app.cell
def _(current):
    print(current.second)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `microsecond` is the fraction of the second. One second is 1,000,000 microseconds.
    """)
    return


@app.cell
def _(current):
    print(current.microsecond)
    return


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
    | `%d` | Day of the month, 01-31 |
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

    `%B`, `%A`, and `%p` depend on the language settings of the computer. In these lessons they appear in English.

    `%Y` is the year in four digits.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%Y"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%y` is the year in two digits.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%y"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%B` is the full month name.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%B"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%b` is the short month name.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%b"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%m` is the month number, from `01` to `12`.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%m"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%d` is the day of the month, from `01` to `31`.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%d"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%A` is the full weekday name.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%A"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%a` is the short weekday name.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%a"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%w` is the weekday number. `0` is Sunday.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%w"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%j` is the day of the year, from `001` to `366`.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%j"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%H` is the hour on a 24-hour clock.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%H"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%I` is the hour on a 12-hour clock.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%I"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%p` is `AM` or `PM`.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%p"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%M` is the minute.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%M"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%S` is the second.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%S"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `%f` is the microsecond.
    """)
    return


@app.cell
def _(current):
    print(current.strftime("%f"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating a date or a time

    `datetime(year, month, day)` builds a datetime. The time defaults to midnight.
    """)
    return


@app.cell
def _(dt):
    print(dt.datetime(2022, 1, 1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `date(year, month, day)` builds a date with no time.
    """)
    return


@app.cell
def _(dt):
    print(dt.date(2022, 4, 4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `time(hour, minute, second)` builds a time with no date.
    """)
    return


@app.cell
def _(dt):
    print(dt.time(5, 20, 21))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Subtracting two `date` objects returns a `timedelta`, the span between them. This is the starting date.
    """)
    return


@app.cell
def _(dt):
    day1 = dt.date(2022, 5, 5)
    print(day1)
    return (day1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `date.today()` reads the clock. Like `datetime.now()`, the result is naive: it has no time zone.
    """)
    return


@app.cell
def _(dt):
    today = dt.date.today()
    print(today)
    return (today,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The difference itself is a `timedelta`. `.days` reads that span as a number of days.
    """)
    return


@app.cell
def _(day1, today):
    print(today - day1)
    print((today - day1).days)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Adding a `timedelta` moves a date. `timedelta(days=7)` is one week after `day1`.
    """)
    return


@app.cell
def _(day1, dt):
    print(day1 + dt.timedelta(days=7))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reading a date from text

    Data files store dates as text. `date.fromisoformat()` reads `YYYY-MM-DD`. `datetime.strptime()` reads text that follows a format you give. The codes are the same ones `strftime` uses. A numeric format does not depend on the computer's language. `%B` would need the month name in that language.
    """)
    return


@app.cell
def _(dt):
    parsed_iso = dt.date.fromisoformat("2022-01-10")
    print(parsed_iso, "->", type(parsed_iso))
    parsed_text = dt.datetime.strptime("10/01/2022", "%d/%m/%Y")
    print(parsed_text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `birthday` to a date you choose and watch the output update.
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
    ### Try it yourself

    Find the number of days from January 1, 2022 to January 10, 2022. Replace `None` with your code. Is the start date counted in that number?
    """)
    return


@app.cell
def _():
    student_span = None
    print(student_span)
    return (student_span,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_span = (dt.date(2022, 1, 10) - dt.date(2022, 1, 1)).days
```
The result is `9`. Subtraction gives the days between the two dates. January 1 is the starting point, so it is not an extra day in the count.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - Import `datetime` to work with dates and times. `datetime.now()` and `date.today()` read the current clock.
    - A datetime object stores the year, month, day, hour, minute, second, and microsecond as separate attributes.
    - `strftime()` formats those parts as text. Each `%` code selects one part.
    - `datetime()`, `date()`, and `time()` build objects from numbers you choose. Subtracting two dates returns a `timedelta`. Adding a `timedelta` moves a date.
    - `date.fromisoformat()` and `datetime.strptime()` read a date from text. `%d` is the day of the month.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. Which module provides `date` and `datetime`?
    2. What does `datetime.now()` return?
    3. Which attribute is the day of the month?
    4. What does `%Y` format?
    5. What does `%B` format?
    6. What time does `datetime(2022, 1, 1)` use when you pass only the date?
    7. What does subtracting two dates give you?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **`datetime`:** A date is not a built-in type such as `int` or `str`.
2. **The current date and time:** It reads the computer's clock.
3. **`day`:** `month` is the month number, and `year` is the year.
4. **The year in four digits:** `%y` uses two digits.
5. **The full month name:** `%b` is the short name, and `%m` is the number.
6. **Midnight:** The hour, minute, and second default to `0`.
7. **A `timedelta`:** `.days` is that span as an integer.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - [`datetime` — basic date and time types](https://docs.python.org/3/library/datetime.html)
    - [The Python Tutorial](https://docs.python.org/3/tutorial/)
    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
