# spartanews
<<<<<<< HEAD
This is the Totoro News project, inspired by the Geek News page.

[팀노션 이동](https://www.notion.so/teamsparta/1e2a365b56ad4cf8acd68bff9c3c59c8/)


## Features
- **Account Management:**
  - User registration
  - Login
  - Logout
  - Change the Password
  - Withdrawal
  - Subscription to the authors
  - User profile(My page)
     - Include 'Like article list', 'Subscribing authors' and 'My articles'.
  
&nbsp;

- **Article Management:**
  - Post articles
  - Edit articles
  - Delete articles
  - Show article list
  - Show article
  - 'Like' to articles
  - Post comments
  - Delete comments
  - Recommend comments
  - Search articles

&nbsp;

## Requirements
- asgiref==3.8.1
- Django==4.2
- django-seed==0.3.1
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- Faker==28.4.1
- pillow==10.4.0
- psycopg2==2.9.9
- PyJWT==2.9.0
- python-dateutil==2.9.0.post0
- six==1.16.0
- sqlparse==0.5.1
- toposort==1.10
- typing_extensions==4.12.2
- tzdata==2024.1


&nbsp;

## Getting started
#### Installation

```python
git clone https://github.com/KimGyeongMinB/spartanews.git
cd spartanews
```


#### Install Dependencies
```python
pip install -r requirements.txt
```

#### Run Migrations

```python
python manage.py makemigrations
python manage.py migrate
```


#### Start the Servers
```python
python manage.py runserver
```
&nbsp;
&nbsp;
&nbsp;
&nbsp;

## ERD
![ERD](/ERD.png)
&nbsp;
&nbsp;
&nbsp;
&nbsp;

## Project Structure

```
📦 
├─ .gitignore
├─ ERD.png
├─ README.md
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ articles
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_delete_comment.py
│  │  ├─ 0003_article_author.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ requirements.txt
└─ spartanews
   ├─ __init__.py
   ├─ asgi.py
   ├─ settings.py
   ├─ urls.py
   └─ wsgi.py
```


&nbsp;
&nbsp;
&nbsp;

## Role & Contribution
* Backend
  - User registration 강다영
  - Login 강다영
  - Logout 강다영
  - Withdrawal 강다영
  - Search articles 강다영
  - Change the Password 김경민
  - Subscription to the authors 김경민
  - User profile(My page) 김경민
  - 'Like' to articles 김나희
  - Post comments 김나희
  - Delete comments 김나희
  - Recommend comments 김나희
  - Post articles 조민희
  - Edit articles 조민희
  - Delete articles 조민희
  - Show article list 조민희
  - Show article 조민희

&nbsp;
* etc
  + 전체 개발 일정 및 이슈 관리 - 전 팀원
  + 발표 - 김경민

&nbsp;

## Developer
- 강다영
- 김경민
- 김나희
- 조민희
=======
뉴스api 사이트


# ERD
![ERD](/ERD.png)

# 기능
ㅇ

# 개발환경
asgiref==3.8.1
Django==4.2
django-seed==0.3.1
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
Faker==28.4.1
pillow==10.4.0
psycopg2==2.9.9
PyJWT==2.9.0
python-dateutil==2.9.0.post0
six==1.16.0
sqlparse==0.5.1
toposort==1.10
typing_extensions==4.12.2
tzdata==2024.1
>>>>>>> aeb25bdcc570298f15345727fb401735fef7b52f
