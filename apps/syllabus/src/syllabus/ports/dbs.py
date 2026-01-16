from abc import ABC, abstractmethod

import pandas as pd

class DatabasePort(ABC):
    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def disconnect(self):
        ...
    
    @abstractmethod
    def query(self, query: str) -> pd.DataFrame:
        ...