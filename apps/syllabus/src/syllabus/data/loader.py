from typing import Literal

from syllabus.ports.dbs import DatabasePort
from syllabus.data._sqlite_driver import SQLiteDriver
from syllabus.data._csv_driver import CSVDriver


class LoaderResolver():
    def resolve(self, db_path: str, driver: Literal['sqlite', 'csv']) -> DatabasePort:
        match driver:
            case 'sqlite':
                instance = SQLiteDriver(db_path)
            case 'csv':
                instance = CSVDriver(db_path)
            case _:
                raise NotImplementedError(f"Driver {driver} is not implemented")
        
        instance.connect()
        return instance