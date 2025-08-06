import argparse
from xlql.commands import create_db, list_db
from xlql.core.utils import get_base_db_location
def main():
    base_db_location = get_base_db_location()

    if base_db_location == "":
        base_db_location = input("Please enter base location to store your db: ")

    with open("config.py", "w") as config_file:
        config_file.write(f"BASE_DB_LOCATION='{base_db_location}'")

    parser = argparse.ArgumentParser(prog="xlql", description="XLQL CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    #create db command
    create_parser = subparsers.add_parser("createdb", help="Create a new database")
    create_parser.set_defaults(func=create_db.main)

    #list db command
    list_parser = subparsers.add_parser("listdb", help="List all the existing database")
    list_parser.set_defaults(func=list_db.main)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
