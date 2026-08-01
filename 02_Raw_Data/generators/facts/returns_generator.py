import pandas as pd
import random
from pathlib import Path
from datetime import timedelta

# ============================================================
# Configuration
# ============================================================

RETURN_RATE = 0.07

RETURN_CONDITIONS = {
    "Sealed": 25,
    "Opened": 40,
    "Damaged": 20,
    "Defective": 15
}

# ============================================================
# Project Root
# ============================================================

project_root = Path(__file__).resolve().parents[2]

# ============================================================
# Read Order Items
# ============================================================

order_items = pd.read_csv(
    project_root
    / "output"
    / "facts"
    / "order_items.csv"
)

# ============================================================
# Read Orders
# ============================================================

orders = pd.read_csv(
    project_root
    / "output"
    / "facts"
    / "orders.csv"
)

orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

# ============================================================
# Read Return Reasons
# ============================================================

return_reasons = pd.read_csv(
    project_root
    / "lookup"
    / "return_reason.csv"
)

# ============================================================
# Merge Order Date
# ============================================================

order_items = order_items.merge(
    orders[
        ["OrderID", "OrderDate"]
    ],
    on="OrderID",
    how="left"
)

# ============================================================
# Generate Returns
# ============================================================

returns = []

return_counter = 1

for _, item in order_items.iterrows():

    if random.random() > RETURN_RATE:
        continue

    return_id = f"RET{return_counter:07}"

    order_item_id = item["OrderItemID"]

    order_date = item["OrderDate"]

    return_reason_id = random.choice(
        return_reasons["ReturnReasonID"]
    )

    return_condition = random.choices(
        population=list(RETURN_CONDITIONS.keys()),
        weights=list(RETURN_CONDITIONS.values()),
        k=1
    )[0]

    return_date = (
        pd.to_datetime(order_date)
        + timedelta(days=random.randint(2, 15))
    )

    returns.append({

        "ReturnID": return_id,

        "OrderItemID": order_item_id,

        "ReturnReasonID": return_reason_id,

        "ReturnDate": return_date.date(),

        "ReturnCondition": return_condition

    })

    return_counter += 1

# ============================================================
# DataFrame
# ============================================================

returns_df = pd.DataFrame(returns)

# ============================================================
# Save CSV
# ============================================================

output_path = project_root / "output" / "facts"

output_path.mkdir(
    parents=True,
    exist_ok=True
)

returns_df.to_csv(
    output_path / "returns.csv",
    index=False
)

# ============================================================
# Validation
# ============================================================

print(returns_df.head())

print(f"\nRows Created : {len(returns_df)}")

print("\nDuplicate Return IDs")
print(returns_df["ReturnID"].duplicated().sum())

print("\nDuplicate OrderItem IDs")
print(returns_df["OrderItemID"].duplicated().sum())

print("\nMissing Values")
print(returns_df.isnull().sum())

print("\nReturn Conditions")
print(
    returns_df["ReturnCondition"]
    .value_counts()
)

print("\nReturn Reasons")
print(
    returns_df["ReturnReasonID"]
    .value_counts()
    .sort_index()
)