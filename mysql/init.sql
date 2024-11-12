CREATE DATABASE IF NOT EXISTS webapp;


CREATE USER 'master'@'%' IDENTIFIED BY 'P@ss4MA';
GRANT ALL PRIVILEGES ON webapp.* TO 'master'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;


USE webapp;

CREATE TABLE users(
	id INT NOT NULL PRIMARY KEY, -- 유저 PK
	username VARCHAR(16) NOT NULL, -- 이름
	userid VARCHAR(32) NOT NULL, -- 아이디
	user_pw VARCHAR(200) NULL, -- 패스워드
	email VARCHAR(50) NULL, -- 이메일
	phone VARCHAR(50) NULL -- 폰번호
);

CREATE TABLE 'membership' (
	id INT NOT NULL PRIMARY KEY, -- 멤버쉽 PK
	u_id INT NOT NULL, -- 유저(users) 외래키
	point INT NOT NULL, -- 포인트
	subscribe INT NOT NULL -- 구독 여부
	FOREIGN KEY(u_id) REFERENCES users(id) ON DELETE CASCADE -- 유저(users) 외래키
);

CREATE TABLE 'board' (
	id INT NOT NULL PRIMARY KEY, -- 게시판 PK
	u_id INT NOT NULL, -- user의 PK 불러오기(PK로 불러온 후, 이름 혹은 아이디 불러오기)
	title VARCHAR(255) NULL, -- 제목
	content VARCHAR(255) NULL, -- 내용
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 등록날짜
	FOREIGN KEY(u_id) REFERENCES users(id) ON DELETE CASCADE -- 유저(users) 외래키
);


CREATE TABLE 'admin' (
	id INT PRIMARY KEY, -- 관리자 PK
	FOREIGN KEY(id) REFERENCES users(id) ON DELETE CASCADE -- 유저(users) 외래키 {유저 안에 관리자 존재}
);


CREATE TABLE 'subjects' (
	id INT AUTO_INCREMENT PRIMARY KEY, -- 과목 PK
	name VARCHAR(64) NOT NULL -- 과목 이름
);


CREATE TABLE 'quizzes' (
	id INT AUTO_INCREMENT PRIMARY KEY, -- 퀴즈 PK
	u_id INT NOT NULL, -- 유저(users) 외래키
	s_id INT NOT NULL, -- 과목(subject) 외래키
	question VARCHAR(255) NOT NULL, -- 문제(지문)
	answer VARCHAR(128) NOT NULL, -- 정답
	opt1 VARCHAR(128) NOT NULL, -- 오답1
	opt2 VARCHAR(128), -- 오답 2
	opt3 VARCHAR(128), -- 오답 3
	comment VARCHAR(512), -- 해설
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 등록 날짜
	FOREIGN KEY(u_id) REFERENCES users(id) ON DELETE CASCADE, -- 유저(users) 외래키
	FOREIGN KEY(s_id) REFERENCES subjects(id) ON DELETE CASCADE-- 과목(subject) 외래키
);

CREATE TABLE 'file' (
	id INT NOT NULL PRIMARY KEY, -- 파일 PK
	b_id INT NOT NULL, -- 게시판(board) PK
	file_url VARCHAR(255) NULL, -- 파일 url(추후 url 불러와서 다운로드 가능하게 만듦)
	FOREIGN KEY(b_id) REFERENCES board(id) ON DELETE CASCADE -- 게시판(board) PK
);



INSERT INTO subjects VALUES (NULL, "인프라 활용을 위한 파이썬");
INSERT INTO subjects VALUES (NULL, "애플리케이션 보안");
INSERT INTO subjects VALUES (NULL, "시스템/네트워크 보안 기술");
INSERT INTO subjects VALUES (NULL, "클라우드 보안 기술");

INSERT INTO subjects VALUES (NULL, "클라우드기반 시스템 운영/구축 실무");
INSERT INTO subjects VALUES (NULL, "클라우드기반 취약점 진단 및 대응 실무");
INSERT INTO subjects VALUES (NULL, "데이터 3법과 개인정보보호");
INSERT INTO subjects VALUES (NULL, "클라우드 보안 컨설팅 실무");
