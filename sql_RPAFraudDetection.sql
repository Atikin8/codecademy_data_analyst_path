-- 1
SELECT *
FROM transaction_data
LIMIT 10;

--2
SELECT full_name, email FROM transaction_data
WHERE zip = 20252;
--3
SELECT full_name, email FROM transaction_data
WHERE full_name ='Art Vandelay' OR full_name LIKE '% der %';
--4
SELECT ip_address, email FROM transaction_data
WHERE ip_address LIKE '10.%';
--5
SELECT email FROM transaction_data
WHERE email LIKE '%temp_email.com';
--6
SELECT * FROM transaction_data
WHERE ip_address LIKE '120.%'
AND full_name LIKE 'John%';
