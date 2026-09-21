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
    # Python Dates

    ## Objectives

    - Read the current date and time with the `datetime` module.
    - Format dates with `strftime` codes.
    - Create `datetime`, `date`, and `time` objects.
    - Parse a date string and find the time between two dates.

    ## Background

    A date is not a built-in type of its own. The `datetime` module supplies `datetime`, `date`, and `time` objects.

    ## Datasets Used

    This notebook does not use external datasets. Examples use dates written in the code and the current date from the computer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The current date and time

    `datetime.now()` includes year, month, day, hour, minute, second, and microsecond.
    """)
    return


@app.cell
def _(dt):
    current = dt.datetime.now()
    print(current)
    print(type(current))
    print("year:", current.year)
    print("month:", current.month)
    print("day:", current.day)
    return (current,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## strftime codes

    `strftime` turns a date into text. The same codes work for the current moment below.

    | Code | Meaning |
    |---|---|
    | `%Y` | year, four digits |
    | `%y` | year, two digits |
    | `%B` | month name |
    | `%b` | short month name |
    | `%m` | month number, 01–12 |
    | `%A` | weekday name |
    | `%a` | short weekday name |
    | `%w` | weekday number, 0 for Sunday |
    | `%j` | day of the year, 001–366 |
    | `%d` | day of the month |
    | `%H` | hour, 00–23 |
    | `%I` | hour, 01–12 |
    | `%p` | AM or PM |
    | `%M` | minute, 00–59 |
    | `%S` | second, 00–59 |
    | `%f` | microsecond |
    """)
    return


@app.cell
def _(current):
    print("year:        ", current.strftime("%Y"), current.strftime("%y"))
    print("month:       ", current.strftime("%B"), current.strftime("%b"), current.strftime("%m"))
    print("weekday:     ", current.strftime("%A"), current.strftime("%a"), current.strftime("%w"))
    print("day of year: ", current.strftime("%j"))
    print("hour:        ", current.hour, current.strftime("%H"), current.strftime("%I"), current.strftime("%p"))
    print("minute:      ", current.minute, current.strftime("%M"))
    print("second:      ", current.second, current.strftime("%S"))
    print("microsecond: ", current.microsecond, current.strftime("%f"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating datetime objects

    `datetime(year, month, day)` builds a specific moment. Hour, minute, second, and microsecond are optional and default to 0.
    """)
    return


@app.cell
def _(dt):
    created = dt.datetime(2020, 8, 1)
    print(created)

    appointments = [
        dt.datetime(2020, 3, 16, 7, 26),
        dt.datetime(2020, 3, 20, 8, 0),
        dt.datetime(2020, 4, 20, 8, 5),
        dt.datetime(2020, 5, 15, 7, 20),
        dt.datetime(2020, 6, 27),
        dt.datetime(2020, 7, 26, 8, 10),
        dt.datetime(2020, 8, 1, 9, 0),
        dt.datetime(2020, 9, 1, 10, 20),
    ]
    print(*appointments, sep="\n")
    return (appointments,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change the year, month, and day, then print the weekday name.
    """)
    return


@app.cell
def _(dt):
    your_year = 2024
    your_month = 1
    your_day = 15
    your_date = dt.date(your_year, your_month, your_day)

    print(your_date.strftime("%A"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## date objects

    `date` stores a calendar day without a time. The loops below format each appointment from the list above.
    """)
    return


@app.cell
def _(appointments):
    for month_entry in appointments:
        print(
            "Month",
            "short:",
            month_entry.strftime("%b"),
            "full:",
            month_entry.strftime("%B"),
        )
    return


@app.cell
def _(appointments):
    for weekday_entry in appointments:
        print(
            "Weekday",
            "short:",
            weekday_entry.strftime("%a"),
            "full:",
            weekday_entry.strftime("%A"),
            "number:",
            weekday_entry.strftime("%w"),
        )
    return


@app.cell
def _(appointments):
    for day_entry in appointments:
        print("Day:", day_entry.strftime("%d"))
    return


@app.cell
def _(appointments):
    for year_entry in appointments:
        print(
            "Year",
            "short:",
            year_entry.strftime("%y"),
            "full:",
            year_entry.strftime("%Y"),
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Subtracting two dates gives a `timedelta`. `.days` is the number of whole days between them.
    """)
    return


@app.cell
def _(appointments):
    gaps = [
        (appointments[index] - appointments[index - 1]).days
        for index in range(1, len(appointments))
    ]
    print(gaps)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next cell splits the span from a birthday to today into years, months, and days using only the standard library.
    """)
    return


@app.cell
def _(dt):
    def calendar_between(start, end):
        years = end.year - start.year
        months = end.month - start.month
        days = end.day - start.day
        if days < 0:
            months -= 1
            previous_month = end.replace(day=1) - dt.timedelta(days=1)
            days += previous_month.day
        if months < 0:
            years -= 1
            months += 12
        return years, months, days

    birthday = dt.date(1980, 8, 18)
    on_this_day = dt.date.today()
    elapsed_years, elapsed_months, leftover_days = calendar_between(birthday, on_this_day)
    print("years:", elapsed_years)
    print("months:", elapsed_years * 12 + elapsed_months)
    print("extra days:", leftover_days)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## time objects

    `time(hour, minute, second)` stores a clock time without a date.
    """)
    return


@app.cell
def _(dt):
    sample_time = dt.time(5, 20, 21)
    print(sample_time)
    print("Hours:", sample_time.hour, "Minutes:", sample_time.minute, "Seconds:", sample_time.second)

    clock_times = [
        dt.time(3, 3, 16),
        dt.time(6, 23, 20),
        dt.time(10, 4, 20),
        dt.time(12, 5, 15),
    ]
    print("hours:")
    for clock_time in clock_times:
        print(clock_time.strftime("%H"))
    print("minutes:")
    for clock_time in clock_times:
        print(clock_time.strftime("%M"))
    print("seconds:")
    for clock_time in clock_times:
        print(clock_time.strftime("%S"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Parsing date strings

    `strptime` reads text using the same codes as `strftime`. The pattern `'%Y-%m-%d-%H-%M'` matches `2020-3-11-3-33`.
    """)
    return


@app.cell
def _(dt):
    date_text = [
        "2020-3-11-3-33",
        "2020-4-16-4-24",
        "2020-5-20-5-25",
        "2020-6-16-6-36",
        "2020-7-26-7-7",
    ]
    print(type(date_text[0]))

    parsed_dates = [dt.datetime.strptime(text, "%Y-%m-%d-%H-%M") for text in date_text]
    print(parsed_dates)
    print(type(parsed_dates[0]))

    def span_between(start, end):
        years = end.year - start.year
        months = end.month - start.month
        days = end.day - start.day
        hours = end.hour - start.hour
        minutes = end.minute - start.minute
        if minutes < 0:
            hours -= 1
            minutes += 60
        if hours < 0:
            days -= 1
            hours += 24
        if days < 0:
            months -= 1
            previous_month = end.replace(day=1) - dt.timedelta(days=1)
            days += previous_month.day
        if months < 0:
            years -= 1
            months += 12
        return years, months, days, hours, minutes

    for index in range(1, len(parsed_dates)):
        earlier = parsed_dates[index - 1]
        later = parsed_dates[index]
        years, months, days, hours, minutes = span_between(earlier, later)
        print("Date1:", earlier, "   Date2:", later)
        print("Diff years   =", years)
        print("Diff months  =", months)
        print("Diff days    =", days)
        print("Diff hours   =", hours)
        print("Diff minutes =", minutes)
        print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Yesterday and tomorrow

    `timedelta(days=1)` moves a date by one day.
    """)
    return


@app.cell
def _(dt):
    today = dt.date.today()
    yesterday = today - dt.timedelta(days=1)
    tomorrow = today + dt.timedelta(days=1)

    print("yesterday:", yesterday)
    print("today:    ", today)
    print("tomorrow: ", tomorrow)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Change `shift_days`. A positive number moves forward. A negative number moves backward.
    """)
    return


@app.cell
def _(dt):
    shift_days = 7
    shifted = dt.date.today() + dt.timedelta(days=shift_days)
    print(shifted.strftime("%Y-%m-%d %A"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - Import `datetime` to work with dates and times.
    - `strftime` formats an object. `strptime` reads a string back into an object.
    - Subtracting two dates produces a `timedelta`.
    - `timedelta` can move a date forward or backward by a number of days.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media.
    """)
    return


if __name__ == "__main__":
    app.run()
