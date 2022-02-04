SELECT a.product_name, (b.counts - a.available_stock) AS needToPurchase
FROM Product a, (SELECT pid, SUM(product_count) AS counts FROM OrderHasProduct GROUP BY pid WITH ROLLUP) b
WHERE a.pid = b.pid;
