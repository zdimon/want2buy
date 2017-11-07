# Хочу купить.

## Деплой проекта.


Окружение

    virtualenv want2buy_ve
    cd want2buy
    . ./bin/activate
   
Клонирование   
   
    git clone git@github.com:zdimon/want2buy.git
    
Установка зависимостей джанги и базы.

    cd want2buy
    pip install -r requirements.txt
    ./manage.py migrate
    
    
Установка статических зависимостей.

    npm install
    
    
    
