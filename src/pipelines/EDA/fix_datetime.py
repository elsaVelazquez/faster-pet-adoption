import pandas as pd
import numpy as np
df = pd.read_csv('../../../data/csv/giant_valid_csv.csv')


#create the time df
df_dirty = (df[['status_changed_at']])
df_fixed = pd.DataFrame(df_dirty)

list_time = []
for row in df_fixed['status_changed_at']: 
    row = str(row)
    row = row.replace(" ", 'T')[:-14] 
    mask = '00:00:00+00:00'
    correct_datetime = row+mask
    df_fixed['status_changed_at'][row] = (correct_datetime)
    list_time.append(correct_datetime)

df_time = pd.DataFrame(list_time).reset_index()
print(df_time)

#create the status df
df_status_col = df[['status']]
df_status = pd.DataFrame(df_status_col).reset_index()
print(df_status)

#join the 2 dataframes
# ColNames = pd.Index(np.concatenate([df_status.columns, df_time.columns])).drop_duplicates()
# print (ColNames)
# Index(['status', 'status_changed_at'], dtype='object')

# df = (df_first.set_index('index')
#       .combine_first(df_second.set_index('index'))
#       .reset_index()
#       .reindex(columns=ColNames))

result = pd.concat([df_status, df_time], axis=1, sort=False)
result.rename(columns = {0:'status_changed_at'}, inplace = True) 
result.drop(['index'], inplace=True, axis=1)
print(result)