FROM apache/airflow:2.6.2

RUN pip3 install -U scikit-learn

WORKDIR /opt/airflow
