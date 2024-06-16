import sys

sys.path.append("/home/deb-gama/personal_projects/Data_Pipeline")

import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

from etl.extract_csv_data import process_csv_extraction
from data.raw_tables.dp_clients import clients_config

default_args = {
    'owner': 'Data Pipeline',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('raw_to_bronze_dp_clients', default_args=default_args, schedule_interval=timedelta(days=1))

step_1 = PythonOperator(task_id='extract_dp_client', python_callable=process_csv_extraction(clients_config), dag=dag)

