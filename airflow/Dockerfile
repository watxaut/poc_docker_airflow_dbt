FROM puckel/docker-airflow:1.10.7
USER root

RUN pip3 install virtualenv
RUN virtualenv /usr/local/airflow/env_dbt --python=python3
RUN /usr/local/airflow/env_dbt/bin/pip3 install dbt

USER airflow