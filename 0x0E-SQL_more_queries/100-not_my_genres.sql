-- Counting the number of shows with each genre
SELECT DISTINCT tv_genres.name
FROM tv_genres
    LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name NOT IN (
        SELECT name
        FROM tv_genres
            INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_genres.id
            INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.genre_id
        WHERE tv_shows.title = 'Dexter'
    )
ORDER BY tv_genres.name;