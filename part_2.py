import datetime
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database(dbname):
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='12345678'"
    conn = psycopg2.connect(conn_string)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    sql_drop_database = f"DROP DATABASE IF EXISTS {dbname};"
    sql_create_database = f"CREATE DATABASE {dbname};"
    cursor.execute(sql_drop_database)
    cursor.execute(sql_create_database)
    print("Database has been created successfully!")
    conn.close()

def connect_postgres(dbname):
    conn_string = f"host='localhost' dbname={dbname} user='postgres' password='12345678'"
    conn = psycopg2.connect(conn_string)
    return conn

def execute_schema_script(conn, script_path):
    with conn.cursor() as cursor:
        with open(script_path, 'r') as f:
            sql_script = f.read()
            cursor.execute(sql_script)
    conn.commit()
    print("Schema has been created successfully!")

def execute_insert_script(conn, script_path):
    with conn.cursor() as cursor:
        with open(script_path, 'r') as f:
            sql_script = f.read()
            cursor.execute(sql_script)
    conn.commit()
    print("Data has been inserted successfully!")

def perform_fragmentation(conn):
    
    cursor = conn.cursor()
    product_categories = ['Electronics', 'Clothing and Fashion', 'Books']
    warehouse_locations = ['Tech City', 'Fashion District']

    for category in product_categories:
        table_name = f'Products_{category.replace(" ", "_")}'
        create_table_query = f'''
        CREATE TABLE {table_name} AS
        SELECT * FROM Products
        WHERE Category = '{category}';
        '''
        cursor.execute(create_table_query)

    for location in warehouse_locations:
        table_name = f'Warehouses_{location.replace(" ", "_")}'
        create_table_query = f'''
        CREATE TABLE {table_name} AS
        SELECT * FROM Warehouses
        WHERE Location = '{location}';
        '''
        cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def replication(dbname):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    copy_dbname = f"{dbname}_backup_{timestamp}"

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='12345678'"
    conn = psycopg2.connect(conn_string)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    sql_create_copy = f"CREATE DATABASE {copy_dbname} TEMPLATE {dbname};"
    cursor.execute(sql_create_copy)
    print(f"Database copy '{copy_dbname}' has been created successfully!")
    conn.close()

if __name__ == '__main__':
    dbname = "supply_chain"
    create_database(dbname)
    conn = connect_postgres(dbname)
    schema_file_path = "main_schema.sql"
    execute_schema_script(conn, schema_file_path)
    insert_data_file_path = "insert_data.sql"
    execute_insert_script(conn, insert_data_file_path)
    perform_fragmentation(conn)
    replication(dbname)

    conn.close()
