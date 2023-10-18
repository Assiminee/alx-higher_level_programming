-- Lists all genres of the show Dexter
SELECT g.name FROM tv_genres g
INNER JOIN tv_show_genres m
ON g.id = m.genre_id
INNER JOIN tv_shows s
ON m.show_id = s.id
WHERE s.title="Dexter";
