USE bit;

SET foreign_key_checks=0;
delete from md_stor_t;
delete from md_area_t;
delete from md_tag_g;
delete from md_user_g;
delete from md_gen;
delete from md_bjd;
delete from md_algy_t;
delete from md_drnk_t;
delete from md_dsrt_t;
delete from md_menu_t;
delete from md_intr_t;
delete from md_tast_t;
delete from md_tag;
delete from md_ice;
delete from md_weather;
delete from md_stor;
delete from md_menu;
delete from md_m_algy;
delete from md_stor_m;
delete from md_user;
delete from md_u_algy;
delete from md_u_drnk;
delete from md_u_dsrt;
delete from md_u_intr;
delete from md_u_tast;
SET foreign_key_checks=1;


select * from md_user where user_id='m001';

select user_id, user_name, user_g_name, user_reg_ts
from md_user u, md_user_g ug
where u.user_g_id = ug.user_g_id;

select *
from md_user u, md_user_g ug
where  u.user_g_id = ug.user_g_id
	and u.user_id = 'abc002';


select * from md_c_like;
select count(*) from md_c_like where comb_id=2;

select * from md_drnk_t;
select * from md_srch;

select * from md_menu;
select * from md_menu where dsrt_t_id=1;
select * from md_menu where menu_name='아메리카노';
select * from md_menu
where menu_name like '%아메%';

select * from md_bjd;
select * from md_bjd where bjd_code=4514013400;
select * from md_bjd where bjd_name like '서울특별시%';
select * from md_bjd where bjd_name like '서울특별시 서초구%';
select * from md_bjd where bjd_name like '서울특별시 서초구 서초동%';
select * from md_bjd where bjd_name = '서울특별시 서초구 방배동';
select bjd_code from md_bjd where bjd_name = '서울특별시 서초구 방배동';


select * from md_stor_m where stor_id=1;
select count(*) from md_stor_m where stor_id=0;

select stor_m_name from md_stor_m
where stor_m_name like '%카페%'
group by stor_m_name;


select *
from md_stor_m sm
where sm.stor_id=107033;

select * from md_stor_m;

delete from md_user;
select * from md_user;
select * from md_u_algy;


select * from md_stor;
select count(*) from md_stor where stor_img not like '%.jpg';
select * from md_stor where stor_img not like '%.jpg';

select distinct stor_id
from md_stor_m sm, md_menu m
where  sm.menu_id = m.menu_id
	and m.menu_name = '아메리카노';

select s.stor_id, s.stor_name, s.stor_img, a.area_t_name, b.bjd_name
from md_stor s, md_bjd b, md_area_t a
where  s.bjd_code = b.bjd_code
	and s.area_t_id = a.area_t_id
	and b.bjd_name = '서울특별시 서초구 서초동';

-- select s.stor_id, s.stor_name, s.stor_img, a.area_t_name, b.bjd_name
select *
from md_stor s, md_bjd b, md_area_t a
where  s.bjd_code = b.bjd_code
	and s.area_t_id = a.area_t_id
--	and 37.4942405717987 < s.stor_lati
--	and s.stor_lati < 37.49604676988036
--	and 127.02722140819515 < s.stor_long
--	and s.stor_long < 127.02857906765026
--	and 35.4942405717987 < s.stor_lati
	and s.stor_lati < 38.49604676988036
--	and 125.02722140819515 < s.stor_long
	and s.stor_long < 128.02857906765026
	and b.bjd_name = '서울특별시 서초구 서초동';

select * from md_stor
where bjd_code=1165010800
	and stor_name like '스타벅스%'
order by stor_addr;

select s.stor_id
from md_bjd b, md_stor s
where  b.bjd_code = s.bjd_code
	and b.bjd_name = '서울특별시 서초구 서초동';

select *
from md_menu m, md_stor_m sm
where m.menu_id = sm.menu_id
	and m.menu_name='아메리카노';
	
select s.stor_id, s.stor_name, a.area_t_name
from md_bjd b, md_stor s, md_area_t a
where  b.bjd_code = s.bjd_code
	and s.area_t_id = a.area_t_id
	and b.bjd_name = '서울특별시 서초구 서초동';

select sm.stor_id
from md_menu m, md_stor_m sm
where m.menu_id = sm.menu_id
	and m.menu_name='아메리카노'
group by sm.stor_id;



select sa.stor_id, stor_name, stor_img, area_t_name
from
	(select s.stor_id, s.stor_name, s.stor_img, a.area_t_name
	from md_bjd b, md_stor s, md_area_t a
	where  b.bjd_code = s.bjd_code
		and s.area_t_id = a.area_t_id
		and b.bjd_name = '서울특별시 서초구 서초동') sa,
	(select sm.stor_id
	from md_menu m, md_stor_m sm
	where m.menu_id = sm.menu_id
		and m.menu_name='아메리카노'
	group by sm.stor_id) sb
where sa.stor_id = sb.stor_id;


-- md_stor.stor_img, md_stor.stor_name, md_area_t.area_t_name
select *
from md_menu m, md_stor_m sm
where m.menu_id = sm.menu_id
	and m.menu_name='아메리카노'
	and sm.stor_id in (
		select s.stor_id
		from md_bjd b, md_stor s
		where  b.bjd_code = s.bjd_code
			and b.bjd_name = '서울특별시 서초구 서초동');

select *
from md_menu m, md_stor_m sm
where m.menu_id = sm.menu_id
	and m.menu_name='아메리카노'
	and sm.stor_id in (
		select s.stor_id
		from md_bjd b, md_stor s
		where  b.bjd_code = s.bjd_code
			and b.bjd_name = '서울특별시 서초구 서초동');

select sm.stor_id
from md_menu m, md_stor_m sm
where m.menu_id = sm.menu_id
	and m.menu_name='아메리카노'
	and sm.stor_id in (
		select s.stor_id
		from md_bjd b, md_stor s
		where  b.bjd_code = s.bjd_code
			and b.bjd_name = '서울특별시 서초구 서초동')
group by sm.stor_id;



select *
from md_stor_m sm, md_stor
where sm.stor_id = s.stor_id;

select *
from md_bjd b, md_menu m, md_stor_m sm, md_stor s
where  b.bjd_code = s.bjd_code
	and b.bjd_name = '서울특별시 서초구 서초동';
	and m.menu_id = sm.menu_id
	and sm.stor_id = s.stor_id
	and m.menu_name = '아메리카노';



select * from md_stor_m where stor_m_id=37957;
select * from md_stor_m where stor_id=5;

select * from md_buck;
delete from md_buck where buck_id > 96 and buck_id < 102;
insert into md_buck (user_id, stor_m_id, buck_num, buck_reg_ts) values ('abc001', 280, 2, now());
insert into md_buck (user_id, stor_m_id, buck_num, buck_reg_ts) values ('abc001', 305, 3, now());
insert into md_buck (user_id, stor_m_id, buck_num, buck_reg_ts) values ('abc001', 37957, 1, now());
insert into md_buck (user_id, stor_m_id, buck_num, buck_reg_ts) values ('abc001', 37967, 2, now());
commit;

select * from md_ordr;


select * from md_review;
select * from md_ordr where ordr_id=1;
select * from md_ordr_m where ordr_id=1;
select * from md_stor_m where stor_m_id=15;
select * from md_stor where stor_id=1;

select o.user_id, o.ordr_id, s.stor_name, r.rev_ts
from md_review r, md_ordr o,
     md_ordr_m om, md_stor_m sm, md_stor s
where  r.ordr_id    = o.ordr_id
	and o.ordr_id    = om.ordr_id
	and om.stor_m_id = sm.stor_m_id
	and sm.stor_id   = s.stor_id
	and r.rev_id     = 1;

SELECT stor_m_name FROM md_stor_m WHERE stor_m_id = 15;
SELECT rev_img,rev_star,rev_cont FROM md_review WHERE rev_id = 1;
SELECT t.tag_name FROM md_tag t JOIN md_rev_t rt ON t.tag_id = rt.tag_id WHERE rt.rev_id = 1;

SELECT stor_id FROM md_stor_reg WHERE reg_id = 5;
SELECT stor_t_id FROM md_stor WHERE stor_id = 100;
SELECT stor_t_name FROM md_stor_t WHERE stor_t_id = 21;

select stor_t_name
from md_stor_reg sr, md_stor s, md_stor_t st
where  sr.stor_id = s.stor_id
	and s.stor_t_id = st.stor_t_id
	and sr.reg_id = 5;
	
select *
from md_stor_m sm, md_menu m
where sm.menu_id = m.menu_id
	and m.;

select * from md_comb;

select *
from md_comb c, md_c_like cl
where c.comb_id = cl.comb_id;

select *
from md_comb c, md_comb_m cm
where  c.comb_id = cm.comb_id
	and c.comb_id = 2;

select *
from md_comb c, md_comb_m cm, md_menu m
where  c.comb_id = cm.comb_id
	and cm.menu_id = m.menu_id
	and c.comb_id = 1;


select * from md_ordr;
select * from md_ordr_m;
select count(*) from md_ordr;
select count(*) from md_stor_m;
select count(*) from md_menu;



SELECT
    m.menu_id,
    m.menu_name,
    count(o.ordr_id) AS total_orders
FROM
    md_menu AS m
LEFT JOIN
    md_stor_m AS sm ON m.menu_id = sm.menu_id
LEFT JOIN
    md_ordr_m AS om ON sm.stor_m_id = om.stor_m_id
LEFT JOIN
    md_ordr AS o ON om.ordr_id = o.ordr_id
WHERE
    m.dsrt_t_id = -1
GROUP BY
    m.menu_id
ORDER BY
    total_orders DESC
LIMIT 5;


SELECT
    menu.menu_id,
    menu.menu_name,
    menu.drnk_t_id,
    menu.dsrt_t_id,
    COALESCE(drnk_orders.total_orders, 0) AS drink_orders,
    COALESCE(dsrt_orders.total_orders, 0) AS dessert_orders
FROM
    md_menu menu
LEFT JOIN (
    SELECT
        stor_m.menu_id,
        SUM(ordr_m.ordr_num) AS total_orders
    FROM
        md_ordr_m ordr_m
    INNER JOIN
        md_stor_m stor_m ON ordr_m.stor_m_id = stor_m.stor_m_id
    GROUP BY
        stor_m.menu_id
) drnk_orders ON menu.menu_id = drnk_orders.menu_id AND menu.drnk_t_id = -1
LEFT JOIN (
    SELECT
        stor_m.menu_id,
        SUM(ordr_m.ordr_num) AS total_orders
    FROM
        md_ordr_m ordr_m
    INNER JOIN
        md_stor_m stor_m ON ordr_m.stor_m_id = stor_m.stor_m_id
    GROUP BY
        stor_m.menu_id
) dsrt_orders ON menu.menu_id = dsrt_orders.menu_id AND menu.dsrt_t_id = -1
ORDER BY
    drink_orders DESC, dessert_orders DESC
LIMIT 5;



SELECT
    menu.menu_id,
    menu.menu_name,
    COALESCE(drink_orders.total_orders, 0) AS drink_orders
FROM
    md_menu menu
LEFT JOIN (
    SELECT
        stor_m.menu_id,
        SUM(ordr_m.ordr_num) AS total_orders
    FROM
        md_ordr_m ordr_m
    INNER JOIN
        md_stor_m stor_m ON ordr_m.stor_m_id = stor_m.stor_m_id
    GROUP BY
        stor_m.menu_id
) drink_orders ON menu.menu_id = drink_orders.menu_id AND menu.drnk_t_id = -1
WHERE
    menu.drnk_t_id = -1
ORDER BY
    drink_orders DESC
LIMIT 5;



SELECT
    menu.menu_id,
    menu.menu_name,
    COALESCE(drink_orders.total_orders, 0) AS drink_orders
FROM
    md_menu menu
LEFT JOIN (
    SELECT
        stor_m.menu_id,
        SUM(ordr_m.ordr_num) AS total_orders
    FROM
        md_ordr_m ordr_m
    INNER JOIN
        md_stor_m stor_m ON ordr_m.stor_m_id = stor_m.stor_m_id
    GROUP BY
        stor_m.menu_id
) drink_orders ON menu.menu_id = drink_orders.menu_id AND menu.dsrt_t_id = -1
WHERE
    menu.dsrt_t_id = -1
ORDER BY
    drink_orders DESC
LIMIT 5;



SELECT
    menu.menu_id,
    menu.menu_name,
    COUNT(ordr_m.ordr_id) AS total_orders
FROM (
    SELECT menu_id, menu_name
    FROM md_menu
    WHERE drnk_t_id = -1
    ORDER BY menu_id -- 혹은 다른 필드를 기준으로 정렬
) menu
LEFT JOIN md_stor_m stor_m ON menu.menu_id = stor_m.menu_id
LEFT JOIN md_ordr_m ordr_m ON stor_m.stor_m_id = ordr_m.stor_m_id
GROUP BY menu.menu_id
ORDER BY total_orders DESC;

SELECT
    menu.menu_id,
    menu.menu_name,
    COUNT(ordr_m.ordr_id) AS total_orders
FROM (
    SELECT menu_id, menu_name
    FROM md_menu
    WHERE dsrt_t_id = -1
    ORDER BY menu_id -- 혹은 다른 필드를 기준으로 정렬
) menu
LEFT JOIN md_stor_m stor_m ON menu.menu_id = stor_m.menu_id
LEFT JOIN md_ordr_m ordr_m ON stor_m.stor_m_id = ordr_m.stor_m_id
GROUP BY menu.menu_id
ORDER BY total_orders DESC;

select * from md_stor where stor_id = 1;
select count(*) from md_stor where stor_addr like '경기%'; -- 10748
select count(*) from md_stor where stor_addr like '서울%';	-- 10161
select count(*) from md_stor where stor_addr like '부산%'; -- 3345
select count(*) from md_stor where stor_addr like '경상남%'; -- 2883
select count(*) from md_stor where stor_addr like '인천%'; -- 2489
select count(*) from md_stor where stor_addr like '대구%'; -- 2417
select count(*) from md_stor where stor_addr like '경상북%'; -- 2246
select count(*) from md_stor where stor_addr like '충청남%'; -- 1644
select count(*) from md_stor where stor_addr like '전라북%'; -- 1569
select count(*) from md_stor where stor_addr like '광주%'; -- 1441
select count(*) from md_stor where stor_addr like '전라남%'; -- 1435
select count(*) from md_stor where stor_addr like '대전%'; -- 1396
select count(*) from md_stor where stor_addr like '강원%'; -- 1293
select count(*) from md_stor where stor_addr like '충청북%'; -- 1200
select count(*) from md_stor where stor_addr like '울산%'; -- 1026
select count(*) from md_stor where stor_addr like '제주%'; -- 653
select count(*) from md_stor where stor_addr like '세종%'; -- 326


select * from md_drnk_t;
select * from md_dsrt_t;

select * from md_stor_reg;
delete from md_stor_reg;

select * from md_ordr where user_id='abc001';
select * from md_review where ordr_id=1;













