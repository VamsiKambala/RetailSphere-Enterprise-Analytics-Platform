# Our config will contain five sections.

# 1. Project Paths

# 2. MySQL Configuration

# 3. Database Names

# 4. Table Mapping

# 5. Metadata Configuration

from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parents[1]

RAW_DATA=PROJECT_ROOT/"raw_data"/"output"


MYSQL_CONFIG={
    "host":"localhost",
    "user":"root",
    "password":"password",
    "port":3306
}


STAGING_DATABASE="retailsphere_staging"

WAREHOUSE_DATABASE="retailsphere_warehouse"


TABLE_MAPPING = [
("customers.csv","stg_customers"),
("products.csv","stg_products"),
("stores.csv","stg_stores"),
("employees.csv","stg_employees"),
("suppliers.csv","stg_suppliers"),
("orders.csv","stg_orders"),
("order_items.csv","stg_order_items"),
("payments.csv","stg_payments"),
("shipments.csv","stg_shipments"),
("returns.csv","stg_returns"),
("inventory_transactions.csv","stg_inventory_transactions"),
("customer_reviews.csv","stg_customer_reviews")
]

METADATA_COLUMNS=[
    "BatchID",
    "SourceFile",
    "LoadTimestamp"
]

