-- 1
 SELECT *
 FROM users
 LIMIT 20;
 
-- 2
 SELECT * FROM users
 WHERE birthday BETWEEN '1980-01-01' AND '1989-12-31';
 --3
 SELECT * FROM users
 WHERE created_at < '2017-05-01';
--4
 SELECT * FROM users
 WHERE test = 'bears'
--5
 SELECT * FROM users
 WHERE campaign LIKE 'BBB%';
 
 --6
 SELECT * FROM users
 WHERE campaign LIKE '%-2';
 --7
SELECT * FROM users
WHERE campaign IS NOT NULL AND test IS NOT NULL;


 