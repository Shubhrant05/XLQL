from xlql.core.utils import get_base_db_location
def main(args=None):
    import os
    db_location = get_base_db_location()
    
    if db_location == "":
        print("[ERROR] Base DB location not found!")
        return
    db_name = input("Enter the name of the new database: ").strip()
    if not db_name:
        print("[ERROR] Database name cannot be empty.")
        return
    
    db_path = os.path.join(db_location, "databases", db_name)

    if os.path.exists(db_path):
        print(f"[ERROR] Database '{db_name}' already exists at {db_path}")
    else:
        os.makedirs(db_path, exist_ok=True)
        print(f"[SUCCESS] Database '{db_name}' created successfully at {db_path}")