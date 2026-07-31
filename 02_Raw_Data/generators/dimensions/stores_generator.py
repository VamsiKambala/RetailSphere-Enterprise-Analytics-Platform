import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake=Faker("en_IN") 
#Because we are creating an Indian company.


#Read regions.csv

project_root=Path(__file__).resolve().parents[2]
#Since stores_generator.py is inside generators/dimensions, 
#we first locate the 02_Raw_Data folder.

#Build the path

regions_path=project_root/ "lookup" / "regions.csv"
#02_Raw_Data/lookup/regions.csv

#Read the CSV
regions=pd.read_csv(regions_path)

#Columns to create

# StoreID	Python
# StoreName	Python
# StoreType	random.choice()
# RegionID	random.choice(regions["RegionID"])
# City	From regions.csv
# OpeningDate	Random date
# ManagerName	Faker
# ContactNumber	Faker
# Email	Python
# IsActive	Random

# 1-Generate StoreID

i=1
store_id=f"ST{i:04}" # Always make this number 4 digits long
print(store_id)

# 1.1 Pick a Region
region_id=random.choice(regions["RegionID"])

#1.2 Find the State for that Region
state=regions.loc[
    regions["RegionID"]==region_id,
    "State"
].values[0]
print(state)
#.loc means - Give me the rows where the condition is True."
# regions["RegionID"] == region_id creates a Boolean condition (True/False) to identify 
# the row where the selected RegionID matches. The .loc[row_condition, "State"] method 
# then filters the DataFrame using that condition and returns only the value(s) from the 
# "State" column for the matching row as a pandas Series. The .values attribute converts 
# that Series into a NumPy array, and [0] extracts the first (and in this case, only) 
# element from the array, giving the actual state name as a string.

#1.3-Generate One Store

for i in range(1,6):

    store_id=f"ST{i:04}" # Always make this number 4 digits long
    print(store_id)


store_id = "ST0001"

store_type = random.choice([
    "Physical Store",
    "Warehouse",
    "Distribution Center"
])

region_id = random.choice(regions["RegionID"])

state = regions.loc[
    regions["RegionID"] == region_id,
    "State"
].values[0]

manager_name = fake.name()

contact_number = fake.phone_number()

opening_date = fake.date_between(
    start_date="-10y",
    end_date="today"
)

is_active = random.choice(["Yes", "No"])
store_name = f"RetailSphere {state}"
email = state.lower().replace(" ", "") + "@retailsphere.com"
print(store_id)
print(store_name)
print(store_type)
print(region_id)
print(state)
print(manager_name)
print(contact_number)
print(opening_date)
print(email)
print(is_active)
