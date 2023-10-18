-- List all genres not linked to the show Dexter
SELECT name FROM tv_genres
WHERE name NOT IN
(
	SELECT g.name FROM tv_genres g
	INNER JOIN tv_show_genres m
	ON g.id=m.genre_id
	INNER JOIN tv_shows s
	ON s.id=m.show_id
	WHERE s.title='Dexter'
)
ORDER BY name ASC;
