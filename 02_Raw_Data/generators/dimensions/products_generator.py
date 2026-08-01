import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake=Faker("en_IN")

NUMBER_OF_PRODUCTS=5000

project_root=Path(__file__).resolve().parents[2]
suppliers_path = project_root / "output" / "dimensions" / "suppliers.csv"

suppliers = pd.read_csv(suppliers_path)

PRODUCT_CATALOG = {

    "Electronics": {

        "Smartphones": [
            "Samsung",
            "Apple",
            "OnePlus",
            "Google",
            "Motorola"
        ],

        "Laptops": [
            "Dell",
            "HP",
            "Lenovo",
            "Asus",
            "Acer"
        ],

        "Televisions": [
            "Sony",
            "LG",
            "Samsung",
            "TCL",
            "Panasonic"
        ]

    },

    "Fashion": {

        "Men's Wear": [
            "Levi's",
            "Allen Solly",
            "US Polo",
            "Louis Philippe",
            "Van Heusen"
        ],

        "Women's Wear": [
            "Biba",
            "W",
            "Global Desi",
            "Zara",
            "H&M"
        ],

        "Footwear": [
            "Nike",
            "Adidas",
            "Puma",
            "Skechers",
            "Bata"
        ]

    },

    "Grocery": {

        "Rice": [
            "India Gate",
            "Daawat",
            "Fortune"
        ],

        "Cooking Oil": [
            "Fortune",
            "Saffola",
            "Dhara"
        ],

        "Beverages": [
            "Coca-Cola",
            "Pepsi",
            "Sprite",
            "Fanta",
            "7UP"
        ]

    }

}

PRICE_RANGE = {
    "Electronics":(500, 200000),
    "Fashion": (300, 15000),
    "Grocery":(20, 2000)
}

MARGIN_RANGE = {
    "Electronics": (0.10,0.20),
    "Fashion": (0.30,0.60),
    "Grocery": (0.05,0.15)
}

ACTIVE_STATUS = {
    "Yes": 98,
    "No": 2
}


PRODUCT_VARIANTS = [
    "Standard",
    "Premium",
    "Pro",
    "Elite",
    "Plus",
    "Max"
]
products=[]
for i in range(1,NUMBER_OF_PRODUCTS+1):
    
    product_id=f"P{i:05}"
    category=random.choice(list(PRODUCT_CATALOG.keys()))
    subcategory=random.choice(list(PRODUCT_CATALOG[category].keys()))
    brand=random.choice(PRODUCT_CATALOG[category][subcategory])
    category_suppliers = suppliers[
    suppliers["PrimaryCategory"] == category]
    supplier_id = random.choice(
    category_suppliers["SupplierID"].tolist()
    )
    variant=random.choice(PRODUCT_VARIANTS)
    product_name=f"{brand} {subcategory} {variant}"
    min_price,max_price=PRICE_RANGE[category]
    selling_price=random.randint(min_price,max_price)
    min_margin,max_margin=MARGIN_RANGE[category]
    margin = random.uniform(min_margin,max_margin)
    cost_price=round(selling_price*(1-margin),2)
    profit=round(selling_price-cost_price,2)
    launch_date=fake.date_between(start_date="-8y",end_date="today")
    is_active=random.choices(
    population=list(ACTIVE_STATUS.keys()),
    weights=list(ACTIVE_STATUS.values()),
    k=1
    )[0]
    product={
       "Product_id":product_id,
        "SupplierID": supplier_id,
       "Category":category,
       "SubCategory":subcategory,
       "Brand":brand,
       "Product_Name":product_name,
       "SellingPrice":selling_price,
       "CostPrice": cost_price,
       "Profit": profit,
       "LaunchDate": launch_date,
       "IsActive": is_active
    }
    products.append(product)
products_df = pd.DataFrame(products)

project_root=Path(__file__).resolve().parents[2]
output_path = project_root / "output" / "dimensions"
output_path.mkdir(parents=True, exist_ok=True)

products_df.to_csv(
    output_path / "products.csv",
    index=False
)

print(len(products_df))
print(products_df["Product_id"].duplicated().sum())
print(products_df.isnull().sum())
print(products_df["Category"].value_counts())
print(products_df["SubCategory"].value_counts())
print(products_df["Brand"].value_counts().head(15))
print(products_df[["SellingPrice", "CostPrice", "Profit"]].describe())
print(products_df["IsActive"].value_counts())
print(products_df["Product_Name"])