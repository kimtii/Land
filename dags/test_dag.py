# import pendulum

# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator

# with DAG(
#      dag_id="test",
#      start_date=pendulum.datetime(2024, 9, 3, tz="Asia/Seoul"),
#      schedule=None,
#      catchup=False,
# ) as dag :

#     #@task(task_id="print_the_context")
#     def print_context():
#         print("Hellow!!!")
    
#     print_the_context = PythonOperator(
#         task_id="print_the_context",
#         python_callable=print_context,
#         dag=dag
#     )

#     print_the_context = print_context()

# from Database import Database

# db = Database()
# print(db.fetchall("select 1"))

