-- 1
SELECT *
FROM orders
LIMIT 10;
-- 2 
SELECT DISTINCT order_date FROM orders
ORDER BY order_date DESC;
--3
SELECT special_instructions FROM orders
LIMIT 20;
--4
SELECT special_instructions FROM orders
WHERE special_instructions IS NOT NULL
LIMIT 20;
--5
SELECT special_instructions FROM orders
WHERE special_instructions IS NOT NULL
ORDER BY special_instructions
LIMIT 20;
--6
SELECT special_instructions FROM orders
WHERE special_instructions LIKE '%sauce%';
--7
SELECT special_instructions FROM orders
WHERE special_instructions LIKE '%door%';
--8
SELECT special_instructions FROM orders
WHERE special_instructions LIKE '%box%';
--9
SELECT id AS '#',special_instructions AS 'Notes' FROM orders
WHERE special_instructions LIKE '%box%';



 