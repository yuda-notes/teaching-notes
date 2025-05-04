from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd


def dataCleaning():
    df = pd.read_csv('/opt/airflow/data/top-1000-trending-youtube-videos.csv')

    # drop rank
    df.drop(columns='rank', inplace=True)
    # drop missing values
    df.dropna(inplace=True)
    # drop duplicates
    df.drop_duplicates(inplace=True)
    # adjust column name
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    df.to_csv('/opt/airflow/data/trending-youtube-videos.csv', index=False)


def convertToJson():
    df = pd.read_csv('/opt/airflow/data/trending-youtube-videos.csv')

    # convert to json
    df.to_json(
        path_or_buf="/opt/airflow/data/trending-youtube-videos.json",
        orient="records"
    )


# define DAG tasks
with DAG(
    dag_id='csv_to_json',
    start_date=datetime.now()
) as dag:

    welcome_msg = BashOperator(
        task_id='welcome_msg',
        bash_command='echo "processing..."'
    )

    data_cleaning = PythonOperator(
        task_id='data_cleaning',
        python_callable=dataCleaning
    )

    convert_to_json = PythonOperator(
        task_id='convert_to_json',
        python_callable=convertToJson
    )

    done = BashOperator(
        task_id='done',
        bash_command='echo "done!"'
    )

    # define flow
    welcome_msg >> data_cleaning >> convert_to_json >> done
