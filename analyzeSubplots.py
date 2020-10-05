# https://archive.ics.uci.edu/ml/index.php
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('data.csv', header = 0)
df = df.drop(['id'], axis=1)

df['catNb'] = pd.factorize(df['diagnosis'].values)[0]

def ScatterplotMaker(param1, param2):
    plt.figure()
    fig, ax = plt.subplots(2, 2)
    ax[0,0].hist(df[param1])
    ax[0,0].set_title('Histogram')
    ax[0,0].set_xlabel(param1)
    ax[0,0].set_ylabel('Count')
    ax[0,1].scatter(df[param1], df[param2])
    ax[0,1].set_title('Scatter Plot')
    ax[0,1].set_xlabel(param1)
    ax[0,1].set_ylabel(param2)
    ax[1,0].boxplot(df[param1])
    ax[1,0].set_title('Box and Whisker Plot')
    ax[1,0].set_xlabel('Cells')
    ax[1,0].set_ylabel(param1)
    ax[1,1].plot(df.index.values, df[param1])
    ax[1,1].set_title('Line Plot')
    ax[1,1].set_xlabel('Index')
    ax[1,1].set_ylabel(param1)
    fig.suptitle('Subplots')
    fig.tight_layout()
    plt.savefig('Subplots.png')
    plt.savefig('Subplots/' + param1 + ' and ' + param2 +'.png')

for z in range(1, 31):
    eVNameX = df.columns[z]
    eVNameY = df.columns[(z%30)+1]
    ScatterplotMaker(eVNameX, eVNameY)