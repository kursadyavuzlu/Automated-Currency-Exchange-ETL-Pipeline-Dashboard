from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from extract import extract_data
from transform import transform_data
from load import run_load_process

with DAG(
    dag_id='currency_etl_pipeline',
    start_date = datetime(2026, 6, 13),
    schedule_interval = None,
    catchup = False
    
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
        provide_context=True
    )

    load_task = PythonOperator(
        task_id="run_load_process",
        python_callable=run_load_process
    )
    
    extract_task >> transform_task >> load_task

    
    
