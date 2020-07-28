#!/usr/bin/env python

import pandas as pd
import argparse
import datetime
import sys
from junit_xml import TestSuite, TestCase
from scrap_utils import *

def main():
    parser = argparse.ArgumentParser(description='generate report from finviz daily data')
    parser.add_argument('-input', type=str, help='input file')
    parser.add_argument('-output', type=str, default='daily_report.xml', help='output file')
    args = parser.parse_args()

    if args.input is None:
        filename = '../stock_data/raw_daily_finviz/finviz_' + str(datetime.date.today()) + '.csv'

    filename = '../stock_data/raw_daily_finviz/finviz_2020-07-27.csv'

    # generate report
    df = pd.read_csv(filename)
    df.set_index('Ticker', inplace=True)
    df.drop_duplicates(inplace=True)

    df['DollarVolume'] = df['Volume'] * df['Price']
    df.sort_values(by=['DollarVolume'], ascending=False, inplace=True)


if __name__ == "__main__":
    status = main()
    sys.exit(0 if status is None else status)

