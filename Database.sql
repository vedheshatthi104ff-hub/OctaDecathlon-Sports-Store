```sql
DROP DATABASE IF EXISTS OctoDecathlon;
CREATE DATABASE OctoDecathlon;
USE OctoDecathlon;

CREATE TABLE Cricket (
    item_id INT(5) PRIMARY KEY,
    Name VARCHAR(30),
    Brand VARCHAR(30),
    Item_Type VARCHAR(30),
    Stock VARCHAR(20),
    Price DECIMAL(12,2)
);

INSERT INTO Cricket VALUES
(121,'Cricket Bat','Spartan','Equipment','Available',6500.00),
(122,'Cricket Bat','Kookaburra','Equipment','Available',7500.00),
(134,'Cricket Bat','SS','Equipment','Unavailable',7000.00),
(124,'Cricket Ball','Kookaburra','Equipment','Available',1500.00),
(143,'Cricket Ball','SG','Equipment','Available',1000.00),
(126,'Gloves','SG','Equipment','Available',1000.00),
(176,'Gloves','BDM','Equipment','Available',1500.00),
(187,'Guard','SG','Equipment','Available',800.00),
(165,'Leg Pads','SG','Equipment','Available',2500.00),
(283,'Helmet','SG','Equipment','Available',2000.00),
(564,'Helmet','Kookaburra','Equipment','Available',2500.00),
(982,'India Team Jersey','Addidas','Jersey','Available',2000.00),
(182,'RCB Team Jersey','Puma','Jersey','Unavailable',2000.00),
(180,'CSK Team Jersey','PlayR','Jersey','Available',2000.00),
(169,'MI Team Jersey','PlayR','Jersey','Available',2000.00),
(723,'Cricket Kit','Kookaburra','Kit','Available',15000.00),
(944,'Cricket Kit','SS','Kit','Available',15999.00),
(638,'Cricket Kit','BDM','Kit','Available',15999.00);

CREATE TABLE Football (
    item_id INT(5) PRIMARY KEY,
    Name VARCHAR(30),
    Brand VARCHAR(30),
    Item_Type VARCHAR(30),
    Stock VARCHAR(20),
    Price DECIMAL(12,2)
);

INSERT INTO Football VALUES
(110,'Football','Cosco','Equipment','Available',2000.00),
(111,'Football','Addidas','Equipment','Available',1500.00),
(112,'Football','Nivia','Equipment','Unavailable',1200.00),
(109,'Air Pump','Nivia','Equipment','Available',750.00),
(818,'Air Pump','Cosco','Equipment','Available',750.00),
(118,'Football Studs','Nivia','Equipment','Available',1500.00),
(119,'Football Studs','Puma','Equipment','Available',2000.00),
(102,'Shinguard','Nivia','Equipment','Available',350.00),
(108,'Goalkeeper Gloves','Nivia','Equipment','Available',750.00),
(101,'India Team Jersey','ODthlon','Jersey','Available',1500.00),
(103,'ISL Jersey','ODthlon','Jersey','Available',1500.00),
(104,'Premier League Jersey','ODthlon','Jersey','Available',2000.00),
(105,'Football Kit','Cosco','Kit','Available',5000.00),
(107,'Football Kit','Nivia','Kit','Available',5500.00);

CREATE TABLE Basketball (
    item_id INT(5) PRIMARY KEY,
    Name VARCHAR(30),
    Brand VARCHAR(30),
    Item_Type VARCHAR(30),
    Stock VARCHAR(20),
    Price DECIMAL(12,2)
);

INSERT INTO Basketball VALUES
(800,'Basketball','Cosco','Equipment','Available',1300.00),
(801,'Basketball','Nivia','Equipment','Available',1200.00),
(802,'Basketball','BoldFit','Equipment','Available',1000.00),
(803,'Basketball Hoop','Nivia','Equipment','Available',4500.00),
(804,'Basketball Shoes','Nivia','Equipment','Available',2000.00),
(805,'Basketball Shoes','Nike','Equipment','Available',2500.00),
(818,'Air Pump','Cosco','Equipment','Available',750.00),
(806,'Indian Team Jersey','ODthlon','Jersey','Available',2000.00),
(807,'NBA Jersey','ODthlon','Jersey','Available',2000.00),
(808,'Basketball Kit','Cosco','Kit','Available',4500.00),
(809,'Basketball Kit','Nivia','Kit','Available',4500.00);

CREATE TABLE Volleyball (
    item_id INT(5) PRIMARY KEY,
    Name VARCHAR(30),
    Brand VARCHAR(30),
    Item_Type VARCHAR(30),
    Stock VARCHAR(20),
    Price DECIMAL(12,2)
);

INSERT INTO Volleyball VALUES
(301,'Volleyball','Cosco','Equipment','Available',1000.00),
(302,'Volleyball','Nivia','Equipment','Available',1200.00),
(303,'Volleyball','ODthlon','Equipment','Available',850.00),
(304,'Volleyball Net','ODthlon','Equipment','Available',2999.00),
(305,'Volleyball Shoes','Puma','Equipment','Available',1599.00),
(818,'Air Pump','Cosco','Equipment','Available',750.00),
(306,'Indian Team Jersey','ODthlon','Jersey','Available',1599.00),
(307,'Volleyball Kit','ODthlon','Kit','Available',4999.00);

CREATE TABLE Motor_Sport (
    item_id INT(5) PRIMARY KEY,
    Name VARCHAR(30),
    Brand VARCHAR(30),
    Item_Type VARCHAR(30),
    Stock VARCHAR(20),
    Price DECIMAL(12,2)
);

INSERT INTO Motor_Sport VALUES
(401,'BMX 500 Cycle','ExODthlon','Equipment','Available',17999.00),
(402,'BMX 750 Cycle','ExODthlon','Equipment','Available',24999.00),
(403,'Electric Air Pump','ExODthlon','Equipment','Available',4999.00),
(404,'Car Gloves','Ferrari','Equipment','Available',2999.00),
(405,'Bike/Cycle Gloves','ODthlon','Equipment','Available',1499.00),
(406,'Formula 1 Suit','ExODthlon','Equipment','Available',4599.00),
(407,'Car/Bike Helmet','Mercedes','Equipment','Available',4999.00),
(408,'Cycle Helmet','ExODthlon','Equipment','Available',2999.00),
(409,'Engine Oil','ExODthlon','Equipment','Available',4500.00),
(410,'F1 Racer Suit/Jersey','ExODthlon','Jersey','Available',4499.00);

CREATE TABLE Order_History (
    customer_id VARCHAR(30),
    Name VARCHAR(30),
    itemid_Bought INT(10),
    Sport VARCHAR(30),
    Date_of_Purchase DATE,
    Payment_method VARCHAR(30)
);
```
