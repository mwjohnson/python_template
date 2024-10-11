

## Filter Dataframe Between Dates
```
def filter_dataframe_by_dates(df, start_date, end_date, date_column_name):
    """
    start_date = datetime.datetime(year=2021, month=1,day=1)
    start_date
    end_date = datetime.datetime(year=2021, month=12, day=31)
    end_date
    """
    mask = (df[date_column_name] > start_date) & (df[date_column_name] <= end_date)
    return w.loc[mask]
```

## Group by Column
`x = df.groupby('ColX')['Col_to_sum'].agg('sum').reset_index()`

## Rename Column
`df = df.rename(columns={'Source_Name': 'Target_Name'})`

## Merge two DataFrames based on a column
`df_merged = pd.merge(df1, df2, on='Col_to_merge_on')`

# Jupyter Notebook

## Print multiple lines of output
```
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```


