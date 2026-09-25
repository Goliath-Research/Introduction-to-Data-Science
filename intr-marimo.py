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
    # Marimo

    ## What is Marimo?

    Marimo is an open-source Python notebook environment for interactive and reproducible computing. One document holds Python code, explanations, visualizations, and interactive controls.

    A Marimo notebook is **reactive**. When a variable changes, Marimo updates the cells that depend on it. You still work in a notebook, and the notebook also behaves like a small interactive application.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Marimo notebooks

    A notebook is made of **cells**. A cell contains either Python code or formatted text written in Markdown.

    In the lessons for this course:

    - **Markdown cells are hidden.** You read the formatted explanation. You do not need to edit the Markdown.
    - **Python cells stay visible.** Read the code, then change it and watch the output.

    ### What a notebook can do

    - **Interactive Python.** You write and run Python directly in a cell. The output appears with that cell.
    - **Reactive execution.** Marimo records which cells use which names. Change a value, and the cells that depend on it run again.
    - **Rich content.** A notebook can place formatted text, mathematical expressions, tables, plots, and images next to Python.
    - **Interactive elements.** Sliders, buttons, dropdown lists, and text fields connect directly to Python. Moving a control changes a value, and the notebook updates.
    - **Reproducibility.** Marimo follows the dependencies between cells, so the result does not depend on the order in which you happened to run cells by hand.
    - **Python files.** A notebook is stored as an ordinary `.py` file. That makes the lessons straightforward to manage with Git and GitHub.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How Marimo works

    The next two cells are a complete example. The first cell defines `x`. The second cell uses `x` to compute `y`.
    """)
    return


@app.cell
def _():
    x = 25
    return (x,)


@app.cell
def _(x):
    y = x * 2
    print(y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Change `x` from `10` to `25`. Marimo reruns the cell that calculates `y`, and that cell prints `50`.

    You only edit `x`. You do not need to run the second cell yourself.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The second cell depends on `x`. Marimo sees that relationship and keeps `y` consistent with the current value of `x`.

    This is the main idea of Marimo: **edit a value, and everything that uses it stays in step.**

    The order of cells on the page is for reading. It is not the order of the program. Marimo builds the execution order from the relationships among variables. A cell can appear lower on the page and still run first, when a cell above it needs a name that the lower cell defines.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Try an interactive control

    A slider is a Python object. The next cell creates one and shows it. The cell after that reads `x_control.value` and computes `y`.

    Drag the slider. The formula does not change. The value does, and the dependent cell updates.
    """)
    return


@app.cell
def _(mo):
    x_control = mo.ui.slider(0, 20, value=10, label="x", show_value=True)
    x_control
    return (x_control,)


@app.cell
def _(x_control):
    y_from_slider = x_control.value * 2
    print("x =", x_control.value)
    print("y = x * 2 =", y_from_slider)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Using the Marimo lessons in this course

    The programming lessons are Marimo notebooks. Use each one in two ways:

    1. **Read the lesson.** Study the explanations, the Python, and the results.
    2. **Run the notebook.** Change the examples, try new values, and complete the activities.

    You are encouraged to change values, modify expressions, and experiment. Programming is learned by writing and running code.

    ### How to work in a lesson

    - Read the text above a Python cell before you edit that cell.
    - Click the cell, change a number, a name, or an expression, then leave the cell. Marimo updates every cell that depends on your change.
    - Do not run the notebook from top to bottom. Marimo chooses the order from the variable relationships.
    - If a cell shows an error, read the message. It names the problem, often a misspelled name or an expression Python cannot evaluate.
    - To restore the original lesson, undo your edit, or discard your changes to that file in Git.
    
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## About the course

    The course uses several kinds of activities:

    - **Videos.** Short introductions and summaries of the main ideas of each topic.
    - **E-books.** Structured explanations of the material.
    - **Marimo notebooks.** The primary programming resource. They contain executable Python you can explore and modify.
    - **Quizzes.** Self-assessment with immediate feedback. They are not formal exams.
    - **Certificate of Knowledge.** Pass a 15-question test within 15 minutes. If you do not pass on the first attempt, you have two further attempts.

    ## Conclusions

    **Key takeaways:**

    - A Marimo notebook combines explanation and Python in one reactive document.
    - In these lessons, Markdown is hidden so you can read it, and Python stays visible so you can study and change it.
    - When a variable changes, Marimo updates the cells that depend on it.
    - Cell order on the page does not decide the logic. Dependencies do.
    - Learn by editing the examples and reading the new results.

    ## References

    - [Marimo](https://marimo.io)
    - [Marimo documentation](https://docs.marimo.io)
    """)
    return


if __name__ == "__main__":
    app.run()
