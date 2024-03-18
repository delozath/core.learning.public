#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import pyperclip

import sys
import yaml
import pdb

import common

class Load_Eval(common.Load):
    SRC_PATH = '/home/omarpr/git/core.cursos/gestion_clases/src/'
    #
    def __init__(self) -> None:
        super().__init__()
        self.calif = {}
        self._get_table_names()
    #
    def _get_table_names(self):
         info = self.config['dbs']['evaluacion']
         path = info['path']
         tab_names = info['tables']
         #
         self.dbs, self.error = self.load_tables_from_calc(path, tab_names)
    #
    def calif_indiv(self):
        indiv_ev = list(self.dbs['ev_ind'].evaluacion.unique())
        indiv_ev = self.dbs['ponderaciones'].query("evaluacion.isin(@indiv_ev)")
        #
        calif = self.dbs['ev_ind'].merge(indiv_ev,
                                         left_on=['item', 'evaluacion'],
                                         right_on=['aspecto', 'evaluacion'])\
                                  .drop(columns=['aspecto', 'no'])
        calif = calif.assign(w_calif=calif.calificacion * calif.ponderacion)
        calif = calif.groupby(['nombre', 'evaluacion']).agg({'w_calif': 'sum'})\
                     .rename(columns={'w_calif': 'calificacion'})\
                     .reset_index()
        #
        self.calif['indiv'] = calif
    #
    def calif_group(self):
        """
        self.dbs['ev_group'].drop(columns='notas')
        self.dbs['estudiantes'][['nombre', 'equipo']]
        self.dbs['ponderaciones']
        """
        calif = self.dbs['ev_group'].drop(columns='notas')\
                                    .merge(self.dbs['ponderaciones'],
                                           left_on=['evaluacion', 'aspecto'],
                                           right_on=['evaluacion', 'aspecto'])\
                                    .fillna(0)
        #
        calif = calif.assign(w_calif=calif.calificacion * calif.ponderacion)
        calif = calif.groupby(['equipo', 'evaluacion'])\
                     .agg({'w_calif': 'sum'})\
                     .reset_index()
        #
        calif = self.dbs['estudiantes'][['nombre', 'equipo']]\
                    .merge(calif,
                        left_on='equipo',
                        right_on='equipo')\
                    .rename(columns={'w_calif': 'calificacion'})\
                    .reset_index(drop=True)\
                    .drop(columns='equipo')
        #
        self.calif['group'] = calif
    #
    def get_calificaciones(self):
        self.calif_indiv()
        self.calif_group()
        #
        calif = pd.concat(self.calif.values())
        calif = calif.pivot_table(index='nombre', 
                                  columns='evaluacion', 
                                  values='calificacion',
                                  fill_value=0)\
                     .reset_index()
        #
        tot_calif = calif[self.dbs['pond_totales']\
                        .evaluacion.to_list()]\
                        .values @\
                     self.dbs['pond_totales']\
                        .ponderacion\
                        .values
        #
        calif = calif.assign(calif_total=tot_calif)
        nota = pd.cut(calif.calif_total,
                                     self.dbs['nota'].limites.to_list(),
                                     labels=self.dbs['nota'].nota.to_list()[1:],
                                     right=False)\
                                .replace('NA_', 'NA')
        self.calif['total'] = calif.assign(nota=nota)
        pyperclip.copy(self.calif['total'].to_csv(index=False))
        print("\n\n\ncalificaciones en portapapeles")
        pdb.set_trace()

def main():
    loader = Load_Eval()
    loader.get_calificaciones()
    pdb.set_trace()

if __name__ == '__main__':
    #cd /store/science/git/cursos/gestion_clases/src
    #./evaluate.py E1 10
    main()