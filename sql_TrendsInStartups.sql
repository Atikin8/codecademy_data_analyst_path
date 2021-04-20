SELECT * FROM startups;

SELECT COUNT(*) FROM startups;

SELECT SUM(valuation) as total_valuation
FROM startups;

SELECT MAX(raised) as max_raised
FROM startups;

SELECT MAX(raised) as max_raised_seed
FROM startups
WHERE stage='Seed';

SELECT MIN(founded) as oldest
FROM startups;

SELECT AVG(valuation)
FROM startups;

SELECT category, ROUND(AVG(valuation),2) as avg_val
FROM startups
GROUP BY category
ORDER BY avg_val DESC;

SELECT category, COUNT(*) as num_companies
FROM startups
GROUP BY category
HAVING num_companies >3
ORDER BY num_companies DESC;

SELECT location, AVG(employees) as avg_workers
FROM startups
GROUP BY location
HAVING avg_workers >500;






 