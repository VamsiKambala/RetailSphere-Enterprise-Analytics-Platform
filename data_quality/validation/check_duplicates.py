import pandas as pd

def check_duplicates(
        dataframe=pd.DataFrame,
        table_name=str
):
    duplicate_count=int(dataframe.duplicated().sum())
    if duplicate_count==0:
        status="SUCCESS"
    else:
        status="FAILED"
    return{
        "Table":table_name,
        "Check":"Duplicate Rows",
        "Status":status,
        "DuplicateRows":duplicate_count,
        "RowChecked":len(dataframe)
    }