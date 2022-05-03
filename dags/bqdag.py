import airflow
from airflow import DAG
from datetime import datetime, timedelta

from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators.bigquery_check_operator import BigQueryCheckOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past' : True,
    'start_date' : datetime.date.today(),
    'end_date' : datetime.date.today() + timedelta(days=5),
    'email' : ['your_email'],
    'email_on_failure' : True,
    'email_on_retry' : False,
    'retries' : 3,
    'retry_delay' : timedelta(minutes=5)
}

# Set up Shceduler
# Run pipeline once in a day at 10am IST. Cron tab is in UTC
schedule_interval = "0 10 * * *"

# Create DAG Object. 
dag = DAG (
    # Set ID
    'bigqyery_Query_Processing',
    default_args= default_args,
    schedule_interval= schedule_interval
)

# BigQuery Connection config variables
BQ_CONN_ID = "my_gcp_conn",
BQ_PROJECT = "gcp_project_name",
BQ_DATASET = "some_dataset"

# Create Tasks a.k.a Operators

# First task is to check is the BQ table & the data is present in it
task1 = BigQueryCheckOperator(
    task_id = 'checking_data_in_BQ',
    sql= '''
    Select * from `dataset.table_id` where column = 1234
    ''',
    use_legacy_sql = False,
    bigquery_conn_id = BQ_CONN_ID,
    dag = dag
)

# Once BQ Table & the data in it is checked, we are going to create a new table
task2 = BigQueryOperator(
    task_id = 'creating_new_bq_table',
    sql= '''
    bq query
    --destination_table = dataset.table
    --use_legacy_sql = false
    'Select column1,column2, column3
    from
    `project_id.dataset_id.table_name`
    where
    condition'
    ''',
    write_disposition = 'WRITE_TRUNCATE',
    allow_large_results = True,
    bigquery_conn_id = BQ_CONN_ID,
    dag=dag
)

# Specify Dependencies
task1 >> task2
