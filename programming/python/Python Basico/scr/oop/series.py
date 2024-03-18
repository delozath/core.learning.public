#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Series():
    def fibonacci(self, n):
        fn = [1]
        if n>1:
            fn.append(1)
            for _ in range(2, n+1):
                f = fn[-1] + fn[-2]
                fn.append(f)
        elif n==1:
            fn.append(1)
        #
        return fn
    #
    def squares(self, n):
        return [i**2 for i in range(1, n+1)]
    #
    def factorial(self, n):
        fn = [1]
        if n>0:
            for c in range(1, n+1):
                f = fn[-1] * c
                fn.append(f)
        elif n==1:
            fn.append(1)
        #
        return fn

class more_series(Series):
    def self.__init__(x)