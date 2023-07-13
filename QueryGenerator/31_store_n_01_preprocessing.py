import pandas as pd
import numpy as np
import time

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 600)

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

# 31_fulldata_07_24_04_일반음식점_영업중.csv 파일 저장 후 검색해서 지워야 함 : 0 진장명촌지구 91B-4L


##########
# read data
##########
df     = pd.read_csv("./31_fulldata_07_24_04_일반음식점_영업중.csv")
stores = pd.read_csv("./11_md_stor_t_01_pre.csv", usecols=["개인"], sep="\t")


##########
## data preprocessing
##########
## 결측치 제거 (소재지전체주소, 도로명전체주소)
df.dropna(subset=["소재지전체주소", "도로명전체주소"], inplace=True)

## 11_md_stor_t 에서 읽어온 브랜드 외 브랜드 검색
# : 커피
additionalStore = ["커피"]

lenS = len(stores)
lenA = len(additionalStore)

for i in range(lenA) :
    stores.loc[lenS+i] = additionalStore[i]

# print(f'type(stores) : {type(stores)}')
# print(f'stores       : {stores}')
# print()

start = time.time()

import re

seriesStoreName = df["사업장명"]
storesList      = [item for store in stores.values for item in store]
escapedList     = [re.escape(store) for store in storesList]
strMatch        = re.compile('|'.join(escapedList))
df              = df[seriesStoreName.str.contains(strMatch, regex=True, na=False)]

# seriesStoreName = df["사업장명"]
# storesList      = [item for store in stores.values for item in store]
# escapedList     = [re.escape(store) for store in storesList]
# pattern         = '|'.join(escapedList)
# matches         = seriesStoreName.str.contains(pattern, regex=True, na=False)
# df = df[matches]

# 병렬 처리를 수행하면서 작은 규모의 작업에 비해 오버헤드가 발생해서 더 느려짐
# from concurrent.futures import ThreadPoolExecutor
#
# seriesStoreName = df["사업장명"]
# storesList      = [item for store in stores.values for item in store]
# escapedList     = [re.escape(store) for store in storesList]
# pattern         = '|'.join(escapedList)
#
# def find_match(row):
#     if isinstance(row, str):
#         return bool(re.search(pattern, row))
#     else:
#         return False
#
# with ThreadPoolExecutor() as executor:
#     matches = executor.map(find_match, seriesStoreName)
#
# df = df[list(matches)]

print(f'실행시간 : {time.time() - start}')

df["소재지면적"].replace(0, np.nan, inplace=True)

## index 변경
df.index = np.arange(0, len(df))

## 좌표계변경 - 중부원점(EPSG:2097) > 위도/경도(WGS84)
from pyproj import Transformer

transformer = Transformer.from_crs("EPSG:2097", "EPSG:4326")
converted   = transformer.transform(df['좌표정보(x)'].values, df['좌표정보(y)'].values)
# transformer = Transformer.from_crs("EPSG:2097", "EPSG:4326")
# coordinates = np.column_stack((df['좌표정보(x)'].values, df['좌표정보(y)'].values))
# converted   = transformer.transform(coordinates[:, 0], coordinates[:, 1])

df['좌표정보(x)'] = converted[0]
df['좌표정보(y)'] = converted[1]

## 문자열 치환
# : 강원도 > 강원특별자치도
# df.replace({"소재지전체주소": {"강원도", "강원특별자치도"}}, inplace=True)
# df["소재지전체주소"] = df["소재지전체주소"].str.replace("강원도", "강원특별자치도")
# df["도로명전체주소"] = df["도로명전체주소"].str.replace("강원도", "강원특별자치도")
df["소재지전체주소"] = df["소재지전체주소"].apply(lambda x: x.replace("강원도", "강원특별자치도"))
df["도로명전체주소"] = df["도로명전체주소"].apply(lambda x: x.replace("강원도", "강원특별자치도"))
# df["소재지전체주소"] = df["소재지전체주소"].str.replace(r"\b강원도\b", "강원특별자치도", regex=True)
# df["도로명전체주소"] = df["도로명전체주소"].str.replace(r"\b강원도\b", "강원특별자치도", regex=True)

# : 메가커피, 메가엠지씨커피, 메가엠지시커피 > 메가MGC커피
# df["사업장명"] = df["사업장명"].str.replace("메가커피", "메가MGC커피")
# df["사업장명"] = df["사업장명"].str.replace("메가엠지씨커피", "메가MGC커피")
# df["사업장명"] = df["사업장명"].str.replace("메가엠지시커피", "메가MGC커피")
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("메가커피", "메가MGC커피"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("메가엠지씨커피", "메가MGC커피"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("메가 엠지씨커피", "메가MGC커피"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("메가엠지씨 커피", "메가MGC커피"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("메가 엠지씨 커피", "메가MGC커피"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("메가엠지씨(MGC)커피", "메가MGC커피"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("메가엠지시커피", "메가MGC커피"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("매머드 익스프레스", "매머드익스프레스"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("커피에 반하다", "커피에반하다"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("이디아커피", "이디야커피"))
df["사업장명"] = df["사업장명"].apply(lambda x: x.replace("블루샥", "Blu Shaak"))

## 매장구분ID, 매장사진 추가
md_stor_t_col = ["id", "name", "img"]
md_stor_t = pd.read_csv("./11_md_stor_t_01_pre_modify.csv", sep="\t", names=md_stor_t_col)
md_stor_p = pd.read_csv("./31_사진_카페_개인.txt", sep="\t")

store_names  = md_stor_t["name"].tolist()
store_images = md_stor_t["img"].tolist()

import random

def get_random_image():
    random_row = random.choice(md_stor_p.index)
    return md_stor_p.loc[random_row, "img"]

df["매장구분ID"] = df["사업장명"].map(lambda x: next((i for i, name in enumerate(store_names) if name in x), 0))
df["매장사진"]   = df.apply(lambda row: store_images[row["매장구분ID"]] if pd.notnull(store_images[row["매장구분ID"]]) else get_random_image(), axis=1)

## 법정동코드 추가
md_bjd    = pd.read_csv("./16_md_bjd.csv", sep="\t", names=["코드", "법정동"])

def find_bjd_code(address):
    addr = address.split(" ")

    if re.search("구$", addr[2]):
        bjd = " ".join(addr[:4])
    elif re.search("^세종특별자치시", addr[0]):
        bjd = " ".join(addr[:2])
    else:
        bjd = " ".join(addr[:3])

    code_list = md_bjd.loc[md_bjd["법정동"] == bjd, "코드"].tolist()
    # return code_list[0] if code_list else 0
    return code_list[0] if code_list else np.nan

start = time.time()

# bjd_code_list = []
#
# for index, row in df.iterrows() :
#     address = row["소재지전체주소"]
#     addr    = address.split(" ")
#     # print(addr)
#     if re.search("구$", addr[2]) :
#         # print(" ".join(addr[:4]))
#         # print(md_bjd[md_bjd["법정동"] == " ".join(addr[:4])]["코드"])
#         bjd_code_list.append(md_bjd[md_bjd["법정동"] == " ".join(addr[:4])]["코드"])
#     elif re.search("^세종특별자치시", addr[0]) :
#         # print(" ".join(addr[:2]))
#         # print(md_bjd[md_bjd["법정동"] == " ".join(addr[:2])]["코드"])
#         bjd_code_list.append(md_bjd[md_bjd["법정동"] == " ".join(addr[:2])]["코드"])
#     else :
#         # print(" ".join(addr[:3]))
#         # print(md_bjd[md_bjd["법정동"] == " ".join(addr[:3])]["코드"])
#         bjd_code_list.append(md_bjd[md_bjd["법정동"] == " ".join(addr[:3])]["코드"])
#     # print("#################################################")
#
# df["법정동코드"] = bjd_code_list

df["법정동코드"] = df["소재지전체주소"].map(find_bjd_code)

print(f'실행시간 : {time.time() - start}')

print(df.shape)


##########
## save data to csv
##########
df.to_csv("./31_fulldata_07_24_04_일반음식점_전처리.csv",
          sep="\t", index=False, header=True,
          columns=["소재지전화", "소재지면적", "소재지전체주소", "도로명전체주소",
                   "사업장명", "좌표정보(x)", "좌표정보(y)", "매장구분ID", "매장사진",
                   "법정동코드"]
          )
print("END")

