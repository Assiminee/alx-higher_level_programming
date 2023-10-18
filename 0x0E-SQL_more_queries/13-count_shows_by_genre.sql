-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.name AS genre, COUNT(g.name) AS number_of_shows
FROM tv_genres g INNER JOIN tv_show_genres m
ON g.id = m.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
