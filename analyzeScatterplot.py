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
    colors = ['red', 'blue']
    markers = ['o', 'x']
    for i in range(0, 2):
        subset = df[df['catNb'] == i]
        plt.scatter(subset[param1], \
            subset[param2], \
            color = colors[i], \
            marker = markers[i], \
            label = subset['diagnosis'].iloc[0])

    plt.title('Scatter Plot of ' + param1.upper() + ' vs. ' + param2.upper())
    plt.xlabel(param1.upper())
    plt.ylabel(param2.upper())
    plt.legend()
    plt.savefig('Scatterplots/' + param1 + ' vs. ' + param2 +'.png')

for z in range(1, 32):
    eVNameX = df.columns[z]
    eVNameY = df.columns[(z%30)+1]
    ScatterplotMaker(eVNameX, eVNameY)


# plt.figure()
# plt.hist(df['radius_mean'])
# plt.title('Histogram for Radius of Cell')
# plt.xlabel('Radius of Cell (Mean)')
# plt.ylabel('Count')
# plt.savefig('HistogramPlot-RadiusMean.png')

# plt.figure()
# plt.hist(df['radius_se'])
# plt.title('Histogram for Radius of Cell')
# plt.xlabel('Radius of Cell (Standard Error)')
# plt.ylabel('Count')
# plt.savefig('HistogramPlot-RadiusSE.png')
# plt.figure()

# plt.hist(df['radius_worst'])
# plt.title('Histogram for Radius of Cell')
# plt.xlabel('Radius of Cell (Largest)')
# plt.ylabel('Count')
# plt.savefig('HistogramPlot-RadiusLargest.png')

# plt.hist(df['smoothness_mean'])
# plt.title('Histogram for Radius of Cell')
# plt.xlabel('Radius of Cell (Largest)')
# plt.ylabel('Count')
# plt.savefig('HistogramPlot-RadiusLargest.png')

