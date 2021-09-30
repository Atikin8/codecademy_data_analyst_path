SELECT * FROM state_climate

--running average for each state
SELECT state, year, tempc, AVG(tempc) OVER (PARTITION BY state ORDER BY year) as 'running_avg_temp' FROM state_climate

--lowest temp for each state
SELECT state, year, tempc, FIRST_VALUE(tempc) OVER (PARTITION BY state ORDER BY year) as 'lowest_temp' FROM state_climate

--highest temp for each state
SELECT state, year, tempc, LAST_VALUE(tempc) OVER (PARTITION BY state ORDER BY year RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as 'highest_temp' FROM state_climate

-- temp change each year in each state in DESC order
SELECT state, year,tempc, tempc -LAG(tempc,1,tempc) OVER (PARTITION BY state ORDER BY year) as 'change_in_temp' FROM state_climate ORDER BY change_in_temp DESC

--rank of the coldest temps for Alabama
SELECT RANK() OVER(ORDER BY tempc) AS 'rank', state, year, tempc FROM state_climate WHERE state = 'Alabama'

--rank of the highest temps for states
SELECT RANK() OVER(PARTITION BY state ORDER BY tempc DESC) AS 'rank', state, year, tempc FROM state_climate

--average yearly temperatures in quartiles for each state
SELECT NTILE(4) OVER(PARTITION BY state ORDER BY tempc) as 'quartile', state, year, AVG(tempc) OVER(PARTITION BY state ORDER BY tempc) as 'avg_temp' FROM state_climate

--average yearly temperatures in quintiles
SELECT NTILE(5) OVER(ORDER BY tempc) as 'quartile', state, year, AVG(tempc) OVER(ORDER BY tempc) as 'avg_temp' FROM state_climate







