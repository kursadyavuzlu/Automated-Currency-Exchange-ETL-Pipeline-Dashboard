import psycopg2

def insert_data(connection, data_list):
    cursor = connection.cursor()

    query = """INSERT INTO exchange_rates (currency_date, base_currency, target_currency, rate)
    VALUES (%s, %s, %s, %s)"""

    for row in data_list: 
        values = (row["date"], row["base"], row["quote"], row["rate"])
        cursor.execute(query, values)

    connection.commit()
    cursor.close()
    print("DATAS UPLOAD SUCCESSFULY")
    
def run_load_process(**kwargs):
    
    ti = kwargs['ti']
    
    real_data = ti.xcom_pull(task_ids='transform_data')
    
    print("Cleaned data successfully pulled from XCom")

    try:
        connection = psycopg2.connect(
            host="my_postgres_container",
            database="postgres",
            user="postgres",
            password="aranel33",
            port="5432"
        )
        print("CONNECTION SUCCESS")
        
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS exchange_rates (
                id SERIAL PRIMARY KEY,
                currency_date TIMESTAMP,
                base_currency VARCHAR(3),
                target_currency VARCHAR(3),
                rate FLOAT
            );
        """)
        connection.commit()
        cursor.close()
        print("TABLE CREATED SUCCESSFULLY")
        
        insert_data(connection, real_data)
        
        connection.close()

    except Exception as error:
        print(f"ERROR FIND!!! ---> {error}")
        raise error