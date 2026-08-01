import pandas as pd
import random
from pathlib import Path

# ============================================================
# Project Root
# ============================================================

project_root = Path(__file__).resolve().parents[2]

# ============================================================
# Read Files
# ============================================================

products = pd.read_csv(
    project_root / "output" / "dimensions" / "products.csv"
)

stores = pd.read_csv(
    project_root / "output" / "dimensions" / "stores.csv"
)

orders = pd.read_csv(
    project_root / "output" / "facts" / "orders.csv"
)

order_items = pd.read_csv(
    project_root / "output" / "facts" / "order_items.csv"
)

returns = pd.read_csv(
    project_root / "output" / "facts" / "returns.csv"
)

# ============================================================
# Merge Store & Order Date into Order Items
# ============================================================

order_items = order_items.merge(
    orders[
        ["OrderID", "StoreID", "OrderDate"]
    ],
    on="OrderID",
    how="left"
)

# ============================================================
# Merge Return Date
# ============================================================

returns = returns.merge(
    order_items[
        ["OrderItemID", "ProductID", "StoreID"]
    ],
    on="OrderItemID",
    how="left"
)

# ============================================================
# Inventory Transactions
# ============================================================

inventory = []

transaction_counter = 1

# ============================================================
# 1. Opening Stock
# ============================================================

for _, store in stores.iterrows():

    store_id = store["StoreID"]

    for _, product in products.iterrows():

        inventory.append({

            "InventoryTransactionID":
                f"INV{transaction_counter:08}",

            "ProductID":
                product["Product_id"],

            "StoreID":
                store_id,

            "TransactionDate":
                "2024-01-01",

            "TransactionTypeID":
                1,

            "Quantity":
                random.randint(100,300),

            "SourceType":
                "Opening Stock",

            "ReferenceID":
                "Opening Stock"

        })

        transaction_counter += 1

# ============================================================
# 2. Sales
# ============================================================

for _, row in order_items.iterrows():

    inventory.append({

        "InventoryTransactionID":
            f"INV{transaction_counter:08}",

        "ProductID":
            row["ProductID"],

        "StoreID":
            row["StoreID"],

        "TransactionDate":
            row["OrderDate"],

        "TransactionTypeID":
            2,

        "Quantity":
            -row["Quantity"],

        "SourceType":
            "Order",

        "ReferenceID":
            row["OrderID"]

    })

    transaction_counter += 1

# ============================================================
# 3. Customer Returns
# ============================================================

returns = returns.merge(
    order_items[
        ["OrderItemID", "Quantity"]
    ],
    on="OrderItemID",
    how="left"
)

for _, row in returns.iterrows():

    inventory.append({

        "InventoryTransactionID":
            f"INV{transaction_counter:08}",

        "ProductID":
            row["ProductID"],

        "StoreID":
            row["StoreID"],

        "TransactionDate":
            row["ReturnDate"],

        "TransactionTypeID":
            3,

        "Quantity":
            row["Quantity"],

        "SourceType":
            "Return",

        "ReferenceID":
            row["ReturnID"]

    })

    transaction_counter += 1

# ============================================================
# DataFrame
# ============================================================

inventory_df = pd.DataFrame(inventory)

# ============================================================
# Save CSV
# ============================================================

output_path = project_root / "output" / "facts"

output_path.mkdir(
    parents=True,
    exist_ok=True
)

inventory_df.to_csv(
    output_path / "inventory_transactions.csv",
    index=False
)

# ============================================================
# Validation
# ============================================================

print(inventory_df.head())

print(f"\nRows Created : {len(inventory_df)}")

print("\nDuplicate Transaction IDs")
print(
    inventory_df["InventoryTransactionID"]
    .duplicated()
    .sum()
)

print("\nMissing Values")
print(
    inventory_df.isnull().sum()
)

print("\nTransaction Types")
print(
    inventory_df["TransactionTypeID"]
    .value_counts()
    .sort_index()
)

print("\nSource Types")
print(
    inventory_df["SourceType"]
    .value_counts()
)