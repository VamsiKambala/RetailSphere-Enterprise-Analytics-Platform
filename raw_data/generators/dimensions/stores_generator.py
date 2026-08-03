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

cities_path=project_root/ "lookup" / "cities.csv"
#02_Raw_Data/lookup/regions.csv

#Read the CSV
cities=pd.read_csv(cities_path)

market_weights = {
    "Metro": 10,
    "Urban": 4,
    "Semi-Urban": 1
    }
cities["Weight"] = cities["MarketType"].map(market_weights)

stores=[]
for i in range(1,201):
    store_id=f"ST{i:04}"
    city_id = random.choices(
    population=cities["CityID"],
    weights=cities["Weight"],
    k=1
    )[0]
    city=cities.loc[
    cities["CityID"]==city_id,
    "City"
    ].values[0]
    store_name = f"RetailSphere {city} {store_id}"
    manager_name = fake.name()
    store_type = random.choices([
    "Physical Store",
    "Warehouse",
    "Distribution Center"],
    weights=[90, 7, 3],
    k=1
    )[0]
    contact_number = f"9{random.randint(100000000,999999999)}"
    opening_date = fake.date_between(
    start_date="-10y",
    end_date="today"
    )
    is_active = random.choices(["Yes", "No"],weights=[98,2],k=1)[0]
    email = f"{store_id.lower()}@retailsphere.com"


    store={
    "StoreID":store_id, # Always make this number 4 digits long
    "CityID": city_id,
    "ManagerName":manager_name,
    "StoreName":store_name,
    "StoreType":store_type,
    "ContactNumber":contact_number,
    "OpeningDate":opening_date,
    "IsActive":is_active,
    "Email":email
    }
    stores.append(store)

stores_df = pd.DataFrame(stores)
print(stores_df.head())

output_path = project_root / "output" / "dimensions"
output_path.mkdir(parents=True, exist_ok=True)

stores_df.to_csv(
    output_path / "stores.csv",
    index=False
)

# print(len(stores_df))
# print(stores_df["StoreID"].duplicated().sum())
# print(stores_df["Email"].duplicated().sum())
# print(stores_df.isnull().sum())
# print(stores_df["StoreType"].value_counts())
# print(stores_df["IsActive"].value_counts())
# print(stores_df["CityID"].value_counts().head(15))    