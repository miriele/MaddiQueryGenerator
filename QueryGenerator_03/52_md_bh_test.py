import PublicDataReader as pdr

dfHB = pdr.code_hdong_bdong()
res  = dfHB.loc[
                  (dfHB['말소일자'] == '')
                & (dfHB['법정동코드'] == '1165010800')
               ]

print(res)