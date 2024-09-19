# spartanews


## 1. 프로젝트 소개
DRF를 통해 뉴스목록 보여주는 api를 만드는 프로젝트

## 2. 팀 소개
김경민(팀장), 강다영, 김나희, 조민희

 [🍭팀노션 이동](https://www.notion.so/teamsparta/1e2a365b56ad4cf8acd68bff9c3c59c8/)

## 3. 개발기간
- 2024.09.12.(목) ~ 2024.09.18.(수)

## 4. 주요기능
- **유저기능 관련:**
  <details>
   <summary>회원가입</summary>
  username, password, email 등을 입력해 회원가입을 요청하고, 입력한 email로 호스트의 인증메일을 받으면 가입이 처리된다.
  </details>
  <details>
  <summary>로그인&로그아웃</summary>
  </details>
  <details>
  <summary>회원탈퇴</summary>
  </details>
  <details>
  <summary>마이페이지</summary>
  </details>
  <details>
  <summary>다른 사용자 구독</summary>
  </details>
  <details>
  <summary>비밀번호 재설정</summary>
 </details>   

&nbsp;

- **게시기능 관련:**
  - 전체글 목록 보기
  - 글 작성
  - 글 수정/삭제
  - 글 좋아요하기
  - 댓글 작성
  - 댓글 삭제
  - 댓글 좋아요하기
  - 글 검색
  - 글 번역 (LLM)
  - 글 요약 (LLM)

&nbsp;

## 5. 개발환경
<details>

- aiohappyeyeballs==2.4.0
- aiohttp==3.10.5
- aiosignal==1.3.1
- annotated-types==0.7.0
- anyio==4.4.0
- asgiref==3.8.1
- async-timeout==4.0.3
- attrs==24.2.0
- blinker==1.8.2
- certifi==2024.7.4
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- distro==1.9.0
- Django==4.2
- django-seed==0.3.1
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- exceptiongroup==1.2.2
- Faker==28.0.0
- Flask==3.0.3
- frozenlist==1.4.1
- greenlet==3.1.0
- h11==0.14.0
- httpcore==1.0.5
- httpx==0.27.2
- idna==3.8
- itsdangerous==2.2.0
- Jinja2==3.1.4
- jiter==0.5.0
- jsonpatch==1.33
- jsonpointer==3.0.0
- langchain==0.3.0
- langchain-core==0.3.0
- langchain-openai==0.2.0
- langchain-text-splitters==0.3.0
- langsmith==0.1.120
- MarkupSafe==2.1.5
- multidict==6.1.0
- numpy==1.26.4
- openai==1.45.0
- orjson==3.10.7
- packaging==24.1
 </details>

## 6. 시작하기

   <details>

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
</details>


## 7. ERD
![ERD](/ERD.png)
&nbsp;
&nbsp;
&nbsp;
&nbsp;


## 8. API명세
![api명세25](https://github.com/user-attachments/assets/0c36ab25-9aa9-49dc-9169-1e784178b3c6)

## 9. 와이어프레임
------


## 10. 프로젝트 파일 구조

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
│  ├─ utils.py
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

## 11. 역할분담 
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
  + PPT제작 & 영상제작 & 발표 - 김경민

&nbsp;

## 12. Trouble Shooting
----------------------------


