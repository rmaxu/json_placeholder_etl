import pandas as pd
import os
from scripts.json_placeholder_requests import JsonPlaceholder
from sqlalchemy import create_engine, text

jph = JsonPlaceholder()

def extract_posts() -> str:
    posts = jph.get_posts()
    df = pd.json_normalize(posts)
    df.rename(columns={"userId": "user_id"}, inplace=True)
    path = "/opt/airflow/dags/posts.csv"
    df.to_csv(path, index=False)
    return path

def extract_comments() -> str:
    comments = jph.get_comments()
    df = pd.json_normalize(comments)
    df.rename(columns={"postId": "post_id"}, inplace=True)
    path = "/opt/airflow/dags/comments.csv"
    df.to_csv(path, index=False)
    return path

def extract_users():
    users = jph.get_users()
    df = pd.json_normalize(users, record_prefix="_")
    return df


def load_data(name, path):
    host = "postgres-placeholder"
    user = os.environ["POSTGRES_USER_PLACEHOLDER"]
    password = os.environ["POSTGRES_PASSWORD_PLACEHOLDER"]
    database = os.environ["POSTGRES_DB_PLACEHOLDER"]
    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:5432/{database}"
    )
    df = pd.read_csv(path)
    with engine.begin() as conn:
        conn.execute(
            text(
                f"DELETE FROM {name};"
            )
        )
    df.to_sql(name=name, con=engine, if_exists='append', index=False)
    