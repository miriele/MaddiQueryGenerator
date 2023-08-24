import pandas as pd
import numpy as np
from random import randint
from datetime import timedelta
from randomtimestamp.functions import randomtimestamp

df_drnk     = pd.read_csv("./61_re_drnk_grop.csv")
df_dsrt     = pd.read_csv("./61_re_dsrt_grop.csv")
df_menu     = pd.read_csv("./33_md_menu.csv", sep="\t", header=None)
df_storm    = pd.read_csv("./35_md_stor_m.csv", sep="\t", header=None)

#buck_drnk
cnt_buck = 30
bu_drnk  = []

for i in range(140):
    gid   = int(i//3.5)
    start = df_drnk.iloc[gid,5]
    end   = df_drnk.iloc[gid,6]
    end2  = df_drnk.iloc[gid,8]
    
    for j in range(cnt_buck):
        rv     = randint(start,end)
        reg_ts = randomtimestamp(2022)
        ord_ts = reg_ts + timedelta(hours=1)
        
        if rv > end2:
            row = [f'abc{i+1:03}',df_storm.index[df_storm[1]==df_menu.iloc[rv,0]][0],np.random.randint(1,4),reg_ts,"",""]
            # print(df_storm.index[df_storm[1]==df_menu.iloc[rv,0]][0])
            bu_drnk.append(row)
        else:
            row = [f'abc{i+1:03}',df_storm.index[df_storm[1]==df_menu.iloc[rv,0]][0],np.random.randint(1,4),reg_ts,"",ord_ts]
            bu_drnk.append(row)
            
df_budrnk = pd.DataFrame(bu_drnk)

#buck_dsrt
bu_dsrt = []

for i in range(140):
    gid   = int(i//2.55)
    start = df_dsrt.iloc[gid,5]
    end   = df_dsrt.iloc[gid,6]
    end2  = df_dsrt.iloc[gid,8]
    
    for j in range(cnt_buck):
        rv     = randint(start,end)
        reg_ts = randomtimestamp(2022)
        ord_ts = reg_ts + timedelta(hours=1)
        
        if rv > end2:
            row = [f'abc{i+1:03}',df_storm.index[df_storm[1]==df_menu.iloc[rv,0]][0],np.random.randint(1,4),reg_ts,"",""]
            bu_dsrt.append(row)
        else:
            row = [f'abc{i+1:03}',df_storm.index[df_storm[1]==df_menu.iloc[rv,0]][0],np.random.randint(1,4),reg_ts,"",ord_ts]
            bu_dsrt.append(row)
            
df_budsrt = pd.DataFrame(bu_dsrt)
buck_data = pd.concat([df_budrnk, df_budsrt], ignore_index=True)

buck_data.to_csv("./62_md_buck.csv", sep="\t", index=False, header=False)

print("END")