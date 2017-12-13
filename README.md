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
    
### Ссылка на модули    
    
    zdimon@webmaster:~/storage1/www/want2buy/main/static$ ln -s ../../node_modules node_modules


    git clone git@github.com:zdimon/want2buy.git; cd want2buy; ./install    