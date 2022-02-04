SELECT SUM(c.product_count * (b. price - b.cost)) AS income 
FROM Orders a, Product b, OrderHasProduct c
WHERE a.is_completed = TRUE AND a.oid = c.oid AND b.pid = c.pid;
