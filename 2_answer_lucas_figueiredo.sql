SELECT concat(first_name, ' ', last_name) AS actor_name
FROM actor
INNER JOIN film_actor
USING (actor_id)
GROUP BY actor_name
ORDER BY count(film_id) desc
LIMIT 16, 1;