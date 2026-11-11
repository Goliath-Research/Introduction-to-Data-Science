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
    # How to Earn Your Certificate
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src="https://raw.githubusercontent.com/Goliath-Research/Introduction-to-Data-Science/main/images/certificate.png",
        alt="Certificate of Knowledge medal",
        width=280,
        style={"display": "block", "margin": "0 auto"},
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Certificate of Knowledge test

    - The test has **15 questions** and a **15-minute** time limit.
    - **Passing score:** at least **70%**.
    - If you do not pass, you can **retake the test twice**, so you have **three attempts in total**.
    - Once you **pass**, the test is **closed** and **cannot be retaken**. Review the ebooks, notebooks, and quizzes before you start.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Before you start

    - Review the **lessons and quizzes** first.
    - Start when you have **15 uninterrupted minutes**.
    - **Read each question carefully**.
    - **Watch the timer**.

    **Good luck!**
    """)
    return


if __name__ == "__main__":
    app.run()
