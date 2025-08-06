import os
from xlql.core.utils import get_base_db_location
def main(args):
    db_location = os.path.join(get_base_db_location(), "databases")
    for item in os.listdir(db_location):
        full_path = os.path.join(db_location ,item)
        if os.path.isdir(full_path):
            print(item)