#!/usr/bin/env bash

time3=$(date "+%Y-%m-%d_%H_%M")
name="release"_$time3.tar.gz
function updata() {
  rm -rf /Users/xj/deploy/python/*
    tar -czvf $name --exclude=./venv *
    mv $name /Users/xj/deploy/python
}


function deploy() {
    docker exec -it BBS ps -ax|grep 'python'|grep 'manage.py'|awk '{print $1}'|xargs kill -9
    docker exec -it BBS ps -ax|grep 'python'|grep 'manage.py'|awk '{print $1}'|xargs kill -9
    docker exec -it BBS rm -rf /app/*
    docker exec -it BBS tar -xzvf /app/$name -C /app/
#    docker exec -it BBS python /app/manage.py makemigrations
#    docker exec -it BBS python /app/manage.py migrate
#    docker exec -it BBS python manage.py runserver 0.0.0.0:8000

#    docker exec -it bbs pip install -r /app

}

updata
deploy