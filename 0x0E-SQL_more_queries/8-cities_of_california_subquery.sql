-- script that shoes all cities of California that can be found in the database hbtn_0d_usa

SELECT cities.name
FROM cities
WHERE cities.state_id IN(
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
);
