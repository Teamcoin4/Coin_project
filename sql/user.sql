Create database coin;
DROP DATABASE coin;

use coin;

create table User(
	user_id varchar(100) primary key,
    user_pw varchar(100) not null,
    user_name varchar(100) not null,
    is_admin boolean not null default false
);

select * from User;
select * from auth_user;
select * from coin_recent;
select * from coin_archive;
select * from trade_request;
select * from asset;
select * from trade_history;


show tables;

Insert into user(user_id, user_pw, user_name, is_admin) values('test', 'test', 'test', True);
