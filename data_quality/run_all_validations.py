import logging
logging.basicConfig(

    filename="data_quality/logs/validation.log",

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

from config import REPORTS
from validation.data_loader import(
    load_dimensions,
    load_facts
)
from validation.check_primary_keys import check_primary_key
from validation.check_foreign_keys import check_foreign_key
from validation.check_nulls import check_nulls
from validation.check_duplicates import check_duplicates
from validation.check_business_rules import validate_positive_values,validate_dates,validate_rating

from report_generator import generate_report



validation_results = []

logging.info("Loading Dimension Tables")
dimensions=load_dimensions()

logging.info("Loading Fact Tables")
facts=load_facts()

PRIMARY_KEYS = [
    ("Customers", dimensions["customers"], "CustomerID"),
    ("Products", dimensions["products"], "Product_id"),
    ("Stores", dimensions["stores"], "StoreID"),
    ("Employees", dimensions["employees"], "EmployeeID"),
    ("Suppliers", dimensions["suppliers"], "SupplierID"),
    ("Orders", facts["orders"], "OrderID"),
    ("Order Items", facts["order_items"], "OrderItemID"),
    ("Payments", facts["payments"], "PaymentID"),
    ("Shipments", facts["shipments"], "ShipmentID"),
    ("Returns", facts["returns"], "ReturnID"),
    ("Inventory", facts["inventory"], "InventoryTransactionID"),
    ("Customer Reviews", facts["customer_reviews"], "ReviewID")
]

logging.info("Running Primary Key Validation")
for table_name, dataframe, primary_key in PRIMARY_KEYS:
    validation_results.append(check_primary_key(
    dataframe=dataframe,
    primary_key=primary_key,
    table_name=table_name
    )
)

FOREIGN_KEYS = [

    (
        facts["orders"],
        "CustomerID",
        dimensions["customers"],
        "CustomerID",
        "Orders → Customers"
    ),

    (
        facts["orders"],
        "StoreID",
        dimensions["stores"],
        "StoreID",
        "Orders → Stores"
    ),

    (
        facts["orders"],
        "EmployeeID",
        dimensions["employees"],
        "EmployeeID",
        "Orders → Employees"
    ),

    (
        facts["order_items"],
        "OrderID",
        facts["orders"],
        "OrderID",
        "Order Items → Orders"
    ),

    (
        facts["order_items"],
        "ProductID",
        dimensions["products"],
        "Product_id",
        "Order Items → Products"
    ),

    (
        facts["payments"],
        "OrderID",
        facts["orders"],
        "OrderID",
        "Payments → Orders"
    ),

    (
        facts["shipments"],
        "OrderID",
        facts["orders"],
        "OrderID",
        "Shipments → Orders"
    ),

    (
        facts["returns"],
        "OrderItemID",
        facts["order_items"],
        "OrderItemID",
        "Returns → Order Items"
    ),

    (
        facts["inventory"],
        "ProductID",
        dimensions["products"],
        "Product_id",
        "Inventory → Products"
    ),

    (
        facts["inventory"],
        "StoreID",
        dimensions["stores"],
        "StoreID",
        "Inventory → Stores"
    ),

    (
        facts["customer_reviews"],
        "OrderItemID",
        facts["order_items"],
        "OrderItemID",
        "Customer Reviews → Order Items"
    )

]

logging.info("Running Foreign Key Validation")
for(child_df,child_column,parent_df,parent_column,relationship_name) in FOREIGN_KEYS:

    validation_results.append(

        check_foreign_key(

            child_df,
            child_column,
            parent_df,
            parent_column,
            relationship_name
        )

    )





NULL_VALIDATIONS = [
    ("Customers", dimensions["customers"], ["CustomerID", "CustomerName", "PhoneNumber", "RegistrationDate"]),
    ("Products", dimensions["products"], ["Product_id", "Category", "SubCategory", "Brand", "SellingPrice", "CostPrice"]),
    ("Stores", dimensions["stores"], ["StoreID", "StoreName", "CityID"]),
    ("Employees", dimensions["employees"], ["EmployeeID", "StoreID", "JoiningDate"]),
    ("Suppliers", dimensions["suppliers"], ["SupplierID", "SupplierName"]),
    ("Orders", facts["orders"], ["OrderID", "CustomerID", "StoreID", "OrderDate"]),
    ("Order Items", facts["order_items"], ["OrderItemID", "OrderID", "ProductID", "Quantity", "UnitPrice"]),
    ("Payments", facts["payments"], ["PaymentID", "OrderID", "PaymentMethodID", "PaymentStatusID", "PaymentDate"]),
    ("Shipments", facts["shipments"], ["ShipmentID", "OrderID", "ShipmentStatusID", "ShipmentDate"]),
    ("Returns", facts["returns"], ["ReturnID", "OrderItemID", "ReturnDate"]),
    ("Inventory", facts["inventory"], ["InventoryTransactionID", "ProductID", "StoreID", "TransactionDate", "Quantity"]),
    ("Customer Reviews", facts["customer_reviews"], ["ReviewID", "OrderItemID", "Rating"])
]

logging.info("Running Null Validation")
for table_name,dataframe,required_columns in NULL_VALIDATIONS:
    validation_results.append(check_nulls(
        dataframe,
        required_columns,
        table_name
    ))


DUPLICATE_VALIDATIONS = [

    ("Customers", dimensions["customers"]),
    ("Products", dimensions["products"]),
    ("Stores", dimensions["stores"]),
    ("Employees", dimensions["employees"]),
    ("Suppliers", dimensions["suppliers"]),
    ("Orders", facts["orders"]),
    ("Order Items", facts["order_items"]),
    ("Payments", facts["payments"]),
    ("Shipments", facts["shipments"]),
    ("Returns", facts["returns"]),
    ("Inventory", facts["inventory"]),
    ("Customer Reviews", facts["customer_reviews"])

]
print(DUPLICATE_VALIDATIONS)
logging.info("Running Duplicate Validation")
for table_name,dataframe in DUPLICATE_VALIDATIONS:
    validation_results.append(
                                check_duplicates(
                                            dataframe,table_name
    ))


BUSINESS_RULES = [
    (
        validate_positive_values,dimensions["products"],"SellingPrice","Products"
    ),
    (
        validate_positive_values,facts["order_items"],"Quantity","Order Items"
    )
]
logging.info("Running Business Rule Validation")
for function,dataframe,column,table in BUSINESS_RULES:
    validation_results.append(function(
        dataframe,column,table
    ))








for result in validation_results:
    print("-" * 80)
    print(result)


logging.info("Generating Validation Report")
generate_report(
    validation_results,
    REPORTS
)
logging.info("Validation Framework Completed Successfully")

print(len(validation_results))
