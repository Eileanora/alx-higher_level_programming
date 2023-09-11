-- a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS average_temperature
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;
