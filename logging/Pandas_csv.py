import os
import sys
import pandas as pd
#from collections import Counter

df = pd.read_csv('C:\\Users\\srijitha.s\\Downloads\\sql\\name_fruit_count.csv',index_col=False)
print(df)
#print(type(df))
#df.name.unique() #list unique names
#grab row names
row_name=df.name.unique().tolist()
print(row_name)
column_name=['name']+df.fruit.unique().tolist()
print(column_name)
def map_name_and_fruit(dataframe):
    result=dict()
    #iterate over the pandas dataframe
    for id,(name,fruit) in dataframe.iterrows():
        if name not in result:
            result[name]={}
        if fruit not in result[name]:
            result[name][fruit]=0
        result[name][fruit]+=1
    return result
result_dict=map_name_and_fruit(df)
print(result_dict)

#create an empty dataframe to store our final result
result_df=pd.DataFrame(data=0,index=range(len(row_name)),columns=column_name)
result_df.name=row_name
result_df.set_index('name',inplace=True)
print(result_df)

#lets iterate over the result dictionary and fill the empty pandas DataFrame
for key,value in result_dict.items():
    for k1,v1 in value.items():
        #set particular cell with particular value
        result_df.at[key,k1]=v1  #position,column name
result_df.to_csv('C:\\Users\\srijitha.s\\Downloads\\sql\\result_fruit.csv')
print(result_df)
