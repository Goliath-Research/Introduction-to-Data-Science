import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Pandas Input/Output

    ## Objectives

    - Read and write CSV and JSON files with Pandas.
    - Tell `read_csv` when a file is separated by semicolons.
    - Read an ARFF file and an Excel workbook.
    - Flatten a nested JSON object with `json_normalize`.

    ## Background

    Pandas can load a file into a DataFrame and write a DataFrame back out. The cells that use a web address need a network connection. Saving `auto.csv` and `countries.json` writes those files in this folder.

    ## Datasets Used

    - **Automobile Dataset** from the UCI Machine Learning Repository, for CSV files.
    - **Higher Education Students Performance Evaluation Dataset**, a CSV file separated by semicolons.
    - **Student Academics Performance Dataset**, an ARFF file.
    - **Countries**, a JSON file.
    - **Immunotherapy Dataset**, an Excel file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Some dataset repositories

    **UCI Machine Learning Repository**

    The UCI Machine Learning Repository, [https://archive.ics.uci.edu/ml/index.php](https://archive.ics.uci.edu/ml/index.php), is a collection of datasets used by the machine learning community. It was created as an ftp archive in 1987 by David Aha and fellow graduate students at UC Irvine.

    For each dataset, the repository records the source, a description of the data, the attributes, and relevant papers.

    **Data.World**

    Data.world, [https://data.world/](https://data.world/), is a catalog of datasets in many formats.
    """)
    return


@app.cell
def _(pd):
    # Controlling the number of columns a DataFrame shows
    pd.set_option('display.max_columns', 8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reading data from a `.csv` file

    Comma-separated values (CSV) is one of the most common ways to store and share a table.

    `read_csv` reads a CSV file and returns a DataFrame. This file has no header row, so the column names are passed with `names`. The character `?` means missing, so `na_values='?'` turns it into `NaN`.

    The Automobile dataset is [https://archive.ics.uci.edu/ml/datasets/automobile](https://archive.ics.uci.edu/ml/datasets/automobile).
    """)
    return


@app.cell
def _():
    headers = [
        'symboling', 'normalized_losses', 'make', 'fuel_type', 'aspiration',
        'num_doors', 'body_style', 'drive_wheels', 'engine_location',
        'wheel_base', 'length', 'width', 'height', 'curb_weight',
        'engine_type', 'num_cylinders', 'engine_size', 'fuel_system',
        'bore', 'stroke', 'compression_ratio', 'horsepower', 'peak_rpm',
        'city_mpg', 'highway_mpg', 'price',
    ]
    return (headers,)


@app.cell
def _(headers, pd):
    df_auto = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data',
        header=None,
        names=headers,
        na_values='?',
    )
    print(df_auto.shape)
    df_auto.head()
    return (df_auto,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `to_csv` writes the DataFrame to a file. The first save includes the index, so reading that file adds an extra unnamed column. That column is the old index.

    The second save passes `index=False`, and the following read does not have that extra column.
    """)
    return


@app.cell
def _(df_auto, pd):
    df_auto.to_csv('auto.csv')
    with_index = pd.read_csv('auto.csv')
    print(with_index.shape)
    print(with_index.head())

    df_auto.to_csv('auto.csv', index=False)
    df2_auto = pd.read_csv('auto.csv')
    print(df2_auto.shape)
    df2_auto.head()
    return (df2_auto,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `describe` summarizes the numeric columns of the automobile data.
    """)
    return


@app.cell
def _(df_auto):
    df_auto.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A CSV file is not always separated by commas. It may use semicolons, tabs, or another character. Set that character with `sep`.

    The Higher Education Students Performance Evaluation dataset is [https://archive.ics.uci.edu/ml/datasets/Higher+Education+Students+Performance+Evaluation+Dataset](https://archive.ics.uci.edu/ml/datasets/Higher+Education+Students+Performance+Evaluation+Dataset).

    The first read uses the default comma. The whole line lands in one column. The second read sets `sep=';'`.
    """)
    return


@app.cell
def _(pd):
    df_hst_comma = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/00623/DATA.csv',
        na_values='?',
    )
    print(df_hst_comma.shape)
    df_hst_comma.head()
    return


@app.cell
def _(pd):
    df_hst = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/00623/DATA.csv',
        sep=';',
        na_values='?',
    )
    print(df_hst.shape)
    df_hst.head()
    return (df_hst,)


@app.cell
def _(df_hst):
    df_hst.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Read the local `auto.csv` file and print its shape and its first three rows.
    """)
    return


@app.cell
def _(df2_auto, pd):
    print('Rows in the saved automobile table:', len(df2_auto))
    check = pd.read_csv('auto.csv')
    print(check.shape)
    check.head(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reading data from an `.arff` file

    An ARFF file (Attribute-Relation File Format) is a text file from the Machine Learning Project at the University of Waikato. It has a header section and a data section.

    `scipy.io.arff.loadarff` reads both sections. The Student Academics file is downloaded from [https://archive.ics.uci.edu/ml/machine-learning-databases/00467/Sapfile1.arff](https://archive.ics.uci.edu/ml/machine-learning-databases/00467/Sapfile1.arff). The download uses `urlopen` from Python's standard library. Text values arrive as byte strings, so each text column is decoded to ordinary text.
    """)
    return


@app.cell
def _():
    # For reading an arff file, we need to import
    from io import StringIO
    from urllib.request import urlopen
    from scipy.io.arff import loadarff

    return StringIO, loadarff, urlopen


@app.cell
def _(urlopen):
    # Fetch the content from the URL
    stAcademic_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00467/Sapfile1.arff'
    with urlopen(stAcademic_url) as downloaded:
        status_code = downloaded.status
        payload = downloaded.read()
    return payload, status_code


@app.cell
def _(StringIO, loadarff, payload, pd, status_code):
    # Check if the request was successful
    if status_code == 200:
        # Parse the ARFF data
        arff_content = payload.decode('utf-8')
        arff_data = StringIO(arff_content)

        # Get the data and metadata
        arff_rows, meta = loadarff(arff_data)

        # Convert to Pandas DataFrame
        df = pd.DataFrame(arff_rows)

        # Decode byte strings if necessary
        for column in df.select_dtypes([object]).columns:
            if df[column].apply(lambda x: isinstance(x, bytes)).any():
                df[column] = df[column].str.decode('utf-8')

        print(df.head())
        print(meta)
    else:
        df = pd.DataFrame()
        meta = None
        print(f'Failed to download the file: {status_code}')
    return df, meta


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The metadata knows the column names. `describe` summarizes the numeric columns.
    """)
    return


@app.cell
def _(meta):
    column_names = meta.names()
    print('Column Names:', column_names)
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reading data from a `.json` file

    JavaScript Object Notation (JSON) is a common way to share data on the web.

    `read_json` reads a JSON file and returns a DataFrame. This example uses a countries file from data.world. `to_json` writes that DataFrame to `countries.json` in this folder.

    `describe` summarizes the numeric columns.
    """)
    return


@app.cell
def _(pd):
    df_countries = pd.read_json('https://query.data.world/s/6wc2blqdaxd6s2k3xmzmfx3zb72v7l')
    print(df_countries.shape)
    df_countries.head()
    return (df_countries,)


@app.cell
def _(df_countries):
    df_countries.describe()
    return


@app.cell
def _(df_countries):
    df_countries.to_json('countries.json')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    JSON can be nested. `json_normalize` flattens it into a table.

    In this example each person has a name, and each car also has a name. `meta_prefix` and `record_prefix` keep those names apart. The result has the columns `person_name`, `person_age`, `car_name`, and `car_models`.
    """)
    return


@app.cell
def _():
    from pandas import json_normalize

    # a simple JSON object
    data = [
        {
            'name': 'John',
            'age': 30,
            'cars': [
                {'name': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang']},
                {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
            ],
        },
        {
            'name': 'Peter',
            'age': 46,
            'cars': [
                {'name': 'Mercedes', 'models': ['E Class', 'S Class']},
            ],
        },
    ]

    # use json_normalize to flatten the data
    # give the fact that name is a column in the data, we need to specify the meta_prefix
    # and record_prefix to avoid conflicts
    # The final dataframe will contain columns: person_name, person_age, car_name, car_models
    cars = json_normalize(
        data,
        record_path='cars',
        meta=['name', 'age'],
        meta_prefix='person_',
        record_prefix='car_',
    )
    print(cars)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reading data from a `.xlsx` file

    `read_excel` reads an Excel workbook and returns a DataFrame. This cell loads the Immunotherapy dataset, [https://archive.ics.uci.edu/ml/datasets/Immunotherapy+Dataset](https://archive.ics.uci.edu/ml/datasets/Immunotherapy+Dataset). `openpyxl` is the library Pandas uses to read `.xlsx` files.
    """)
    return


@app.cell
def _(pd):
    import openpyxl

    df_immuno = pd.read_excel(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/00428/Immunotherapy.xlsx',
        engine='openpyxl',
    )
    print(df_immuno.shape)
    df_immuno.head()
    return (df_immuno,)


@app.cell
def _(df_immuno):
    df_immuno.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `read_csv` and `to_csv` move a table to and from a CSV file. `index=False` leaves the index out of the file.
    - `sep` sets the character between columns. `na_values` names the text that should become missing data. `names` supplies the column headers.
    - An ARFF file can be loaded with `loadarff` and turned into a DataFrame. Byte strings need to be decoded.
    - `read_json` and `to_json` handle JSON tables. `json_normalize` flattens nested records, and prefixes keep duplicate field names apart.
    - `read_excel` reads an `.xlsx` file. `describe` is a quick summary of the numeric columns after the load.

    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 3.
    """)
    return


if __name__ == "__main__":
    app.run()
