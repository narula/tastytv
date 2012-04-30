drop table if exists tvshows;
create table tvshows (
  show_id integer primary key autoincrement,
  show_name string not null,
  show_pic string not null,
  show_video string not null,
  show_description string not null
);

drop table if exists users;
create table users (
  user_id integer primary key autoincrement,
  user_name string not null
);

drop table if exists watchbox;
create table watchbox (
  user_id integer not null,
  show_id integer not null
);
