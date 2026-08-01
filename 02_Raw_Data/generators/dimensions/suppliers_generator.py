import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")

# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

NUMBER_OF_SUPPLIERS = 80

SUPPLIER_CATALOG = {

    "Electronics": [
        "Samsung India",
        "Apple India",
        "Sony India",
        "Dell Technologies",
        "Lenovo India",
        "HP India",
        "LG Electronics",
        "Acer India"
    ],

    "Fashion": [
        "Nike India",
        "Adidas India",
        "Puma India",
        "Levi Strauss",
        "Allen Solly",
        "Bata India",
        "Zara India"
    ],

    "Grocery": [
        "Nestlé India",
        "ITC Foods",
        "Britannia",
        "Amul",
        "Parle",
        "Tata Consumer",
        "Fortune Foods",
        "Coca-Cola India",
        "PepsiCo India"
    ]
}

SUPPLIER_RATINGS = {
    5: 20,
    4: 45,
    3: 25,
    2: 8,
    1: 2
}

ACTIVE_STATUS = {
    "Yes": 98,
    "No": 2
}

# -----------------------------------------------------
# Read cities.csv
# -----------------------------------------------------

project_root = Path(__file__).resolve().parents[2]

cities_path = project_root / "lookup" / "cities.csv"

cities = pd.read_csv(cities_path)

# -----------------------------------------------------
# Generate Suppliers
# -----------------------------------------------------


market_weights = {
    "Metro": 10,
    "Urban": 4,
    "Semi-Urban": 1
}

cities["Weight"] = cities["MarketType"].map(market_weights)




suppliers = []

for i in range(1, NUMBER_OF_SUPPLIERS + 1):

    supplier_id = f"SUP{i:04}"

    # Category
    category = random.choice(
        list(SUPPLIER_CATALOG.keys())
    )

    # Supplier Company
    supplier_company = random.choice(
        SUPPLIER_CATALOG[category]
    )

    # City
    city_id = random.choices(
        population=cities["CityID"],
        weights=cities["Weight"],
        k=1
    )[0]

    city = cities.loc[
        cities["CityID"] == city_id,
        "City"
    ].values[0]

    # Supplier Name
    supplier_name = f"{supplier_company} - {city}"

    # Contact Person
    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        contact_person = fake.name_male()
    else:
        contact_person = fake.name_female()

    # Email
    email = f"{supplier_id.lower()}@retailsphere.com"

    # Phone Number
    phone_number = f"9{random.randint(100000000,999999999)}"

    # GST Number (Simple Fake Format)
    gst_number = (
        f"{random.randint(10,38)}"
        f"{fake.bothify(text='?????#####?')}"
        "1Z5"
    )

    # Registration Date
    registration_date = fake.date_between(
        start_date="-15y",
        end_date="today"
    )

    # Rating
    rating = random.choices(
        population=list(SUPPLIER_RATINGS.keys()),
        weights=list(SUPPLIER_RATINGS.values()),
        k=1
    )[0]

    # Active Status
    is_active = random.choices(
        population=list(ACTIVE_STATUS.keys()),
        weights=list(ACTIVE_STATUS.values()),
        k=1
    )[0]

    supplier = {

        "SupplierID": supplier_id,
        "SupplierName": supplier_name,
        "PrimaryCategory": category,
        "CityID": city_id,
        "ContactPerson": contact_person,
        "Email": email,
        "PhoneNumber": phone_number,
        "GSTNumber": gst_number,
        "RegistrationDate": registration_date,
        "Rating": rating,
        "IsActive": is_active

    }

    suppliers.append(supplier)

# -----------------------------------------------------
# Create DataFrame
# -----------------------------------------------------

suppliers_df = pd.DataFrame(suppliers)

# -----------------------------------------------------
# Save CSV
# -----------------------------------------------------

output_path = project_root / "output" / "dimensions"

output_path.mkdir(
    parents=True,
    exist_ok=True
)

suppliers_df.to_csv(
    output_path / "suppliers.csv",
    index=False
)

# -----------------------------------------------------
# Validation
# -----------------------------------------------------

print(suppliers_df.head())

print(f"Rows Created : {len(suppliers_df)}")

print("\nDuplicate Supplier IDs")
print(suppliers_df["SupplierID"].duplicated().sum())

print("\nMissing Values")
print(suppliers_df.isnull().sum())

print("\nPrimary Category Distribution")
print(suppliers_df["PrimaryCategory"].value_counts())

print("\nSupplier Ratings")
print(suppliers_df["Rating"].value_counts())

print("\nActive Status")
print(suppliers_df["IsActive"].value_counts())