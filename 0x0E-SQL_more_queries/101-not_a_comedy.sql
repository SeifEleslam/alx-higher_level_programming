-- Counting the number of shows with each tv_genresenre
SELECT DISTINCT tv_shows.title,
    tv_genres.name
FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title NOT IN (
        SELECT title
        FROM tv_shows
            INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
            INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
        WHERE tv_genres.name = "Comedy"
    )
ORDER BY tv_shows.title;