import random

from sklearn import linear_model
import numpy as np

# Same linear regression model can be applied for both the Primary as well as secondary classes in schools


def generate_data():
    """
    Takes no input and generates some random data
    :return: Random data array in numpy array format for X and y
    """
    date = []
    attendance = []

    for i in range(20):
        for j in range(6):
            date.append([j])
            attendance.append([35 + int(random.random() * 20)])

    arr = np.asarray([date, attendance])

    return arr


def train_data(X, y):
    """
    :param X: numpy array for date(0-5), school_id
    :param y: output for the data provided
    :return: return the learned linear regression model
    """
    regression = linear_model.LinearRegression()

    regression.fit(X, y)
    return regression


def predict(X, y, prediction_data):
    """
    returns the result of the training data after prediction for the Machine learning training model
    :param X: The data to train the model. To be called every time for continuos learning.
    :param y: The output data for the learning model
    :param prediction_data: to be in the same format as X.
    :return: returns a value of y for the required prediction_data value
    """

    reg = train_data(X, y)
    y_val = reg.predict(prediction_data)

    return y_val


if __name__ == '__main__':
    print generate_data()
    print "Training..."
