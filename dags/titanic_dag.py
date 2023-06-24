
from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

import sys, os
sys.path.append(os.getcwd())

from titanic.titanic import *

# Instantiate the TitanicMain class
titanic = TitanicMain()

# Function to print the result
def print_result(**kwargs):
    r = kwargs['task_instance'].xcom_pull(key='result_msg')
    print("message : ", r)

# Default arguments for the DAG
default_args = {
    'owner': 'owner-name',
    'depends_on_past': False,
    'email': ['..'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=30)
}

# Arguments for the DAG
dag_args = dict(
    dag_id="titanic",
    default_args=default_args,
    description='tutorial DAG ml',
    schedule_interval=timedelta(minutes=50),
    start_date=datetime(2023, 6, 23),
    tags=['example'],
)

# Define the DAG
with DAG( **dag_args ) as dag:
    # Start task
    start = BashOperator(
        task_id='start',
        bash_command='echo "start!"',
    )

    # Preprocessing task
    prepro_task = PythonOperator(
        task_id='preprocessing',
        python_callable=titanic.prepro_data,
        op_kwargs={'f_name': "train"}
    )

    # Modeling task
    modeling_task = PythonOperator(
        task_id='modeling',
        python_callable=titanic.run_modeling,
        op_kwargs={'n_estimator': 100, 'flag' : True}
    )

    # Message task
    msg = PythonOperator(
        task_id='msg',
        python_callable=print_result
    )

    # Complete task
    complete = BashOperator(
        task_id='complete_bash',
        bash_command='echo "complete~!"',
    )

    # Define the task dependencies
    start >> prepro_task >> modeling_task >> msg >> complete