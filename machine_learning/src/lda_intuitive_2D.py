import pdb

import numpy   as np
import pandas  as pd
import seaborn as sns; sns.set(style="ticks", palette="pastel")

from matplotlib           import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use({  'figure.figsize'    :(12,6),
                 'axes.titlesize'    :20,
                 'axes.titleweight'  :True,
                 'lines.markersize'  :10,
                 'axes.grid'         :True,
                 'axes.labelsize'    :16,
                 'xtick.labelsize'   :14,
                 'xtick.major.width' :True,
                 'ytick.labelsize'   :14,
                 'ytick.major.width' :True, 
                 'lines.linewidth'   :2.5   })

def pseudo_inv (X: np.array, Y: np.array)->np.array:
    """
      Compute the pseudoinverse matrix for regression/classification
        -> pinv = (X^T X)^-1 X^T y
        
      @param X: -> shape = (n_samples,k_features)
      @param Y: -> shape = (n_samples,1)
      
      @return pinv: -> shape = (k_features,1)
    """
    pinv = np.dot( X.T,X )
    pinv = np.linalg.inv(pinv)
    pinv = np.dot( pinv,X.T )
    pinv = np.dot( pinv,Y   )
    
    return pinv

def extend_x(X: np.array)->np.array:
    """
      Appends a colum of ones to the X matrix
        -> X_ex = [X Ones]
      
      @param X: -> shape = (n_samples,k_features)
      
      @return X_ex: -> shape = (n_samples,k_features+1)
    """
    ones = np.ones( X.shape[0] )[:,np.newaxis]
    
    return np.concatenate( (X,ones), axis=-1 ).copy()

def plot_varrows( x,y1,y2,alpha=1,color='black' ):
    for i,j,k in zip( x,y1,y2 ):
        plt.arrow( i,j, 0,k-j,alpha=alpha,color=color )

def motivation( data,experiment ):
    title = experiment.replace(', ','-')
    y     = np.zeros( data.shape[0] )
    
    plt.figure( title )
    sns.scatterplot( x='X', y=y, hue='Y', data=data,
                      palette=['forestgreen','darkblue'],
                      alpha=.8)
    plt.title(title)
    
    plt.figure( title + ' etiquetas' )
    sns.scatterplot( x='X', y='Y', hue='Y', data=data,
                      palette=['forestgreen','darkblue'],
                      alpha=.8)
    plt.title( title +' etiquetas')
    
    plt.show()
    

def planes(data,experiment,lines):
    title    = experiment.replace(', ','-') + u' planos separación'
    nlines   = lines.shape[0]
    min, max = data['X'].min(), data['X'].max()
    min, max = min + 2*min , max + 0.1*max
    
    xline  = np.linspace( min,max,100 )[np.newaxis]
    ylines = np.dot( lines[:,0:1],xline ).T
    ylines = ylines + lines[:,1]
    
    plt.figure( title )
    sns.scatterplot( x='X', y='Y', hue='Y', data=data,
                      palette=['forestgreen','darkblue'],
                      alpha=.8)
    plt.plot( np.tile( xline,(nlines,1) ).T, ylines)
    plt.title(title)
    
    plt.show()

def planes_predict(data,experiment,lines):
    title    = experiment.replace(', ','-') + u' planos predicción'
    
    x = data['X'].values[np.newaxis]
    y = np.dot( lines[:,0:1],x ).T
    y = y + lines[:,1]
    
    plt.figure( title )
    plot_varrows( x.ravel(),
                  data['Y'].values,    
                  y[:,0],
                  alpha=1,color='black' )
    
    sns.scatterplot( x='X', y='Y', hue='Y', data=data,
                      palette=['forestgreen','darkblue'],
                      alpha=.8)
    plt.plot( x.T, y)
    plt.title(title)
    
    plt.show()

def threshold(data,thre=0.0,comparison=0):
    if comparison==0:
        l = data >= thre
    else:
        l = data < thre
    return (-2*l+1).copy()

def empiric_decision(X,Y,lines,thre,signs):
    y = np.dot( X,lines[:,0:1].T )
    y = y + lines[:,1]
    
    L = list(  map( lambda z: threshold(z[0],z[1],z[2]), zip( y.T,thre,signs )  )  )
    L = np.array(L).T
    
    plt.pcolormesh(L==-Y,edgecolors='k', linewidth=.5,cmap='cool')
        
    index = np.arange( L.shape[1] )
    plt.xticks(  index +.5, [ "Modelo-%d"%i for i in index ], fontsize=10  )
    
    ax = plt.gca()
    #ax.xticklabels()
    ax.set_aspect(.05)
    plt.gca().invert_yaxis()
    plt.show()
    print(np.array(Y).T)

def pseudoinverse_train(X,Y,N):
    X_ext = extend_x(X)
    W     = pseudo_inv(X_ext, Y)
    
    return W.copy()

def main( **params ):
    lines = np.array([ [-0.2  , 0.9  ],
                       [-0.1  , 0.3  ],
                       [ 0.0  , 0.3  ],
                       [ 0.1  ,-0.3  ],
                       [ 0.4  ,-0.8  ] ])                   
    data  = pd.read_csv( params['fname_uninormals'] )
    
    motivation    (data,'Un Rasgo, Dos clases')
    planes        (data,'Un Rasgo, Dos clases',lines)
    planes        (data,'Un Rasgo, Dos clases',lines[ [0,-1] ])
    planes_predict( data, 'Un Rasgo, Dos clases', lines[ [0] ])
    planes_predict( data, 'Un Rasgo, Dos clases', lines[ [1] ])
    planes_predict( data, 'Un Rasgo, Dos clases', lines[ [2] ])
    planes_predict( data, 'Un Rasgo, Dos clases', lines[ [3] ])
    planes_predict( data, 'Un Rasgo, Dos clases', lines[ [4] ])
    
    thre, sign = [.5, .1, .3, -0.15, 0], [0,0,0,-1,-1]
    X          = data['X'].values[:,np.newaxis]
    Y          = data['Y'].values[:,np.newaxis]
    
    empiric_decision(X,Y,lines,thre, sign)
    
    N     = 40
    P     = X.shape[0]-N
    index = np.arange( X.shape[0] ); np.random.shuffle(index)
    
    X_Train, Y_Train = X[ index[  :N] ], Y[ index[  :N] ]
    X_Test , Y_Test  = X[ index[-P: ] ], Y[ index[-P: ] ]
    
    W = pseudoinverse_train(X,Y,N)
    empiric_decision( X,Y, 
                        np.concatenate( (lines,W.T) ), 
                        thre + [0]                   ,
                        sign + [0]
                    )
    
    planes_predict( data, 'Un Rasgo, Dos clases', W.T )
    
    ecs = ["$$y(x) = %.1fx %+ .1f$$"%(tuple(i)) for i in lines]
    for e in ecs:
        print(e)
    
    pdb.set_trace()

if __name__ == '__main__':
    PATH             = '/home/omarpr/git/machine_learning/data/'
    fname_uninormals = 'CNIB 2020 TWO UNIV NORMALS.csv'
    fname_binormals  = 'CNIB 2020 TWO BIV NORMALS.csv'
    
    main( fname_uninormals=PATH+fname_uninormals  )
    