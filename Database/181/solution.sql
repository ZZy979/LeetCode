# Write your MySQL query statement below
select e.Name as Employee
from Employee as e inner join Employee as m on e.ManagerId = m.Id
where e.ManagerId is not null and e.Salary > m.Salary
