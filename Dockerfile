FROM apache/airflow:2.5.1
RUN pip install --no-cache-dir psycopg2-binary sqlalchemy numpy pandas