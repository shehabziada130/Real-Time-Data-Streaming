from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator 

default_args={
    'owner':'shehab',
    'start_date':datetime(2024,9,4,10,00)
}

def get_data():
    import requests

    res=requests.get('https://randomuser.me/api/')
    res=res.json()
    return res['results'][0]

def format_data(res):
    import json 

    data={
        'first_name':res['name']['first'],
        'last_name':res['name']['last'],
        'gender':res['gender'],
        'address':f"{str(res['location']['street']['number'])} {res['location']['street']['name']}"\
                  f"{res['location']['city']}, {res['location']['state']}, {res['location']['country']}",
        'email':res['email'],
        'username': res['login']['username'],
        'dob': res['dob']['date'],
        'registered_date': res['registered']['date'],
        'phone': res['phone'],
        'picture': res['picture']['medium'],
    }
    return data

def stream_data():
    import time
    from kafka import KafkaProducer
    import json 
    import logging 

    producer = KafkaProducer(bootstrap_servers=['broker:29092'],max_block_ms=5000)
    curr_time=time.time()

    while True: 
        if time.time()>curr_time+60:
            break
        try:
            res=get_data()
            res=format_data(res)
            producer.send('user_created',json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An Error: {e}')
            continue


with DAG ('user_automation',
default_args=default_args,
schedule_interval='@daily',
catchup=False) as dag:
    streaming_data=PythonOperator(
        task_id='stream_data',
        python_callable=stream_data
)


