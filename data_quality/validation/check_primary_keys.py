import pandas as pd

def check_primary_key(
        dataframe:pd.DataFrame,
        primary_key:str,
        table_name:str
):
     """
    Checks whether the primary key column contains duplicates.
    """
     duplicate_count=int(dataframe[primary_key].duplicated().sum())
     if duplicate_count==0:
        status="PASSED"
     else:
        status="FAILED"
     return{
        "Table": table_name,

        "Check": "Primary Key",

        "Status": status,

        "DuplicateKeys": duplicate_count,

        "RowsChecked": len(dataframe)
     }

