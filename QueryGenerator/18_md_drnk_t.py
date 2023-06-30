import pandas as pd

##########
# read data
##########
data = pd.read_csv("./18_음료분류.txt", sep="\t", header=None)


##########
## data preprocessing
##########
# print(data)
# print(data.shape)


##########
## save data to csv
##########
data.to_csv("./18_md_drnk_t.csv", sep="\t", index=True, header=False)


##########
# make query
##########
len_max = 0

for index, row in data.iterrows() :
    l = len(row[0])
    
    if l > len_max :
        len_max = l
        
print(f"len(data.index) : {len(data.index)}")
print(f"max length : {len_max} -> need to set {len_max * 3} bytes in DB")
