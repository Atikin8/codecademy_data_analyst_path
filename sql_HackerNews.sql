
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

SELECT SUM(score) as alltime_score
FROM hacker_news;

SELECT user, SUM(score) as total_score
FROM hacker_news
GROUP BY user
HAVING total_score >200
ORDER BY total_score DESC;

SELECT (517+309+304+282)/6366.0;

SELECT user, count(*)
FROM hacker_news
WHERE url LIKE '%dQw4w9WgXcQ'
GROUP BY user
ORDER BY count(*) DESC;

SELECT CASE
WHEN url LIKE '%github.com%' THEN 'GitHub'
WHEN url LIKE '%medium.com%' THEN 'Medium'
WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
ELSE 'Other'
END AS 'Source' , count(*)
FROM hacker_news
GROUP BY 1;

SELECT timestamp, strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

SELECT strftime('%H', timestamp) as hour, ROUND(AVG(score),1) as avg_score, COUNT(*) as num_posts
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER By 1;















 