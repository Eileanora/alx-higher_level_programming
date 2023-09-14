-- script that litsts all cities contained in the database hbtn_0d_usa
-- sort ascending by cities.id
-- one select statment

SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
