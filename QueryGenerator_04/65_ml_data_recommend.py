import pandas as pd
import numpy as np
import pymysql
from scipy.sparse.linalg._eigen._svds import svds
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics._regression import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# db데이터 -> dataframe
def db_to_df(table_name):
    conn = pymysql.connect(
        host='218.153.113.78',
        user='bit',
        password='bit',
        db='bit',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
    try:
        # 커서 생성
        with conn.cursor() as cursor:
        # 레코드 조회 쿼리 실행
            select_query = 'SELECT * FROM `' + table_name + '`;'
            cursor.execute(select_query)
            result = cursor.fetchall()
        # 조회 결과를 DataFrame으로 변환
        df = pd.DataFrame(result)
        # DataFrame 출력
    finally:
        # 연결 닫기
        conn.close()
    return df

# md_stor_m -> dataframe
def stormdb_to_df():
    conn = pymysql.connect(
        host='218.153.113.78',
        user='bit',
        password='bit',
        db='bit',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
    try:
        with conn.cursor() as cursor:
            select_query = 'SELECT stor_m_id,menu_id FROM md_stor_m;'
            cursor.execute(select_query)
            result = cursor.fetchall()
        df = pd.DataFrame(result)
        # DataFrame 출력
    finally:
        # 연결 닫기
        conn.close()
    return df

# 데이터 전처리

# 전처리에 필요한 db데이터 데이터프레임화
df_srch_data    = db_to_df("md_srch")
df_click_data   = db_to_df("md_click")
df_buck_data    = db_to_df("md_buck")
df_ordr_data    = db_to_df("md_ordr")
df_ordrm_data   = db_to_df("md_ordr_m")
menu_data       = db_to_df("md_menu")
storm_data      = stormdb_to_df()
review_data     = db_to_df("md_review")

# 검색 데이터 전처리

# srch_word -> md_menu/menu_name
map_srchdata = dict(zip(menu_data["menu_name"],menu_data["menu_id"]))
# mapping
df_srch_data["srch_word"] = df_srch_data["srch_word"].map(map_srchdata)

# 특정 컬럼만 저장
df_srch_data = df_srch_data[["user_id","srch_word"]]
df_srch_data.columns=["user","menu_id"]

# 결측치 제거 -> menu_name이 없는경우가 발생
df_srch_data=df_srch_data.dropna(axis=0)

# 검색어 횟수만큼 점수 부과하기
srch_counts = df_srch_data.groupby('menu_id').size()
srchuser_counts = df_srch_data.groupby(['user', 'menu_id']).size().reset_index(name='user_srch_count')
srchuser_total_counts = srchuser_counts.groupby('user')['user_srch_count'].sum()

# 검색 가중치 구하기
def srch_weight(row):
    user = row['user']
    user_count = row['user_srch_count']
    total_count = srchuser_total_counts[user]
    weight = user_count / total_count
    return weight

srchuser_counts['weight'] = srchuser_counts.apply(srch_weight, axis=1)
srchuser_counts = srchuser_counts[["user","menu_id","weight"]]

# 검색 가중치에 따른 score
srchuser_max_weight = srchuser_counts.groupby('user')['weight'].transform('max')
srchuser_min_weight = srchuser_counts.groupby('user')['weight'].transform('min')

def srch_score(row):
    user_weight = row['weight']
    max_weight = row['srchuser_max_weight']
    min_weight = row['srchuser_min_weight']

    if user_weight == max_weight:
        return 5
    elif user_weight == min_weight:
        return 1
    else:
        return round(1 + (user_weight - min_weight) / (max_weight - min_weight) * 4,1)

srchuser_counts['srchuser_max_weight'] = srchuser_max_weight
srchuser_counts['srchuser_min_weight'] = srchuser_min_weight
srchuser_counts['score'] = srchuser_counts.apply(srch_score, axis=1)

# 결과 출력
srchuser_counts = srchuser_counts[["user","menu_id","score"]]

# 클릭데이터
# 클릭한 매장매뉴id -> menu_id로 치환

map_clickdata = dict(zip(storm_data["stor_m_id"],storm_data["menu_id"]))
df_click_data["stor_m_id"] = df_click_data["stor_m_id"].map(map_clickdata)

# 특정 컬럼만 저장
df_click_data = df_click_data[["user_id","stor_m_id"]]

# 컬럼이름 변경
df_click_data.columns=["user","menu_id"]

# 클릭 가중치 구하기
click_counts = df_click_data.groupby('menu_id').size()
clickuser_counts = df_click_data.groupby(['user', 'menu_id']).size().reset_index(name='user_click_count')
clickuser_total_counts = clickuser_counts.groupby('user')['user_click_count'].sum()

def click_weight(row):
    user = row['user']
    user_count = row['user_click_count']
    total_count = clickuser_total_counts[user]
    weight = user_count / total_count
    return weight

clickuser_counts['weight'] = clickuser_counts.apply(click_weight, axis=1)
clickuser_counts = clickuser_counts[["user","menu_id","weight"]]

# 클릭 가중치에 따른 score
clickuser_max_weight = clickuser_counts.groupby('user')['weight'].transform('max')
clickuser_min_weight = clickuser_counts.groupby('user')['weight'].transform('min')

def click_score(row):
    user_weight = row['weight']
    max_weight = row['clickuser_max_weight']
    min_weight = row['clickuser_min_weight']

    if user_weight == max_weight:
        return 5
    elif user_weight == min_weight:
        return 1
    else:
        return round(1 + (user_weight - min_weight) / (max_weight - min_weight) * 4,1)

clickuser_counts['clickuser_max_weight'] = clickuser_max_weight
clickuser_counts['clickuser_min_weight'] = clickuser_min_weight
clickuser_counts['score'] = clickuser_counts.apply(click_score, axis=1)

# 결과 출력
clickuser_counts = clickuser_counts[["user","menu_id","score"]]

# 장바구니 데이터
df_buck_data = df_buck_data[["user_id","stor_m_id"]]

# mapping
map_buckdata = dict(zip(storm_data["stor_m_id"],storm_data["menu_id"]))
df_buck_data["stor_m_id"] = df_buck_data["stor_m_id"].map(map_buckdata)

# 특정 컬럼만 저장
df_buck_data.columns=["user","menu_id"]

# 장바구니 가중치 구하기
buck_counts = df_buck_data.groupby('menu_id').size()
buckuser_counts = df_buck_data.groupby(['user', 'menu_id']).size().reset_index(name='user_buck_count')
buckuser_total_counts = buckuser_counts.groupby('user')['user_buck_count'].sum()

def buck_weight(row):
    user = row['user']
    user_count = row['user_buck_count']
    total_count = buckuser_total_counts[user]
    weight = user_count / total_count
    return weight

buckuser_counts['weight'] = buckuser_counts.apply(buck_weight, axis=1)
buckuser_counts = buckuser_counts[["user","menu_id","weight"]]

# 장바구니 가중치에 따른 score
buckuser_max_weight = buckuser_counts.groupby('user')['weight'].transform('max')
buckuser_min_weight = buckuser_counts.groupby('user')['weight'].transform('min')

def buck_score(row):
    user_weight = row['weight']
    max_weight = row['buckuser_max_weight']
    min_weight = row['buckuser_min_weight']

    if user_weight == max_weight:
        return 5
    elif user_weight == min_weight:
        return 1
    else:
        return round(1 + (user_weight - min_weight) / (max_weight - min_weight) * 4,1)

buckuser_counts['buckuser_max_weight'] = buckuser_max_weight
buckuser_counts['buckuser_min_weight'] = buckuser_min_weight
buckuser_counts['score'] = buckuser_counts.apply(buck_score, axis=1)

buckuser_counts = buckuser_counts[["user","menu_id","score"]]

# md_ordr + md_ordr_m
df_ordr_data = df_ordr_data[["ordr_id","user_id"]]
df_ordrm_data = df_ordrm_data[["ordr_id","stor_m_id"]]
df_ordr_merge_start = pd.merge(df_ordr_data,df_ordrm_data)
df_ordr_merge = df_ordr_merge_start[["user_id","stor_m_id"]]

# mapping
map_ordrdata = dict(zip(storm_data["stor_m_id"],storm_data["menu_id"]))
df_ordr_merge["stor_m_id"] = df_ordr_merge["stor_m_id"].map(map_ordrdata)
df_ordr_merge.columns=["user","menu_id"]

# 주문 가중치 구하기
ordr_counts = df_ordr_merge.groupby('menu_id').size()
ordruser_counts = df_ordr_merge.groupby(['user', 'menu_id']).size().reset_index(name='user_ordr_count')
ordruser_total_counts = ordruser_counts.groupby('user')['user_ordr_count'].sum()

def ordr_weight(row):
    user = row['user']
    user_count = row['user_ordr_count']
    total_count = ordruser_total_counts[user]
    weight = user_count / total_count
    return weight

ordruser_counts['weight'] = ordruser_counts.apply(ordr_weight, axis=1)
ordruser_counts = ordruser_counts[["user","menu_id","weight"]]

# 주문 가중치에 따른 score
ordruser_max_weight = ordruser_counts.groupby('user')['weight'].transform('max')
ordruser_min_weight = ordruser_counts.groupby('user')['weight'].transform('min')

def ordr_score(row):
    user_weight = row['weight']
    max_weight = row['ordruser_max_weight']
    min_weight = row['ordruser_min_weight']

    if user_weight == max_weight:
        return 5
    elif user_weight == min_weight:
        return 1
    else:
        return round(1 + (user_weight - min_weight) / (max_weight - min_weight) * 4,1)

ordruser_counts['ordruser_max_weight'] = ordruser_max_weight
ordruser_counts['ordruser_min_weight'] = ordruser_min_weight
ordruser_counts['score'] = ordruser_counts.apply(ordr_score, axis=1)

ordruser_counts = ordruser_counts[["user","menu_id","score"]]

#리뷰 평점

# md_review + md_ordr + md_ordr_m
review_data = review_data[["ordr_id","rev_star"]]
review_merge = pd.merge(df_ordr_merge_start,review_data)
review_merge = review_merge[["user_id","stor_m_id","rev_star"]]

# mapping
map_revdata = dict(zip(storm_data["stor_m_id"],storm_data["menu_id"]))
review_merge["stor_m_id"] = review_merge["stor_m_id"].map(map_revdata)
review_merge = review_merge[["user_id","stor_m_id","rev_star"]]
review_merge.columns = ["user","menu_id","score"]

# 유저와 메뉴에따른 리뷰 평균 구하기
reviewuser_counts = review_merge.groupby(['user','menu_id'])['score'].mean().reset_index()

# 데이터 타입 변경
clickuser_counts['menu_id'] = clickuser_counts['menu_id'].astype(int)
buckuser_counts['menu_id'] =  buckuser_counts['menu_id'].astype(int)
ordruser_counts['menu_id'] =  ordruser_counts['menu_id'].astype(int)
reviewuser_counts['score'] =  reviewuser_counts['score'].astype(float)

# 전처리결과
# print(srchuser_counts)
# print(clickuser_counts)
# print(buckuser_counts)
# print(ordruser_counts)
# print(reviewuser_counts)

# DataFrame concat
rating_df = [srchuser_counts,clickuser_counts,buckuser_counts,ordruser_counts,reviewuser_counts]
mrating_df = pd.concat(rating_df)
result_rating = mrating_df.groupby(['user','menu_id'],as_index=False)['score'].sum()
result_rating['score'] = result_rating['score'] / 5.0
result_rating['score'] = result_rating['score'].round(1)

# 최근접 이웃 협업필터링 - 아이템 기반
result_rating = result_rating.pivot_table('score',index='user',columns = "menu_id").fillna(0)

# 유사도 계산을 위해 행과 열을 교환
result_rating_T = result_rating.transpose()

# 아이템-유저 매트릭스로부터 코사인 유사도 구하기
item_sim = cosine_similarity(result_rating_T, result_rating_T)
# cosine_similarity()로 반환된 넘파이 행렬에 menu_id을 매핑해 DataFrame으로 변환
item_sim_df = pd.DataFrame(data=item_sim, index=result_rating.columns,columns=result_rating.columns)

# 코사인 유사도 시각화

# 개인의 평점이 반영된 추천시스템을 구현
def predict_rating(ratings_arr, item_sim_arr):
    ratings_pred = ratings_arr.dot(item_sim_arr) / np.array([np.abs(item_sim_arr).sum(axis=1)])
    return ratings_pred

# 개인화된 예측 평점 구하기
# 평점 value와 유사도 value만 뽑아서 대입
ratings_pred = predict_rating(result_rating.values, item_sim_df.values)
ratings_pred_matrix = pd.DataFrame(data=ratings_pred, index=result_rating.index,
                                  columns = result_rating.columns)

# 예측한 평점과 실제 평점간의 차이를 MSE로 계산
# 평균제곱오차(Mean Squared Error, MSE)는 오차(error)를 제곱한 값의 평균. 
# 오차란 알고리즘이 예측한 값과 실제 정답과의 차이를 의미
# 즉, MSE 값은 작을수록 알고리즘의 성능이 좋음

def get_mse(pred, actual):
    # 평점이 있는 실제 menu만 추출
    pred = pred[actual.nonzero()].flatten()
    actual = actual[actual.nonzero()].flatten()
    return mean_squared_error(pred, actual)
# print('아이템 기반 모든 최근접 이웃 MSE: ',get_mse(ratings_pred, result_rating.values))
# mse: 0.1898451613643213

# top_n 추천 : 사용자별로 가장 높은 예측 평점을 가진 N개의 아이템을 추천
top_n_items = [np.argsort(item_sim_df.values[:,3])[:-5:-1]]

def predict_rating_topsim(ratings_arr, item_sim_arr, n=20):
    # 사용자-아이템 평점 행렬 크기만큼 0으로 채운 예측 행렬 초기화
    pred = np.zeros(ratings_arr.shape)
    # 사용자-아이템 평점 행렬의 디저트 개수만큼 루프
    for col in range(ratings_arr.shape[1]):
        # 유사도 행렬에서 유사도가 큰 순으로 n개의 데이터 행렬의 인덱스 반환
        top_n_items = [np.argsort(item_sim_arr[:, col])[:-n-1:-1]]
        for row in range(ratings_arr.shape[0]):
            pred[row, col] = item_sim_arr[col,:][top_n_items].dot(
            ratings_arr[row, :][top_n_items].T)
            pred[row, col] /= np.sum(item_sim_arr[col,:][top_n_items])
    return pred

ratings_pred = predict_rating_topsim(result_rating.values, item_sim_df.values, n=10)
# print('아이템 기반 최근접 TOP-N 이웃 MSE: ', 
#       get_mse(ratings_pred, result_rating.values))
#아이템 기반 최근접 TOP-N 이웃 MSE:  0.11152594905236973

ratings_pred_matrix = pd.DataFrame(data=ratings_pred, index=result_rating.index,
                                  columns=result_rating.columns)

# ratings_pred_matrix -> heatmap
# fig = plt.figure(figsize=(8,8))
# fig.set_facecolor('white')
#
# sns.heatmap(ratings_pred_matrix,cmap='Reds')
# plt.xticks(range(0, len(ratings_pred_matrix.columns), 20), ratings_pred_matrix.columns[::20], rotation=45)
# plt.yticks(range(0, len(ratings_pred_matrix.index), 20), ratings_pred_matrix.index[::20])
# plt.show()

# 예측한 점수를 바탕으로 회원별 추천 메뉴아이디
def re_dessert(result_rating,user):
    user_rating = result_rating.loc[user, :] 
    tried = user_rating[user_rating>0].index.tolist()  
    dessert_list = result_rating.columns.tolist()   
    not_tried = [dessert for dessert in dessert_list if dessert not in tried]   
    return not_tried
ratings_pred = predict_rating_topsim(result_rating.values, item_sim_df.values, n=5)
ratings_pred_df = pd.DataFrame(data=ratings_pred, index=result_rating.index, columns=result_rating.columns)

drnk_menu_id = db_to_df("md_menu")
dsrt_menu_id = db_to_df("md_menu")

drnk_menu_id = drnk_menu_id[['menu_id','dsrt_t_id','drnk_t_id']]
dsrt_menu_id = dsrt_menu_id[['menu_id','dsrt_t_id','drnk_t_id']]

drnk_menu_id = drnk_menu_id.loc[(drnk_menu_id.drnk_t_id>-1)]
dsrt_menu_id = dsrt_menu_id.loc[(dsrt_menu_id.dsrt_t_id>-1)]

# print(drnk_menu_id[['menu_id']])
# print(dsrt_menu_id[['menu_id']])

dist_menu_id = drnk_menu_id.max()['menu_id']

user_pred_dataframes = []

def recomm_dessert_by_user(pred_df, user, recom_dessert, top_n):
    recomm_dessert = pred_df.loc[user, recom_dessert].sort_values(ascending=False)[:top_n]
    return recomm_dessert

for user in ratings_pred_df.index:
    recom_dessert = re_dessert(result_rating, user)   
    recommend = recomm_dessert_by_user(ratings_pred_df, user, recom_dessert, top_n=20)
    user_pred = pd.DataFrame(data={'user': user, 'menu_id': recommend.index, '예측평점': recommend.values})
    user_pred_dataframes.append(user_pred)

# 전체 사용자별 추천 데이터프레임 생성
all_user_pred_df = pd.concat(user_pred_dataframes, ignore_index=True)

# 결과 출력
md_recommend = all_user_pred_df[['user','menu_id']]
md_recommend = md_recommend.groupby('user').apply(lambda x: pd.concat([x[x['menu_id'] <= dist_menu_id].head(3), x[x['menu_id'] > dist_menu_id].head(3)]))
md_recommend = pd.DataFrame(md_recommend)
md_recommend.to_csv("./65_md_recommend.csv", sep="\t", index=False, header=False)
