-- list all cities in hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
-- join state_id from cities table and states.id from states table
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id
