-- list all cities of California found in hbtn_0d_usa
SELECT id, name
FROM cities
-- select california from states column
WHERE state_id =(
	SELECT id
	FROM states
	WHERE name = 'California'
);
