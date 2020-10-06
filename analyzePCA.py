# https://archive.ics.uci.edu/ml/index.php
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('data.csv', header = 0)
df = df.drop(['id'], axis=1)
#print(df.head())
#print('Description =')
#print(df.describe())

df['catNb'] = pd.factorize(df['diagnosis'].values)[0]

# PCA plot
x = df.iloc[:,1:31].values      # x is now an Numpy array
covMat = np.cov(x.T)            # covMat is (4,4)
eigenValues, eigenVectors = np.linalg.eig(covMat)
idx = eigenValues.argsort()[::-1]
# Sort the eigenvalues and eigenvectors
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]
#print(idx)
# print('Components using Numpy =')
# print(eigenValues)
# print(eigenVectors)
# Keep the largest 2 eigenvectors for projection
for z in range(0, 28):
    projMat = eigenVectors[:,z:2+z]
    xP = x.dot(projMat)

    #eVNameX = df.columns[idx[z]+1]
    #eVNameY = df.columns[idx[z+1]+1]

    plt.figure()
    projDf = pd.DataFrame(data = xP, columns = ['eig1', 'eig2'])
    projDf['diagnosis'] = df['diagnosis']
    projDf['catNb'] = pd.factorize(projDf['diagnosis'].values)[0]
    # Plot one diagnosis at a time
    colors = ['red', 'blue']
    markers = ['o', 'x']
    for i in range(0, 2):
        subset = projDf[projDf['catNb'] == i]
        plt.scatter(subset['eig1'], subset['eig2'], \
            color = colors[i], marker = markers[i], label = subset['diagnosis'].iloc[0])
    plt.title('PCA Scatter Plot: Eigenvector')
    plt.xlabel(str(z+1) + 'th Eigenvector ')
    plt.ylabel(str(z+2) + 'th Eigenvector: ')
    plt.legend()
    plt.savefig('PCAplots/'+str(z+1) + ' vs. ' + str(z+2) + '.png')