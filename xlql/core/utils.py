import os
import os
import duckdb
import pandas as pd

def get_base_db_location():
    with open("config.py", "r") as file:
        for line in file:
            if line.startswith("BASE_DB_LOCATION="):
                return line.split("=", 1)[1].strip().strip("'\"")
            
def add_base_db_location(base_db_location):
    with open("config.py", "w") as config_file:
        config_file.write(f"BASE_DB_LOCATION='{base_db_location}'")
    
def get_csv_path(db_name, table_name):
    base_path = get_base_db_location()
    return os.path.join(base_path, "databases", db_name, table_name)

def run_query_on_csv(query: str, db_name: str, table_name: str):
    base_path = get_base_db_location()
    if not base_path:
        raise FileNotFoundError("Base DB location is not set.")

    csv_path = os.path.join(base_path, "databases", db_name, table_name)
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Table (CSV) '{table_name}' not found in '{db_name}'.")

    con = duckdb.connect()
    try:
        # Register as a temp view to allow using `table_name` in the query
        con.execute(f"CREATE OR REPLACE VIEW temp_table AS SELECT * FROM read_csv_auto('{csv_path}')")
        
        # Replace any mention of table_name in the query with `temp_table`
        safe_query = query.replace(table_name, "temp_table")
        result = con.execute(safe_query).fetchdf()
        result =result.fillna("")
        result = result.astype(str)
        return result
    finally:
        con.close()

def get_csv_headers(file_path):
    """
    Returns the headers (column names) of a CSV file using pandas.
    
    :param file_path: Path to the CSV file
    :return: List of header names
    """
    try:
        df = pd.read_csv(file_path, nrows=0)  # Read only the headers
        return df.columns.tolist()
    except FileNotFoundError:
        print(f"\033[91m[ERROR]\033[0m File not found: {file_path}")
        return []
    except Exception as e:
        print(f"\033[91m[ERROR]\033[0m Failed to read CSV headers: {e}")
        return []
