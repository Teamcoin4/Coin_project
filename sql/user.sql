Create database coin;

use coin;

create table user(
	user_id varchar(100) primary key,
    user_pw varchar(100) not null,
    user_name varchar(100) not null,
    is_admin boolean not null default false
);

select * from user;