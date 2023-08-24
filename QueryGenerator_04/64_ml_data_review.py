import pandas as pd
from random import randint
from datetime import timedelta, datetime
import pymysql
import re
from dateutil.relativedelta import relativedelta
##########
# read data
##########
df_ordr     = pd.read_csv("./63_md_ordr.csv", sep="\t", header=None)
# df_ordr_m = pd.read_csv("./63_md_ordr_m.csv", sep="\t", header=None)
df_drnk     = pd.read_csv("./61_re_drnk_grop.csv")
df_dsrt     = pd.read_csv("./61_re_dsrt_grop.csv")


# df_ordr.columns   = ["a", "b", "c", "d", "e"]
# df_ordr_m.columns = ["a", "b", "c"] 

##########
# connect to mysql
##########
conn   = pymysql.connect(host='218.153.113.78', user='bit', password='bit', db='bit', charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)

ordr_i = df_ordr.index.values
drnk_mid = []
dsrt_mid = []

for i in ordr_i :
    sql = """select m.menu_id , o.ordr_id, o.user_id, o.ordr_com_ts
                from md_ordr o, md_ordr_m om, md_stor_m sm, md_menu m 
                where o.ordr_id = om.ordr_id
                and   om.stor_m_id = sm.stor_m_id
                and   sm.menu_id = m.menu_id
                and   o.ordr_id = %s order by o.ordr_id ;"""     # 오더 아이디에 해당하는 메뉴 아이디는 가져옴
    cursor.execute(sql, i)
    result = cursor.fetchall()

    for j in result :
        if j['menu_id'] < 121 :
            drnk_mid.append(j)
            
        else :
            dsrt_mid.append(j)

drnk_rev = []
dsrt_rev = []
  
for i in drnk_mid :
    string     = i['user_id']
    num        = int(re.sub(r'[^0-9]', '', string ) )
    mid        = int(num//3.5)
    i['group'] = mid
    
    rev_ts = i['ordr_com_ts'] + timedelta(hours = 1)
    
    for j in df_drnk.iloc[:,0] :
        if i['group'] == j :
            start = df_drnk.iloc[j,9]
            end   = df_drnk.iloc[j,10]
            # print(start)
            if i['menu_id'] >= start and i['menu_id'] <= end :
                rev_star      = randint(4,5)
                i['rev_star'] = rev_star
            else :
                rev_star      = randint(1,3)
                i['rev_star'] = rev_star
        #그룹40
        if i['group'] == 40 :
            rev_star      = randint(1,5)
            i['rev_star'] = rev_star
    
    items = [i['ordr_id'], i['rev_star'], rev_ts, "", ""]
    drnk_rev.append(items)
drnk_r = pd.DataFrame(drnk_rev)

for i in dsrt_mid :
    string     = i['user_id']
    num        = int(re.sub(r'[^0-9]', '', string ) )
    mid        = int(num//2.55)
    i['group'] = mid

    rev_ts = i['ordr_com_ts'] + timedelta(hours = 1)
    # print(rev_ts)
    for j in df_dsrt.iloc[:,0] :
        if i['group'] == j :
            start = df_dsrt.iloc[j,9]
            end   = df_dsrt.iloc[j,10]
            # print(start)
            if i['menu_id'] >= start and i['menu_id'] <= end :
                rev_star      = randint(4,5)
                i['rev_star'] = rev_star
            else :
                rev_star      = randint(1,3)
                i['rev_star'] = rev_star
        #그룹40
        if i['group'] == 40 :
            rev_star      = randint(1,5)
            i['rev_star'] = rev_star

    items = [i['ordr_id'], i['rev_star'], rev_ts, "", ""]
    dsrt_rev.append(items)

dsrt_r = pd.DataFrame(dsrt_rev)
rev_data = pd.concat([drnk_r, dsrt_r], ignore_index=True)    

#########
# save data to csv
#########
rev_data.to_csv("./64_md_review.csv",   sep="\t", index=False, header=False)


print("END")
    

