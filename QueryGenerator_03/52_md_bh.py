import pandas as pd
import numpy as np
import time

##########
# read data
##########
# df columns : 행정동코드, 시도명, 시군구명, 읍면동명, 법정동코드,
#              동리명, 생성일자, 말소일자

df = pd.read_csv("./52_KIKmix.20230703.csv",
# df = pd.read_csv("./52_KIKmix.20230703(말소코드포함).csv",
                 encoding="cp949",
                 usecols=["행정동코드", "법정동코드"],
                 dtype={"행정동코드" : np.int64,
                        "법정동코드" : np.int64}
                )


##########
## data preprocessing
##########
print(f'df        :\n{df}')
print(f'df.shape  : {df.shape}')
print(f'df.dtypes :\n{df.dtypes}')

# column 순서 변경
df = df[["법정동코드", "행정동코드"]]


##########
## save data to csv
##########
df.to_csv("./52_md_bh.csv", sep="\t", index=False, header=False)

print("END")



