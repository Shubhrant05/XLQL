import argparse
from xlql.commands import create_db, list_db

def main():
    print("XLQL CLI tool activated!")
    parser = argparse.ArgumentParser(prog="xlql", description="XLQL CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    #create db command
    create_parser = subparsers.add_parser("createdb", help="Create a new database")
    create_parser.set_defaults(func=create_db.main)

    #list db command
    drop_parser = subparsers.add_parser("listdb", help="List all the existing database")
    drop_parser.set_defaults(func=list_db.main)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
