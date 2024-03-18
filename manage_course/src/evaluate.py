#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd

import os
import pdb

import common

class Evaluation(common.Load):
    def __init__(self) -> None:
        super().__init__()
        self.calif = {}
        self._get_tables()
    #
    def evaluate(self):
        weights = self.tables['weight_items'][['item', 'subitem', 'ponderacion']].copy()
        weights['index'] = weights.item.str.cat(weights.subitem.astype(str), sep='.')
        weights = weights.set_index('index')
        #
        table = self.tables['evaluation'].copy()
        table['index'] = table.item.str.cat(table.subitem.astype(str), sep='.')
        table = table.set_index('index').drop(columns=['item', 'subitem'])
        #
        table = table.join(weights)
        #
        table['w_evals'] = table['calificacion'] * table['ponderacion']
        cols = ['Matrícula', 'Nombre','item', 'w_evals']
        #
        path = os.path.dirname(self.config['dbs']['evaluacion']['path'])
        fname = os.path.join(path, 'output.csv')
        #
        pdb.set_trace()
        table[cols].fillna(0).pivot_table(index=['Matrícula', 'Nombre'], columns='item', aggfunc=sum).fillna(0).round(2)
        table[cols].groupby(cols[:-1]).agg('sum').to_csv(fname)
        print(4*"\n", "Lista para evaluación por items almacenada en archivo CSV")
        #
        table.query("item=='e2'")
        pdb.set_trace()
    #
    def gen_table_eval(self, items):
        table = []
        for i in items:
            item, subitem = i.split('.')
            tab = self.tables['students']\
                        .drop(columns=['No.', 
                                       'inscripción', 
                                       'correo electrónico'])\
                        .copy()
            #
            tab['item'] = item
            tab['subitem'] = subitem
            table.append(tab)
        #
        table = pd.concat(table)
        path = os.path.dirname(self.config['dbs']['evaluacion']['path'])
        fname = os.path.join(path, 'output.csv')
        #
        table.to_csv(fname, index=False)
        print(4*"\n", "Lista para evaluación por items almacenada en archivo CSV")
    #
    def _get_tables(self):
         info = self.config['dbs']['evaluacion']
         path = info['path']
         tab_names = info['tables']
         #
         self.tables, self.error = self.load_tables_from_calc(path, tab_names)