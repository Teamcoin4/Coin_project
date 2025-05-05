Create database coin;
DROP DATABASE coin;

use coin;

create table User(
	user_id varchar(100) primary key,
    user_pw varchar(100) not null,
    user_name varchar(100) not null,
    is_admin boolean not null default false
);

drop table user;
DROP TABLE IF EXISTS user;
DROP TABLE social_auth_association;
DROP TABLE social_auth_code;
DROP TABLE social_auth_nonce;
DROP TABLE social_auth_partial;
DROP TABLE social_auth_usersocialauth;
SHOW TABLES LIKE 'app_user';

select * from app_user;

select * from User;

select * from auth_user;

show tables;

Insert into user(user_id, user_pw, user_name, is_admin) values('test', 'test', 'test', True);