# WineDataProject

**Description:** 
Part of my university coursework, in this small project I took a look at the field of Data Science.

## Technologies Used:
- Written in Python

## Libraries Used:
- pandas
- matplotlib
- numpy
- seaborn
- scikit-learn (sklearn)

## Quality Distribution
- **File:** Quality Distribution
- **Findings:** 
    - Created graphs to represent the distribution of wine quality for both red and white wine.
    - Observed clear differences between red and white wine qualities, with white wine generally having higher quality ratings.

## Alcohol Quality
- **File:** Alcohol Quality
- **Findings:** 
    - Plotted the relationship between quality and alcohol content.
    - Discovered a clear connection between higher alcohol levels and higher quality ratings for both red and white wines.

## Sweet Quality
- **File:** Sweet Quality
- **Findings:** 
    - Analyzed the relationship between sweet and dry wines and their quality distribution.
    - Found that white wines are generally sweeter than red wines.
    - Identified no strong positive or negative relationship between sweetness and quality, although there's a weak positive correlation for dry white wines.

## Correlation Matrix
- **File:** Correlation Matrix
- **Findings:** 
    - Utilized heatmap visualization to understand the correlation between different variables and wine quality.
    - Discovered several strong correlations, such as between density and residual sugar in white wines, and between alcohol content and density in both red and white wines.

## Machine Learning
- **File:** Machine Learning
- **Findings:** 
    - Applied logistic regression for binary classification to predict wine quality.
    - Achieved fairly positive results, with mean cross-validation scores suggesting accurate predictions of wine quality.
    - Tested model with varying thresholds and found that lower thresholds resulted in greater accuracy, particularly with a threshold of 4 achieving near-perfect prediction accuracy.
    - Highlighted the importance of variable selection and testing in achieving accurate predictions.
