-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT c.id, c.name
FROM (SELECT * FROM states WHERE name = 'California') AS s 
INNER JOIN cities c ON s.id = c.state_id;
