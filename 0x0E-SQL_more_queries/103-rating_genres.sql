-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT g.name, SUM(r.rate) AS rating FROM tv_genres g
INNER JOIN tv_show_genres m ON g.id=m.genre_id
INNER JOIN tv_show_ratings r ON m.show_id=r.show_id
GROUP BY g.name ORDER BY rating DESC;
