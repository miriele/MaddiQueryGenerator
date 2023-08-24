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
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 600)
df = pd.read_csv("./31_fulldata_07_24_04_일반음식점_전처리.csv", sep="\t")

# md_stor_t_col = ["id", "name", "img"]
# md_stor_t = pd.read_csv("./11_md_stor_t_01_pre_modify.csv", sep="\t", names=md_stor_t_col)
#
# store_names = md_stor_t["name"].tolist()
# store_images = md_stor_t["img"].tolist()
#
# df["번호"] = df["사업장명"].map(lambda x: next((i for i, name in enumerate(store_names) if name in x), 0))
# df["사진"] = df["번호"].map(lambda x: store_images[x])


md_bjd    = pd.read_csv("./16_md_bjd.csv", sep="\t", names=["코드", "법정동"])


import pandas as pd
import re

bjd_code_list = df["소재지전체주소"].map(lambda address: md_bjd.loc[md_bjd["법정동"].isin([
    " ".join(address.split(" ")[:4]) if re.search("구$", address.split(" ")[2]) else "",
    " ".join(address.split(" ")[:2]) if re.search("^세종특별자치시", address.split(" ")[0]) else "",
    " ".join(address.split(" ")[:3])
]), "코드"].values[0])

df["법정동코드"] = bjd_code_list

# 결과 출력
print(df[["법정동코드"]])



def find_code(address):
    addr = address.split(" ")
    res_code = 0
    
    if len(addr) > 2 and "구" not in addr[2]:
        # print(f'address : {address}\n" ".join(addr[:3] >> {" ".join(addr[:3])}')
        # res = next((code for code, bjd in zip(md_bjd["코드"], md_bjd["법정동"]) if bjd in " ".join(addr[:3])), 0)
        # for code, bjd in zip(md_bjd["코드"], md_bjd["법정동"]) :
        #     if bjd == " ".join(addr[:3]) :
        #         res_code = code
        #         print(f'res_code : {res_code}')
        # print(res)
        # return res_code
        return next((code for code, bjd in zip(md_bjd["코드"], md_bjd["법정동"]) if bjd == " ".join(addr[:3])), 0)

    elif len(addr) > 3 and "구" in addr[2]:
        # print(f'address : {address}\n" ".join(addr[:4] >> {" ".join(addr[:4])}')
        # res = next((code for code, bjd in zip(md_bjd["코드"], md_bjd["법정동"]) if bjd in " ".join(addr[:4])), 0)
        # for code, bjd in zip(md_bjd["코드"], md_bjd["법정동"]) :
        #     if bjd == " ".join(addr[:4]) :
        #         res_code = code
        #         print(f'res_code : {res_code}')
        # print(res)
        # return res_code
        return next((code for code, bjd in zip(md_bjd["코드"], md_bjd["법정동"]) if bjd == " ".join(addr[:4])), 0)
    else:
        return 0

# df["코드"] = df["소재지전체주소"].apply(find_code)
# print(df["코드"])

# print(df.head())



##########
# make query
##########

