-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT s.title, g.name FROM tv_shows s
LEFT OUTER JOIN tv_show_genres m
ON s.id = m.show_id
LEFT OUTER JOIN tv_genres g
ON m.genre_id = g.id
ORDER BY s.title, g.name ASC;
