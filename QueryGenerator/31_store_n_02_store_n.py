import pandas as pd
import numpy as np
import pyproj

##########
# read data
##########
# # import time
# #
# # start = time.time()
#
# # 번호 "157087" 데이터 오류 수정해야 함 "수제족발, 구수"" >> "수제족발, 구수" (큰따옴표가 2개 찍혀서 오류남)
# df = pd.read_csv("./31_fulldata_07_24_04_일반음식점.csv",
#                  encoding="cp949",
#                  usecols=["상세영업상태코드", "소재지전화", "소재지면적", "소재지전체주소", "도로명전체주소",
#                           "사업장명", "좌표정보(x)", "좌표정보(y)"],
#                  dtype={"상세영업상태코드" : np.int16,
#                         "소재지전화"       : object,
#                         "소재지면적"       : np.float32,
#                         "소재지전체주소"   : object,
#                         "도로명전체주소"   : object,
#                         "사업장명"         : object,
#                         "좌표정보(x)"      : np.float32,
#                         "좌표정보(y)"      : np.float32}
#                 )
#
# # end = time.time()
# #
# # print(f"수행시간 : {end-start} sec")
# # print(df)
# # print(df.shape)
# # print(df.dtypes)


##########
## data preprocessing
##########
# df = df[df["상세영업상태코드"] == 1]


##########
## save data to csv
##########
# df.to_csv("./31_fulldata_07_24_04_일반음식점_영업중.csv", index=None)
# del df


##########
# read data
##########
## 11_md_stor_t 에서 읽어온 브랜드 외 브랜드 검색
# : 커피
# : 메가커피
# : 파리크라상, 파리바게뜨
df     = pd.read_csv("./31_fulldata_07_24_04_일반음식점_영업중.csv")
stores = pd.read_csv("./11_md_stor_t.csv", usecols=["개인"], sep="\t")

##########
## data preprocessing
##########
additionalStore = ["메가커피", "파리크라상", "파리바게뜨", "커피"]

lenS = len(stores)
lenA = len(additionalStore)

for i in range(lenA) :
    stores.loc[lenS+i] = additionalStore[i]

print(f'type(stores) : {type(stores)}')
print(f'stores       : {stores}')
print()

import re

seriesStoreName = df["사업장명"]
storesList      = [item for list in stores.values for item in list]
escapedList     = [re.escape(store) for store in storesList]
strMatch        = re.compile('|'.join(escapedList))
print(f'type(seriesStoreName) : {type(seriesStoreName)}\nseriesStoreName :\n{seriesStoreName}')
print(f'type(seriesStoreName.str) : {type(seriesStoreName.str)}\nseriesStoreName.str :\n{seriesStoreName.str}')
print(f'storesList  : {storesList}')
print(f'escapedList : {escapedList}')
print(f'type(strMatch) : {type(strMatch)}\nstrMatch : {strMatch}')
print()

df = df[seriesStoreName.str.contains(strMatch, regex=True, na=False)]

df["소재지면적"].replace(0, np.nan, inplace=True)

## index 변경
df.index = np.arange(0, len(df))

##########
## save data to csv
##########
df.to_csv("./31_fulldata_07_24_04_일반음식점_전처리.csv", sep="\t", index=True, header=False)
print("END")



