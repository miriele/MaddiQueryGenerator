import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 600)

##########
# read data
##########
data_mgc = pd.read_csv("./35_md_stor_m_메가엠지씨커피.txt", sep="\t")      # 2
data_sta = pd.read_csv("./35_md_stor_m_스타벅스.txt", sep="\t")            # 785
data_two = pd.read_csv("./35_md_stor_m_투썸플레이스.txt", sep="\t")        # 3
data_edi = pd.read_csv("./35_md_stor_m_이디야.txt", sep="\t")              # 1
data_bag = pd.read_csv("./35_md_stor_m_빽다방.txt", sep="\t")              # 5
data_etc = pd.read_csv("./35_md_stor_m_기타.txt", sep="\t")                # 기타
print(f'data_mgc.shape  : {data_mgc.shape}')
print(f'data_bag.shape  : {data_bag.shape}')
print(f'data_sta.shape  : {data_sta.shape}')
print(f'data_edi.shape  : {data_edi.shape}')
print(f'data_two.shape  : {data_two.shape}')
# print(f'data_mgc.dtypes :\n{data_mgc.dtypes}')
# print(f'data_bag.dtypes :\n{data_bag.dtypes}')
# print(f'data_sta.dtypes :\n{data_sta.dtypes}')
# print(f'data_edi.dtypes :\n{data_edi.dtypes}')
# print(f'data_two.dtypes :\n{data_two.dtypes}')

##########
## data preprocessing
##########
## make empty dataframe
data = pd.DataFrame()

## 1, 2, 3, 5, 785 제외한 나머지 매장에 메뉴 등록
data_stor = pd.read_csv("./31_md_stor.csv"  , sep="\t", header=None)
print(f'data_stor.shape  : {data_stor.shape}')
# print(f'data_stor :\n{data_stor}')

import time

start = time.time()

# for index, row in data_stor.iterrows() :
#     print(index, row[0])
#     if row[0] == 2 :
#         data_temp = data_mgc.copy()
#         data_temp.insert(0, "stor_id", index)
#         data = pd.concat([data, data_temp], ignore_index=True)
#     elif row[0] == 785 :
#         data_temp = data_sta.copy()
#         data_temp.insert(0, "stor_id", index)
#         data = pd.concat([data, data_temp], ignore_index=True)
#     elif row[0] == 3 :
#         data_temp = data_two.copy()
#         data_temp.insert(0, "stor_id", index)
#         data = pd.concat([data, data_temp], ignore_index=True)
#     elif row[0] == 1 :
#         data_temp = data_edi.copy()
#         data_temp.insert(0, "stor_id", index)
#         data = pd.concat([data, data_temp], ignore_index=True)
#     elif row[0] == 5 :
#         data_temp = data_bag.copy()
#         data_temp.insert(0, "stor_id", index)
#         data = pd.concat([data, data_temp], ignore_index=True)
#     else :
#         data_temp = data_etc.copy()
#         data_temp.insert(0, "stor_id", index)
#         data = pd.concat([data, data_temp], ignore_index=True)

data_list = []

for index, row in data_stor.iterrows():
    print(index, row[0])
    stor_id = index
    stor_t_id = row[0]

    if stor_t_id == 2:
        data_temp = data_mgc.copy()
    elif stor_t_id == 785:
        data_temp = data_sta.copy()
    elif stor_t_id == 3:
        data_temp = data_two.copy()
    elif stor_t_id == 1:
        data_temp = data_edi.copy()
    elif stor_t_id == 5:
        data_temp = data_bag.copy()
    else:
        data_temp = data_etc.copy()

    data_temp.insert(0, "stor_id", stor_id)
    data_list.append(data_temp)

data = pd.concat(data_list, ignore_index=True)

print(f'data.shape  : {data.shape}')

print(f'실행시간 : {time.time() - start}')

##########
## save data to csv
##########
data.to_csv("./35_md_stor_m.csv", sep="\t", index=False, header=False)


##########
# make query
##########
# len_max_menu = 0
# len_max_disc = 0
# len_max_img  = 0
#
# for index, row in data.iterrows() :
#     # print(index, row)
#     lm = len(row[2])
#     ld = len(row[4])
#     # li = len(row[5])
#
#     if lm > len_max_menu :
#         len_max_menu = lm
#
#     if ld > len_max_disc :
#         len_max_disc = ld
#
#     # if li > len_max_img :
#     #     len_max_img = li
#
# print(f"len(data.index) : {len(data.index)}")
# print(f"max length for menu field        : {len_max_menu} -> need to set {len_max_menu * 3} bytes in DB")
# print(f"max length for discription field : {len_max_disc} -> need to set {len_max_disc * 3} bytes in DB")
# # print(f"max length for image field       : {len_max_img } -> need to set {len_max_img  * 3} bytes in DB")

print("END")
