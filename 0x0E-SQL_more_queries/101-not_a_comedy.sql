-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title FROM tv_shows
WHERE title NOT IN
(
	SELECT s.title FROM tv_shows s
	INNER JOIN tv_show_genres m
	ON s.id=m.show_id
	INNER JOIN tv_genres g
	ON g.id=m.genre_id
	WHERE g.name='Comedy'
)
ORDER BY title ASC;
