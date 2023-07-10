import pandas as pd
import numpy as np

##########
# read data
##########
beverage = pd.read_csv("./33_메뉴_음료.txt"  , sep="\t")
dessert  = pd.read_csv("./33_메뉴_디저트.txt", sep="\t")
print(f'beverage.shape  : {beverage.shape}')
print(f'dessert.shape   : {dessert.shape}')
# print(f'beverage.dtypes :\n{beverage.dtypes}')
# print(f'dessert.dtypes  :\n{dessert.dtypes}')

##########
## data preprocessing
##########
## concat data
data = pd.concat([beverage, dessert], ignore_index=True)
# print(f'data.dtypes  :\n{data.dtypes}')
# print(data)

## convert float data type to Nullabel Interger
data['디저트분류'] = data['디저트분류'].astype('Int16')
data['음료분류']   = data['음료분류'].astype('Int16')
print(f'data.dtypes  :\n{data.dtypes}')


##########
## save data to csv
##########
data.to_csv("./33_md_menu.csv", sep="\t", index=True, header=False)


##########
# make query
##########
len_max_menu = 0
len_max_disc = 0
len_max_img  = 0

for index, row in data.iterrows() :
    # print(index, row)
    lm = len(row[2])
    ld = len(row[4])
    # li = len(row[5])

    if lm > len_max_menu :
        len_max_menu = lm

    if ld > len_max_disc :
        len_max_disc = ld

    # if li > len_max_img :
    #     len_max_img = li

print(f"len(data.index) : {len(data.index)}")
print(f"max length for menu field        : {len_max_menu} -> need to set {len_max_menu * 3} bytes in DB")
print(f"max length for discription field : {len_max_disc} -> need to set {len_max_disc * 3} bytes in DB")
# print(f"max length for image field       : {len_max_img } -> need to set {len_max_img  * 3} bytes in DB")
