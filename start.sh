ps -aux | grep 7777|xargs kill -9
nohup python manage.py runserver 0.0.0.0:7777 >djo.out 2>&1 &
