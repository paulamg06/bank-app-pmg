@echo off

cd .\frontend\
start cmd /k "npm run dev"

cd ..\backend\
start cmd "python manage.py migrate"
start cmd /k "python manage.py runserver 0.0.0.0:8000"

start "chrome" "http://localhost:5173/"