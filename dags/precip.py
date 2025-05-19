from airflow.sdk import dag, task
from datetime import datetime



@dag(schedule='@daily', start_date=datetime(2025, 5, 21), catchup=False)
def precip_dag():

    @task
    def extract():
        return {'precip': 0.5, 'temperature': 20}

    @task
    def transform(data):
        data['precip'] *= 2
        return data

    @task
    def load(data):
        print(f"Data loaded: {data}")

    data = extract()
    transformed_data = transform(data)
    load(transformed_data)

# Instantiate the DAG
precip_dag()
