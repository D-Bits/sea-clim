FROM apache/airflow:latest

USER root
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

ADD requirements.txt .
RUN pip install --upgrade pip && pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt

USER airflow