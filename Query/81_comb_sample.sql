INSERT INTO md_comb(user_id,comb_tit,comb_nop,comb_cont,comb_img,comb_reg_ts) VALUES('abc001','abc001의조합',2,'커피엔브레드','abc001.jpg',NOW());
INSERT INTO md_comb(user_id,comb_tit,comb_nop,comb_cont,comb_img,comb_reg_ts) VALUES('abc002','abc002의조합',2,'abc002의내용','abc002.jpg',NOW());
INSERT INTO md_comb_m(comb_id,menu_id) VALUES(1,5);
INSERT INTO md_comb_m(comb_id,menu_id) VALUES(1,153);
INSERT INTO md_comb_m(comb_id,menu_id) VALUES(2,0);
INSERT INTO md_comb_m(comb_id,menu_id) VALUES(2,179);
COMMIT;