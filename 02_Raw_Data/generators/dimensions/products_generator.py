import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake=Faker("en_IN")

NUMBER_OF_PRODUCTS=5000

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

#PRICE CONFIGURATION
PRICE_RANGE = {
    "Electronics": (500, 200000),
    "Fashion": (300, 15000),
    "Grocery": (20, 2000)
}

ACTIVE_STATUS = {
    "Yes": 98,
    "No": 2
}

