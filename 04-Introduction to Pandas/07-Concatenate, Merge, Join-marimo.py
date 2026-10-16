import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd

    return mo, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Concatenate, Merge, Join

    ## Objectives

    - Stack and place DataFrames side by side with `concat`.
    - Keep every label, or only the shared labels, with `join='outer'` and `join='inner'`.
    - Combine DataFrames on a column with `merge`, using inner, outer, left, and right joins.
    - Combine DataFrames on their index with `join`.

    ## Background

    These operations combine tables the way a database does. `concat` stacks tables or places them side by side. `merge` matches rows by a column. `join` matches rows by the index.

    ## Datasets Used

    This lesson does not use an external dataset. The tables are written in the cells.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concatenate

    These three DataFrames have the same column names. `concat` stacks them vertically. The default axis is `0`, which means "add rows".
    """)
    return


@app.cell
def _(pd):
    df1 = pd.DataFrame({'A': [0, 1, 2], 'B': [0, 1, 2], 'C': [0, 1, 2]}, index=[0, 1, 2])
    df1
    return (df1,)


@app.cell
def _(pd):
    df2 = pd.DataFrame(
        {'A': [3, 4, 5, 6], 'B': [3, 4, 5, 6], 'C': [3, 4, 5, 6]},
        index=[3, 4, 5, 6],
    )
    df2
    return (df2,)


@app.cell
def _(pd):
    df3 = pd.DataFrame({'A': [7, 8, 9], 'B': [7, 8, 9], 'C': [7, 8, 9]}, index=[7, 8, 9])
    df3
    return (df3,)


@app.cell
def _(df1, df2, df3, pd):
    # concatenating dataframes
    frames = [df1, df2, df3]
    res = pd.concat(frames)
    res
    return frames, res


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The rows of the three tables are stacked: 3 + 4 + 3 = 10 rows, and the same 3 columns.
    """)
    return


@app.cell
def _(res):
    res.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `keys` adds an outer index, one label for each DataFrame in the list. `loc['c']` selects the block that came from `df3`. `loc['c', 9]` selects one row inside that block.
    """)
    return


@app.cell
def _(frames, pd):
    res1 = pd.concat(frames, keys=['a', 'b', 'c'])
    res1
    return (res1,)


@app.cell
def _(res1):
    res1.loc['c']
    return


@app.cell
def _(res1):
    res1.loc['c', 9]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `df4` has different column names and a partly shared index. Stacking `df1` and `df4` keeps every column. A row that does not have a column is filled with `NaN`.
    """)
    return


@app.cell
def _(pd):
    df4 = pd.DataFrame({'E': [1, 2, 3, 5], 'F': [1, 2, 3, 5]}, index=[1, 2, 3, 5])
    df4
    return (df4,)


@app.cell
def _(df1, df4, mo, pd):
    mo.Html(pd.concat([df1, df4]).to_html())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `axis=1` places the tables side by side and aligns them on the index.
    """)
    return


@app.cell
def _(df1, df4, mo, pd):
    res2 = pd.concat([df1, df4], axis=1)
    mo.Html(res2.to_html())
    return (res2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `reset_index` moves that index into a column called `index`, and numbers the rows from 0.
    """)
    return


@app.cell
def _(mo, res2):
    mo.Html(res2.reset_index().to_html())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `drop=True` discards the old index instead of keeping it as a column.
    """)
    return


@app.cell
def _(mo, res2):
    mo.Html(res2.reset_index(drop=True).to_html())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `join='inner'` keeps only the index labels that appear in both DataFrames. This is the same idea as an inner join of two tables. Here the shared labels are 1 and 2.
    """)
    return


@app.cell
def _(df1, df4, mo, pd):
    mo.Html(pd.concat([df1, df4], axis=1, join='inner').to_html())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `join='outer'` keeps every index label. It is the default, so this is the same table as `res2`. Missing cells are `NaN`. The result has every column and every row label from either DataFrame.
    """)
    return


@app.cell
def _(df1, df4, mo, pd):
    mo.Html(pd.concat([df1, df4], axis=1, join='outer').to_html())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Place `df1` and `df4` side by side with `concat`, keeping only the shared index labels. Replace `None` with your code. What fills a cell when `join` is `'outer'` instead?
    """)
    return


@app.cell
def _():
    student_shared = None
    student_shared
    return (student_shared,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_shared = pd.concat([df1, df4], axis=1, join='inner')
```
`NaN`. An outer concatenation keeps every index label, and a label that is missing from one table has missing cells.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Merge

    `merge` matches rows by a column. `how` chooses which rows to keep:

    - `inner`: only rows whose key is in both DataFrames.
    - `outer`: every row from both DataFrames. A key that is missing on one side is `NaN`.
    - `left`: every row from the first DataFrame, and the matching rows from the second.
    - `right`: every row from the second DataFrame, and the matching rows from the first.

    The picture of these four joins is not in this folder. The four cells below show the same four results.
    """)
    return


@app.cell
def _(pd):
    d1 = {
        'Customer_id': pd.Series([1, 2, 3, 4, 5, 6]),
        'Product': pd.Series(['Radio', 'Radio', 'Radio', 'Television', 'Television', 'Television']),
    }
    customers = pd.DataFrame(d1)
    customers
    return customers, d1


@app.cell
def _(pd):
    d2 = {
        'Customer_id': pd.Series([2, 4, 6, 8, 10]),
        'State': pd.Series(['Nevada', 'Nevada', 'Texas', 'Florida', 'Florida']),
    }
    states = pd.DataFrame(d2)
    states
    return states, d2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Inner join.** Customers 2, 4, and 6 are in both tables.
    """)
    return


@app.cell
def _(customers, pd, states):
    # inner join
    pd.merge(customers, states, on='Customer_id', how='inner')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Outer join.** Every customer id is kept. Product or state is missing where that id was in only one table.
    """)
    return


@app.cell
def _(customers, pd, states):
    # outer join
    pd.merge(customers, states, on='Customer_id', how='outer')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Left join.** Every row of `customers` is kept.
    """)
    return


@app.cell
def _(customers, pd, states):
    # left join
    pd.merge(customers, states, on='Customer_id', how='left')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Right join.** Every row of `states` is kept.
    """)
    return


@app.cell
def _(customers, pd, states):
    # right join
    pd.merge(customers, states, on='Customer_id', how='right')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Merge `customers` and `states` on `Customer_id`, keeping only keys that appear in both tables. Replace `None` with your code. Which rows does `how='left'` keep that this merge drops?
    """)
    return


@app.cell
def _():
    student_inner = None
    student_inner
    return (student_inner,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_inner = pd.merge(customers, states, on='Customer_id', how='inner')
```
Rows of `customers` whose `Customer_id` is not in `states`. A left merge keeps every customer. An inner merge keeps only the matches.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Join

    `join` combines columns by the index. It is a convenient way to place two DataFrames side by side when their indexes are the keys.

    Matching can also use a column, through the `on` argument, including columns that do not share a name. The examples below match on the index only.

    The default is a left join: every row of the DataFrame before the dot, plus the matching rows of the DataFrame inside the parentheses. `how='inner'` keeps only the shared index labels. The order of the call decides which columns come first.
    """)
    return


@app.cell
def _(pd):
    left = pd.DataFrame(
        {
            'Col_A': ['A0', 'A1', 'A2'],
            'Col_B': ['B0', 'B1', 'B2'],
        },
        index=['a', 'b', 'c'],
    )
    left
    return (left,)


@app.cell
def _(pd):
    right = pd.DataFrame(
        {
            'Col_C': ['C0', 'C1', 'C2'],
            'Col_D': ['D0', 'D1', 'D2'],
        },
        index=['a', 'c', 'd'],
    )
    right
    return (right,)


@app.cell
def _(left, right):
    # left join (rows from left dataframe and matching rows from right dataframe)
    left.join(right)
    return


@app.cell
def _(left, right):
    # rows from right dataframe and matching rows from left dataframe
    right.join(left)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `how='inner'` returns only the rows whose index label is in both tables.
    """)
    return


@app.cell
def _(left, right):
    left.join(right, how='inner')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same inner join with the tables reversed. The rows are the same, and the columns of `right` come first.
    """)
    return


@app.cell
def _(left, right):
    right.join(left, how='inner')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    Join `left` to the matching rows of `right` with `how='inner'`. Replace `None` with your code. Which labels does this result share with `left.join(right)` when `how` is left at its default?
    """)
    return


@app.cell
def _():
    student_index_join = None
    student_index_join
    return (student_index_join,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r'''
```python
student_index_join = left.join(right, how='inner')
```
The shared index labels. The default is a left join, so it also keeps labels that belong only to `left`, with `NaN` where `right` has no match.
''')}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Orders and their items

    `orders` has the order id and the time. `itemsByOrder` has the products in each order: `OrderID`, `Idx`, `Product`, and `Price`.

    A left merge keeps every order. Order 4 has no products, so its product columns are `NaN`. Order 5 is only in the items table, so a left merge from `orders` does not include it.

    An inner merge keeps only orders that have at least one item. The total price of each remaining order is the sum of its `Price` values.

    A real catalog would store a product id, look up the name and the price, and use a quantity when an order contains more than one of the same product.
    """)
    return


@app.cell
def _(pd):
    # Create the orders DataFrame
    orders = pd.DataFrame(
        {
            'ID': [1, 2, 3, 4],
            'timestamp': [
                '2024-06-01 12:34',
                '2024-06-02 15:20',
                '2024-06-03 08:50',
                '2024-06-04 10:10',
            ],
        }
    )
    orders
    return (orders,)


@app.cell
def _(pd):
    # Create the itemsByOrder DataFrame
    itemsByOrder = pd.DataFrame(
        {
            'OrderID': [1, 1, 2, 3, 5],
            'Idx': [1, 2, 1, 1, 1],
            'Product': ['Widget', 'Gadget', 'Sticker', 'Baloon', 'Helium'],
            'Price': [19.99, 29.99, 19.99, 24.99, 9.99],
        }
    )
    itemsByOrder
    return (itemsByOrder,)


@app.cell
def _(itemsByOrder, mo, orders, pd):
    # Perform a left join
    left_orders = pd.merge(orders, itemsByOrder, how='left', left_on='ID', right_on='OrderID')
    mo.Html(left_orders.to_html())
    return (left_orders,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Order 4 was never finished: it has no products. The inner join below keeps only orders that have items.
    """)
    return


@app.cell
def _(itemsByOrder, mo, orders, pd):
    # The correct join should be inner (we only want orders that have items)
    merged_df = pd.merge(orders, itemsByOrder, how='inner', left_on='ID', right_on='OrderID')
    mo.Html(merged_df.to_html())
    return (merged_df,)


@app.cell
def _(merged_df):
    for order_id in merged_df['OrderID'].unique():
        print(
            f'Total price for order {order_id}: '
            f'{merged_df[merged_df["OrderID"] == order_id].Price.sum()}'
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Try it yourself

    The first cell stacks `part_a` and `part_b`. The second places them side by side with `axis=1`. Change the values or the column names and run both cells again.
    """)
    return


@app.cell
def _(pd):
    part_a = pd.DataFrame({'A': [1, 2]})
    part_b = pd.DataFrame({'B': [3, 4]})
    pd.concat([part_a, part_b])
    return part_a, part_b


@app.cell
def _(part_a, part_b, pd):
    pd.concat([part_a, part_b], axis=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions

    **Key takeaways:**

    - `concat` stacks DataFrames by default. `axis=1` places them side by side and aligns the index.
    - `keys` builds an outer index so you can select one of the original blocks with `loc`.
    - `join='inner'` keeps shared labels. `join='outer'` keeps every label and fills the gaps with `NaN`.
    - `merge` matches a column. `how` is `inner`, `outer`, `left`, or `right`. `left_on` and `right_on` name the keys when the columns differ.
    - `join` matches the index. The DataFrame before the dot supplies the rows that a left join keeps.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Check your understanding

    1. What is the default direction of `concat`?
    2. What does `axis=1` change?
    3. What does `join='inner'` keep, and what does `join='outer'` put in the gaps?
    4. What does `keys` add to a concatenation?
    5. Which argument of `merge` chooses inner, outer, left, or right?
    6. When do you use `left_on` and `right_on` instead of `on`?
    7. What does `join` match, and whose rows does the default join keep?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"Show answers": mo.md(r"""
1. **Down the rows:** `axis=0` stacks the tables.
2. **The tables sit side by side:** Rows are aligned by the index.
3. **Shared labels, and `NaN`:** An inner join keeps labels that appear in both tables. An outer join keeps every label and fills a missing side with `NaN`.
4. **An outer index:** `loc` can then select one of the original blocks.
5. **`how`:** `inner` keeps matching keys, `outer` keeps every key, and `left` or `right` keeps one side.
6. **When the key columns have different names:** `on` is for a shared column name.
7. **The index:** The default is a left join, so the DataFrame before the dot supplies the rows that are kept.
""")}, lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - VanderPlas, J. (2017). *Python Data Science Handbook: Essential Tools for Working with Data*. O'Reilly Media. Chapter 3.
    """)
    return


if __name__ == "__main__":
    app.run()
