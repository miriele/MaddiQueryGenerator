import pandas as pd

##########
# read data
##########
data = pd.read_csv("./16_법정동코드.txt", sep="\t")


##########
## data preprocessing
##########
data = data.iloc[:, :2][data["폐지여부"]=="존재"]
# print(data)
# print(data.shape)


##########
## save data to csv
##########
data.to_csv("./16_md_bjd.csv", sep="\t", index=False, header=False)


##########
# make query
##########
len_max = 0

for index, row in data.iterrows() :
    l = len(row[1])
    
    if l > len_max :
        len_max = l
        
print(f"len(data.index) : {len(data.index)}")
print(f"max length : {len_max} -> need to set {len_max * 3} bytes in DB")
