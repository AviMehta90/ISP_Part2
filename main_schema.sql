-- Products Table
CREATE TABLE Products (
    ProductID UUID PRIMARY KEY,
    ProductName TEXT,
    ProductDescription TEXT,
    Category TEXT,
    Price NUMERIC,
    SupplierID UUID
);

-- Warehouses Table
CREATE TABLE Warehouses (
    WarehouseID UUID PRIMARY KEY,
    WarehouseName TEXT,
    Location TEXT,
    Capacity INT,
    ContactInformation TEXT
);

-- Suppliers Table
CREATE TABLE Suppliers (
    SupplierID UUID PRIMARY KEY,
    SupplierName TEXT,
    ContactInformation TEXT,
    ProductCategoriesSupplied TEXT[] -- Using array for simplicity
);

-- Orders Table
CREATE TABLE Orders (
    OrderID UUID PRIMARY KEY,
    OrderDate DATE,
    CustomerName TEXT,
    OrderStatus TEXT,
    TotalOrderAmount NUMERIC,
    ShippingAddress TEXT
);

-- Order Details Table
CREATE TABLE OrderDetails (
    OrderDetailID UUID PRIMARY KEY,
    OrderID UUID,
    ProductID UUID,
    QuantityOrdered INT,
    UnitPrice NUMERIC,
    TotalLineItemAmount NUMERIC
);

-- Shipments Table
CREATE TABLE Shipments (
    ShipmentID UUID PRIMARY KEY,
    OrderID UUID,
    WarehouseID UUID,
    ShipmentDate DATE,
    ShipmentStatus TEXT,
    TrackingInformation TEXT
);

-- Inventory Levels Table
CREATE TABLE InventoryLevels (
    WarehouseID UUID,
    ProductID UUID,
    QuantityOnHand INT,
    MinimumStockLevel INT,
    MaximumStockLevel INT,
    ReorderPoint INT,
    LastRestockDate DATE,
    PRIMARY KEY (WarehouseID, ProductID)
);
