import json
import os
import pandas as pd

path_bmtop = os.environ['BMTOP']
sdy_csv_file = "/equity-data/groups/holdings-sdy.csv"

# Read the company name and symbol from a csv file
# and write the data out to json
def sdy_to_json():
    filename = path_bmtop + sdy_csv_file
    df = pd.read_csv(filename, sep=',')

    sseries = df['Ticker']
    svalues = sseries.values
    # convert strings in array to lowercase
    svlc = map(str.lower, svalues)
    symbols = tuple(svlc)

    nseries = df['Name']
    nvalues = nseries.values
    names = tuple(nvalues)
    d = {}
    for s, n in zip(symbols, names):
        d[s] = n
    myjson = json.dumps(d)
    print(myjson)

# Read the company name and symbol from a csv file
# and write it out to some other format
def sdy():
    filename = path_bmtop + sdy_csv_file
    df = pd.read_csv(filename, sep=',')
    tseries = df['Ticker']
    tickers = tseries.values
    nseries = df['Name']
    names = nseries.values
    # convert strings in array to lowercase
    tickers = map(str.lower, tickers)
    tickers = tuple(tickers)
    #names = map(str.lower,names)
    names = tuple(names)
    for i, name in enumerate(tickers):
        print(tickers[i],names[i])

# py sdy.py > sdyn.json
if __name__ == "__main__":
    sdy_to_json()
