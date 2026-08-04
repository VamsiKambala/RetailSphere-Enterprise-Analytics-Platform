extractor.py → Reads CSV files.It only reads files.It knows nothing about MySQL.It knows nothing about staging.
Read data from any source and return it as a DataFrame.


loader.py → Loads DataFrames into MySQL.

metadata.py → Adds BatchID, SourceFile, and LoadTimestamp.It never reads CSVs.It never inserts into MySQL.It only adds metadata.

logger.py → Writes ETL logs.

report_generator.py → Produces ETL execution reports.

run_etl.py → Orchestrates the entire pipeline.It doesn't read CSVs.
It doesn't connect to MySQL.
It simply orchestrates everything.

config.py → Holds configuration (paths, database names, table mappings).

database.py ->This module knows how to connect to MySQL.