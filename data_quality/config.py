from pathlib import Path 

PROJECT_ROOT=Path(__file__).resolve().parents[1]

RAW_DATA=PROJECT_ROOT/ "raw_data"/ "output"

DIMENSIONS=RAW_DATA/ "dimensions"
FACTS=RAW_DATA/ "facts"

REPORTS = PROJECT_ROOT / "data_quality" / "reports"


#Now every validator simply imports
#from config import DIMENSIONS
#instead of repeating long paths.