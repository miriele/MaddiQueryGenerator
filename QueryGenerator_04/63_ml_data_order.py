import pandas as pd
from datetime import datetime, timedelta

##########
# read data
##########
df_buck = pd.read_csv("./62_md_buck.csv", sep="\t", header=None)


#########
# data preprocessing (order)
#########

df_buck.columns = ["A", "B", "C", "D", "E", "F"]
df_buck.dropna(subset=["F"], inplace=True)
# print(df_buck)

or_list = []
for name, date1 in zip(df_buck['A'], df_buck['F']) :
    ord_ts = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S' )
    com_ts = ord_ts + timedelta(minutes=10)
    
    item = [name, 0, 0, ord_ts, com_ts]
    or_list.append(item)

ordr_data = pd.DataFrame(or_list)

#########
# save data to csv
#########
ordr_data.to_csv("./63_md_ordr.csv", sep="\t", index=False, header=False)


##########
# read data
##########
df_ordr = pd.read_csv("./63_md_ordr.csv", sep="\t", header=None)

#########
# data preprocessing (ordr_m)
#########
# ordr 인덱스 = 주문id / 장바구니[1] = 매장메뉴아이디/ 장바구니num = 주문수량

ordrm_list=[]

ordr_i = df_ordr.index.values           # 인덱스
s_menu = df_buck['B']                   # 매장메뉴아이디
o_num  = df_buck['C']                   # 주문수량

for oi, sm, on in zip(ordr_i, s_menu, o_num ) :
    item = [oi, sm, on]
    ordrm_list.append(item)

# print(ordrm_list)

odm_data = pd.DataFrame(ordrm_list)

#########
# save data to csv
#########
odm_data.to_csv("./63_md_ordr_m.csv", sep="\t", index=False, header=False)

print("END")
