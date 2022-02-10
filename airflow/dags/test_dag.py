import datetime

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow import DAG

default_args = {
    "owner": "joan.heredia",
    "depends_on_past": False,
    "start_date": datetime.datetime(2020, 3, 7, 0, 0, 0),
    "email": ["watxaut@gmail.com", ],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
description = "A simple DAG"


def dummy_func(x, y):
    return (x + y) ** 2


with DAG(dag_id="test_dag", default_args=default_args, description=description, schedule_interval="@once") as dag:
    d_ops = {n: DummyOperator(dag=dag, task_id=f"dummy_{n}") for n in range(5)}
    py_op = PythonOperator(dag=dag, task_id="python_dummy_task", python_callable=dummy_func, op_args=[5, 2])

    test_dbt = BashOperator(
        task_id="test_dbt", bash_command="source /usr/local/airflow/env_dbt/bin/activate && dbt --help", dag=dag,
    )

d_ops[0] >> d_ops[1] >> d_ops[2] >> d_ops[4]
d_ops[1] >> d_ops[3] >> d_ops[4]
d_ops[3] << py_op << test_dbt
