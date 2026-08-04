from datetime import datetime
import pandas as pd

def add_metadata(
        dataframe:pd.DataFrame,
        source_file:str,
        batch_id:str
) -> pd.DataFrame:
    dataframe["BatchID"]=batch_id
    dataframe["SourceFile"]=source_file
    dataframe["LoadTimestamp"]=datetime.now().replace(microsecond=0)
    
    return dataframe