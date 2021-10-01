SELECT * FROM survey LIMIT 10;

SELECT question, count(user_id)
FROM survey GROUP BY question ORDER BY question;

-- Home Try-On Funnel
 
SELECT * FROM quiz LIMIT 5;
 
SELECT * FROM home_try_on LIMIT 5;
 
SELECT * FROM purchase LIMIT 5;

SELECT q.user_id, h.user_id IS NOT NULL as 'is_home_try_on',
h.number_of_pairs, p.user_id IS NOT NULL as 'is_purchase' FROM quiz q
LEFT JOIN home_try_on h  ON q.user_id=h.user_id LEFT JOIN purchase p ON h.user_id=p.user_id
LIMIT 10;

with q AS (SELECT '1-quiz' AS STAGE, COUNT(*) FROM quiz),
h AS (SELECT '2-home-try-on' AS STAGE, COUNT(*) FROM home_try_on),
p AS (SELECT '3-purchase' AS STAGE, COUNT(*)FROM purchase)
SELECT * FROM q
UNION ALL SELECT * FROM h
UNION ALL SELECT * FROM p;

WITH base_table AS (SELECT q.user_id,h.user_id IS NOT NULL AS 'is_home_try_on',h.number_of_pairs AS 'AB_variant',p.user_id IS NOT NULL AS 'is_purchase' FROM quiz q LEFT JOIN home_try_on h ON q.user_id=h.user_id LEFT JOIN purchase p ON p.user_id=q.user_id)
SELECT AB_variant, sum(is_home_try_on) AS 'home_trial', sum(is_purchase) AS 'purchase' FROM base_table GROUP BY AB_variant HAVING home_trial >0;