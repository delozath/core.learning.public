#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy  as np
import pandas as pd

import os
import re
import yaml

import pyperclip

from itertools import repeat

import pdb

BUSINESSDAYS  = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']

class setup_curso:
    def __init__(self) -> None:
        self.path   = os.path.dirname(os.path.abspath(__file__)) + '/'
        self.output = ''
        self._get_config()
        self._generate_calendar()
        #
        temario = self._load_temario()
        self._temario2latex(temario)
    #
    def _load_temario(self):
        """Lee la base de datos del temario y la agrega a la
        los atributos de la clase
        """
        path   = self.config['dbs']['main']['path']
        tables = self.config['dbs']['main']['tables']['planeacion']
        #
        self.df_temario, _ = self._load_tables_from_calc(path, tables)
        
        exclude = self.config['query']['exclude']['temario']
        df = self.df_temario.query("~relevancia.isin(@exclude)")
        #
        return df
    #
    def _temario2latex(self, df):
        output = ""
        output += "\\\\begin{enumerate}\n"
        alphabet = [chr(a) for a in range(97, 110)]          
        for nm_tema, df_tema in self._decode_topics(df, 'tema'):
            output += f"  \\item {nm_tema}\n"
            output +=  "  \\\\begin{enumerate}\n"
            for nm_subtema, df_subtema in self._decode_topics(df_tema, 'subtema'):
                descr = [f'{a}) {d}' for a, d in zip(alphabet, df_subtema['descripción'].values)]
                descr = '. '.join(descr) + '.'
                output += f"    \\item {nm_subtema}. {descr}\n"
            #
            output += "  \\\\end{enumerate}\n"
        #
        output += "\\\\end{enumerate}\n"
        self.output += output
    #
    def _decode_topics(self, df, col):
        unique = df[col].unique()
        for u in unique:
            yield u, df.query(f"{col}==@u")
    #
    def _generate_calendar(self):
        """Genera un cuadro con sintaxis de Latex de las sesiones
        del trimestre agrupadas por semana y con los tag contenidos
        en calendario --> sesiones del archivo YAML considerando los
        eventos --> feriado y examen
        """
        dates = pd.date_range(self.config['calendario']['inicio'], 
                              self.config['calendario']['fin'],
                              freq='d')
        dates = pd.DataFrame(dates, columns=['fechas'])
        #
        dates = self._traduce_weekdays(dates)
        dates = self._get_sessions(dates)
        pdb.set_trace()
        #
        #aggfunc con x o con S, E
        table = dates.replace({'sesion':{None: 'x'}}).\
                      query("weekdays.isin(@BUSINESSDAYS) & (sesion!='feriado')").\
                      pivot_table(index=['semana', 'month', 'sesion'],
                                  columns='weekdays',
                                  #aggfunc=lambda x, e=exam_dates: 'E' if x.values[0] in e else 'S'
                                  aggfunc='count')
        #
        indexes = table.index.names
        table   = table.reset_index().\
                        query("`('sesion', '')`!='x'").\
                        set_index(indexes).\
                        replace({np.nan: '', 1: 'x'})
        table   = table[[('fechas',     'lunes'),
                         ('fechas',    'martes'),
                         ('fechas', 'miércoles'),
                         ('fechas',    'jueves'),
                         ('fechas',   'viernes')]]
        #
        output = table.style.to_latex(hrules=True) + '\n'*3
        self.output = output.replace("\\end", "\\\\end")\
                            .replace("\\begin","\\\\begin")\
                            .replace("\\\\\n", "\\\\\\\\\n")\
                            .replace("\\toprule", "")\
                            .replace("\\bottomrule", "")
    #
    def _traduce_weekdays(self, df):
        days = df.fechas.\
                  dt.\
                  day_name().\
                  replace(self.config['dbs']['traducción']['días'])
        #
        days.name = 'weekdays'
        #
        months = df.fechas.\
                    dt.\
                    month_name().\
                    replace(self.config['dbs']['traducción']['meses'])
        #
        months.name = 'month'
        #
        semana = df.fechas.dt.isocalendar().week.astype('int') -  self.config['calendario']['uam_offset']
        semana.name = 'semana'
        #
        df = pd.concat((df, days, months, semana), axis=1)
        return df
    #
    def _get_sessions(self, df):
        df['sesion'] = None
        for key, sesion in self.config['calendario']['sesiones'].items():
            df.loc[df.weekdays.isin(sesion), 'sesion'] = key
        #
        df = df.set_index('fechas')
        for key, evt in self.config['calendario']['eventos'].items():
            try:
                df.loc[pd.to_datetime(evt), 'sesion'] = key
            except KeyError as e:
                print(f"\nAlgunas fechas están fuera de rango en el tag {key}\n")
        #
        return df.reset_index()

def copy(text):
    os.system(f"echo '{text}' | xclip -selection clipboard")

def main():
    curso = setup_curso()
    copy(curso.output)
    
    pdb.set_trace()

if __name__ == '__main__':
    main()
