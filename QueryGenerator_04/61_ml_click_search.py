import pandas as pd
import numpy as np
import time
from random import randint
from datetime import datetime
from randomtimestamp.functions import randomtimestamp

##########
# read data
##########
df_drnk = pd.read_csv("./61_re_drnk_grop.csv")
df_dsrt = pd.read_csv("./61_re_dsrt_grop.csv")
df_menu = pd.read_csv("./33_md_menu.csv", sep="\t", header=None)
df_storm = pd.read_csv("./35_md_stor_m.csv",sep="\t",header=None)

cnt_srch   = 50
cnt_click  = 40
cnt_buck   = 30
#cnt_ordr   = 20
#cnt_review = 20

##########
## data preprocessing (search)
##########

## drnk ##
se_drnk = []
for i in range(140) :
    gid   = int(i//3.5)
    start = df_drnk.iloc[gid, 1]
    end   = df_drnk.iloc[gid, 2]
    
    for j in range(cnt_srch) :
        rv  = randint(start, end)
        row = [f'abc{i+1:03}', 1100000000, df_menu.iloc[rv, 3], randomtimestamp(2022)]
        se_drnk.append(row)

df_se_drnk = pd.DataFrame(se_drnk)
# print(df_se_drnk)

## dsrt ##
se_dsrt = []
for i in range(140) :
    gid   = int(i//2.55)
    start = df_dsrt.iloc[gid, 1]
    end   = df_dsrt.iloc[gid, 2]
    
    for j in range(cnt_srch) :
        rv    = randint(start, end)
        row = [f'abc{i+1:03}', 1100000000, df_menu.iloc[rv, 3], randomtimestamp(2022)]
        se_dsrt.append(row)

df_se_dsrt = pd.DataFrame(se_dsrt)
# print(df_se_dsrt)


##########
## data preprocessing (click)
##########

## drnk ##
cl_drnk = []
for i in range(140):
    gid   = int(i//3.5)
    start = df_drnk.iloc[gid, 3]
    end   = df_drnk.iloc[gid, 4]
    
    for j in range(cnt_click):
            rv = randint(start,end)
            row = [df_storm.index[df_storm[1]==df_menu.iloc[rv,0]][0],f'abc{i+1:03}',randomtimestamp(2022)]
            cl_drnk.append(row)
df_cl_drnk = pd.DataFrame(cl_drnk)

## dsrt ##
cl_dsrt = []
for i in range(140):
    gid   = int(i//2.55)
    start = df_dsrt.iloc[gid, 3]
    end   = df_dsrt.iloc[gid, 4]
    
    for j in range(cnt_click):
            rv = randint(start,end)
            row = [df_storm.index[df_storm[1]==df_menu.iloc[rv,0]][0],f'abc{i+1:03}',randomtimestamp(2022)]
            cl_dsrt.append(row)
df_cl_dsrt = pd.DataFrame(cl_dsrt)


##########
##concat drnk,dsrt
##########
srch_data  = pd.concat([df_se_drnk, df_se_dsrt], ignore_index=True)
click_data = pd.concat([df_cl_drnk, df_cl_dsrt], ignore_index=True)

##########
## save data to csv
##########
srch_data.to_csv("./61_md_srch.csv",   sep="\t", index=False, header=False)
click_data.to_csv("./61_md_click.csv", sep="\t", index=False, header=False)


##########
## data preprocessing (order)
##########

# srch_data.to_csv("./61_md_buck.csv",   sep="\t", index=False, header=False)
# srch_data.to_csv("./61_md_ordr.csv",   sep="\t", index=False, header=False)
# srch_data.to_csv("./61_md_review.csv", sep="\t", index=False, header=False)

print("END")



