import mysql.connector as a
b=a.connect(host='localhost',user='root',passwd='root')
m=b.cursor()

m.execute('create database OctoDecathlon')
m.execute('use OctoDecathlon')
m.execute('create table Cricket( item_id int(5) primary key,Name varchar(30),Brand varchar(30),Item_Type varchar(30),Stock varchar(20),Price decimal(12,2))')
m.execute("insert into Cricket values(121,'Cricket Bat','Spartan','Equipment','Available',6500.00),(122,'Cricket Bat','Kookaburra','Equipment','Available',7500.00),(134,'Cricket Bat','SS','Equipment','Unavailable',7000.00),(124,'Cricket Ball','Kookaburra','Equipment','Available',1500.00),(143,'Cricket Ball','SG','Equipment','Available',1000.00),(126,'Gloves','SG','Equipment','Available',1000.00),(176,'Gloves','BDM','Equipment','Available',1500.00),(187,'Guard','SG','Equipment','Available',800.00),(165,'Leg Pads','SG','Equipment','Available','2500.00'),(283,'Helmet','SG','Equipment','Available','2000.00'),(564,'Helmet','Kookaburra','Equipment','Available',2500.00),(982,'India Team Jersey','Addidas','Jersey','Available',2000.00),(182,'RCB Team Jersey','Puma','Jersey','Unavailable',2000.00),(180,'CSK Team Jersey','PlayR','Jersey','Available',2000.00),(169,'MI Team Jersey','PlayR','Jersey','Available',2000.00),(723,'Cricket Kit','Kookaburra','Kit','Available',15000.00),(944,'Cricket Kit','SS','Kit','Available',15999.00),(638,'Cricket Kit','BDM','Kit','Available',15999.00)")
b.commit()
b.close()#creating and inserting items of cricket

m.execute('use OctoDecathlon')
m.execute('create table Football( item_id int(5) primary key,Name varchar(30),Brand varchar(30),Item_Type varchar(30),Stock varchar(20),Price decimal(12,2))')
m.execute("insert into Football values(110,'Football','Cosco','Equipment','Available',2000.00),(111,'Football','Addidas','Equipment','Available',1500.00),(112,'Football','Nivia','Equipment','Unavailable',1200.00),(109,'Air Pump','Nivia','Equipment','Available',750.00),(818,'Air Pump','Cosco','Equipment','Available',750.00),(118,'Football Studs','Nivia','Equipment','Available',1500.00),(119,'Football Studs','Puma','Equipment','Available',2000.00),(102,'Shinguard','Nivia','Equipment','Available',350.00),(108,'Goalkeeper Gloves','Nivia','Equipment','Available',750.00),(101,'India Team Jersey','ODthlon','Jersey','Available',1500.00),(103,'ISL Jersey','ODthlon','Jersey','Available',1500.00),(104,'Premier League Jersey','ODthlon','Jersey','Available','2000.00'),(105,'Football Kit','Cosco','Kit','Available',5000.00),(107,'Football Kit','Nivia','Kit','Available',5500.00)")
b.commit()
b.close()#creating and inserting items of football

m.execute('use OctoDecathlon')
m.execute('create table Basketball( item_id int(5) primary key,Name varchar(30),Brand varchar(30),Item_Type varchar(30),Stock varchar(20),Price decimal(12,2))')
m.execute("insert into Basketball values(800,'Basketball','Cosco','Equipment','Available',1300.00),(801,'Basketball','Nivia','Equipment','Available',1200.00),(802,'Basketball','BoldFit','Equipment','Available',1000.00),(803,'Basketball Hoop','Nivia','Equipment','Available',4500.00),(804,'Basketball Shoes','Nivia','Equipment','Available',2000.00),(805,'Basketball Shoes','Nike','Equipment','Available',2500.00),(818,'Air Pump','Cosco','Equipment','Available',750.00),(806,'Indian Team Jersey','ODthlon','Jersey','Available',2000.00),(807,'NBA Jersey','ODthlon','Jersey','Available',2000.00),(808,'Basketball Kit','Cosco','Kit','Available',4500.00),(809,'Basketball Kit','Nivia','Kit','Available',4500.00)")
b.commit()
b.close()#creating and inserting items of basketball

m.execute('use OctoDecathlon')
m.execute('create table Volleyball( item_id int(5) primary key,Name varchar(30),Brand varchar(30),Item_Type varchar(30),Stock varchar(20),Price decimal(12,2))')
m.execute("insert into Volleyball values(301,'Volleyball','Cosco','Equipment','Available',1000.00),(302,'Volleyball','Nivia','Equipment','Available',1200.00),(303,'Volleyball','ODthlon','Equipment','Available',850.00),(304,'Volleyball Net','ODthlon','Equipment','Available',2999.00),(305,'Volleyball Shoes','Puma','Equipment','Available',1599.00),(818,'Air Pump','Cosco','Equipment','Available',750.00),(306,'Indian Team Jersey','ODthlon','Jersey','Available',1599.00),(307,'Volleyball Kit','ODthlon','Kit','Available',4999.00)")
b.commit()
b.close()#creating and inserting items of volleyball

m.execute('use OctoDecathlon')
m.execute('create table Motor_Sport( item_id int(5) primary key,Name varchar(30),Brand varchar(30),Item_Type varchar(30),Stock varchar(20),Price decimal(12,2))')
m.execute("insert into Motor_Sport values(401,'BMX 500 Cycle','ExODthlon','Equipment','Available',17999.00),(402,'BMX 750 Cycle','ExODthlon','Equipment','Available',24999.00),(403,'Electric Air Pump','ExODthlon','Equipment','Available',4999.00),(404,'Car Gloves','Ferrari','Equipment','Available',2999.00),(405,'Bike/Cycle Gloves','ODthlon','Equipment','Available',1499.00),(406,'Formula 1 Suit','ExODthlon','Equipment','Available',4599.00),(407,'Car/Bike Helmet','Mercedes','Equipment','Available',4999.00),(408,'Cycle Helmet','ExODthlon','Equipment','Available',2999.00),(409,'Engine Oil','ExODthlon','Equipment','Available',4500.00),(410,'F1 Racer Suit/Jersey','ExODthlon','Jersey','Available',4499.00)")
b.commit()
b.close()#creating and inserting items of motor sport

m.execute('use OctoDecathlon')#date is in yyyy-mm-dd format
m.execute('create table Order_History( customer_id varchar(30),Name varchar(30),itemid_Bought int(10),Sport varchar(30),Date_of_Purchase date,Payment_method varchar(30))')
