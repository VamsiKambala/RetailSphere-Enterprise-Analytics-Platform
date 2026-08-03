import pandas as pd

def check_foreign_key(
        child_df:pd.DataFrame,
        child_column:str,
        parent_df:pd.DataFrame,
        parent_column:str,
        relationship_name:str
):
    invalid_records=int((~child_df[child_column].isin(parent_df[parent_column])).sum())
    if invalid_records==0:
        status="PASSED"
    else:
        status="FAILED"
    return{
        "Relationship": relationship_name,
        "Check": "Foreign Key",
        "Status": status,
        "InvalidRecords": invalid_records,
        "RowsChecked": len(child_df)
    }