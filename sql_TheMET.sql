 SELECT * FROM met
 LIMIT 10;

 SELECT department, COUNT(*) from met
 GROUP BY department;

 SELECT COUNT(*) as celery_cat
 FROM met
 WHERE category like '%celery%';

 SELECT  title, medium, date
 FROM met
 WHERE date like '%1600%';

 SELECT country, COUNT(*) as num
 FROM met
 WHERE country NOT NULL
 GROUP BY 1
 ORDER BY num DESC
 LIMIT 10;

 SELECT category, COUNT(*) as num
 FROM met
 GROUP BY 1
 HAVING num>100;

 SELECT
 CASE WHEN medium LIKE '%gold%' THEN 'Gold'
 WHEN medium LIKE '%silver%' THEN 'Silver'
 END AS 'Metals',
 COUNT(*) as num
 FROM met
 GROUP BY 1
 ORDER BY 1 DESC;








 