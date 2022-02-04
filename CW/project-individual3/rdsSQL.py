import MySQLdb

USERNAME = 'root'
PASSWORD = 'password'
DB_NAME = 'mytest'

print ("Connecting to RDS instance")

conn = MySQLdb.connect(host = "mysql-db-instance.cz4jqqocwk5w.us-west-1.rds.amazonaws.com", user = USERNAME, passwd = PASSWORD, db = DB_NAME, port = 3306)

print ("Connected to RDS instance")

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print ("server version: ", row[0])

cursor.execute("SHOW tables")
cursor.execute("DROP TABLE Customer")
cursor.execute("DROP TABLE Orders")
cursor.execute("DROP TABLE Product")
cursor.execute("DROP TABLE OrderHasProduct")

cursor.execute( "CREATE TABLE Customer( \
cid varchar(50) NOT NULL PRIMARY KEY, \
customer_name varchar(100), \
gender boolean, \
phone varchar(20) \
)")

cursor.execute( "CREATE TABLE Orders( \
oid varchar(50) NOT NULL PRIMARY KEY, \
cid varchar(50) NOT NULL REFERENCES Customer (cid), \
is_completed boolean, \
total_price int \
)")

cursor.execute( "CREATE TABLE Product( \
pid varchar(50) NOT NULL PRIMARY KEY, \
product_name varchar(100), \
price int, \
cost int, \
is_on_sale boolean, \
available_stock int, \
description varchar(200) \
)")

cursor.execute( "CREATE TABLE OrderHasProduct( \
oid varchar(50) REFERENCES Orders (oid), \
pid varchar(50) REFERENCES Product (pid), \
product_count int \
)")

cursor.execute( "INSERT INTO Customer VALUES ('0', 'Alice', TRUE, '6693112564')")
cursor.execute( "INSERT INTO Customer VALUES ('1', 'Oliiva', TRUE, '6695483265')")
cursor.execute( "INSERT INTO Customer VALUES ('2', 'Ava', TRUE, '6682548364')")
cursor.execute( "INSERT INTO Customer VALUES ('3', 'Emily', TRUE, '6691254896')")
cursor.execute( "INSERT INTO Customer VALUES ('4', 'Liam', FALSE, '6696648124')")
cursor.execute( "INSERT INTO Customer VALUES ('5', 'Lucas', FALSE, '6694747223')")
cursor.execute( "INSERT INTO Customer VALUES ('6', 'James', FALSE, '6694874359')")
cursor.execute( "INSERT INTO Customer VALUES ('7', 'Jason', FALSE, '6693015987')")
cursor.execute( "INSERT INTO Customer VALUES ('8', 'Bob', FALSE, '6693015964')")

cursor.execute( "INSERT INTO Orders VALUES ('0', '2', FALSE, 66)")
cursor.execute( "INSERT INTO Orders VALUES ('1', '3', FALSE, 108)")
cursor.execute( "INSERT INTO Orders VALUES ('2', '1', TRUE, 66)")
cursor.execute( "INSERT INTO Orders VALUES ('3', '1', TRUE, 70)")
cursor.execute( "INSERT INTO Orders VALUES ('4', '0', FALSE, 54)")
cursor.execute( "INSERT INTO Orders VALUES ('5', '5', FALSE, 2148)")
cursor.execute( "INSERT INTO Orders VALUES ('6', '7', TRUE, 410)")
cursor.execute( "INSERT INTO Orders VALUES ('7', '4', FALSE, 717)")
cursor.execute( "INSERT INTO Orders VALUES ('8', '6', TRUE, 164)")

cursor.execute( "INSERT INTO Product VALUES ('0', 'shoes', 35, 32, TRUE, 3, 'NO DESCRIPTION')")
cursor.execute( "INSERT INTO Product VALUES ('1', 'water', 41, 25, TRUE, 8, 'NO DESCRIPTION')")
cursor.execute( "INSERT INTO Product VALUES ('2', 'wine', 66, 41, TRUE, 32, 'NO DESCRIPTION')")
cursor.execute( "INSERT INTO Product VALUES ('3', 'cookie', 3, 2, TRUE, 678, 'NO DESCRIPTION')")
cursor.execute( "INSERT INTO Product VALUES ('4', 'pen', 6, 3, TRUE, 452, 'NO DESCRIPTION')")
cursor.execute( "INSERT INTO Product VALUES ('5', 'apple', 108, 22, FALSE, 0, 'NO DESCRIPTION')")
cursor.execute( "INSERT INTO Product VALUES ('6', 'juice', 6, 1, TRUE, 365, 'NO DESCRIPTION')")
cursor.execute( "INSERT INTO Product VALUES ('7', 'macbook pro', 99, 50, TRUE, 8, 'NO DESCRIPTION')")
cursor.execute( "INSERT INTO Product VALUES ('8', 'wallet', 179, 110, TRUE, 90, 'NO DESCRIPTION')")

cursor.execute( "INSERT INTO OrderHasProduct VALUES ('0', '2', 1)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('4', '4', 3)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('6', '1', 10)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('7', '2', 9)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('8', '1', 4)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('4', '3', 2)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('1', '5', 1)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('2', '2', 1)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('3', '0', 2)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('7', '1', 3)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('5', '8', 12)")
cursor.execute( "INSERT INTO OrderHasProduct VALUES ('4', '4', 5)")

# query 4
#cursor.execute( "SELECT COUNT(*) FROM Product where is_on_sale = TRUE")

# query 5
'''
cursor.execute( "SELECT SUM(c.product_count * (b. price - b.cost)) AS income \
FROM Orders a, Product b, OrderHasProduct c \
WHERE a.is_completed = TRUE AND a.oid = c.oid AND b.pid = c.pid")
'''

# query 6
'''
cursor.execute( "SELECT a.product_name, (b.counts - a.available_stock) AS needToPurchase \
FROM Product a, (SELECT pid, SUM(product_count) AS counts FROM OrderHasProduct GROUP BY pid WITH ROLLUP) b \
WHERE a.pid = b.pid")
'''

rows = cursor.fetchall()

for row in rows:
  print (row)

conn.commit()

cursor.close()

conn.close()
