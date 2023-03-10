# Premier League Review
#### Video Demo: https://youtu.be/RTaHAbHLV7E
## Description
### purpose
My hobby is watching the Premier League.The Premier League is a league of English soccer.I wanted to summarize and analyze the game by myself and see what others thought. So I created an app that allows you to review the Premier League matches.
### Service Contents
An application that allows you to review Premier League matches.
### Technology
Python, flask, HTML, CSS, bootstrap, SQlite
### DataBase
CREATE TABLE user (
    id integer primary key autoincrement,　　username text not null unique,
    password text not null,　　
)　　

CREATE TABLE review (
    id integer primary key autoincrement,
    user_id integer not null,
    username text not null,
    match text not null,
    review text not null,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE like (
    id integer primary key autoincrement,
    user_id integer not null,
    review_id integer not null,
    FOREIGN KEY(user_id) REFERENCES user(id),
    FOREIGN KEY(review_id) REFERENCES review(id)
);
### URL Patterns
login page (/login)
signup page (/signup)
top page (/)
post page (/post)
Like List page (/likelist)
### Application Overview
