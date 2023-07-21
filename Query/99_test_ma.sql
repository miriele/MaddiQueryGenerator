USE mysql;
USE BIT;
SELECT USER, HOST FROM user;
SELECT * FROM USER;
SHOW VARIABLES LIKE '%dir';


SHOW GRANTS FOR root@'%';


CREATE user 'bit'@'%'


grant all privileges on *.* TO 'root'@'%' identified BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' identified BY '1234';
GRANT ALL ON *.* TO root@%;



SHOW VARIABLES LIKE 'local%';
SHOW VARIABLES LIKE 'secure_file_priv';

SELECT @@secure_file_priv;

SET secure_file_priv="";


DESC md_stor;

SELECT * FROM md_stor_t;
SELECT * FROM md_area_t;
SELECT * FROM md_tag_g;
SELECT * FROM md_user_g;
SELECT * FROM md_gen;
SELECT * FROM md_bjd;
SELECT * FROM md_algy_t;
SELECT * FROM md_drnk_t;
SELECT * FROM md_dsrt_t;
SELECT * FROM md_menu_t;
SELECT * FROM md_intr_t;
SELECT * FROM md_tast_t;
SELECT * FROM md_tag;
SELECT * FROM md_ice;
SELECT * FROM md_weather;

SELECT * FROM md_stor;
SELECT * FROM md_menu;
SELECT * FROM md_m_algy;
SELECT * FROM md_stor_m;
SELECT * FROM md_user;

SELECT * FROM md_u_algy;
SELECT * FROM md_u_drnk;
SELECT * FROM md_u_dsrt;
SELECT * FROM md_u_intr;
SELECT * FROM md_u_tast;

SELECT * FROM md_user WHERE user_id='dlekdbgb';
SELECT * FROM md_drnk_t;

DELETE FROM md_drnk_t;
DELETE FROM md_dsrt_t;
DELETE FROM md_intr_t;
DELETE FROM md_stor;
DELETE FROM md_area_t;
DELETE FROM md_menu;
DELETE FROM md_m_algy;
delete from md_stor_m;
DELETE FROM md_u_algy;
delete FROM md_u_drnk;
DELETE FROM md_u_dsrt;
DELETE FROM md_u_intr;
DELETE FROM md_u_tast;
DELETE FROM md_user;

SHOW GRANTS FOR CURRENT_USER;
SHOW GRANTS FOR 'bit'@'%';
SHOW GRANTS FOR 'root'@'%';

DESC board_imageboard;