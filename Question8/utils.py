import psycopg2
from dotenv import load_dotenv
import os
from typing import List,Any

load_dotenv()

username=os.getenv("POSTGRES_USERNAME")
password=os.getenv("POSTGRES_PASSWORD")

class DBConnError(Exception):
    "Custom error for DB Exceptions- when connection fails"
    pass
class TableExistError(Exception):
    "Custom error for DB Exception- when table already exist or table creation fails"
    pass
class TableInsertException(Exception):
    "Custom error for DB Exception- when insert statement isnt correct"
    pass

def createConnectionObject(dbname:str="sample",username:str=username,password:str=password)->psycopg2.extensions.connection:
    try:
        conn=psycopg2.connect(
            dbname=dbname,
            user=username,
            password=password,
            host="localhost"
        )
        return conn
    except Exception as e:
        raise DBConnError("Connection to database failed")

#def createCursorObject()

def printAllTables(cursor:psycopg2.extensions.cursor)->List[str]:
    try:
        cursor.execute("""
        SELECT table_name FROM information_schema.tables where table_schema='public';
        """)
        rows=cursor.fetchall()
        print("-----Tables------")
        table_names=[]
        for row in rows:
            print(row[0])
            table_names.append(row[0])
        print("-----------------")
        return table_names
    except Exception as e:
        raise Exception(str(e))


def checkTableExist(cursor:psycopg2.extensions.cursor,table_name:str)->bool:
    try:
        
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = %s 
                AND table_name = %s
            );
        """, ("public", table_name))
        return cursor.fetchone()[0]
    except Exception as e:
        raise TableExistError("Failed to operate")

def createTable(cursor:psycopg2.extensions.cursor,attributeList:List[tuple[str]],table_name:str="myTable"):
    try:
        if(checkTableExist(cursor,table_name)):
            raise TableExistError("Table Already exist")
        command=f"create table {table_name} (\n"
        column_defs = [f"{attr_name} {attr_type}" for attr_name, attr_type in attributeList]
        command+=",".join(column_defs)
        command+=");"
        print(command)
        cursor.execute(command)

    except Exception as e:
        raise TableExistError(str(e))

def insertToTable(cursor:psycopg2.extensions.cursor,table_name:str,val_list:List[Any]):
    try:
        placeholders = ', '.join(['%s'] * len(val_list))  
        command = f"INSERT INTO {table_name} VALUES ({placeholders});"
        print("Executing:", command)
        cursor.execute(command, val_list)
        print("Inserted into table")
    except Exception as e:
        raise TableInsertException("Format not matching")



def readTable(cursor: psycopg2.extensions.cursor, table_name: str, attributeList: List[str]):
    try:
        if(not checkTableExist(cursor,table_name)):
            raise TableExistError("Table doesnt exist")
        columns = ", ".join(attributeList) if attributeList else "*"
        command = f"SELECT {columns} FROM {table_name};"
        cursor.execute(command)
        rows = cursor.fetchall()

  
        if attributeList:
            headers = attributeList
        else:
            headers = [desc[0] for desc in cursor.description]

    
        widths = [len(h) for h in headers]
      
        for row in rows:
            for i, val in enumerate(row):
                widths[i] = max(widths[i], len(str(val)))

        
        fmt = "| " + " | ".join(f"{{:<{w}}}" for w in widths) + " |"


        sep = "+-" + "-+-".join("-" * w for w in widths) + "-+"


        print(sep)
        print(fmt.format(*headers))
        print(sep)


        for row in rows:
            print(fmt.format(*(str(v) for v in row)))
        print(sep)

    except Exception as e:
        raise Exception(f"Error while reading table: {e}")

