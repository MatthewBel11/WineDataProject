import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Takes a data input and threshold for that type
def create_is_sweet_variable(data, threshold):

    #Checks if it's above threshold and if so sorts it into that type & returns that sorted data
    data['isSweet'] = (data['residual sugar'] > threshold).astype(int)
    return data

def plot_quality_vs_isSweet(data, wine_type):
    #Sets the plot size
    plt.figure(figsize=(10, 6))

    #Just sorts the data into the levels needed e.g 10 has no values therefore not needed
    quality_levels = sorted(data['quality'].unique())
    #0.4 as we are doing two bars per, leaves a 0.2 gap
    bar_width = 0.4

    #Checks if its sweet or dry denoted by 1 or 0 we got from is sweet variable function
    for isSweet_value in [0, 1]:
        subset = data[data['isSweet'] == isSweet_value]

        #Sets up the bars off set
        offset = bar_width / 2 if isSweet_value == 0 else -bar_width / 2
        plt.bar(np.arange(len(quality_levels)) + offset,subset['quality']
                .value_counts().sort_index(),
                bar_width,label=f'isSweet={isSweet_value}',edgecolor='black'
        )
    #Format & label the plot
    plt.title(f'Wine Quality vs. isSweet for {wine_type} Wines')
    plt.xlabel('Quality')
    plt.ylabel('Frequency')
    plt.xticks(np.arange(len(quality_levels)), quality_levels)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=1)
    plt.show()

#Gets the wines data from csv files
redData = pd.read_csv('data/winequality-red.csv', sep=';')
whiteData = pd.read_csv('data/winequality-white.csv', sep=';')
#The values i got earlier from the medians
redT = 2.2
whiteT = 5.2
#Function thast determines if stuff is dry or sweet and saved to variable
redDataHold = create_is_sweet_variable(redData, redT)
whiteDataHold = create_is_sweet_variable(whiteData, whiteT)
#Passed the sweet and dry data and other data
plot_quality_vs_isSweet(redDataHold, 'Red')
plot_quality_vs_isSweet(whiteDataHold, 'White')