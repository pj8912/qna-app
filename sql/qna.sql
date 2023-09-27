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


CREATE TABLE IF NOT EXISTS vote_questions(
	vqid INT auto_increment primary key not null,
	q_id int NOT null,
	user_id  int NOT null,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (q_id) REFERENCES  questions(qid),
	FOREIGN KEY (user_id) REFERENCES  users(user_id),
);

CREATE TABLE IF NOT EXISTS vote_answers(
	aqid INT auto_increment primary key not null,
	a_id int NOT null,
	user_id  int NOT null,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (a_id) REFERENCES  answers(aid),
	FOREIGN KEY (user_id) REFERENCES  users(user_id),

);

CREATE TABLE IF NOT EXISTS useful_answers(
	ua_id INT auto_increment primary KEY NOT null,
	answer_id INT NOT null,
	user_id INT not  null,
	created_date datetime default current_timestamp,
	FOREIGN KEY user_id REFERENCES users(user_id),
	FOREIGN KEY answer_id REFERENCES answers(aid)
);


CREATE TABLE IF NOT EXISTS save_questions(
	sa_qid INT auto_increment primary KEY NOT null,
	q_id INT NOT null,
	user_id INT not  null,
	created_date datetime default current_timestamp,
	FOREIGN KEY (q_id) REFERENCES  questions(qid),
	FOREIGN KEY answer_id REFERENCES answers(aid)
);


CREATE TABLE IF NOT EXISTS save_answers(
	sa_aid INT auto_increment primary KEY NOT null,
	a_id INT NOT null,
	user_id INT not  null,
	created_date datetime default current_timestamp,
	FOREIGN KEY user_id REFERENCES users(user_id),
	FOREIGN KEY a_id REFERENCES answers(aid)
);



