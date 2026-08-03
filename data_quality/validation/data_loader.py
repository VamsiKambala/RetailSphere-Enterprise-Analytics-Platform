import pandas as pd
from config import DIMENSIONS,FACTS 

def load_dimensions():
    return{
        "calendar":pd.read_csv(DIMENSIONS/ "calendar.csv"),
        "customers":pd.read_csv(DIMENSIONS/ "customers.csv"),
        "employees":pd.read_csv(DIMENSIONS / "employees.csv"),
        "products":pd.read_csv(DIMENSIONS / "products.csv"),
        "stores":pd.read_csv(DIMENSIONS / "stores.csv"),
        "suppliers":pd.read_csv(DIMENSIONS / "suppliers.csv")
    }

def load_facts():
    return {
        "orders":pd.read_csv(FACTS / "orders.csv"),
        "order_items":pd.read_csv(FACTS / "order_items.csv"),
        "payments":pd.read_csv(FACTS / "payments.csv"),
        "shipments":pd.read_csv(FACTS / "shipments.csv"),
        "returns":pd.read_csv(FACTS / "returns.csv"),
        "inventory":pd.read_csv(FACTS /"inventory_transactions.csv"),
        "customer_reviews":pd.read_csv(FACTS /"customer_reviews.csv")
    }