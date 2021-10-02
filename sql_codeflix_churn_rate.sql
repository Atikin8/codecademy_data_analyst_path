 SELECT * FROM subscriptions
 LIMIT 100;

SELECT MIN(subscription_start) as 'first_month',
MAX(subscription_end) as 'last_month'
FROM subscriptions; --range from DEC 2016 to March 2017, so churn can be calculate from JAN 2016 to March 2017

-- create temp months table
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),cross_join AS --cross join 
(SELECT
  subscriptions.*, months.* FROM subscriptions CROSS JOIN months
), status AS --is active, is cancelled columns
(SELECT id, segment, subscription_start,subscription_end, first_day AS 'month',
CASE WHEN (subscription_start<first_day) AND ((subscription_end > first_day) OR (subscription_end IS NULL)) AND (segment=87) THEN 1 ELSE 0 END AS 'is_active_87',
CASE WHEN (subscription_start<first_day) AND ((subscription_end > first_day) OR (subscription_end IS NULL)) AND (segment=30) THEN 1 ELSE 0 END AS 'is_active_30',
CASE WHEN (subscription_end BETWEEN first_day AND last_day) AND (segment=87) THEN 1 ELSE 0 END AS 'is_canceled_87',
CASE WHEN (subscription_end BETWEEN first_day AND last_day) AND (segment=30) THEN 1 ELSE 0 END AS 'is_canceled_30' FROM cross_join
),--aggregate
 status_aggregate AS (SELECT month, SUM(is_active_87) AS 'sum_active_87',SUM(is_active_30) AS 'sum_active_30',SUM(is_canceled_87) AS 'sum_canceled_87',SUM(is_canceled_30) AS 'sum_canceled_30' FROM status GROUP BY Month)

--churn rate
SELECT (1.0*sum_canceled_87/sum_active_87) AS 'churn_87',
(1.0*sum_canceled_30/sum_active_30) AS 'churn_30' FROM status_aggregate
