SELECT * FROM stream LIMIT 10;
SELECT * FROM chat LIMIT 10;

SELECT DISTINCT game from stream;
SELECT DISTINCT channel from stream;

SELECT game , COUNT(*) from stream
GROUP BY game ORDER BY 2 desc;  --most popular games

SELECT country, COUNT(*) from stream
WHERE game = 'League of Legends'
GROUP BY 1 ORDER BY 2 DESC;  --LoL stream viewers countries

SELECT player, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

SELECT game,
CASE WHEN game = 'League of Legends' OR game ='Dota 2' OR 'Heroes of the Storm' THEN 'MOBA'
WHEN game ='Counter-Strike: Global Offensive' THEN 'FPS'
WHEN game ='DayZ' or game='ARK: Survival Evolved' THEN 'Survival'
ELSE 'Other' END AS 'genre', COUNT(*)
FROM stream
GROUP BY 1 ORDER BY 3 DESC;

SELECT time
FROM stream
LIMIT 10;  --time column is a datetime object

SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;  --returns seconds

SELECT strftime('%H',time) as 'hour_streamed', COUNT(*)
FROM stream WHERE country='US' GROUP BY 1 ORDER BY 2 DESC;

SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;





