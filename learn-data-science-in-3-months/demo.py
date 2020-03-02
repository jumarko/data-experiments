# see also https://scikit-learn.org/stable/getting_started.html
# https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

# use specific submodule to build a decision tree
X = [[181,80,44], [177,70,43], [160,60,38], 
     [166, 65,40], [190,90,47], [175,64,39], 
     [177,70,40], [171,75,42], [181,85,43]]

Y = ['male', 'female', 'female', 
     'female', 'male', 'male', 
     'male', 'female', 'male']

def fitAndReport(classifier):
    clf = classifier().fit(X,Y)
    prediction = clf.predict([[190,70,43]])
    print("Using classifier", classifier, ": \n  result=", prediction)

for cl in [DecisionTreeClassifier, RandomForestClassifier, GaussianNB]:
    fitAndReport(cl)
