 /* We have put together a table of restaurants called nomnom and we need your help to answer some questions. 
 Use the SQL commands you just learned and find the best dinner spots in the city.  */
 
 
 SELECT * FROM nomnom; 

  SELECT DISTINCT neighborhood FROM nomnom; 

  SELECT DISTINCT cuisine FROM nomnom; 

 SELECT * FROM nomnom
WHERE cuisine ="Chinese"; 

 SELECT * FROM nomnom
WHERE review>4; 

 SELECT * FROM nomnom
WHERE cuisine = 'Italian' AND price = '$$$'; 

 SELECT * FROM nomnom
WHERE name LIKE "%meatball%"; 

 SELECT * FROM nomnom
WHERE neighborhood = 'Midtown' OR neighborhood = 'Downtown'
OR neighborhood = 'Chinatown'; 

 SELECT * FROM nomnom
WHERE health IS NULL; 

 SELECT * FROM nomnom
ORDER BY review DESC
LIMIT 10; 

SELECT *,
  CASE
    WHEN review > 4.5 THEN  'Extraordinary'
    WHEN review > 4 THEN 'Excellenet'
    WHEN review > 3 THEN 'Good'
    WHEN review > 2 THEN 'Fair'
    ELSE 'Poor'
  END AS 'Outcome'
FROM nomnom;
