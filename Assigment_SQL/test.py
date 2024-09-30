"""
kamu nanya










SELECT P.productname, SUM(OD.UnitPrice * OD.Quantity) AS TotalValue
FROM [Order Details] OD
JOIN Orders O ON OD.orderid = O.orderid
JOIN Products P ON OD.productid = P.productid
WHERE YEAR(O.OrderDate) = 1997
GROUP BY P.productname;


"""