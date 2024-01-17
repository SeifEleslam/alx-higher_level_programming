-- score too low
SELECT score, name
WHERE name NOT NULL
FROM second_table
ORDER BY score DESC;
