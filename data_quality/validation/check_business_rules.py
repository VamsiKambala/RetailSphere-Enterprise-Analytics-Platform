import pandas as pd

def validate_positive_values(
    dataframe:pd.DataFrame,  
    column:str,
    table_name:str
#selling_price,quantity,payment
):
    invalid_records=int((dataframe[column]<=0).sum())
    status="PASSED"
    if invalid_records>0:
        status="FAILED"
    return{
        "Table":table_name,
        "Check":f"{column} > 0",
        "Status":status,
        "InvalidRecords":invalid_records,
        "RowsChecked":len(dataframe)
    }


def validate_rating(
        dataframe,
        column,
        table_name
):
    invalid=int((
        dataframe[column]<1
    )|(dataframe[column]>5)
    ).sum()
    status="PASSED"
    if invalid>0:
        status="FAILED"
    return{
        "Table":table_name,
        "Check":"Invalid_Rating",
        "Status":status,
        "InvalidRecords":invalid,
        "RowsChecked":len(dataframe)
    }

def validate_dates(
    dataframe,
    start_column,
    end_column,
    table_name
):

    invalid = int(

        (

            dataframe[end_column]

            <

            dataframe[start_column]

        ).sum()

    )

    if invalid>0:
            status="FAILED"
    return{
            "Table":table_name,
            "Check":"Invalid_Date",
            "Status":status,
            "InvalidRecords":invalid,
            "RowsChecked":len(dataframe)
        }