from pathlib import Path
import trace

import pandas as pd

from syllabus.ports.dbs import DatabasePort


class CSVDriver(DatabasePort):
    def __init__(self, db_path) -> None:
        self.db_path = {k: Path(i) for k, i in db_path.items()}
        self.connection = None

    def connect(self):
        connection = {}
        for name, path in self.db_path.items():
            if not path.exists():
                raise FileNotFoundError(f"CSV file for name {name} not found at {path}")
            connection[name] = pd.read_csv(path)
        self.connection = connection

    def disconnect(self):
        if self.connection is not None:
            self.connection = None
            print("Closed CSV file")
    
    def query(self, query: str):
        """
        Regresa el DataFrame correspondiente al key 'query' del diccionario de conexiones
        """
        if self.connection is None:
            raise ConnectionError("No CSV file is already closed.")
        
        return self.connection[query]