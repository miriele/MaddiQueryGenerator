SET SESSION FOREIGN_KEY_CHECKS=0;

/* Drop Tables */

DROP TABLE IF EXISTS md_m_algy;
DROP TABLE IF EXISTS md_u_algy;
DROP TABLE IF EXISTS md_algy_t;
DROP TABLE IF EXISTS md_favorite;
DROP TABLE IF EXISTS md_buck;
DROP TABLE IF EXISTS md_ordr_m;
DROP TABLE IF EXISTS md_stor_m;
DROP TABLE IF EXISTS md_stor_reg;
DROP TABLE IF EXISTS md_stor;
DROP TABLE IF EXISTS md_area_t;
DROP TABLE IF EXISTS md_bjd;
DROP TABLE IF EXISTS md_comb_m;
DROP TABLE IF EXISTS md_comb_r;
DROP TABLE IF EXISTS md_c_like;
DROP TABLE IF EXISTS md_comb;
DROP TABLE IF EXISTS md_menu;
DROP TABLE IF EXISTS md_u_drnk;
DROP TABLE IF EXISTS md_drnk_t;
DROP TABLE IF EXISTS md_u_dsrt;
DROP TABLE IF EXISTS md_dsrt_t;
DROP TABLE IF EXISTS md_rev_t;
DROP TABLE IF EXISTS md_review;
DROP TABLE IF EXISTS md_ordr;
DROP TABLE IF EXISTS md_u_intr;
DROP TABLE IF EXISTS md_u_tast;
DROP TABLE IF EXISTS md_user;
DROP TABLE IF EXISTS md_gen;
DROP TABLE IF EXISTS md_ice;
DROP TABLE IF EXISTS md_intr_t;
DROP TABLE IF EXISTS md_m_type;
DROP TABLE IF EXISTS md_stor_t;
DROP TABLE IF EXISTS md_tag;
DROP TABLE IF EXISTS md_tag_g;
DROP TABLE IF EXISTS md_tast_t;
DROP TABLE IF EXISTS md_user_g;
DROP TABLE IF EXISTS md_weather;




/* Create Tables */

-- 알러지분류
CREATE TABLE md_algy_t
(
	algy_t_id smallint NOT NULL COMMENT '알러지분류ID',
	algy_t_name varchar(15) NOT NULL COMMENT '알러지분류명',
	PRIMARY KEY (algy_t_id)
) COMMENT = '알러지분류';


-- 매장면적타입
CREATE TABLE md_area_t
(
	area_t_id tinyint NOT NULL COMMENT '면적분류ID',
	area_t_name varchar(10) NOT NULL COMMENT '면적분류명',
	area_t_min smallint NOT NULL COMMENT '면적 min',
	area_t_max smallint NOT NULL COMMENT '면적 max',
	PRIMARY KEY (area_t_id)
) COMMENT = '매장면적타입';


-- 법정동코드
CREATE TABLE md_bjd
(
	bjd_code numeric(10) NOT NULL COMMENT '법정동코드',
	bjd_name varchar(80) NOT NULL COMMENT '법정동명',
	PRIMARY KEY (bjd_code)
) COMMENT = '법정동코드';


-- 장바구니
CREATE TABLE md_buck
(
	buck_id int NOT NULL AUTO_INCREMENT COMMENT '장바구니ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	stor_m_id int NOT NULL COMMENT '매장메뉴ID',
	buck_num tinyint NOT NULL COMMENT '주문수량',
	buck_reg_ts timestamp NOT NULL COMMENT '등록일시',
	buck_del_ts timestamp COMMENT '삭제일시',
	buck_ord_ts timestamp COMMENT '주문일시',
	PRIMARY KEY (buck_id)
) COMMENT = '장바구니';


-- 추천조합
CREATE TABLE md_comb
(
	comb_id int NOT NULL AUTO_INCREMENT COMMENT '추천조합ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	comb_tit varchar(90) NOT NULL COMMENT '제목',
	comb_nop tinyint NOT NULL COMMENT '인원수',
	comb_cont text NOT NULL COMMENT '조합내용',
	comb_img varchar(30) COMMENT '이미지경로',
	comb_reg_ts timestamp NOT NULL COMMENT '작성일시',
	PRIMARY KEY (comb_id)
) COMMENT = '추천조합';


-- 조합메뉴
CREATE TABLE md_comb_m
(
	comb_m_id int NOT NULL AUTO_INCREMENT COMMENT '조합메뉴ID',
	comb_id int NOT NULL COMMENT '추천조합ID',
	menu_id int NOT NULL COMMENT '메뉴ID',
	PRIMARY KEY (comb_m_id)
) COMMENT = '조합메뉴';


-- 추천조합댓글
CREATE TABLE md_comb_r
(
	c_reply_id int NOT NULL AUTO_INCREMENT COMMENT '댓글ID',
	comb_id int NOT NULL COMMENT '추천조합ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	c_reply_cont varchar(300) NOT NULL COMMENT '댓글내용',
	c_reply_ts timestamp NOT NULL COMMENT '댓글작성일',
	PRIMARY KEY (c_reply_id)
) COMMENT = '추천조합댓글';


-- 추천조합_Like
CREATE TABLE md_c_like
(
	like_id int NOT NULL AUTO_INCREMENT COMMENT 'LikeID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	comb_id int NOT NULL COMMENT '추천조합ID',
	like_reg_ts timestamp NOT NULL COMMENT '등록일',
	PRIMARY KEY (like_id)
) COMMENT = '추천조합_Like';


-- 음료분류
CREATE TABLE md_drnk_t
(
	drnk_t_id smallint NOT NULL COMMENT '음료분류ID',
	drnk_t_name varbinary(30) NOT NULL COMMENT '음료분류명',
	PRIMARY KEY (drnk_t_id)
) COMMENT = '음료분류';


-- 디저트분류
CREATE TABLE md_dsrt_t
(
	dsrt_t_id smallint NOT NULL COMMENT '디저트분류ID',
	dsrt_t_name varbinary(20) NOT NULL COMMENT '디저트분류명',
	PRIMARY KEY (dsrt_t_id)
) COMMENT = '디저트분류';


-- 즐겨찾기
CREATE TABLE md_favorite
(
	fav_id int NOT NULL AUTO_INCREMENT COMMENT '즐겨찾기ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	stor_id int NOT NULL COMMENT '매장ID',
	fav_reg_ts timestamp NOT NULL COMMENT '등록일',
	PRIMARY KEY (fav_id)
) COMMENT = '즐겨찾기';


-- 성별
CREATE TABLE md_gen
(
	gen_id tinyint NOT NULL COMMENT '성별ID',
	gen_name varchar(10) NOT NULL COMMENT '성별',
	PRIMARY KEY (gen_id)
) COMMENT = '성별';


-- 아이스분류
CREATE TABLE md_ice
(
	ice_t_id tinyint NOT NULL COMMENT '아이스분류ID',
	ice_t_name varchar(10) NOT NULL COMMENT '아이스타입명',
	PRIMARY KEY (ice_t_id)
) COMMENT = '아이스분류';


-- 관심사분류
CREATE TABLE md_intr_t
(
	intr_t_id tinyint NOT NULL COMMENT '관심사분류ID',
	intr_t_name varchar(21) NOT NULL COMMENT '관심사분류명',
	PRIMARY KEY (intr_t_id)
) COMMENT = '관심사분류';


-- 메뉴
CREATE TABLE md_menu
(
	menu_id int NOT NULL COMMENT '메뉴ID',
	dsrt_t_id smallint COMMENT '디저트분류ID',
	drnk_t_id smallint COMMENT '음료분류ID',
	menu_name varchar(60) NOT NULL COMMENT '메뉴명',
	menu_cal tinyint NOT NULL COMMENT '칼로리',
	menu_info varchar(300) NOT NULL COMMENT '메뉴소개',
	menu_img varchar(30) COMMENT '메뉴이미지',
	PRIMARY KEY (menu_id)
) COMMENT = '메뉴';


-- 메뉴알러지
CREATE TABLE md_m_algy
(
	m_algy_id smallint NOT NULL AUTO_INCREMENT COMMENT '메뉴알러지ID',
	menu_id int NOT NULL COMMENT '메뉴ID',
	algy_t_id smallint NOT NULL COMMENT '알러지분류ID',
	PRIMARY KEY (m_algy_id)
) COMMENT = '메뉴알러지';


-- 메뉴타입 : 1 : 일반
-- 2 : 시그니처
CREATE TABLE md_m_type
(
	m_type_id tinyint NOT NULL COMMENT '메뉴타입ID',
	m_type_n varchar(15) NOT NULL COMMENT 'm_type_n',
	PRIMARY KEY (m_type_id)
) COMMENT = '메뉴타입 : 1 : 일반
2 : 시그니처';


-- 주문
CREATE TABLE md_ordr
(
	ordr_id int NOT NULL AUTO_INCREMENT COMMENT '주문ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	weather_id tinyint NOT NULL COMMENT '날씨분류ID',
	ordr_temp tinyint NOT NULL COMMENT '기온',
	ordr_ord_ts timestamp NOT NULL COMMENT '주문일시',
	ordr_com_ts timestamp COMMENT '완료일시',
	PRIMARY KEY (ordr_id)
) COMMENT = '주문';


-- 주문메뉴
CREATE TABLE md_ordr_m
(
	ordr_m_id int NOT NULL AUTO_INCREMENT COMMENT '주문메뉴ID',
	ordr_id int NOT NULL COMMENT '주문ID',
	stor_m_id int NOT NULL COMMENT '매장메뉴ID',
	ordr_num tinyint NOT NULL COMMENT '주문수량',
	PRIMARY KEY (ordr_m_id)
) COMMENT = '주문메뉴';


-- 리뷰
CREATE TABLE md_review
(
	rev_id int NOT NULL AUTO_INCREMENT COMMENT '리뷰ID',
	ordr_id int NOT NULL COMMENT '주문ID',
	rev_star numeric(2,1) NOT NULL COMMENT '리뷰별점',
	rev_ts timestamp NOT NULL COMMENT '작성일시',
	rev_cont varchar(300) COMMENT '리뷰내용',
	rev_img varchar(30) COMMENT '이미지경로',
	PRIMARY KEY (rev_id)
) COMMENT = '리뷰';


-- 리뷰태그
CREATE TABLE md_rev_t
(
	rev_t_id int NOT NULL AUTO_INCREMENT COMMENT '리뷰태그ID',
	rev_id int NOT NULL COMMENT '리뷰ID',
	tag_id smallint NOT NULL COMMENT '태그ID',
	PRIMARY KEY (rev_t_id)
) COMMENT = '리뷰태그';


-- 매장
CREATE TABLE md_stor
(
	stor_id int NOT NULL AUTO_INCREMENT COMMENT '매장ID',
	stor_t_id int NOT NULL COMMENT '매장구분ID',
	user_id varchar(20) COMMENT '회원ID',
	bjd_code numeric(10) NOT NULL COMMENT '법정동코드',
	area_t_id tinyint NOT NULL COMMENT '면적분류ID',
	stor_img varchar(150) NOT NULL COMMENT '이미지',
	stor_name varchar(50) NOT NULL COMMENT '매장명',
	stor_addr varchar(200) NOT NULL COMMENT '매장주소',
	stor_lati numeric(18,15) COMMENT '위치-위도',
	stor_long numeric(18,15) COMMENT '위치-경도',
	stor_tel varchar(20) COMMENT '전화번호',
	stor_num varchar(20) COMMENT '사업자등록번호',
	PRIMARY KEY (stor_id)
) COMMENT = '매장';


-- 매장메뉴
CREATE TABLE md_stor_m
(
	stor_m_id int NOT NULL COMMENT '매장메뉴ID',
	stor_id int NOT NULL COMMENT '매장ID',
	menu_id int NOT NULL COMMENT '메뉴ID',
	ice_t_id tinyint NOT NULL COMMENT '아이스분류ID',
	m_type_id tinyint NOT NULL COMMENT '메뉴타입ID',
	stor_m_pric smallint NOT NULL COMMENT '가격',
	stor_m_name varchar(60) NOT NULL COMMENT '매장메뉴명',
	stor_m_cal tinyint NOT NULL COMMENT '매장메뉴칼로리',
	stor_m_ifno varchar(600) NOT NULL COMMENT '매장메뉴소개',
	stor_m_img varchar(30) NOT NULL COMMENT '매장메뉴이미지',
	PRIMARY KEY (stor_m_id)
) COMMENT = '매장메뉴';


-- 매장등록신청
CREATE TABLE md_stor_reg
(
	reg_id int NOT NULL AUTO_INCREMENT COMMENT '매장등록신청ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	stor_id int NOT NULL COMMENT '매장ID',
	reg_num varchar(40) NOT NULL COMMENT '사업자등록번호',
	reg_img varchar(50) NOT NULL COMMENT '사업자등록증경로',
	reg_sub_ts timestamp NOT NULL COMMENT '신청일시',
	reg_con_ts timestamp COMMENT '승일일시',
	PRIMARY KEY (reg_id)
) COMMENT = '매장등록신청';


-- 매장구분 : 1 : 개인
-- 2 : 스타벅스
-- 3 : 커피빈
-- 4 : 바나프레소
CREATE TABLE md_stor_t
(
	stor_t_id int NOT NULL COMMENT '매장구분ID',
	stor_t_name varchar(60) NOT NULL COMMENT '구분명',
	PRIMARY KEY (stor_t_id)
) COMMENT = '매장구분 : 1 : 개인
2 : 스타벅스
3 : 커피빈
4 : 바나프레소';


-- 태그
CREATE TABLE md_tag
(
	tag_id smallint NOT NULL COMMENT '태그ID',
	tag_g_id tinyint NOT NULL COMMENT '태그그룹ID',
	tag_name varchar(50) NOT NULL COMMENT '태그명',
	PRIMARY KEY (tag_id)
) COMMENT = '태그';


-- 태그그룹
CREATE TABLE md_tag_g
(
	tag_g_id tinyint NOT NULL COMMENT '태그그룹ID',
	tag_g_name varchar(15) NOT NULL COMMENT '태그그룹명',
	PRIMARY KEY (tag_g_id)
) COMMENT = '태그그룹';


-- 맛분류
CREATE TABLE md_tast_t
(
	tast_t_id tinyint NOT NULL COMMENT '맛분류ID',
	tast_t_name varchar(12) NOT NULL COMMENT '맛분류명',
	PRIMARY KEY (tast_t_id)
) COMMENT = '맛분류';


-- 회원
CREATE TABLE md_user
(
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	user_g_id tinyint NOT NULL COMMENT '회원등급ID',
	gen_id tinyint NOT NULL COMMENT '성별ID',
	user_nick varchar(45) NOT NULL COMMENT '닉네임',
	user_pass varchar(20) NOT NULL COMMENT '비밀번호',
	user_name varchar(30) NOT NULL COMMENT '회원이름',
	user_bir date NOT NULL COMMENT '생년월일',
	user_img varchar(50) NOT NULL COMMENT '이미지',
	user_reg_ts timestamp NOT NULL COMMENT '가입일시',
	user_ext_ts timestamp COMMENT '탈퇴일시',
	PRIMARY KEY (user_id),
	UNIQUE (user_nick)
) COMMENT = '회원';


-- 회원등급
CREATE TABLE md_user_g
(
	user_g_id tinyint NOT NULL COMMENT '회원등급ID',
	user_g_name varchar(15) NOT NULL COMMENT '등급명',
	PRIMARY KEY (user_g_id)
) COMMENT = '회원등급';


-- 사용자알러지
CREATE TABLE md_u_algy
(
	u_algy_id int NOT NULL AUTO_INCREMENT COMMENT '사용자알러지ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	algy_t_id smallint NOT NULL COMMENT '알러지분류ID',
	PRIMARY KEY (u_algy_id)
) COMMENT = '사용자알러지';


-- 사용자음료
CREATE TABLE md_u_drnk
(
	u_drnk_id int NOT NULL AUTO_INCREMENT COMMENT '사용자음료ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	drnk_t_id smallint NOT NULL COMMENT '음료분류ID',
	PRIMARY KEY (u_drnk_id)
) COMMENT = '사용자음료';


-- 사용자디저트
CREATE TABLE md_u_dsrt
(
	u_dsrt_id int NOT NULL AUTO_INCREMENT COMMENT '사용자디저트ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	dsrt_t_id smallint NOT NULL COMMENT '디저트분류ID',
	PRIMARY KEY (u_dsrt_id)
) COMMENT = '사용자디저트';


-- 사용자관심사
CREATE TABLE md_u_intr
(
	u_intr_id int NOT NULL AUTO_INCREMENT COMMENT '사용자관심사ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	intr_t_id tinyint NOT NULL COMMENT '관심사분류ID',
	PRIMARY KEY (u_intr_id)
) COMMENT = '사용자관심사';


-- 사용자맛
CREATE TABLE md_u_tast
(
	u_tast_id int NOT NULL AUTO_INCREMENT COMMENT '사용자맛ID',
	user_id varchar(20) NOT NULL COMMENT '회원ID',
	tast_t_id tinyint NOT NULL COMMENT '맛분류ID',
	PRIMARY KEY (u_tast_id)
) COMMENT = '사용자맛';


-- 날씨분류
CREATE TABLE md_weather
(
	weather_id tinyint NOT NULL COMMENT '날씨분류ID',
	weather_name varchar(10) NOT NULL COMMENT '날씨분류명',
	PRIMARY KEY (weather_id)
) COMMENT = '날씨분류';



/* Create Foreign Keys */

ALTER TABLE md_m_algy
	ADD FOREIGN KEY (algy_t_id)
	REFERENCES md_algy_t (algy_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_algy
	ADD FOREIGN KEY (algy_t_id)
	REFERENCES md_algy_t (algy_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor
	ADD FOREIGN KEY (area_t_id)
	REFERENCES md_area_t (area_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor
	ADD FOREIGN KEY (bjd_code)
	REFERENCES md_bjd (bjd_code)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_comb_m
	ADD FOREIGN KEY (comb_id)
	REFERENCES md_comb (comb_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_comb_r
	ADD FOREIGN KEY (comb_id)
	REFERENCES md_comb (comb_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_c_like
	ADD FOREIGN KEY (comb_id)
	REFERENCES md_comb (comb_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_menu
	ADD FOREIGN KEY (drnk_t_id)
	REFERENCES md_drnk_t (drnk_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_drnk
	ADD FOREIGN KEY (drnk_t_id)
	REFERENCES md_drnk_t (drnk_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_menu
	ADD FOREIGN KEY (dsrt_t_id)
	REFERENCES md_dsrt_t (dsrt_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_dsrt
	ADD FOREIGN KEY (dsrt_t_id)
	REFERENCES md_dsrt_t (dsrt_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_user
	ADD FOREIGN KEY (gen_id)
	REFERENCES md_gen (gen_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor_m
	ADD FOREIGN KEY (ice_t_id)
	REFERENCES md_ice (ice_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_intr
	ADD FOREIGN KEY (intr_t_id)
	REFERENCES md_intr_t (intr_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_comb_m
	ADD FOREIGN KEY (menu_id)
	REFERENCES md_menu (menu_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_m_algy
	ADD FOREIGN KEY (menu_id)
	REFERENCES md_menu (menu_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor_m
	ADD FOREIGN KEY (menu_id)
	REFERENCES md_menu (menu_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor_m
	ADD FOREIGN KEY (m_type_id)
	REFERENCES md_m_type (m_type_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_ordr_m
	ADD FOREIGN KEY (ordr_id)
	REFERENCES md_ordr (ordr_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_review
	ADD FOREIGN KEY (ordr_id)
	REFERENCES md_ordr (ordr_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_rev_t
	ADD FOREIGN KEY (rev_id)
	REFERENCES md_review (rev_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_favorite
	ADD FOREIGN KEY (stor_id)
	REFERENCES md_stor (stor_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor_m
	ADD FOREIGN KEY (stor_id)
	REFERENCES md_stor (stor_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor_reg
	ADD FOREIGN KEY (stor_id)
	REFERENCES md_stor (stor_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_buck
	ADD FOREIGN KEY (stor_m_id)
	REFERENCES md_stor_m (stor_m_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_ordr_m
	ADD FOREIGN KEY (stor_m_id)
	REFERENCES md_stor_m (stor_m_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor
	ADD FOREIGN KEY (stor_t_id)
	REFERENCES md_stor_t (stor_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_rev_t
	ADD FOREIGN KEY (tag_id)
	REFERENCES md_tag (tag_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_tag
	ADD FOREIGN KEY (tag_g_id)
	REFERENCES md_tag_g (tag_g_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_tast
	ADD FOREIGN KEY (tast_t_id)
	REFERENCES md_tast_t (tast_t_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_buck
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_comb
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_comb_r
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_c_like
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_favorite
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_ordr
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_stor_reg
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_algy
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_drnk
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_dsrt
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_intr
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_u_tast
	ADD FOREIGN KEY (user_id)
	REFERENCES md_user (user_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_user
	ADD FOREIGN KEY (user_g_id)
	REFERENCES md_user_g (user_g_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE md_ordr
	ADD FOREIGN KEY (weather_id)
	REFERENCES md_weather (weather_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;



