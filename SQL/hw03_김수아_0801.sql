use shoppingmall;

drop table if exists user_table;
drop table if exists buy_table;

create table user_table
(userID char(8),
userName varchar(10) not null,
birthYear int not null,
addr char(2) not null,
mobile1 char(3),
mobile2 char(8),
height smallint,
mDate date,
constraint primary key (userID));

desc user_table;


create table buy_table
(num int auto_increment,
userID char(8) not null,
prodName char(6) not null,
groupName char(4),
price int not null,
amount smallint not null,
constraint primary key (num),
constraint foreign key (userID)
references user_table(userID));

desc buy_table;




insert into user_table
values 
('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'),
('KJD', '김제동', 1974, '경남', null, null, 173, '2013-03-03'),
('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-05-05'),
('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-05-05'),
('SDY', '신동엽', 1971, '경기', null, null, 176, '2008-10-10'),
('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08');

select * from user_table;


insert into buy_table
values
(null, 'KHD', '운동화', null, 30, 2),
(null, 'KHD', '노트북', '전자', 1000, 1),
(null, 'KYM', '모니터', '전자', 200, 1),
(null, 'PSH', '모니터', '전자', 200, 5),
(null, 'KHD', '청바지', '의류', 50, 3),
(null, 'PSH', '메모리', '전자', 80, 10),
(null, 'KJD', '책', '서적', 15, 5),
(null, 'LHJ', '책', '서적', 15, 2),
(null, 'LHJ', '청바지', '의류', 50, 1),
(null, 'PSH', '운동화', null, 30, 2),
(null, 'LHJ', '책', '서적', 15, 1),
(null, 'PSH', '운동화', null, 30, 2);

select * from buy_table;




# 2. 두 테이블을 내부조인(buy_table.useID와 user_table.userID)한 다음
# 아래의 결과와 같이 출력이 되도록 SQL 쿼리를 작성하시오.
# 1) 내부 조인한 결과에 '연락처' 컬럼 추가
select userName, prodName, addr, concat(mobile1, mobile2) as '연락처'
from user_table as u
inner join buy_table as b
on u.userID=b.userID;

# 2) userID가 KYM인 사람이 구매한 물건과 회원 정보 출력
select u.userID, userName, prodName, addr, concat(mobile1, mobile2) as '연락처'
from user_table u 
inner join buy_table b
on u.userID=b.userID
where u.userID='KYM';

# 3) 전체 회원이 구매한 목록을 회원 아이디 순으로 정렬
select u.userID, userName, prodName, addr, concat(mobile1,mobile2) as '연락처'
from user_table u
inner join buy_table b
on u.userID=b.userID
order by u.userID;

# 4) 쇼핑몰에서 한 번이라도 구매한 기록이 있는 회원 정보를 회원 아이디 순으로 출력(distinct 사용)
select distinct u.userID, userName, addr
from user_table u
inner join buy_table b
on u.userID=b.userID;

# 5) 쇼핑몰 회원 중에서 주소가 경북과 경남인 회원 정보를 회원 아이디 순으로 출력
select u.userID, userName, addr, concat(mobile1,mobile2) as '연락처'
from user_table u
inner join buy_table b
on u.userID=b.userID
where addr in ('경북', '경남')
order by u.userID;



select userID, userName, addr, concat(mobile1,mobile2) as '연락처'
from user_table
where addr in ('경북', '경남')
order by userID;


delete from buy_table;
delete from user_table;

select userid from user_table;