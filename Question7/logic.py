from typing import List, Tuple, Dict, Any
import psycopg2
from utils import createConnectionObject,readTable,checkTableExist,createTable,insertToTable

database_structure: Dict[str, Dict[str, Any]] = {
    "new_employees": {
        "attributes": [("id", "INT"), ("name", "TEXT"), ("salary", "INT")],
        "rows": [
            [1, "Alice", 50000],
            [2, "Bob", 60000],
            [3, "Charlie", 55000],
            [4, "Diana", 62000],
            [5, "Eve", 58000]
        ]
    },
    "departments": {
        "attributes": [("dept_id", "INT"), ("dept_name", "TEXT"), ("floor", "INT")],
        "rows": [
            [1, "HR", 2],
            [2, "Engineering", 5],
            [3, "Sales", 3],
            [4, "Marketing", 4],
            [5, "Finance", 1]
        ]
    },
    "projects": {
        "attributes": [("project_id", "INT"), ("project_name", "TEXT"), ("budget", "INT")],
        "rows": [
            [101, "Apollo", 100000],
            [102, "Zeus", 200000],
            [103, "Hermes", 150000],
            [104, "Athena", 120000],
            [105, "Poseidon", 180000]
        ]
    },
    "clients": {
        "attributes": [("client_id", "INT"), ("client_name", "TEXT"), ("country", "TEXT")],
        "rows": [
            [1, "Acme Corp", "USA"],
            [2, "Globex", "UK"],
            [3, "Initech", "Canada"],
            [4, "Umbrella", "Germany"],
            [5, "Wayne Enterprises", "USA"]
        ]
    },
    "assets": {
        "attributes": [("asset_id", "INT"), ("asset_name", "TEXT"), ("value", "INT")],
        "rows": [
            [1, "Laptop", 1500],
            [2, "Monitor", 300],
            [3, "Printer", 500],
            [4, "Desk", 200],
            [5, "Chair", 100]
        ]
    }
}

def read_all(cursor):
    for table_name,values in database_structure.items():
        attribute_list=[att_name[0] for att_name in values['attributes']]
        
        readTable(cursor,table_name,attribute_list)

def main():
    try:
        conn = createConnectionObject()
        with conn.cursor() as cursor:
            
            for table_name, table_info in database_structure.items():
               
                createTable(
                    cursor=cursor,
                    attributeList=table_info["attributes"],
                    table_name=table_name
                )
               
                for row in table_info["rows"]:
                    insertToTable(cursor, table_name, row)

            conn.commit()
            print("All tables created and populated successfully.")
            read_all(cursor)
    except Exception as e:
        print(f"Exception raised: {e}")


if __name__=="__main__":
    main()

