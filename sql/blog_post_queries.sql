SELECT 
    p.user_id, COUNT(c.id) AS n_comments
FROM comments AS c
LEFT JOIN posts AS p
    ON c.post_id = p.id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

SELECT
    post_id, COUNT(id)
FROM comments
GROUP BY 1;

SELECT 
    id, 
    post_id, 
    body, 
    LENGTH(body) AS comment_size 
FROM comments 
ORDER BY 4 DESC 
LIMIT 1;