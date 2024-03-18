#!/usr/bin/python3
# -*- coding: utf-8 -*-

import series

class display():
    def __init__(self, x):
        self.x = x
    #
    def show(self, format='list'):
        if format=='list':
            print(self.x)
        #
        else:
            for n, i in enumerate(self.x, 1):
                print(f"s_{n:4} = {i}")
#
def main():
    ss = series.Series()
    fn = ss.fibonacci(8)
    #print(fn)
    disp_serie = display(fn)
    disp_serie.show('serie')

if __name__ == '__main__':
    main()