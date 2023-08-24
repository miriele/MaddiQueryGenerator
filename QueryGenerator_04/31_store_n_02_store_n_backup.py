import pandas as pd
import numpy as np

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

# df columns : 소재지전화, 소재지면적, 소재지전체주소, 도로명전체주소, 사업장명, 좌표정보(x), 좌표정보(y)

## read data
md_stor_t_col = ["id", "name", "img"]
md_stor_t = pd.read_csv("./11_md_stor_t_01_pre_modify.csv", sep="\t", names=md_stor_t_col)
md_bjd    = pd.read_csv("./16_md_bjd.csv", sep="\t")
print(f'md_stor_t.shape : {md_stor_t.shape}')
print(f'md_bjd.shape    : {md_bjd.shape}')

# 결측치 제거 ()
md_stor_t.dropna(subset=["img"], inplace=True)
print(f'md_stor_t.shape : {md_stor_t.shape}')

## add rows
for index, row in df.iterrows() :
    # print(index, row)
    store = []
    image = ""
    
    # 매장ID
    # store.append(index+100) # 매장 index는 100부터 시작하도록

    # 매장구분ID
    # print(md_stor_t.dtypes)
    for i, v in md_stor_t.iterrows() :
        # if "커피빈" in row["사업장명"] :
        #     print(f'사업장명 : {row["사업장명"]} \t\tv[1] : {v[1]}')
        if v[1] in row["사업장명"] :
            store.append(i)
            image = v[2]
            break
    else :
        store.append(0)

    # 회원ID : null 로 채움
    store.append(np.nan)

    # 법정동코드
    for i, v in md_bjd.values :
        addr = v.split(" ")
        if (len(addr) > 2 and "구" not in addr[2]) or (len(addr) > 3 and "구" in addr[2]):
            # print(i, v)
            # print(f'row["소재지전체주소"] : {row["소재지전체주소"]}\t\tv:{v}')
            if v in row["소재지전체주소"] :
                # print(f'row["소재지전체주소"] : {row["소재지전체주소"]}\t\tv:{v}')
                store.append(i)
                break
    else :
        # store.append(0)
        continue

    # 면적 분류
    area = row["소재지면적"]
    if area < 3 :
        store.append(0)
    elif area < 30 :
        store.append(1)
    elif area < 70 :
        store.append(2)
    elif area < 300 :
        store.append(3)
    else :
        store.append(4)

    # 이미지
    # 대표 이미지 검색 후 할당
    store.append(image)

    # 매장명
    store.append(row["사업장명"])

    # 매장주소 : 도로명주소
    store.append(row["도로명전체주소"])

    # 위치-위도/경도 : 좌표정보(x), 좌표정보(y)
    store.append(row["좌표정보(x)"])
    store.append(row["좌표정보(y)"])

    # 전화번호
    store.append(row["소재지전화"])

    # 사업자등록번호 : null로 채움
    store.append(np.nan)
    # print(f'store : {store}')

    # 매장 목록에 추가    
    stores.append(store)
    
    if index%100 == 0 :
        print(index)
    
    # test
    # if (index+1)%1000 == 0 :
    #     break
    

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



