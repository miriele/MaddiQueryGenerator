import pandas as pd
import numpy as np
import pyproj

##########
# read data
##########
# df = pd.read_csv("./31_fulldata_07_24_04_일반음식점.csv",
#                  encoding="cp949",
#                  usecols=["상세영업상태코드", "소재지전화", "소재지면적", "소재지전체주소", "도로명전체주소",
#                           "사업장명", "업태구분명", "좌표정보(x)", "좌표정보(y)"] )

import time

start = time.time()

df = pd.read_csv("./31_fulldata_07_24_04_일반음식점.csv",
                 encoding="cp949",
                 usecols=["상세영업상태코드", "소재지전화", "소재지면적", "소재지전체주소", "도로명전체주소",
                          "사업장명", "업태구분명", "좌표정보(x)", "좌표정보(y)"],
                 # dtype={"상세영업상태코드" : np.int16,
                 #        "소재지전화"       : object,
                 #        "소재지면적"       : np.float32,
                 #        "소재지전체주소"   : object,
                 #        "도로명전체주소"   : object,
                 #        "사업장명"         : object,
                 #        "업태구분명"       : object,
                 #        "좌표정보(x)"      : object,
                 #        "좌표정보(y)"      : object}
                 )

end = time.time()

print(f"수행시간 : {end-start} sec")
# print(df)
print(df.shape)
print(df.dtypes)
##########
## data preprocessing
##########
df = df[  (df["상세영업상태코드"] == 1)           \
        & (  df["사업장명"].str.contains("커피")  \
           | df["사업장명"].str.contains("파스쿠찌")  \
           | df["사업장명"].str.contains("파리크라상")  \
           | df["사업장명"].str.contains("파리바게뜨")  \
           | df["사업장명"].str.contains("공차")  \
           | df["사업장명"].str.contains("빽다방")  \
           | df["사업장명"].str.contains("스타벅스")  \
           | df["사업장명"].str.contains("투썸플레이스")  \
           | df["사업장명"].str.contains("이디야")  \
           | df["사업장명"].str.contains("폴바셋")  \
           | df["사업장명"].str.contains("엔제리너스")  \
           | df["사업장명"].str.contains("할리스")  \
           | df["사업장명"].str.contains("더벤티")  \
           | df["사업장명"].str.contains("탐앤탐스")  \
           | df["사업장명"].str.contains("카페베네")  \
           | df["사업장명"].str.contains("드롭탑")  \
           | df["사업장명"].str.contains("더카페")  \
           | df["사업장명"].str.contains("빈스빈스")  \
           | df["사업장명"].str.contains("토프레소")  \
           | df["사업장명"].str.contains("그라찌에")  \
           | df["사업장명"].str.contains("카페보니또")  \
          )   \
       ]

df["소재지면적"].replace(0, np.nan, inplace=True)


##########
## save data to csv
##########
df.to_csv("./31_fulldata_07_24_04_일반음식점_전처리.csv", index=None)




