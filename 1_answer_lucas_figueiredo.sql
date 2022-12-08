SELECT f.title
FROM film AS f
INNER JOIN inventory AS i USING (film_id)
INNER JOIN rental AS R USING (inventory_id)
GROUP BY f.title,r.rental_id
ORDER BY count(r.inventory_id) DESC   
LIMIT 2;