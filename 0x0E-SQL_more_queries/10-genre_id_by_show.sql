-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT s.title, m.genre_id
FROM tv_shows s INNER JOIN tv_show_genres m
ON m.show_id = s.id
ORDER BY s.title, m.genre_id;
