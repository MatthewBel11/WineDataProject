import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def plot_correlation_matrix(data, wine_type):
    #Calculates correlation matrix uses Pearson correlation coefficient
    correlation_matrix = data.corr()

    #Plot the heatmap
    plt.figure(figsize=(14, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'Correlation Matrix for {wine_type} Wines')
    plt.show()

#Gets wine daTa
red_wine_data = pd.read_csv('data/winequality-red.csv', sep=';')
white_wine_data = pd.read_csv('data/winequality-white.csv', sep=';')

#Plot matric for red and white wines
plot_correlation_matrix(red_wine_data, 'Red')
plot_correlation_matrix(white_wine_data, 'White')