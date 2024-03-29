import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile);
        next(csvFileReader) # skip the header
        for row in csvFileReader:
            # parse the first column as date and convert to int (Unix epoch?)
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
        return

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, len(dates), 1)

    svr_lin = SVR(kernel = 'linear', C=1e3)
    svr_poly = SVR(kernel = 'poly', C=1e3, degree = 2)
    svr_rbf = SVR(kernel = 'rbf', C=1e3, gamma = 0.1)

    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support VEctor Regression')
    plt.legend()
    plt.show()

# TODO: download CSV file - HOW???
get_data('aapl.csv')
predicted_price = predict_price(dates, prices, 29)
print(predicted_price)
