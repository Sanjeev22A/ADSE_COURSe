import psycopg2
username="postgres"
password="changeme"

try:
    conn=psycopg2.connect(
        dbname="sample",
        user=username,
        password=password,
        host="localhost"
    )
    cursor=conn.cursor()
    cursor.execute("""SELECT table_name from information_schema.tables 
    where table_schema='public' and table_type='BASE TABLE'
    """)
    tables=cursor.fetchall()
    print("-"*20)
    print(f"Table names:")
    for table in tables:
        print(table[0])
    print("-"*20)
    
    for table in tables:
        print("-"*20)
        print("-"*20)
        print(f"Fetching from tablename : {table[0]}")
        print("-"*20)
        command=f"select * from {table[0]}";

        rows=cursor.execute(command)
        for row in rows:
            print(f"{row}")
        print("-"*20)
    conn.close()
except Exception as e:
    print(f"Connection failed:{e}")


