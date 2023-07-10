import pandas as pd
import numpy as np

##########
# read data
##########

data = pd.read_csv("./11_md_stor_t_01_pre_modify.csv", sep="\t", 
                  )

print(f'read_csv >> data.shape  : {data.shape}')
print(f'read_csv >> data.dtypes : {data.dtypes}')
# print(data)


##########
## data preprocessing
##########
for i, v in data.iterrows() :
    print(f'i : {i}')
    print(f'v[0] : {v[0]}')
    print(f'v[1] : {v[1]}')
    print(f'v[2] : {v[2]}')

##########
## save data to csv
##########


##########
# make query
##########

