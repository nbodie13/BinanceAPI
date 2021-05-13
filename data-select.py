import csv

def data-select(symbol, time_interval)
    filename = '%s-%s-data.csv' % (symbol, time_interval)

    csvfile = open(filename, 'w', newline='')