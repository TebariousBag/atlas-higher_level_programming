-- list num of records with same score from second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;