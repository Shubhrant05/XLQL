import os
from xlql.core.utils import get_base_db_location, list_databases
import questionary
from xlql.core.logger_config import logger

def main(args=None):
    db_location = get_base_db_location()

    if not db_location:
        logger.warning('Try running `xlql createdb` to get started.')
        return
    
    db_list = list_databases()
    if not db_list:
        logger.error('No databases found. Please create one first.')
        return

    db_name = questionary.select(
        "Select a database:",
        choices=db_list
    ).ask()
    if not db_name:
        logger.info('Operation cancelled.')
        return
    
    db_folder = os.path.join(db_location, "databases", db_name)

    if not os.path.exists(db_folder):
        logger.error(f"Database '{db_name}' does not exist.")
        return

    print(f"\033[94mTables inside database '{db_name}':\033[0m")

    files = os.listdir(db_folder)
    if not files:
        print("\033[2mNo tables found in this database.\033[0m")
    else:
        for file in files:
            display_name = file.rpartition('.')[0]
            print(f"  - {display_name}")
