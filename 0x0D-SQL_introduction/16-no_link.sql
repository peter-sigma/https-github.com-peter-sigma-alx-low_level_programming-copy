-- ALL RECORDS OF THE TABLE WITHOUT NAME, DESCENDING ORDER AND DB NAME IS PASSED AS ARGUMENT
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;