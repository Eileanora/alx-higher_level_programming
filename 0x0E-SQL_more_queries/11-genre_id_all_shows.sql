-- script that lists all shows contained in the database hbtn_0d_tvshows
-- each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results should be sorted in ascending order by the tv_shows.title and tv_show_genres.genre_id
-- if a show doesn't have a genre, display NULL

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
