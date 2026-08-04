import pandas as pd

def extract_csv(
        file_path
)-> pd.DataFrame:
    dataframe=pd.read_csv(file_path)
    return dataframe