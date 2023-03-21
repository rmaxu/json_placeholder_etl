/* 
1. Retrieve the userId that made most comments on all the Posts

Note that this query return the user_id with the most number of comments,
howerver, if you delete the 'LIMIT 1' we can notice that all the users have 
the same amount of comments, so at the end we're just taking one of them.
*/
SELECT 
    p.user_id, 
    COUNT(c.id) AS n_comments
FROM comments AS c
LEFT JOIN posts AS p
    ON c.post_id = p.id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;


-- 2. Retrieve the number of comments per Post
SELECT
    post_id, 
    COUNT(id)
FROM comments
GROUP BY 1;

-- 3. Retrieve the longest post comment made on all the posts
SELECT 
    id, 
    post_id, 
    body, 
    LENGTH(body) AS comment_size 
FROM comments 
ORDER BY 4 DESC 
LIMIT 1;