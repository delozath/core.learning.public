#!/usr/bin/python3
# -*- coding: utf-8 -*-

from itertools import repeat
import aminoacid as am

def main():
    protein = ''
    with open('protein.txt', 'r') as file:
        for f in file:
            protein += f
    #
    protein = protein.replace('\n', '')
    #
    transcript = transcript_iter(protein)
    #transcript = transcript_map(protein)
    #transcript = transcript_map_v2(protein)
    #
    print(transcript)
#
def transcript_iter(protein):
    transcript = ''
    for i in range(0, len(protein)//3, 3):
        a = am.table[protein[i:i+3]]
        transcript += a
    #
    return transcript
#
def search(i, x, tab):
    return tab[x[i:i+3]]
#
def transcript_map(protein):
    index   = range(0, len(protein)//3, 3)
    mapping = map(search, index, repeat(protein), repeat(am.table))
    #
    return list(mapping)
#
def transcript_map_v2(protein):
    index   = range(0, len(protein)//3, 3)
    mapping = map(search, index, repeat(protein), repeat(am.table))
    #
    transcript = list(mapping)
    #
    return ''.join(transcript)
#
if __name__ == '__main__':
    main()