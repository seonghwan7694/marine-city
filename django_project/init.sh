#!/bin/bash

# db를 초기화 시켜주고, id : admin 과 pwd : qwert1234인 어드민 계정을 생성하고, 로컬서버를 자동으로 열어주는 쉘 스크립트입니다.

rm -rf base/migrations/*
touch base/migrations/__init__.py
rm -rf db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'qwert1234')" | python manage.py shell
python manage.py runserver