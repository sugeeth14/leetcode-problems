# Write your MySQL query statement below

SELECT E.name as Employee from Employee E Join Employee F ON E.managerId = F.id WHERE E.salary > F.salary;