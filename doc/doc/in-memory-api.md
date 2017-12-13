## In memory web API

Ставим

    npm install angular-in-memory-web-api --save
    
Описываем класс

    import { InMemoryDbService } from 'angular-in-memory-web-api';
    import { Http } from '@angular/http';
    import { Injectable } from '@angular/core';




    export class InMemCatalogService implements InMemoryDbService {
     createDb() {
       let categories = [
         { id: '1', name: 'Windstorm' },
         { id: '2', name: 'Bombasto' },
         { id: '3', name: 'Magneta' },
         { id: '4', name: 'Tornado' }
       ];
       return {categories};
     }
    }

Теперь доступны ссылки вида 'app/categories'


Подключаем в модуле

    @NgModule({
        imports: [
            ...
             InMemoryWebApiModule.forRoot(InMemCatalogService),
            ...
        ],
        
Делаем сервис.

    @Injectable()
    export class CatalogService {

        constructor(private http: Http) { }

        getCatalog(){
            return this.http.get('app/categories')
            .map(res => res.json()['data']);       
        }
    }

Используем в компоненте.


    ngOnInit() { 
        
            this.catalog.getCatalog().subscribe(data=>{
                this.cats = data
            });
                    
                
    }
    
    
