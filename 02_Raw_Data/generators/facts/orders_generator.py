import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

NUMBER_OF_ORDERS = 50000

ORDER_CHANNELS = {
    "Store": 75,
    "Online": 25
}

# -------------------------------------------------------
# Project Path
# -------------------------------------------------------

project_root = Path(__file__).resolve().parents[2]

# -------------------------------------------------------
# Read Master Tables
# -------------------------------------------------------

customers = pd.read_csv(
    project_root / "output" / "dimensions" / "customers.csv"
)

stores = pd.read_csv(
    project_root / "output" / "dimensions" / "stores.csv"
)

employees = pd.read_csv(
    project_root / "output" / "dimensions" / "employees.csv"
)

calendar = pd.read_csv(
    project_root / "output" / "dimensions" / "calendar.csv"
)

# -------------------------------------------------------
# Read Lookup Tables
# -------------------------------------------------------

order_status = pd.read_csv(
    project_root / "lookup" / "order_status.csv"
)

promotion_type = pd.read_csv(
    project_root / "lookup" / "promotion_type.csv"
)

# -------------------------------------------------------
# Generate Orders
# -------------------------------------------------------

orders = []

for i in range(1, NUMBER_OF_ORDERS + 1):

    # Order ID
    order_id = f"ORD{i:07}"

    # Customer
    customer_id = random.choice(
        customers["CustomerID"]
    )

    # Store
    store_id = random.choice(
        stores["StoreID"]
    )

    # Employee (only from selected store)
    store_employees = employees[
        employees["StoreID"] == store_id
    ]

    employee_id = random.choice(
        store_employees["EmployeeID"].tolist()
    )

    # Order Date
    order_date = random.choice(
        calendar["Date"]
    )   # Change "Date" if your calendar column name is different

    # Order Channel
    order_channel = random.choices(
        population=list(ORDER_CHANNELS.keys()),
        weights=list(ORDER_CHANNELS.values()),
        k=1
    )[0]

    # Order Status
    order_status_value = random.choice(
        order_status["OrderStatus"]
    )   # Change column name if needed

    # Promotion
    promotion = random.choice(
        promotion_type["PromotionType"]
    )   # Change column name if needed

    # Order Dictionary
    order = {

        "OrderID": order_id,
        "CustomerID": customer_id,
        "StoreID": store_id,
        "EmployeeID": employee_id,
        "OrderDate": order_date,
        "OrderChannel": order_channel,
        "OrderStatus": order_status_value,
        "PromotionType": promotion

    }

    orders.append(order)

# -------------------------------------------------------
# DataFrame
# -------------------------------------------------------

orders_df = pd.DataFrame(orders)

# -------------------------------------------------------
# Save CSV
# -------------------------------------------------------

output_path = project_root / "output" / "facts"

output_path.mkdir(
    parents=True,
    exist_ok=True
)

orders_df.to_csv(
    output_path / "orders.csv",
    index=False
)

# -------------------------------------------------------
# Validation
# -------------------------------------------------------

print(orders_df.head())

print(f"Rows Created : {len(orders_df)}")

print("\nDuplicate Order IDs")
print(orders_df["OrderID"].duplicated().sum())

print("\nMissing Values")
print(orders_df.isnull().sum())

print("\nOrder Channels")
print(orders_df["OrderChannel"].value_counts())

print("\nOrder Status")
print(orders_df["OrderStatus"].value_counts())

print("\nPromotion Types")
print(orders_df["PromotionType"].value_counts())