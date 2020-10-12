# Write your MySQL query statement below
select Customers.Name as Customers
from Customers left join Orders on Customers.Id = Orders.CustomerId
where Orders.CustomerId is null;
