import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

def prepare_data(wineData, threshold):
    #Takes wine data and threshold
    #Essentially sorts the data into two categories ( high and low ) high being a 1, low being 0 based on threshold
    wineData['binary_quality'] = (wineData['quality'] >= threshold).astype(int)

    #Sets the x and y variable and returns them
    X = wineData.drop(['quality', 'binary_quality'], axis=1)
    y = wineData['binary_quality']

    return X, y

def train_and_evaluate(X, y):
    #Sets up the logistirc regression model we are using and set iterations to 10000
    model = LogisticRegression(max_iter=10000)

    #5 fold k-cross eval
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

    # prints the cross val scores
    print("Cross-Validation Scores:", cv_scores)
    print("Mean CV Score:", cv_scores.mean())
    print("Standard Deviation of CV Scores:", cv_scores.std())

# Load your red and white wine datasets
redData = pd.read_csv('data/winequality-red.csv', sep=';')
whiteData = pd.read_csv('data/winequality-white.csv', sep=';')

#Setting the quality threshold above 6 = 1, less than 6 = 0
threshold = 4

# Preps data for red & white wine
X_red, y_red = prepare_data(redData, threshold)
X_white, y_white = prepare_data(whiteData, threshold)

#Trains and evaluates model for red & white wine using k-fold cross-val
print("\nResults for Red Wine:")
train_and_evaluate(X_red, y_red)
print("\nResults for White Wine:")
train_and_evaluate(X_white, y_white)


