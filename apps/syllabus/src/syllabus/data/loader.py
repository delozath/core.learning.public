from typing import Literal

from omegaconf import DictConfig

from syllabus.ports.dbs import DatabasePort
from syllabus.data._sqlite_driver import SQLiteDriver

class LoaderResolver():
    def resolve(self, db_path: str, driver: Literal['sqlite']) -> DatabasePort:
        match driver:
            case 'sqlite':
                instance = SQLiteDriver(db_path)
                instance.connect()
            case _:
                raise NotImplementedError(f"Driver {driver} is not implemented")
        return instance