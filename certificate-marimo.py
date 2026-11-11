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

    Every course in Goliath Research Academy uses the same assessment path: practice quizzes during the lessons, then one certificate test at the end.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How the course is assessed

    Each course has **two lesson sections**. Each lesson section ends with a short **quiz**.

    - Quizzes are for **practice**. They are **not graded** and **do not count** toward your certificate.
    - Quizzes show **feedback** on your answers.

    At the end of the course there is the **Certificate of Knowledge** test. **Pass the test** to earn your **Certificate of Knowledge**.
    """)
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
