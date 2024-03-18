#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#import common
import evaluate as evals

import pdb

def gen_evaluation_tables():
    loader = evals.Evaluation()
    loader.gen_table_eval([f"e1.{i}" for i in range(1, 4)])
#
def get_calificaciones():
    loader = evals.Evaluation()
    loader.evaluate()
#
def main():
    #SRC_PATH = '/home/omarpr/git/core.cursos/gestion_clases/src/'
    #gen_evaluation_tables()
    get_calificaciones()
    pdb.set_trace()

if __name__ == '__main__':
    main()

