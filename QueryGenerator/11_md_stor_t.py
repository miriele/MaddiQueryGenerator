import pandas as pd
import numpy as np

##########
# read data
##########

# data 출처
# : 공정거래위원회 가맹사업거래 (https://franchise.ftc.go.kr/index.do)
# : > 가맹희망 플러스 > 정보공개서 비교정보 (https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do)
# : >> 비교항목 - 브랜드별 / 가맹점 현황 정보
# : >> 업종 - 외식 / 커피

data = pd.read_csv("./11_매장구분.txt", sep="\t", header="infer", thousands=",", 
                    usecols=["브랜드", "가맹점수"],
                    dtype={"브랜드"   : object,
                           "가맹점수" : np.int16}
                  )

# data.columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

# print(data)
print(f"read_csv >> data.shape : {data.shape}")
# print(data.dtypes)


##########
## data preprocessing
##########
numFran = 0

# data = data[data["가맹점수"] != 0]
data = data[data["가맹점수"] >= numFran].sort_values("가맹점수", ascending=False)
# print(f"data[data['가맹점수'] >= {numFran} >> data.shape : {data.shape}")

data = pd.DataFrame(data["브랜드"], columns=["브랜드"])
# print(f'pd.DataFrame(data["브랜드"], columns=["브랜드"]) : {data.shape}')

## 브랜드명 변경 (영문, 특수문자 제거)
import re

pattern = r'\([^)]*\)'

for index, row in data.iterrows() :
    row[0] = re.sub(pattern=pattern, repl='', string=row[0]).strip()

## 특수 브랜드명 수정
data[data["브랜드"]=="할리스/할리스커피"] = "할리스"
data[data["브랜드"]=="탐앤탐스커피"] = "탐앤탐스"
data[data["브랜드"]=="꿀스커피GGUL'S COFFEE"] = "꿀스커피"
data[data["브랜드"]=="포트캔커피 PORT CAN COFFEE"] = "포트캔커피"
data[data["브랜드"]=="cafe65℃"] = "cafe65"
data[data["브랜드"]=="카페안시,스튜디오안시"] = "카페안시"
data[data["브랜드"]=="올디스커피 ALL THIS COFFEE"] = "올디스커피"
data[data["브랜드"]=="샐러리아 SALARIA"] = "샐러리아"

## 중복 제거
data.drop_duplicates(subset=None, keep='first', inplace=True, ignore_index=False)
# print(f'data.drop_duplicates >> data.shape : {data.shape}')

## 개인 추가
new_row = pd.DataFrame({"브랜드" : "개인"}, index=[0])
# print(f'new_row.shape : {new_row.shape}')

data = pd.concat([new_row, data.loc[:]])
# print(f'pd.concat([new_row, data.loc[:]]) >> data.shape : {data.shape}')

## index 변경
data.index = np.arange(0, len(data))
# data.index = np.arange(1, len(data)+1)    # index 번호를 1부터 증가~
print(data)


##########
## save data to csv
##########
data.to_csv("./11_md_stor_t.csv", sep="\t", index=True, header=False,
            columns=["브랜드"])


##########
# make query
##########
len_max = 0

for index, row in data.iterrows() :
    l = len(row[0])
    
    if l > len_max :
        len_max = l
        
print(f"len(data.index) : {len(data.index)}")
print(f"max length : {len_max} -> need to set {len_max * 3} bytes in DB")
