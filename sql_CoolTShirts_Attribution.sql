SELECT COUNT(DISTINCT utm_campaign) AS 'unique campaigns' from page_visits;  --8 unique campaigns

SELECT COUNT(DISTINCT utm_source) AS 'unique sources' from page_visits; -- 6 sources

SELECT DISTINCT utm_campaign, utm_source FROM page_visits;

SELECT DISTINCT page_name FROM page_visits;  --4 pages


WITH first_touch AS (
    SELECT user_id,
        MIN(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id),ft_utm AS(
SELECT ft.user_id,
    ft.first_touch_at,
    pv.utm_source,
		pv.utm_campaign
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id
    AND ft.first_touch_at = pv.timestamp)
SELECT utm_source, utm_campaign,COUNT(first_touch_at)
FROM ft_utm GROUP BY 1,2 ORDER BY 3 DESC; --first touch by campaign

WITH last_touch AS (
    SELECT user_id,
        MAX(timestamp) as last_touch_at
    FROM page_visits WHERE page_name='4 - purchase'
    GROUP BY user_id),lt_utm AS(
SELECT lt.user_id,
    lt.last_touch_at,
    pv.page_name,
    pv.utm_source,
		pv.utm_campaign
FROM last_touch lt
JOIN page_visits pv
    ON lt.user_id = pv.user_id
    AND lt.last_touch_at = pv.timestamp)
SELECT utm_source, utm_campaign,COUNT(last_touch_at)
FROM lt_utm GROUP BY 1,2 ORDER BY 3 DESC; --last touch that resulted in purchase

SELECT COUNT(DISTINCT user_id) FROM page_visits
 WHERE page_name='4 - purchase';
    
