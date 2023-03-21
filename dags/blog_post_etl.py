from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.models.baseoperator import chain
from datetime import datetime, timedelta
from scripts.functions import extract_posts, extract_comments, load_data

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
        "blog_post_etl",
        start_date= datetime(2021,1,1),
        schedule_interval= "@daily",
        default_args= default_args, 
        catchup= False) as dag :

    # Extract
    posts = PythonOperator(
        task_id="extract_posts",
        python_callable=extract_posts)
    
    comments = PythonOperator(
        task_id="extract_comments",
        python_callable=extract_comments)
    

    are_posts_available = FileSensor(
        task_id="are_posts_available",
        filepath="/opt/airflow/dags/posts.csv",
        poke_interval=2,
        timeout=10,
        fs_conn_id='posts'
    )

    are_comments_available = FileSensor(
        task_id="are_comments_available",
        filepath="/opt/airflow/dags/comments.csv",
        poke_interval=2,
        timeout=10,
        fs_conn_id='comments'
    )

    # Load
    load_posts = PythonOperator(
        task_id="load_posts",
        python_callable=load_data,
        op_kwargs={"name": "posts", "path": "/opt/airflow/dags/posts.csv"})
    
    load_comments = PythonOperator(
        task_id="load_comments",
        python_callable=load_data,
        op_kwargs={"name": "comments", "path": "/opt/airflow/dags/comments.csv"})

    # Order of execution
    chain([posts, comments], [are_posts_available, are_comments_available], [load_posts, load_comments])
