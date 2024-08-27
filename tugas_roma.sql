SELECT
    o.orderNumber AS OrderNumber,
    o.orderDate AS OrderDate,
    c.customerName AS CustomerName,
    c.city AS City,
    c.country AS Country,
    od.quantityOrdered AS QuantityOrdered,
    p.productName AS ProductName
FROM
    orders o
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    JOIN customers c ON o.customerNumber = c.customerNumber
    JOIN products p ON od.productCode = p.productCode
WHERE
    p.productName = '1992 Ferrari 360 Spider red'
    AND o.orderDate BETWEEN '2004-08-01' AND '2004-12-01';

