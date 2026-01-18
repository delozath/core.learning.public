from pathlib import Path
import trace

import pandas as pd

from syllabus.ports.dbs import DatabasePort


class CSVDriver(DatabasePort):
    def __init__(self, db_path) -> None:
        self.db_path = Path(db_path)
        self.connection = None

    def connect(self):
        if not self.db_path.exists():
            raise FileNotFoundError(f"CSV file not found at {self.db_path}")
        
        self.connection = pd.read_csv(self.db_path)

    def disconnect(self):
        if self.connection is not None:
            self.connection = None
            print("Closed CSV file")
    
    def query(self, query: str):
        """"
        Se ignora el query y se regresa todo el dataframe porque ya está en formato completo
        Reimplementar si se requiere hacer queries más complejas
        """
        if self.connection is None:
            raise ConnectionError("No CSV file is already closed.")
        
        return self.connection