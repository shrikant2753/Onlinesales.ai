SELECT d.NAME AS "DEPT_NAME", AVG(s.AMT_(USD)) AS "AVG_MONTHLY_SALARY (USD)"
FROM Salaries as s JOIN Employees as e on e.id=s.EMP_ID
JOIN Departments as d on d.id=e.DEPT_ID
GROUP BY d.NAME
ORDER BY AVG(s.AMT_(USD)) desc
LIMIT 3;

-- header name of departments.csv change from DEPT ID to DEPT_ID
-- header name of Salaries.csv change from AMT (USD) to AMT_(USD)

-- we have join the the salary and employee table on employees id and salaries foreign key EMP_ID
-- and then join this table to department on department id and employee foreign key DEPT_ID
-- then we group the content of the table by department name and get modified ans as per quey
-- of 5 rows of department name and respective content on that
-- then we use order by to sorted the avg salaries of departments by descending oreder using
-- aggregated function AVG()
-- we just need top 3 department so resrict it to only top 3 department we use limit by 3
-- as given in task we have to show output in given format so we only select thos columns from 
-- table and change the name of those columns we create alias using keyword 'as'