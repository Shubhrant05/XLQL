def get_base_db_location():
    with open("config.py", "r") as file:
        for line in file:
            if line.startswith("BASE_DB_LOCATION="):
                return line.split("=", 1)[1].strip().strip("'\"")