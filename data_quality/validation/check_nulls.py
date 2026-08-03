import pandas as pd

def check_nulls(
        dataframe:pd.DataFrame,
        required_columns:list,
        table_name:str
):
    null_summary={}
    status="PASSED"
    for column in required_columns:
        null_count=dataframe[column].isnull().sum()
        null_summary[column]=int(null_count)
        if null_count>0:
            status="FAILED"
    return{
        "Table":table_name,
        "Check":"Null_Validation",
        "Status": status,
        "RowsChecked": len(dataframe),
        "NullSummary": null_summary
    }