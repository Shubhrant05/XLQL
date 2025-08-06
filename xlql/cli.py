import argparse
from xlql.commands import create_db, list_db, delete_db, insert, list_table, delete_table
from xlql.core.utils import get_base_db_location, add_base_db_location
def main():
    base_db_location = get_base_db_location()

    if base_db_location == "":
        base_db_location = input("Please enter base location to store your db: ")
        add_base_db_location(base_db_location)
   

    parser = argparse.ArgumentParser(prog="xlql", description="XLQL CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    #create db command
    create_parser = subparsers.add_parser("createdb", help="Create a new database")
    create_parser.set_defaults(func=create_db.main)

    #list db command
    list_parser = subparsers.add_parser("listdb", help="List all the existing database")
    list_parser.set_defaults(func=list_db.main)

    #drop db command
    drop_parser = subparsers.add_parser("dropdb", help="Deletes the chosen database")
    drop_parser.set_defaults(func=delete_db.main)

    #insert table command
    insert_parser = subparsers.add_parser("insert", help="Insert the file in the selected DB")
    insert_parser.set_defaults(func=insert.main)

    #list table command
    list_parser = subparsers.add_parser("list", help="List the tables in the selected DB")
    list_parser.add_argument("db_name", type=str, help="Name of the database to lookup")
    list_parser.set_defaults(func=list_table.main)

    #delete table command
    delete_parser = subparsers.add_parser("droptable", help="Deletes the selected tables from the selected DB")
    delete_parser.add_argument("db_name", type=str, help="Name of the database to lookup")
    delete_parser.set_defaults(func=delete_table.main)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
