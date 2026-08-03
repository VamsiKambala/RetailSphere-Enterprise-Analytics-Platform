# RetailSphere Data Quality Report

Execution Date: 2026-08-03 22:49:17.748555

---

## Customers
- Table: Customers
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 100000

## Products
- Table: Products
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 5000

## Stores
- Table: Stores
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 200

## Employees
- Table: Employees
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 2500

## Suppliers
- Table: Suppliers
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 80

## Orders
- Table: Orders
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 50000

## Order Items
- Table: Order Items
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 96993

## Payments
- Table: Payments
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 50000

## Shipments
- Table: Shipments
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 50000

## Returns
- Table: Returns
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 6723

## Inventory
- Table: Inventory
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 474377

## Customer Reviews
- Table: Customer Reviews
- Check: Primary Key
- Status: PASSED
- DuplicateKeys: 0
- RowsChecked: 29120

## Orders → Customers
- Relationship: Orders → Customers
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 50000

## Orders → Stores
- Relationship: Orders → Stores
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 50000

## Orders → Employees
- Relationship: Orders → Employees
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 50000

## Order Items → Orders
- Relationship: Order Items → Orders
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 96993

## Order Items → Products
- Relationship: Order Items → Products
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 96993

## Payments → Orders
- Relationship: Payments → Orders
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 50000

## Shipments → Orders
- Relationship: Shipments → Orders
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 50000

## Returns → Order Items
- Relationship: Returns → Order Items
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 6723

## Inventory → Products
- Relationship: Inventory → Products
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 474377

## Inventory → Stores
- Relationship: Inventory → Stores
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 474377

## Customer Reviews → Order Items
- Relationship: Customer Reviews → Order Items
- Check: Foreign Key
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 29120

## Customers
- Table: Customers
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 100000
- NullSummary: {'CustomerID': 0, 'CustomerName': 0, 'PhoneNumber': 0, 'RegistrationDate': 0}

## Products
- Table: Products
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 5000
- NullSummary: {'Product_id': 0, 'Category': 0, 'SubCategory': 0, 'Brand': 0, 'SellingPrice': 0, 'CostPrice': 0}

## Stores
- Table: Stores
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 200
- NullSummary: {'StoreID': 0, 'StoreName': 0, 'CityID': 0}

## Employees
- Table: Employees
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 2500
- NullSummary: {'EmployeeID': 0, 'StoreID': 0, 'JoiningDate': 0}

## Suppliers
- Table: Suppliers
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 80
- NullSummary: {'SupplierID': 0, 'SupplierName': 0}

## Orders
- Table: Orders
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 50000
- NullSummary: {'OrderID': 0, 'CustomerID': 0, 'StoreID': 0, 'OrderDate': 0}

## Order Items
- Table: Order Items
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 96993
- NullSummary: {'OrderItemID': 0, 'OrderID': 0, 'ProductID': 0, 'Quantity': 0, 'UnitPrice': 0}

## Payments
- Table: Payments
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 50000
- NullSummary: {'PaymentID': 0, 'OrderID': 0, 'PaymentMethodID': 0, 'PaymentStatusID': 0, 'PaymentDate': 0}

## Shipments
- Table: Shipments
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 50000
- NullSummary: {'ShipmentID': 0, 'OrderID': 0, 'ShipmentStatusID': 0, 'ShipmentDate': 0}

## Returns
- Table: Returns
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 6723
- NullSummary: {'ReturnID': 0, 'OrderItemID': 0, 'ReturnDate': 0}

## Inventory
- Table: Inventory
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 474377
- NullSummary: {'InventoryTransactionID': 0, 'ProductID': 0, 'StoreID': 0, 'TransactionDate': 0, 'Quantity': 0}

## Customer Reviews
- Table: Customer Reviews
- Check: Null_Validation
- Status: PASSED
- RowsChecked: 29120
- NullSummary: {'ReviewID': 0, 'OrderItemID': 0, 'Rating': 0}

## Customers
- Table: Customers
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 100000

## Products
- Table: Products
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 5000

## Stores
- Table: Stores
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 200

## Employees
- Table: Employees
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 2500

## Suppliers
- Table: Suppliers
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 80

## Orders
- Table: Orders
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 50000

## Order Items
- Table: Order Items
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 96993

## Payments
- Table: Payments
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 50000

## Shipments
- Table: Shipments
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 50000

## Returns
- Table: Returns
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 6723

## Inventory
- Table: Inventory
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 474377

## Customer Reviews
- Table: Customer Reviews
- Check: Duplicate Rows
- Status: SUCCESS
- DuplicateRows: 0
- RowChecked: 29120

## Products
- Table: Products
- Check: SellingPrice > 0
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 5000

## Order Items
- Table: Order Items
- Check: Quantity > 0
- Status: PASSED
- InvalidRecords: 0
- RowsChecked: 96993

