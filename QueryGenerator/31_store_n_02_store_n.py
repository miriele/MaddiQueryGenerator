import pandas as pd
import numpy as np
import time

##########
# read data
##########
df_n = pd.read_csv("./31_fulldata_07_24_04_일반음식점_전처리.csv", sep="\t")
df_r = pd.read_csv("./32_fulldata_07_24_05_휴게음식점_전처리.csv", sep="\t")


##########
## data preprocessing
##########
## concat data
df = pd.concat([df_n, df_r], ignore_index=True)
print(f'df.shape  : {df.shape}')
# print(f'df.dtypes :\n{df.dtypes}')
# print(df)

## make store DataFrame
stores = []

# df columns : 소재지전화, 소재지면적, 소재지전체주소, 도로명전체주소, 사업장명, 좌표정보(x), 좌표정보(y), 매장구분ID, 매장사진

## read data
md_stor_t_col = ["id", "name", "img"]
md_stor_t = pd.read_csv("./11_md_stor_t_01_pre_modify.csv", sep="\t", names=md_stor_t_col)
md_bjd    = pd.read_csv("./16_md_bjd.csv", sep="\t")
print(f'md_stor_t.shape : {md_stor_t.shape}')
print(f'md_bjd.shape    : {md_bjd.shape}')

# 결측치 제거 ()
# md_stor_t.dropna(subset=["img"], inplace=True)
# print(f'md_stor_t.shape : {md_stor_t.shape}')

start = time.time()

## add rows
for index, row in df.iterrows() :
    # print(index, row)
    # store = []
    
    # 매장ID
    # store.append(index+100) # 매장 index는 100부터 시작하도록

    # 면적 분류
    area = row["소재지면적"]
    areacode = 0
    
    if np.isnan(area) :
        areacode = np.nan
    elif area < 16.5 :
        areacode = 0
    elif area < 33 :
        areacode = 1
    elif area < 49.5 :
        areacode = 2
    elif area < 66 :
        areacode = 3
    elif area < 330 :
        areacode = 3
    else :
        areacode = 4
        # print(f'area : {area},\t type(area) : {type(area)}')

    # 매장 목록에 추가    
    stores.append([row["매장구분ID"], np.nan, row["법정동코드"], areacode, row["매장사진"], row["사업장명"], row["도로명전체주소"], row["좌표정보(x)"], row["좌표정보(y)"], row["소재지전화"], np.nan])
    
    if index%100 == 0 :
        print(index)

    # test code    
    # if (index+1)%500 == 0 :
    #     break

print(f'실행시간 : {time.time() - start}')

# df_s = pd.DataFrame(columns=["매장ID", "매장구분", "회원ID", "법정동코드", "면적분류", "이미지",
#                                "매장명", "매장주소", "위치-위도", "위치-경도", "전화번호", "사업자등록번호"])
# df_s = pd.DataFrame(columns=["매장구분", "회원ID", "법정동코드", "면적분류", "이미지",
#                                "매장명", "매장주소", "위치-위도", "위치-경도", "전화번호", "사업자등록번호"])
# df_s.loc[index] = pd.Series(store, index=stores.columns)

# col_s = ["매장ID", "매장구분", "회원ID", "법정동코드", "면적분류", "이미지",
#          "매장명", "매장주소", "위치-위도", "위치-경도", "전화번호", "사업자등록번호"]
col_s = ["매장구분", "회원ID", "법정동코드", "면적분류", "이미지",
         "매장명", "매장주소", "위치-위도", "위치-경도", "전화번호", "사업자등록번호"]
df_s  = pd.DataFrame(stores, columns=col_s)
print(f'df_s.shape : {df_s.shape}')
print(f'df_s : {df_s}')


##########
## save data to csv
##########
df_s.to_csv("./31_md_stor.csv", sep="\t", index=False, header=False)

print("END")



