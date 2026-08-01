import pandas as pd
import random
from pathlib import Path
from datetime import timedelta

# ============================================================
# Configuration
# ============================================================

SHIPMENT_STATUS_WEIGHTS = {
    1: 85,   # Delivered
    2: 8,    # In Transit
    3: 4,    # Out for Delivery
    4: 2,    # Returned
    5: 1     # Lost
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

orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

# ============================================================
# Read Lookup Tables
# ============================================================

delivery_partners = pd.read_csv(
    project_root
    / "lookup"
    / "delivery_partners.csv"
)

shipment_status = pd.read_csv(
    project_root
    / "lookup"
    / "shipment_status.csv"
)

# ============================================================
# Generate Shipments
# ============================================================

shipments = []

for i, (_, order) in enumerate(orders.iterrows(), start=1):

    shipment_id = f"SHP{i:07}"

    order_id = order["OrderID"]

    order_date = order["OrderDate"]

    # Random Delivery Partner
    delivery_partner_id = random.choice(
        delivery_partners["DeliveryPartnerID"]
    )

    # Shipment Status
    shipment_status_id = random.choices(
        population=list(SHIPMENT_STATUS_WEIGHTS.keys()),
        weights=list(SHIPMENT_STATUS_WEIGHTS.values()),
        k=1
    )[0]

    # Shipment Date
    shipment_date = order_date + timedelta(
        days=random.randint(0, 2)
    )

    # Estimated Delivery
    estimated_delivery_date = shipment_date + timedelta(
        days=random.randint(2, 7)
    )

    # Actual Delivery
    if shipment_status_id == 1:     # Delivered

        actual_delivery_date = estimated_delivery_date + timedelta(
            days=random.randint(-1, 2)
        )

    else:

        actual_delivery_date = pd.NaT

    tracking_number = f"TRK{i:010}"

    shipment = {

        "ShipmentID": shipment_id,

        "OrderID": order_id,

        "DeliveryPartnerID": delivery_partner_id,

        "ShipmentStatusID": shipment_status_id,

        "ShipmentDate": shipment_date.date(),

        "EstimatedDeliveryDate": estimated_delivery_date.date(),

        "ActualDeliveryDate":
            None if pd.isna(actual_delivery_date)
            else actual_delivery_date.date(),

        "TrackingNumber": tracking_number

    }

    shipments.append(shipment)

# ============================================================
# DataFrame
# ============================================================

shipments_df = pd.DataFrame(shipments)

# ============================================================
# Save CSV
# ============================================================

output_path = project_root / "output" / "facts"

output_path.mkdir(
    parents=True,
    exist_ok=True
)

shipments_df.to_csv(
    output_path / "shipments.csv",
    index=False
)

# ============================================================
# Validation
# ============================================================

print(shipments_df.head())

print(f"\nRows Created : {len(shipments_df)}")

print("\nDuplicate Shipment IDs")
print(shipments_df["ShipmentID"].duplicated().sum())

print("\nMissing Values")
print(shipments_df.isnull().sum())

print("\nShipment Status Distribution")
print(shipments_df["ShipmentStatusID"].value_counts().sort_index())

print("\nDelivery Partner Distribution")
print(shipments_df["DeliveryPartnerID"].value_counts().sort_index())

print("\nDuplicate Tracking Numbers")
print(shipments_df["TrackingNumber"].duplicated().sum())
print("successful")