#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import numpy as np

from matplotlib import pyplot as plt

import pdb

def generate_1d_data(N=10,):
    m1, std1 = 0, 1
    m2, std2 = 3, 1
    #
    x1 = np.random.normal(m1, std1, N)
    x2 = np.random.normal(m2, std2, N)
    #
    y1 = np.zeros(N)
    y2 = np.ones(N)
    #
    x = np.concatenate((x1, x2))[:, np.newaxis]
    y = np.concatenate((y1, y2))[:, np.newaxis]
    #
    data = np.concatenate((x, y), axis=1)
    return data

def lin_plot(data, N):
    plt.plot(data[data[:, 1]==0, 0], N*[0], 'go')
    plt.plot(data[data[:, 1]==1, 0], N*[0], 'bo')
    plt.show()

def y_plot(data):
    mask_0 = data[:, 1]==0
    mask_1 = data[:, 1]==1
    plt.plot(data[mask_0, 0], data[mask_0, 1], 'go')
    plt.plot(data[mask_1, 0], data[mask_1, 1], 'bo')
    plt.show()

def extend(X):
    return np.concatenate((X, np.ones((X.shape[0], 1))), axis=1)

def pseudoinversa(x):
    X = x[:, :-1]
    y = x[:, -1]
    #
    X_ext = extend(X)
    W = (np.linalg.inv(X_ext.T @ X_ext) @ X_ext.T) @ y
    return W

def discr_func(score):
    return 1*(score>=0.5)

def visual_metric(y_true, y_est):
    for yt, ye in zip(y_true, y_est):
        print(f"({int(yt)}, {ye})")

def confusion_matrix(y_true, y_est):
    comp = np.concatenate(([y_true], [y_est])).T
    pdb.set_trace()

def validation(model, data):
    X = data[:, :-1]
    y = data[:, -1]
    #
    X_ext = extend(X)
    #
    score = X_ext @ model
    label = discr_func(score)
    visual_metric(y, label)
    confusion_matrix(y, label)
    pdb.set_trace()

def main():
    N = 15
    data_train = generate_1d_data(N)
    W = pseudoinversa(data_train)
    #
    N = 10
    data_test = generate_1d_data(N)
    validation(W, data_test)
    pdb.set_trace()
    lin_plot(data, N)
    y_plot(data)


    pdb.set_trace()

if __name__=='__main__':
    main()