# Data Quality Validation Framework

## Overview

This module validates the RetailSphere datasets before they are used in the ETL pipeline and reporting layer.

---

## Features

- Primary Key Validation
- Foreign Key Validation
- Null Validation
- Duplicate Validation
- Business Rule Validation
- Markdown Report Generation
- Execution Logging

---

## Folder Structure

```
data_quality/

├── logs/
├── reports/
├── validation/
├── config.py
├── report_generator.py
├── run_all_validations.py
└── README.md
```

---

## How to Run

```bash
python data_quality/run_all_validations.py
```

---

## Output

### Report

```
reports/data_quality_report.md
```

### Logs

```
logs/validation.log
```

---

## Validation Coverage

### Dimension Tables

- Customers
- Products
- Stores
- Employees
- Suppliers

### Fact Tables

- Orders
- Order Items
- Payments
- Shipments
- Returns
- Inventory Transactions
- Customer Reviews

---

## Future Improvements

- Data Type Validation
- Date Format Validation
- Outlier Detection
- HTML Reports
- Dashboard Summary