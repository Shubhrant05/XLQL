def get_base_db_location():
    with open("config.py", "r") as file:
        for line in file:
            if line.startswith("BASE_DB_LOCATION="):
                return line.split("=", 1)[1].strip().strip("'\"")
            
def add_base_db_location(base_db_location):
    with open("config.py", "w") as config_file:
        config_file.write(f"BASE_DB_LOCATION='{base_db_location}'")