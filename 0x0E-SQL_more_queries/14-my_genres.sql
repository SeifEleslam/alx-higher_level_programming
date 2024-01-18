-- Counting the number of shows with each genre
SELECT tv_genres.name,
    FROM tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    INNER JOIN tv_shows ON tv_shows.title = 'Dexter'
GROUP BY genre
ORDER BY number_of_shows DESC;