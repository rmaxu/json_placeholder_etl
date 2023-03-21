CREATE TABLE IF NOT EXISTS public.posts
(
    id integer NOT NULL,
    user_id integer NOT NULL,
    title text,
    body text,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.comments
(
    id integer NOT NULL,
    post_id integer NOT NULL,
    "name" text,
    email text,
    body text,
    PRIMARY KEY (id)
);