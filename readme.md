# POC Docker - Airflow - DBT
## Install
To use the repo locally you should install the requirements.txt into a virtual environment
using:
```shell script
pip install -r requirements
```  

To start the docker and run it locally:
```shell script
docker-compose build
docker-compose up
```

And it will build automatically the docker-compose.yml file.
Airflow will be available at http://localhost:8081 after building