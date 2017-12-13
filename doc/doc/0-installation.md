##Установка

# npm

    sudo apt-get install npm

# nodejs 

    sudo apt-get install nodejs


# typescript

    npm install -g typescript

# инициализация

    npm init
    
# Доступ к системной директории.

    https://docs.npmjs.com/getting-started/fixing-npm-permissions    
    
    sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
    
#Установка

    npm install @angular/core @angular/common @angular/compiler --save

core - основные компоненты

common - фильтры директивы и пр.

compiler - компиляция HTML шаблонов

    npm install @angular/platform-browser @angular/platform-browser-dynamic  --save
    
platform-browser - взаимодействие с элементами DOM в контексте браузера

platform-browser-dynamic - инициализация приложения

    npm install es6-shim rxjs zone.js  --save
    
    
es6-shim - полифил для совместимости

rxjs - библиотека для создания асинхронных основанных на событиях программ, используемые отслеживаемые коллекции.

zone - полифилл для отслеживания изменений Ангуляра.

## Настройки tsconfig.ts

"experimentalDecorators": true - для декораторов ES7
"moduleResolution": "node" - для корректного поиска библиотек


