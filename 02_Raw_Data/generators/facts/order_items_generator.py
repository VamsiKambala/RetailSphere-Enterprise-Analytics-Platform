import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")

# ============================================================
# Configuration
# ============================================================

MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 5

GST_RATE = 0.18

DISCOUNT_PERCENTAGES = {
    0: 50,
    5: 20,
    10: 15,
    15: 8,
    20: 5,
    25: 2
}

# ============================================================
# Project Root
# ============================================================

project_root = Path(__file__).resolve().parents[2]

# ============================================================
# Read Orders
# ============================================================

orders = pd.read_csv(
    project_root
    / "output"
    / "facts"
    / "orders.csv"
)

# ============================================================
# Read Products
# ============================================================

products = pd.read_csv(
    project_root
    / "output"
    / "dimensions"
    / "products.csv"
)

# ============================================================
# Empty List
# ============================================================

order_items = []

order_item_counter = 1

# ============================================================
# Generate Order Items
# ============================================================

for _, order in orders.iterrows():

    order_id = order["OrderID"]

    # --------------------------------------------------------
    # Decide how many products are in this order
    # --------------------------------------------------------

    number_of_products = random.choices(
    population=[1,2,3,4,5],
    weights=[45,30,15,7,3],
    k=1
    )[0]

    # --------------------------------------------------------
    # Select Unique Products
    # --------------------------------------------------------

    selected_products = products.sample(
        n=number_of_products,
        replace=False
    )

    # --------------------------------------------------------
    # Generate One Row Per Product
    # --------------------------------------------------------
    line_number = 1
    for _, product in selected_products.iterrows():

        order_item_id = f"OI{order_item_counter:08}"

        product_id = product["Product_id"]

        unit_price = product["SellingPrice"]

        # Quantity
        quantity = random.choices(
            population=[1, 2, 3, 4, 5],
            weights=[45, 25, 15, 10, 5],
            k=1
        )[0]
                # --------------------------------------------------------
        # --------------------------------------------------------
        # Discount Percentage
        # --------------------------------------------------------

        discount_percent = random.choices(
            population=list(DISCOUNT_PERCENTAGES.keys()),
            weights=list(DISCOUNT_PERCENTAGES.values()),
            k=1
        )[0]


        order_item = {

            "OrderItemID": order_item_id,

            "OrderID": order_id,
             "LineNumber": line_number,

            "ProductID": product_id,

            "Quantity": quantity,

            "UnitPrice": unit_price,

            "DiscountPercent": discount_percent,

        }

        order_items.append(order_item)

        order_item_counter += 1
        line_number += 1

order_items_df = pd.DataFrame(order_items)

output_path = project_root / "output" / "facts"

output_path.mkdir(
    parents=True,
    exist_ok=True
)

order_items_df.to_csv(
    output_path / "order_items.csv",
    index=False
)


print("=" * 60)
print("ORDER ITEMS SUMMARY")
print("=" * 60)

print(f"Rows Created : {len(order_items_df)}")

print("\nDuplicate OrderItemID")
print(order_items_df["OrderItemID"].duplicated().sum())

print("\nMissing Values")
print(order_items_df.isnull().sum())

print("\nAverage Items Per Order")
print(
    round(
        len(order_items_df) / len(orders),
        2
    )
)

print("\nQuantity Distribution")
print(order_items_df["Quantity"].value_counts().sort_index())

print("\nDiscount Distribution")
print(order_items_df["DiscountPercent"].value_counts().sort_index())

print("\nAverage Items Per Order")
print(
    round(
        len(order_items_df) /
        orders["OrderID"].nunique(),
        2
    )
)
print("Successfull")