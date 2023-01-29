CREATE TABLE users(

	user_id int auto_increment primary key not null,
	fullname varchar(300) not null,
	user_uname varchar(100) not null,
	user_pwd varchar(300) not null,
	created_at datetime default current_timestamp,
	updated_at datetime default current_timestamp
);


CREATE TABLE questions(
	qid int auto_increment primary key not null, 
	question text not null,
	user_id int not null,
	foreign key (user_id) REFERENCES users(user_id),
	created_at datetime default current_timestamp,
        updated_at datetime default current_timestamp
);


CREATE TABLE answers(
	
	aid int auto_increment primary key not null,
	q_id int not null,
	answer text not null,
	user_id int not null,
	foreign key (q_id) REFERENCES questions(qid),
	foreign key (user_id) REFERENCES users(user_id),
	created_at datetime default current_timestamp,
        updated_at datetime default current_timestamp
);



