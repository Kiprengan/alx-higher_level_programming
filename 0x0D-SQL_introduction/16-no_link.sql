-- Ommits records withoyt value in name column
SELECT score, name FROM second_table WHERE name NOT NULL
ORDER BY score DESC;
