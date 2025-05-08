Create database coin;
DROP DATABASE coin;

use coin;

create table User(
	user_id varchar(100) primary key,
    user_pw varchar(100) not null,
    user_name varchar(100) not null,
    is_admin boolean not null default false
);

DROP TABLE auth_permission, auth_group, auth_group_permissions,
           auth_user, auth_user_groups, auth_user_user_permissions,
           django_content_type;

DROP TABLE auth_permission;
DROP TABLE auth_group;
DROP TABLE auth_group_permissions;
DROP TABLE auth_user;
DROP TABLE auth_user_groups;
DROP TABLE auth_user_user_permissions;
DROP TABLE django_content_type;


drop table user;

select * from app_user;

select * from User;

select * from auth_user;

show tables;

Insert into user(user_id, user_pw, user_name, is_admin) values('test', 'test', 'test', True);