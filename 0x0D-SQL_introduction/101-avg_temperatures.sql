-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending) from the table hbtn_0c_0
USE hbtn_0c_0;
SOURCE temperatures.sql;
SELECT city, AVG(value) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
