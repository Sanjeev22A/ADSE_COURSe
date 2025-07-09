from utils import printAllTables,createConnectionObject,readTable,insertToTable

if __name__=="__main__":
    try:
        conn=createConnectionObject()
        with conn.cursor() as cursor:
            printAllTables(cursor)
            #insertToTable(cursor, "my_users", [1, "Alice", 30])
            conn.commit()
            readTable(cursor,"my_users",["id","name","age"])

    except Exception as e:
        print(str(e))