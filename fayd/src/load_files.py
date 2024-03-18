#!/usr/bin/python3
# -*- codinf: utf-8 -*-

import numpy as np
import pandas as pd

import pdb

class load_files:
    def __init__(self, path, fname) -> None:
        self.path = path
        self.fname = path + fname
        #TODO: regex para extraer extensión
        self.ext = fname[-3:]
        #
        self._selector()
    #
    def _selector(self):
        ext = self.ext.lower()
        match ext:
            case "npz":
                self.load = self.load_npz
            #
            case _ :
                self.load = lambda x=self.ext: print(f"No hay decodificador para la extensión {x}")
    #
    def load_npz(self, **params):
        data = np.load(self.fname, allow_pickle=True, **params)
        files = data.files
        #
        self.record =  dict(zip(files, map(data.get, files)))
        print("\nload from npz file\n")

class display:
    def __init__(self, data) -> None:
        self.data = data

class processing:
    @staticmethod
    def p300rec2ecg(data, path, lim=30):
        """
        Toma un registro de P300 Scenario-Screen y selecciona stim_start el inicio 
        de la estumulación como punto de partida. Toma un segmento del EEG 
        entre lim segundos antes y lim segundos después de stim_start. Lo almacena
        en un archivo CSV
        """
        channels = ['Fz', 'C3', 'Cz', 'C4', 'P3', 'Pz', 'P4', 'Oz']
        SR = 512
        LEN = int(SR*lim)
        stim_start = data['index_stim'][0]
        eeg = data['data'][:, 1:]
        #
        segment = slice(stim_start-LEN, stim_start+LEN)
        pd.DataFrame(eeg[segment], 
                    columns=channels).to_csv(path + 'eeg_pre_post_stim.csv', index=False)
        #
        print("EEG segment saved")

def main():
    path = "/home/omarpr/Dropbox/Brain/data/cursos/senales/"
    fname = "eeg.npz"
    load = load_files(path, fname)
    load.load()
    processing.p300rec2ecg(load.record, path)
    disp = display(load)
    #
    pdb.set_trace()

if __name__=='__main__':
    main()