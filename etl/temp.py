from database import get_connection
# from config import STAGING_DATABASE

# # connection=get_connection(
# #     STAGING_DATABASE
# # )
# # print(connection)
# # connection.close()
from pathlib import Path
from extractor import extract_csv

from config import RAW_DATA,PROJECT_ROOT

customers=extract_csv(
    PROJECT_ROOT/ "raw_data" /"lookup" /
    "categories.csv"
)


from metadata import add_metadata


customers = add_metadata(
    customers,
    source_file="customers.csv",
    batch_id="BATCH_001"
)

print(type(customers))
