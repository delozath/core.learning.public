import os
import yaml

import pandas as pd

import pdb

class Load:
    def __init__(self) -> None:
        self.path   = os.path.dirname(os.path.abspath(__file__)) + '/'
        self.output = ''
        self.get_config()
    #
    def get_config(self, cfg_fname='config'):
        """Abre archivo YAML que contiene el setup del curso
        
        Attributes
        ----------
        cfg_fname: str
            nombre del archivo YAML de setup del curso
        """
        config = {}
        with open(f"{self.path}{cfg_fname}.yml") as cfg_file:
            for read in yaml.safe_load_all(cfg_file):
                key = [*read.keys()][0]
                config[key] = read[key]
        #
        self.config = config
    #
    def load_tables_from_calc(self, path: str, tables: dict):
        """Lee de un archivo XLSX o ODS las tablas contenidas en el dict tables
        
        Attributes:
        -----------
        
        path : str
            Ruta del archivo que será leído
        table : dict
            Diccionario con los nombres de las tablas que serán leídas del 
            archivo de la hoja de cálculo
        
        Returns:
        --------
        
        tables_df : (pd.DataFrame, dict of pd.DataFrame)
            Tablas leídas del archivo de hoja de cálculo
        table_names: list of str
           Nombres de las tablas leídas
        """
        #
        if isinstance(tables, str):
            tables_df = pd.read_excel(path, sheet_name=[tables])
            tables_df = tables_df[tables]
            table_names = tables
        #
        elif isinstance(tables, dict):
            tables_df = pd.read_excel(path, sheet_name=[t for t in tables.values()])
            table_names = -1
        #
        else:
            tables_df = pd.read_excel(path)
            table_names = -1
            RuntimeWarning("No se especificó tabla para abrir, se cargaron  todas")
        #
        return tables_df, table_names