create database realtimedataanalytics;

use realtimedataanalytics;



CREATE TABLE salesdata (
    SaleID INT PRIMARY KEY,       				     -- primary key
    ProductID INT NOT NULL,                          -- Product identifier
    CustomerID INT NOT NULL,                         -- Customer identifier
    SaleAmount DECIMAL(10, 2) NOT NULL,              -- Sale amount
    Quantity INT NOT NULL,                           -- Quantity of products sold
    SaleTime DATETIME NOT NULL,  					 -- Timestamp of sale
    PaymentMethod VARCHAR(50),                       -- Payment method (e.g., Credit Card, PayPal)
    SaleStatus VARCHAR(20) CHECK (SaleStatus IN ('Completed', 'Pending', 'Canceled')), -- Sale status
    DiscountApplied DECIMAL(5, 2) DEFAULT 0,         -- Discount percentage applied
    TotalAmountBeforeDiscount DECIMAL(10, 2),       -- Amount before discount
    Region VARCHAR(100),                             -- Customer region (e.g., City or Country)
    StoreID INT NOT NULL                             -- Store or location identifier
);


INSERT INTO salesdata (
    SaleID,ProductID, CustomerID, SaleAmount, Quantity, SaleTime, PaymentMethod, 
    SaleStatus, DiscountApplied, TotalAmountBeforeDiscount, Region, StoreID
)
VALUES (
    101, 2505, 99.99, 1, '2025-02-13 10:15:00', 'Credit Card', 
    'Completed', 10.00, 110.00, 'North America', 1
);


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/random_sales_data.csv'
INTO TABLE salesdata
FIELDS TERMINATED BY ','  -- CSV delimiter
ENCLOSED BY '"'           -- Optional, if your fields are enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line break delimiter (usually \n)
IGNORE 1 LINES            -- Skip header row
(SaleID,ProductID, CustomerID, SaleAmount, Quantity, SaleTime, PaymentMethod, 
    SaleStatus, DiscountApplied, TotalAmountBeforeDiscount, Region, StoreID);

Select * from salesdata;