import pandas as pd
df = pd.read_csv('../../../data/csv/giant_valid_csv.csv')

df_fixed_time = (df['status_changed_at'])

df_fixed = pd.DataFrame(df_fixed_time)
list_time = []
for row in df_fixed['status_changed_at']: 
    row = str(row)
    row = row.replace(" ", 'T')[:-14] 
    mask = '00:00:00+00:00'
    correct_datetime = row+mask
    df_fixed['status_changed_at'][row] = (correct_datetime)
    list_time.append(correct_datetime)

df_time = pd.DataFrame(list_time) #.reset_index()
concatenated = pd.concat([df, df_time], axis=1)
clean_df = concatenated[['status_changed_at', 'id', 'status']]
print(clean_df)
