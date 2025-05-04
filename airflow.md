# Airflow

## Definition

- Airflow is a platform for developing, scheduling, and monitoring batch-oriented workflows.
- It's widely used for orchestrating ETL (Extract, Transform, Load) processes, but it's also applicable to various other data and computing workflows.
- Airflow allows users to define workflows as Directed Acyclic Graphs (DAGs) using Python, enabling visualization and management of dependencies, execution, and monitoring.
    ![](https://airflow.apache.org/docs/apache-airflow/2.5.1/_images/branch_with_trigger.png)

### DAG ([reference](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html))

- DAG is an object that encapsulates everything needed to execute a workflow.
- Some DAG attributes include the following:
  - Schedule
  - Task
  - Task Dependencies
  - etc.

### Task

- Task is the basic unit of execution.
- Tasks are arranged into DAGs, and then have upstream and downstream dependencies set between them into order to express the order they should run in.
- There are three basic kinds of Task:
  - [Operator](https://airflow.apache.org/docs/apache-airflow/2.3.0/concepts/operators.html), predefined task templates that you can define declaratively inside your DAG.
    - For a list of all core operators, [see here](https://airflow.apache.org/docs/apache-airflow/2.3.0/operators-and-hooks-ref.html)
  - [Sensors](https://airflow.apache.org/docs/apache-airflow/2.3.0/concepts/sensors.html), a special type of Operator that are designed to do exactly one thing - wait for something to occur.
  - [TaskFlow](https://airflow.apache.org/docs/apache-airflow/2.3.0/concepts/taskflow.html), is an API that consist of `@task` decorator to create a clean DAG without extra boilerplate.

## Setup

- To create airflow DAG we must install this package

    ```bash
    pip install apache-airflow
    ```

- We also need to install docker for running Airflow in localhost environment.
  - See the sample docker compose [here]()

## DAG Example

```py
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
```
