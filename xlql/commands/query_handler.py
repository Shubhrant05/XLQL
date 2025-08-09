from xlql.core.utils import read_query_from_file, register_csv
import os
import duckdb as dd

def main(args):
    try:
        db_name = args.db_name
        query_path = args.query_path

        # validating db name
        if not db_name:
            print("[ERROR] Database name is required.")
            return

        # validating query path
        if not query_path or not os.path.exists(query_path):
            print(f"[ERROR] Query file '{query_path}' not found.")
            return

        # reading SQL query
        query = read_query_from_file(query_path)
        if not query:
            print("[ERROR] Query file is empty.")
            return
        
        # Run query
        conn = dd.connect(':memory:')
        register_csv(conn, db_name)
        result = conn.execute(query).fetchdf()

        # Pretty-print results if any
        if result is not None and not result.empty:
            from tabulate import tabulate
            print(tabulate(result, headers=result.columns, tablefmt="fancy_grid", showindex=False))
        else:
            print("[INFO] Query executed successfully, but returned no results.")

    except Exception as e:
        print(f"[ERROR] {e}")
