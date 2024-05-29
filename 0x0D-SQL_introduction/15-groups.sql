-- script that displays the number of records with id = 89
-- in the table first_table of the database hbtn_0c_0 in your MySQL server
-- SELECT * FROM first_table where id=89   -> To list a the data with same id
SELECT score, COUNT(*) AS number FROM second_table GROUP BY
score ORDER BY number DESC;
