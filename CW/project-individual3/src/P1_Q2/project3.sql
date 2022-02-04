CREATE DATABASE project3;

USE project3;

CREATE TABLE Customer(
cid varchar(50) NOT NULL PRIMARY KEY,
customer_name varchar(100),
gender boolean,
phone varchar(20)
);

CREATE TABLE Orders(
oid varchar(50) NOT NULL PRIMARY KEY,
cid varchar(50) NOT NULL REFERENCES Customer (cid),
is_completed boolean,
total_price int
);

CREATE TABLE Product(
pid varchar(50) NOT NULL PRIMARY KEY,
product_name varchar(100),
price int,
cost int,
is_on_sale boolean,
available_stock int,
description varchar(200)
);

CREATE TABLE OrderHasProduct(
oid varchar(50) REFERENCES Orders (oid),
pid varchar(50) REFERENCES Product (pid),
product_count int
);
