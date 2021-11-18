-- Lists the number of records within a group in a table
SELECT score, COUNT(score) AS num FROM second_table GROUP BY score ORDER BY num DESC;
