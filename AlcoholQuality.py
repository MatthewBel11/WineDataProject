import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def discretize_alcohol(data):
    # This essentially gets the average of alcohol aka the mean, and also the standard deviation
    average = data['alcohol'].mean()
    stddev = data['alcohol'].std()

    #The low and upper threshold is the average - standard deviation, average + standard deviation using above vals
    low_threshold = average - stddev
    high_threshold = average + stddev

    # This justputs the data into 3 catergories : low, mid, high. The np.inf is so all values are included aswell and include lowest
    data['alcohol_cat'] = pd.cut(data['alcohol'], bins=[-np.inf, low_threshold, high_threshold, np.inf], labels=['low', 'mid', 'high'], include_lowest=True)

    # Returns the data thats been put into 3 catergories above
    return data

def plot_quality_distribution(data, wine_type):
    data = discretize_alcohol(data) # Just calls function above and gets the thresholds for the data

    # This just styles the plot size, color, levels and width of bar
    plt.figure(figsize=(15, 8))
    colors = {'low': 'blue', 'mid': 'orange', 'high': 'green'}
    quality_levels = range(3, 10)
    bar_width = 0.2 # 0.2 is ideal for this as it allows for 3 bars with a 0.4 gap after each giving us a good graph


    # This loops through getting the index and category for each
    for index, category in enumerate(['low', 'mid', 'high']):

        #Filters the data and makes subset for alcohol category
        subset = data[data['alcohol_cat'] == category]

        #Calculates offset for bars & also counts freq of each qual level
        offset = (index - 1) * bar_width
        quality_counts = subset['quality'].value_counts().sort_index()

        #Finds any levels that are missing and assigns them a value of 0 so they are represented kind of
        missing_levels = set(quality_levels) - set(quality_counts.index)
        for level in missing_levels:
            quality_counts[level] = 0

        quality_counts = quality_counts.sort_index()

        #Sorted into quality level and plots the 3 bars for each quality
        plt.bar(np.arange(len(quality_levels)) + offset, quality_counts, bar_width,
                label=f'{category} alcohol', color=colors[category])

    # Just formats the graph and labels it then shows it
    plt.title('Wine Quality Distribution for' + wine_type +  'based on Alcohol')
    plt.xlabel('Quality')
    plt.ylabel('Frequency')
    plt.xticks(np.arange(len(quality_levels)) + bar_width, quality_levels)
    plt.grid(axis='y', linestyle='--', alpha=1)
    plt.legend()
    plt.show()



#Loads the red wine data and puts in a graph & also does for white wine
redData = pd.read_csv('data/winequality-red.csv', sep=';')
whiteData = pd.read_csv('data/winequality-white.csv', sep=';')
# Plot the quality distribution for red and white wines
plot_quality_distribution(redData, 'Red')
plot_quality_distribution(whiteData, 'White')
