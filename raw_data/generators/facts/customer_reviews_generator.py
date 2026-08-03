import pandas as pd
import random
from faker import Faker
from pathlib import Path
from datetime import timedelta

fake = Faker("en_IN")

# ============================================================
# Configuration
# ============================================================

REVIEW_RATE = 0.30

RATINGS = {
    5: 45,
    4: 30,
    3: 15,
    2: 7,
    1: 3
}

REVIEWS = {
    5: [
        ("Excellent Product", "Excellent quality and highly recommended."),
        ("Worth the Money", "Completely satisfied with the purchase."),
        ("Highly Recommended", "Exceeded my expectations."),
        ("Amazing", "Very happy with the product.")
    ],
    4: [
        ("Very Good", "Good quality and works as expected."),
        ("Satisfied", "Nice product for the price."),
        ("Good Purchase", "Happy with my purchase."),
        ("Good Quality", "Quality is quite good.")
    ],
    3: [
        ("Average Product", "The product is okay."),
        ("Decent", "Average quality, nothing special."),
        ("Could Be Better", "Expected slightly better quality.")
    ],
    2: [
        ("Not as Expected", "Product quality could be improved."),
        ("Below Average", "Not completely satisfied."),
        ("Needs Improvement", "There are a few issues.")
    ],
    1: [
        ("Poor Quality", "Very disappointed with the product."),
        ("Bad Experience", "Would not recommend."),
        ("Defective Product", "Stopped working very quickly.")
    ]
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

orders["OrderDate"] = pd.to_datetime(
    orders["OrderDate"]
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
# Generate Reviews
# ============================================================

reviews = []

review_counter = 1

for _, item in order_items.iterrows():

    if random.random() > REVIEW_RATE:
        continue

    review_id = f"REV{review_counter:07}"

    order_item_id = item["OrderItemID"]

    rating = random.choices(
        population=list(RATINGS.keys()),
        weights=list(RATINGS.values()),
        k=1
    )[0]

    review_title, review_text = random.choice(
        REVIEWS[rating]
    )

    review_date = (
        item["OrderDate"]
        + timedelta(days=random.randint(2,10))
    )

    review = {

        "ReviewID": review_id,

        "OrderItemID": order_item_id,

        "Rating": rating,

        "ReviewTitle": review_title,

        "ReviewText": review_text,

        "ReviewDate": review_date.date()

    }

    reviews.append(review)

    review_counter += 1

# ============================================================
# DataFrame
# ============================================================

reviews_df = pd.DataFrame(reviews)

# ============================================================
# Save CSV
# ============================================================

output_path = project_root / "output" / "facts"

output_path.mkdir(
    parents=True,
    exist_ok=True
)

reviews_df.to_csv(
    output_path / "customer_reviews.csv",
    index=False
)

# ============================================================
# Validation
# ============================================================

print(reviews_df.head())

print(f"\nRows Created : {len(reviews_df)}")

print("\nDuplicate Review IDs")
print(
    reviews_df["ReviewID"]
    .duplicated()
    .sum()
)

print("\nDuplicate OrderItem IDs")
print(
    reviews_df["OrderItemID"]
    .duplicated()
    .sum()
)

print("\nMissing Values")
print(
    reviews_df.isnull().sum()
)

print("\nRating Distribution")
print(
    reviews_df["Rating"]
    .value_counts()
    .sort_index()
)