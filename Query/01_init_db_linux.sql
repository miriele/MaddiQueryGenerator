USE bit;

SET GLOBAL local_infile=1;
SET bulk_insert_buffer_size=536870912;
SET autocommit=0;
SET unique_checks=0;
SET foreign_key_checks=0;


LOAD DATA INFILE '/home/bit/md_ddl/11_md_stor_t_01_pre_modify.csv'
IGNORE INTO TABLE md_stor_t
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(stor_t_id, stor_t_name, @dummy);

LOAD DATA INFILE '/home/bit/md_ddl/12_md_area_t.csv'
IGNORE INTO TABLE md_area_t
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(area_t_id, area_t_name, area_t_min, area_t_max);

LOAD DATA INFILE '/home/bit/md_ddl/13_md_tag_g.csv'
IGNORE INTO TABLE md_tag_g
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(tag_g_id, tag_g_name);

LOAD DATA INFILE '/home/bit/md_ddl/14_md_user_g.csv'
IGNORE INTO TABLE md_user_g
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_g_id, user_g_name);

LOAD DATA INFILE '/home/bit/md_ddl/15_md_gen.csv'
IGNORE INTO TABLE md_gen
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(gen_id, gen_name);

LOAD DATA INFILE '/home/bit/md_ddl/16_md_bjd.csv'
IGNORE INTO TABLE md_bjd
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(bjd_code, bjd_name);

LOAD DATA INFILE '/home/bit/md_ddl/17_md_algy_t.csv'
IGNORE INTO TABLE md_algy_t
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(algy_t_id, algy_t_name);

LOAD DATA INFILE '/home/bit/md_ddl/18_md_drnk_t.csv'
IGNORE INTO TABLE md_drnk_t
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(drnk_t_id, drnk_t_name);

LOAD DATA INFILE '/home/bit/md_ddl/19_md_dsrt_t.csv'
IGNORE INTO TABLE md_dsrt_t
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(dsrt_t_id, dsrt_t_name);

LOAD DATA INFILE '/home/bit/md_ddl/20_md_menu_t.csv'
IGNORE INTO TABLE md_menu_t
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(menu_t_id, menu_t_name);

LOAD DATA INFILE '/home/bit/md_ddl/21_md_intr_t.csv'
IGNORE INTO TABLE md_intr_t
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(intr_t_id, intr_t_name);

LOAD DATA INFILE '/home/bit/md_ddl/22_md_tast_t.csv'
IGNORE INTO TABLE md_tast_t
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(tast_t_id, tast_t_name);

LOAD DATA INFILE '/home/bit/md_ddl/23_md_tag.csv'
IGNORE INTO TABLE md_tag
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(tag_id, tag_g_id, tag_name);

LOAD DATA INFILE '/home/bit/md_ddl/24_md_ice.csv'
IGNORE INTO TABLE md_ice
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(ice_t_id, ice_t_name);

LOAD DATA INFILE '/home/bit/md_ddl/25_md_weather.csv'
IGNORE INTO TABLE md_weather
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(weather_id, weather_name);

LOAD DATA INFILE '/home/bit/md_ddl/31_md_stor.csv'
IGNORE INTO TABLE md_stor
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(stor_t_id, @dumy, bjd_code, area_t_id, stor_img, stor_name, stor_addr, stor_lati, stor_long, stor_tel, stor_num);

LOAD DATA INFILE '/home/bit/md_ddl/33_md_menu.csv'
IGNORE INTO TABLE md_menu
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(menu_id, dsrt_t_id, drnk_t_id, menu_name, menu_cal, menu_info, menu_img);

LOAD DATA INFILE '/home/bit/md_ddl/34_md_m_algy.csv'
IGNORE INTO TABLE md_m_algy
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(menu_id, algy_t_id);

LOAD DATA INFILE '/home/bit/md_ddl/35_md_stor_m.csv'
IGNORE INTO TABLE md_stor_m
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(stor_id, menu_id, ice_t_id, menu_t_id, stor_m_pric, stor_m_name, stor_m_cal, stor_m_info, stor_m_img);

LOAD DATA INFILE '/home/bit/md_ddl/36_md_user.csv'
IGNORE INTO TABLE md_user
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, user_g_id, gen_id, user_nick, user_pass, user_name, user_bir, user_img, user_reg_ts);

-- LOAD DATA INFILE 'C:/Temp/41_md_u_algy.csv'
LOAD DATA INFILE '/home/bit/md_ddl/41_md_u_algy.csv'
IGNORE INTO TABLE md_u_algy
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, algy_t_id);

LOAD DATA INFILE '/home/bit/md_ddl/42_md_u_drnk.csv'
IGNORE INTO TABLE md_u_drnk
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, drnk_t_id);

LOAD DATA INFILE '/home/bit/md_ddl/43_md_u_dsrt.csv'
IGNORE INTO TABLE md_u_dsrt
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, dsrt_t_id);

LOAD DATA INFILE '/home/bit/md_ddl/44_md_u_intr.csv'
IGNORE INTO TABLE md_u_intr
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, intr_t_id);

LOAD DATA INFILE '/home/bit/md_ddl/45_md_u_tast.csv'
IGNORE INTO TABLE md_u_tast
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, tast_t_id);

LOAD DATA INFILE '/home/bit/md_ddl/51_md_hjd.csv'
IGNORE INTO TABLE md_hjd
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(hjd_code, hjd_name, hjd_x, hjd_y);

LOAD DATA INFILE '/home/bit/md_ddl/52_md_bh.csv'
IGNORE INTO TABLE md_bh
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(bjd_code, hjd_code);

LOAD DATA INFILE '/home/bit/md_ddl/61_md_click.csv'
IGNORE INTO TABLE md_click
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(stor_m_id, user_id, click_ts);

LOAD DATA INFILE '/home/bit/md_ddl/61_md_srch.csv'
IGNORE INTO TABLE md_srch
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, bjd_code, srch_word, srch_ts);

LOAD DATA INFILE '/home/bit/md_ddl/62_md_buck.csv'
IGNORE INTO TABLE md_buck
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, stor_m_id, buck_num, buck_reg_ts, @buck_del_ts, buck_ord_ts);

LOAD DATA INFILE '/home/bit/md_ddl/63_md_ordr.csv'
IGNORE INTO TABLE md_ordr
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, weather_id, ordr_temp, ordr_ord_ts, ordr_com_ts);

LOAD DATA INFILE '/home/bit/md_ddl/63_md_ordr_m.csv'
IGNORE INTO TABLE md_ordr_m
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(ordr_id, stor_m_id, ordr_num);

LOAD DATA INFILE '/home/bit/md_ddl/64_md_review.csv'
IGNORE INTO TABLE md_review
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(ordr_id, rev_star, rev_ts, @rev_cont, @rev_img);

LOAD DATA INFILE '/home/bit/md_ddl/65_md_recommend.csv'
IGNORE INTO TABLE md_recommend
FIELDS
	TERMINATED BY '\t'
LINES
	TERMINATED BY '\n'
	STARTING BY ''
(user_id, menu_id);

-- insert into md_buck (user_id, stor_m_id, buck_num, buck_reg_ts) values ('abc001', 280, 2, now());
-- insert into md_buck (user_id, stor_m_id, buck_num, buck_reg_ts) values ('abc001', 305, 3, now());
-- insert into md_buck (user_id, stor_m_id, buck_num, buck_reg_ts) values ('abc001', 37957, 1, now());
-- insert into md_buck (user_id, stor_m_id, buck_num, buck_reg_ts) values ('abc001', 37967, 2, now());

COMMIT;

SET bulk_insert_buffer_size=8388608;
SET autocommit=1;
SET unique_checks=1;
SET foreign_key_checks=1;
SET GLOBAL local_infile=0;


