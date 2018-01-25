drop table if exists entries;

create table entries (
	id integer primary key autoincrement,
	age REAL not null,
	species text not null,
	score REAL not null
);