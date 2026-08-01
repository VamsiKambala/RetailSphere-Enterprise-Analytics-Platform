import pandas as pd
from faker import Faker
import random
from pathlib import Path
from datetime import date
from dateutil.relativedelta import relativedelta

fake=Faker("en_IN")

#configuration
NUMBER_OF_CUSTOMERS = 100000

#Read cities.csv
project_root=Path(__file__).resolve().parents[2]
cities_path=project_root / "lookup" / "cities.csv"
cities=pd.read_csv(cities_path)

CUSTOMER_TYPES={
    "Regular":85,
    "Premium":12,
    "VIP":3
}

ACTIVE_STATUS={
    "Yes":98,
    "No":2
}

market_weights={
    "Metro":10,
    "Urban":4,
    "Semi-Urban": 1
}

cities["Weight"]=cities["MarketType"].map(market_weights)

customers=[]

for i in range(1,NUMBER_OF_CUSTOMERS+1):
    customer_id=f"C{i:06}"
    customer_name = fake.name()
    date_of_birth=fake.date_between(
            start_date="-70y",
            end_date="-18y"
    )
    city_id=random.choices(
        population=cities["CityID"],
        weights=cities["Weight"],
        k=1
    )[0]
    email = f"{customer_id.lower()}@customer.retailsphere.com"
    phone_number =f"9{random.randint(100000000,999999999)}"
    registration_start = date_of_birth + relativedelta(years=18)
    registration_date=fake.date_between(
        start_date=registration_start,
        end_date="today"
    )
    customer_type=random.choices(
        population=list(CUSTOMER_TYPES.keys()),
        weights=list(CUSTOMER_TYPES.values()),
        k=1
    )[0]
    is_active=random.choices(
        population=list(ACTIVE_STATUS.keys()),
        weights=list(ACTIVE_STATUS.values()),
        k=1
    )[0]
    customer = {
    "CustomerID": customer_id,
    "CustomerName": customer_name,
    "DateOfBirth": date_of_birth,
    "CityID": city_id,
    "Email": email,
    "PhoneNumber": phone_number,
    "RegistrationDate": registration_date,
    "CustomerType": customer_type,
    "IsActive": is_active
    }
    customers.append(customer)

customers_df=pd.DataFrame(customers)
output_path=project_root/ "output" / "dimensions"
output_path.mkdir(parents=True,exist_ok=True)

customers_df.to_csv(output_path/"customers.csv",index=False)

print(customers_df.head())
print(f"Rows Created : {len(customers_df)}")
print(len(customers_df))

print(customers_df["CustomerID"].duplicated().sum())

print(customers_df.isnull().sum())

print(customers_df["CustomerType"].value_counts())

print(customers_df["IsActive"].value_counts())

print(customers_df["CityID"].value_counts().head(10))
    
