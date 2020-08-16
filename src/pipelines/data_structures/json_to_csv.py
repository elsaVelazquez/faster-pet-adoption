import pandas as pd


if __name__ == "__main__":
    # file_name = '../../../data/json/clean_giant_json.json'
    df = pd.read_json (r'../../../data/json/prepped_for_csv/all_dogs_copied_off_console.json')
    # dirName = ../../../data/json/prepped_for_csv/all_dogs_copied_off_console.json
  
    
    # df = pd.read_json (r'../../../data/json/json_dump_by_animal/animal_id_48549546.JSON')
    # 
    # df = pd.read_json (r'../../../data/json/json_dump/animal_id_48549546.JSON')
    # df = pd.read_json (r'../../../data/json/big_json_v4.json')
    # df = /Users/elsa/Documents/faster-pet-adoption/src/pipelines/EDA/clean_giant_json.json
    df.to_csv (r'../../../data/csv/all_dogs_copied_off_console_json_to_csv.csv', index = None)