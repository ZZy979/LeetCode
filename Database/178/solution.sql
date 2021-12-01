# Write your MySQL query statement below
select s1.Score, (select count(distinct Score) + 1 from Scores as s2 where s2.Score > s1.Score) as `Rank` from Scores as s1 order by `Rank`;
