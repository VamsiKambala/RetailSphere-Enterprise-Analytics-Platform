import pandas as pd
import random
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

PAYMENT_METHOD_WEIGHTS = {
    1: 15,   # Credit Card
    2: 10,   # Debit Card
    3: 35,   # UPI
    4: 8,    # Net Banking
    5: 2,    # Cash
    6: 10,   # Cash on Delivery
    7: 8,    # Wallet
    8: 4,    # EMI
    9: 2,    # Gift Card
    10: 2,   # Store Credit
    11: 2,   # Buy Now Pay Later
    12: 2    # Bank Transfer
}

PAYMENT_STATUS_WEIGHTS = {
    1: 94,   # Success
    2: 3,    # Pending
    3: 2,    # Failed
    4: 1     # Refunded
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
# Read Lookup Tables
# ============================================================

payment_methods = pd.read_csv(
    project_root
    / "lookup"
    / "payments_method.csv"
)

payment_status = pd.read_csv(
    project_root
    / "lookup"
    / "payment_status.csv"
)

# ============================================================
# Generate Payments
# ============================================================

payments = []

for i, (_, order) in enumerate(orders.iterrows(), start=1):

    payment_id = f"PAY{i:07}"

    order_id = order["OrderID"]

    payment_date = order["OrderDate"]

    payment_method_id = random.choices(
        population=list(PAYMENT_METHOD_WEIGHTS.keys()),
        weights=list(PAYMENT_METHOD_WEIGHTS.values()),
        k=1
    )[0]

    payment_status_id = random.choices(
        population=list(PAYMENT_STATUS_WEIGHTS.keys()),
        weights=list(PAYMENT_STATUS_WEIGHTS.values()),
        k=1
    )[0]

    transaction_reference = f"TXN{i:010}"

    payment = {

        "PaymentID": payment_id,

        "OrderID": order_id,

        "PaymentMethodID": payment_method_id,

        "PaymentStatusID": payment_status_id,

        "PaymentDate": payment_date,

        "TransactionReference": transaction_reference

    }

    payments.append(payment)

# ============================================================
# DataFrame
# ============================================================

payments_df = pd.DataFrame(payments)

# ============================================================
# Save CSV
# ============================================================

output_path = project_root / "output" / "facts"

output_path.mkdir(
    parents=True,
    exist_ok=True
)

payments_df.to_csv(
    output_path / "payments.csv",
    index=False
)

# ============================================================
# Validation
# ============================================================

print(payments_df.head())

print(f"\nRows Created : {len(payments_df)}")

print("\nDuplicate Payment IDs")
print(payments_df["PaymentID"].duplicated().sum())

print("\nMissing Values")
print(payments_df.isnull().sum())

print("\nPayment Method Distribution")
print(payments_df["PaymentMethodID"].value_counts().sort_index())

print("\nPayment Status Distribution")
print(payments_df["PaymentStatusID"].value_counts().sort_index())

print("\nUnique Transaction References")
print(payments_df["TransactionReference"].duplicated().sum())

print("\nSuccessful")