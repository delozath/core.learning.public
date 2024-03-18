#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyperclip

import pdb

def main():
    text = pyperclip.paste()
    text = text.split('\n\n')
    #TODO modificar porque no funciona en todos los caso
    #usar regex
    text = '\n'.join([t.replace('\n', ', ') for t in text])
    pyperclip.copy(text)
    print("Ouput list copied to clipboard")
    pdb.set_trace()

if __name__ == '__main__':
    main() 