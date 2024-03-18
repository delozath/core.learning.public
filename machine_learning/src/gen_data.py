import pdb

import numpy   as np
import pandas  as pd
import seaborn as sns; sns.set(style="ticks", palette="pastel")

from matplotlib           import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

def two_bivariate_normals( **params ):
    X1 = np.random.multivariate_normal( params['M1'],params['S1'],params['N1'] )
    X2 = np.random.multivariate_normal( params['M2'],params['S2'],params['N2'] )
    
    Y      = -np.ones( params['N1'] + params['N2'])
    
    Y[ params['N1']: ] = 1
    Y                  = Y[:,np.newaxis]
    
    data = np.concatenate( (X1  ,X2),axis=0 )
    data = np.concatenate( (data, Y),axis=1 )
    
    data = pd.DataFrame(data,columns=['X_1','X_2','Y'])
    return data.copy()


def two_univariate_normals( **params ):
    x = np.random.normal( params['m1'], params['s1'], params['n1'] )
    x = np.concatenate( (x, np.random.normal( params['m2'], 
                                              params['s2'],
                                              params['n2'] )   )    )
    y                  = -np.ones( params['n1']+params['n2'] )
    y[ :params['n1'] ] = 1
    
    data = np.hstack( (x[:,np.newaxis],y[:,np.newaxis]) )
    data = pd.DataFrame( data, columns=['X','Y'] )
    
    return data.copy()

# TODO: Agregar los otros generadores de datos del jupyter notebook


def main(fname, func, **params ):
    data = func( **params )
    D    = data.shape[-1]
    
    plt.figure( figsize=(12,5) )
    if D==3:
        sns.scatterplot( x='X_1', y='X_2', hue='Y', data=data,
                          palette=['b','k'] )
    elif D==2:
        sns.scatterplot( x='X', y='Y', hue='Y', data=data,
                          palette=['b','k'] )
    
    plt.grid(True)
    plt.show()
    data.to_csv(fname,index=False)   
    pdb.set_trace()


def setup(fname,case):
    if case=='two_bivariate_normals':
        M_C1 = np.array([    1.0,  0.0 ])
        S_C1 = np.array([ [  1.0,  0.0 ],
                          [  0.0,  1.0 ] ])
        
        M_C2 = np.array([   -3.0,  2.0 ])
        S_C2 = np.array([ [  2.0, -0.5 ],
                          [ -0.5,  2.0 ] ])
        
        N_C1 = 300
        N_C2 = 300
        
        main( fname+'TWO BIV NORMALS.csv',
              two_bivariate_normals,
                case=case,
                M1=M_C1, S1=S_C1, N1=N_C1,
                M2=M_C2, S2=S_C2, N2=N_C2 )
    
    elif case=='two_univariate_normals':
        m1,s1,n1 = 1, .7  , 35
        m2,s2,n2 = 2.5, .5, 35
        
        main( fname+'TWO UNIV NORMALS.csv',
                two_univariate_normals,
                m1=m1, s1=s1, n1=n1,
                m2=m2, s2=s2, n2=n2  )
        


if __name__ == '__main__':
    PATH   = '/home/omarpr/git/machine_learning/data/'
    prefix = 'CNIB 2020 '
    case   = 'two_bivariate_normals'
    case   = 'two_univariate_normals'
    
    setup( PATH+prefix, case=case )