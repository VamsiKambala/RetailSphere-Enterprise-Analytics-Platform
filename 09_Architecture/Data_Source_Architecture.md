## Section 1 – Current Systems

| System                            | Purpose         |
| --------------------------------- | --------------- |
| Website/Ecommerce                 | Online Orders   |
| Inventory                         | Stock           |
| Payment                           | Transaction     |
| CRM                               | Customer Data   |
| Delivery                          | delivery orders |
| POS system                        | Sales orders    |
| Warehouse Management System (WMS) | picks and pakcs |
| Ads                               | ads information |
| ERP System                        |                 |
| Supplier Management System        |                 |
| Returns Management                |                 |
| Product Master                    |                 |
| Employee/HR System                |                 |

## Section 2 – Data Sources

| Source              | Data Available                                                                                             |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| Point of Sale (POS) | product_id,customer_id,transaction_id,quantity,price,order_id,order_date,order_delivery                    |
| Website/Ecommerce   | product_id,customer_id,transaction_id,quantity,price,product_name,order_id,order_date,order_delivery       |
| Inventory           | product_id,order_id,stock_availabe,quantity,date_of_available                                              |
| Payment             | payment_id,transaction_id,order_id,customer_id,payment_type,payment_status                                 |
| CRM                 | customer_id,customer_name,age,email,ph_no,state,country,device_type.membership,preferences,support tickets |
| Delivery            | delivery_id,delivery_date,order_id,customer_id,customer_name,shipment_type                                 |
| Warehouse           | order_id,quantity,in_stock,is_pickup                                                                       |
| ads                 | ad_id,ad_company,ad_product,ad_duration,clicks,device_type,location                                        |

## Section 3 – Source Owner

| Source    | Owner                  |
| --------- | ---------------------- |
| POS       | Retail Operations Team |
| CRM       | Customer Success       |
| Payment   | Finance                |
| Marketing | Marketing team         |
| Inventory | Warehouse Operations   |
| Website   | ECommerce Team         |
| Delivery  | Logistics              |
| WMS       | Warehouse team         |

## Section 4 – Refresh Frequency

| Source    | Frequency       | Why                            |
| --------- | --------------- | ------------------------------ |
| POS       | Every 5 minutes | Near real-time sales reporting |
| Website   | Real Time       | Online Orders                  |
| CRM       | Daily           | Customer updates               |
| Inventory | Every hour      | Stock changes                  |
| Marketing | Daily           | Campaign reports               |
| HR        | Daily           | Employee updates               |

## Section 5 – Priority

Which data is most important?

Critical

Sales - to estimate the profits and loss

Orders - to identify the total orders

Payments - to know about the payment type ex:upi,credit card,debit card etc

Medium

Inventory - to verify the product is in stock or not

Reviews - this is used to verify that the how satisfied the customer with the product.

Low

HR - Employee information changes infrequently and is not required for daily sales analytics.

Employee Attendance

## Section 6 – Initial Architecture

<img width="212" height="1122" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/ecc2ecb1-2fc3-482a-b742-c475c24d7686" />

## Sample
