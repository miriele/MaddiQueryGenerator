import pandas as pd
import numpy as np
import time

##########
# read data
##########
# df columns : 구분, 행정구역코드, 1단계, 2단계, 3단계,
#              격자 X, 격자 Y, 경도(시), 경도(분), 경도(초),
#              위도(시), 위도(분), 위도(초), 경도(초/100), 위도(초/100),
#              위치업데이트
df = pd.read_csv("./51_기상청41_단기예보 조회서비스_오픈API활용가이드_격자_위경도(20210401).csv",
                 encoding="cp949",
                 usecols=["행정구역코드", "1단계", "2단계", "3단계", "격자 X", "격자 Y"],
                 dtype={"행정구역코드" : np.int64,
                        "1단계"        : object,
                        "2단계"        : object,
                        "3단계"        : object,
                        "격자 X"       : np.int16,
                        "격자 Y"       : np.int16}
                )


##########
## data preprocessing
##########
print(f'df        :\n{df}')
print(f'df.shape  : {df.shape}')
print(f'df.dtypes :\n{df.dtypes}')

start = time.time()

# hjd_name = [row[1] + row[2] + row[3] for row in df.values]
# hjd_name = [(row[1] + (str(row[2]) if not pd.isna(row[2]) else '') + (str(row[3]) if not pd.isna(row[3]) else '')) for row in df.values]
# hjd_name = [' '.join(str(elem) for elem in row[1:4] if not pd.isna(elem)) for row in df.values]
# print(hjd_name)

# '행정동명' 컬럼을 만듭니다. NaN 값을 공백으로 대체한 후 필요한 컬럼들을 선택합니다.
df['행정동명'] = df[['1단계', '2단계', '3단계']].fillna('').agg(' '.join, axis=1)

df_hjd = df[['행정구역코드', '행정동명', '격자 X', '격자 Y']]

print(f'실행시간 : {time.time() - start}')


##########
## save data to csv
##########
df_hjd.to_csv("./51_md_hjd.csv", sep="\t", index=False, header=False)

print("END")



