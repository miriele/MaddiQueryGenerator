import pandas as pd
import numpy as np
import pyproj

##########
# read data
##########
df = pd.read_csv("./32_fulldata_07_24_05_휴게음식점.csv",
                 encoding="cp949",
                 usecols=["상세영업상태코드", "소재지전화", "소재지면적", "소재지전체주소", "도로명전체주소",
                          "사업장명", "업태구분명", "좌표정보(x)", "좌표정보(y)"] )

print(df)
print(df.shape)


##########
## data preprocessing
##########
df = df[  (df["상세영업상태코드"] == 1)              \
        & (                                          \
              (df["업태구분명"] == "커피숍")         \
            | (df["업태구분명"] == "다방")           \
            | (df["사업장명"].str.contains("커피"))  \
          )                                          \
       ]

df["소재지면적"].replace(0, np.nan, inplace=True)


##########
## save data to csv
##########
df.to_csv("./32_fulldata_07_24_05_휴게음식점_전처리.csv", index=None)
print(df)



################### for testing ############################
# df = pd.read_csv("./fulldata_07_24_05_휴게음식점_test.csv",
#                  encoding='utf-8',
#                  usecols=["좌표정보(x)", "좌표정보(y)"],
#                  dtype={"좌표정보(x)":"string",
#                         "좌표정보(y)":"string"})

# df = pd.read_csv("./fulldata_07_24_05_휴게음식점_test.csv",
#                  encoding="utf-8",
#                  usecols=["상세영업상태코드", "소재지전화", "소재지면적", "소재지전체주소", "도로명전체주소",
#                           "사업장명", "업태구분명", "좌표정보(x)", "좌표정보(y)"] )

# df = pd.read_csv("./fulldata_07_24_05_휴게음식점2.csv",
#                  encoding="cp949",
#                  usecols=["상세영업상태코드", "소재지전화", "소재지면적", "소재지전체주소", "도로명전체주소",
#                           "사업장명", "업태구분명", "좌표정보(x)", "좌표정보(y)"])

# print(df)

# df = df[(df["상세영업상태코드"] == 1)]
# df = df[(df["사업장명"].str.contains("커피"))]
# df = df[(df["상세영업상태코드"] == 1) & (df["사업장명"].str.contains("커피"))]

# df["소재지면적"].replace(0, np.nan, inplace=True)
#
# df.to_csv("./전처리_test.csv", index=None)
#
# print(df)
#############################################################