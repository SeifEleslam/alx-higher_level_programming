-- Counting the number of shows with each genre
SELECT DISTINCT tv_genres.name,
    tv_shows.title
FROM tv_genres
    LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
--  (
--         SELECT title
--         FROM tv_shows
--             INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
--             INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
--         WHERE tv_genres.name = "Comedy"
--     )