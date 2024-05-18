import pandas as pd
from functools import reduce
import os
import glob
import json

directory =os.getcwd() + '/scrapy/json/' 

json_files = glob.glob(os.path.join(directory, '*.json'))
json_datas = []

for json_file in json_files:
    with open(json_file, 'r') as f:
        data = json.load(f)
        json_datas.append(data)

len(json_datas)
data_dataframe = []
sum = 0 
for each_data in json_datas:
    data_list = []
    for page in each_data:
        for index in each_data[page]:
            data_list.append(each_data[page][index])
    # print(len(data_list))
    sum += len(data_list)
    data_dataframe.append(pd.DataFrame(data_list))
sum
sum = 0 
for df in data_dataframe:
    sum += len(df)
for i in range(len(data_dataframe)):
    data_dataframe[i]["CATEGORIES"] = data_dataframe[i]['CATEGORIES'].apply(tuple)

merged_df = pd.concat(data_dataframe, ignore_index=True)
merged_df = merged_df.drop_duplicates()
len(merged_df)

merged_df.to_csv("directory"+ "json.csv")