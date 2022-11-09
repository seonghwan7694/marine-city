# django_flow

MVT 디자인 패턴의 장고 프로젝트 구조입니다. 어드민 계정의 아이디는 admin, 비밀번호는 qwert1234입니다.
```python
.
├── base # django-admin startapp base 를 쳐서 생성한 앱
│   ├── admin.py # http://127.0.0.1:8000/admin/ 을 쳤을 때, 나오는 레이아웃
│   ├── apps.py # 한 개의 장고 프로젝트는 여러 개의 앱을 포함함. 
│   ├── form.py # models.py에서 모델을 정의했고, 그것에 대한 form을 만들기 위한 파일.
│   ├── __init__.py
│   ├── migrations # python manage.py makemigrations 과 python manage.py migrate 을 했을 때
│   │   ├── 0001_initial.py # 앞서 언급한 두 명령어를 실행했을 때, 커밋기록 마냥 생성됨.
│   │   └── __init__.py
│   ├── models.py # 매우 중요. 클래스를 선언함으로서 데이터베이스의 테이블을 쉽게 만들 수 있음.
│   ├── __pycache__ # 손댈 일이 없는 디렉터리.
│   ├── templates # HTML 파일을 보관하는 디렉터리. 디렉터리 구조에 제약이 존재함.  
│   │   └── base
│   │       ├── container_delete.html
│   │       ├── container_form.html
│   │       ├── container.html
│   │       └── home.html
│   ├── tests.py # 손댈 일이 없는 파일
│   ├── urls.py # 매우 중요.
│   └── views.py # 매우 중요.
├── db.sqlite3 # 손댈 일이 없는 파일. 'sqlite3 viewer'를 설치하면 파일을 열 수 있음.
├── conf # django-admin startproject conf . 을 쳐서 생성한 장고 프로젝트. 따라서, 앱은 아님.
│   ├── asgi.py 
│   ├── __init__.py
│   ├── settings.py # 중요. 장고 프로젝트 설정 파일. 왠만한건 전부 설정해두었음.
│   ├── urls.py # 매우 중요.
│   └── wsgi.py
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── static # 정적 파일을 보관하는 디렉터리. 디렉터리 구조에 제약이 존재함.
│   ├── css
│   │   └── main.css
│   ├── images
│   │   ├── avatar.svg
│   │   ├── box.svg
│   │   ├── goods
│   │   └── world_map.svg
│   └── js
│       └── main.js
└── templates # HTML 파일을 보관하는 디렉터리.
    ├── main.html
    └── nav_bar.html
```