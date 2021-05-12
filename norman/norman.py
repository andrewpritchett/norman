import argparse
import json
import os
import sys

import pandas as pd


class DataInput:

    def __init__(self, data):
        self.df = pd.json_normalize(data, sep='.')
        self.flat = self.df.to_dict(orient='records')[0]


def main():
    parser = argparse.ArgumentParser(description='Let Norman help you with JSON normalization!')
    parser.add_argument("-p", "--path",
                       type=str,
                       help='path to your raw log json input file')
    parser.add_argument("-d", "--data",
                    type=json.loads,
                    help="raw log json data")
    parser.add_argument("-c", "--csv",
                    type=str,
                    help="output path for csv file")

    args = parser.parse_args()
    path = args.path
    data = args.data
    csv = args.csv

    if path:
        if not os.path.exists(path):
            print('The path specified does not exist')
            sys.exit()
        else:
            with open(path, 'r') as f:
                data = json.load(f)

    d = DataInput(data)
    for k, v in d.flat.items():
        print(f'{k} : {str(type(v).__name__)} : {v}')

    if csv:
        with open(csv, 'w') as f:
            f.write('path,type,sample_value\n')
            for k, v in d.flat.items():
                f.write(f'{k},{str(type(v).__name__)},{v}\n')


if __name__ == "__main__":
    main()

