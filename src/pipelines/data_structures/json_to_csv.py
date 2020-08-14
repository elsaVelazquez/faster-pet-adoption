import pandas as pd


if __name__ == "__main__":
        
    df = pd.read_json (r'../../../data/json/big_json_v4.json')
    df.to_csv (r'../../../data/csv/aggregated_csv_2.csv', index = None)