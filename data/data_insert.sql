INSERT INTO users(username, hashed_password) VALUES('Gerald', '$argon2id$v=19$m=65536,t=3,p=4$bdMsTHecGs62+Qr0hY6REg$qt2ezNuDbMuyvXqKhB0Riys9WRSFElXBJiWh2XHSkgk');

INSERT INTO users(username, hashed_password) VALUES('Hector', '$argon2id$v=19$m=65536,t=3,p=4$bdMsTHecGs62+Qr0hY6REg$qt2ezNuDbMuyvXqKhB0Riys9WRSFElXBJiWh2XHSkgk');

INSERT INTO users(username, hashed_password, is_admin) VALUES('Bastien', '$argon2id$v=19$m=65536,t=3,p=4$no0skltpLijPPfoPrOI6oA$D2mFj6DsTl7qKXEAyp3+TCJAT/5t9xIhhbQYjXH8Ddk', TRUE);

INSERT INTO have(id_user, id_ingredient) VALUES(1,337);
INSERT INTO have(id_user, id_ingredient) VALUES(1,305);
INSERT INTO have(id_user, id_ingredient) VALUES(1,312);
INSERT INTO have(id_user, id_ingredient) VALUES(1,476);
INSERT INTO have(id_user, id_ingredient) VALUES(1,455);

INSERT INTO have(id_user, id_ingredient) VALUES(2,337);
INSERT INTO have(id_user, id_ingredient) VALUES(2,305);


INSERT INTO have(id_user, id_ingredient) VALUES(3,337);
INSERT INTO have(id_user, id_ingredient) VALUES(3,305);
INSERT INTO have(id_user, id_ingredient) VALUES(3,312);