# Write your MySQL query statement below
select w2.Id as Id
from Weather as w1 inner join Weather as w2 on w2.RecordDate = adddate(w1.RecordDate, 1)
where w2.Temperature > w1.Temperature;
