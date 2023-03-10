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
    id integer primary key autoincrement,
    username text not null unique,
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
login page (/login),
signup page (/signup),
top page (/),
post page (/post),
Like List page (/likelist)
### Application Overview
#### Design
The front part of the application is implemented with HTML, CSS and Bootstrap.
#### Header
Before logging in, login and signup are shown. If you click on the login section, you will be redirected to the login page, and if you click on the signup section, you will be redirected to the signup page.After logging in, you will see top, post, like list and logout. If you click on the "like list," you will be redirected to the like list page, and if you click on "post," you will be redirected to the post page. Click "logout" to log out.
#### Top page
The top page is not displayed unless you log in. On the top page, you can see your match reviews and other users' reviews. When you click on the "Submit" button, you will be redirected to the "Submit" page.When you click on the Like button, you can like the page. After clicking the Like button, the button changes to show "Unlike". When you click on the "Unlike" button, the Like is cancelled.
#### Post page
If you click on the button "Home", you will be returned to the top page.Enter the match in the text box labeled Match. Write a match review in the text area labeled Review. Click the "Submit" button to post the review and go to the top page.
#### Like list page
You will see reviews that you have liked.When you click on the "Unlike" button, the Like is canceled.
