'''

pattern_recog_func.py

'''

from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn import svm #support vector machine

def interpol_im(im, dim1 = 8, dim2 = 8, plot_new_im = False,\
                cmap = 'binary', axis_off = False):
    
    x = np.arange(im.shape[1])
    y = np.arange(im.shape[0])

    f2d = interp2d(x, y, im)

    x_new = np.linspace(0, im.shape[1], dim1)
    y_new = np.linspace(0, im.shape[0], dim2)

    im_new = f2d(x_new, y_new)
    
    if plot_new_im == True:
        plt.imshow(im_new, cmap = cmap, interpolation = "nearest")
        if axis_off:
            plt.grid('off')
        plt.show()
    
    return np.array([let_new_new.flatten()])
    
def pca_svm_pred(imfile, md_pca, md_clf, dim1 = 45, dim2 = 60): 
    #md_pca = PCA(n_comp),md_clf = classification  
    image = mpimg.imread('letter'+str(let_file)+'.png')
    image_red = image[:,:,0]
    interpol_image = interpol_im(image_red)
    # apply SVM to training data and draw boundaries.
    md_pca, Xproj = pca_X(X) # projects interpolated, flattened image array onto PCA space
    md_clf = svm_train() #calls md_clf
    md_clf.fit(Xproj, y) #applies boundaries
    pred = md_clf.predict(Xproj) #makes a prediction using md_clf
    
def pca_X(X, n_comp = 10):
    md_pca = PCA(n_comp)
    X_proj = md_pca.fit_transform(imfile)
    return md_pca, X_proj
    
def rescale_pixel(X, unseen, ind = 0):
    feature_range = (min(X[ind]), max(X[ind]))
    scale = pre.MinMaxScaler(feature_range)
    scaling_unseen = scaling.fit_transform(X[ind]) 
    return scaling_unseen

def svm_train(gamma = 0.001, C = 100):
    # instantiating an SVM classifier
    md_clf = svm.SVC(gamma, C)
    return md_clf