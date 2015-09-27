import datetime
import random

import numpy as np

from main import predict


def learn_and_predict(dates, attendance, date_predict):
    date = []
    for i in dates:
        date.append([int(datetime.datetime.strptime(str(i), '%Y-%m-%d').strftime('%u'))])

    Y = []
    for i in attendance:
        Y.append([int(i)])

    X = np.asarray(date)
    y = np.asarray(Y)
    dt = [int(datetime.datetime.strptime(str(date_predict), '%Y-%m-%d').strftime('%u'))]
    pr = np.asarray([dt])

    return predict(X, y, pr)


if __name__ == '__main__':
    print "ASD"
