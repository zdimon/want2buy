## HTTP запросы

###HttpClient

https://angular.io/guide/http


*HttpClientModule is for Angular 4.3.0 and above.*

    import {HttpClientModule} from '@angular/common/http';
        
    @NgModule({
      imports: [
        BrowserModule,
        // Include it under 'imports' in your application module
        // after BrowserModule.
        HttpClientModule,
      ],
    })
    
##HttpModule   

https://angular.io/tutorial/toh-pt6
    
    import {HttpModule} from '@angular/http';
    
    constructor(private http: Http) { }

    ngOnInit() { 
        
            this.http.get('assets/catalog.json')
            .map(res => res.json())
            .subscribe(data=>{
                this.cats = data
                console.log(data)
            })
                    
                
    }
    
###Выносим в сервис.

    import { Http } from '@angular/http';
    import { Injectable } from '@angular/core';

    @Injectable()
    export class CatalogService {

        constructor(private http: Http) { }

        getCatalog(){
            return this.http.get('assets/catalog.json')
            .map(res => res.json());       
        }
    }    
   
Подключаем в модуле.

    
    import { CatalogService }     from './catalog.service';
        
        
    @NgModule({
        imports: [ HttpModule ],
        providers: [CatalogService],   
        ...
        
        
Используем в компоненте.

   
    import { CatalogService } from './catalog.service';

  
    export class CatalogNavComponent implements OnInit {
        cats: any
        constructor(private catalog: CatalogService) { }

        ngOnInit() { 
            
                this.catalog.getCatalog().subscribe(data=>{
                    this.cats = data
                 
                });
                        
                    
        }
    }        
          
          
Разворачиваем в шаблоне.

    <div class="card">
        <ul class="list-group">
            <li *ngFor="let c of cats" class="list-group-item active">{{ c.name }}</li>
        </ul>
    </div>  
    
предваридельно импортнув функционал браузенрых директив

    import { BrowserModule } from '@angular/platform-browser';

    @NgModule({
        imports: [
             HttpModule,
             BrowserModule
        ],
        ...
    })
    
### Обработка ошибок.



    ngOnInit() { 
        
            this.catalog.getCatalog().subscribe(data=>{
                this.cats = data
                console.log(data)
            }, err=>{
                this.logError(err)
            });
                    
                
    }

    logError(err: any){
        console.log(err);
    }
    
## Использование промисов

    import 'rxjs/add/operator/toPromise';


    @Injectable()
    export class CatalogService {

        constructor(private http: Http) { }

        getCatalog(){
            return this.http.get('app/categories').toPromise()
               
        }
    }
            
            
- компонент

    export class CatalogNavComponent implements OnInit {
        cats: any
        constructor(private catalog: CatalogService) { }

        ngOnInit() { 
            
                this.catalog.getCatalog().then(response=>{
                    this.cats = response.json().data
                }
                ).catch(this.logError);
                        
                    
        }

        logError(err: any){
            console.log(err);
        }
    }
            
### Использование колбэков

- сервис

    getCatalog(clb: any){
        return this.http.get('app/categories')
        .toPromise()
        .then(data=> {clb(data.json().data)})
        .catch(this.logError);
    
    }

    logError(err: any){
        console.log('Errorr');
        console.log(err);
    }
    
- компонент    
    
    export class CatalogNavComponent implements OnInit {
        cats: any
        constructor(private catalog: CatalogService) { }

        ngOnInit() { 
                this.catalog.getCatalog(data=>{
                    this.cats = data
                })         
        }
    }
      
      
      
      
### Комбинация колбека и Observer

- сервис 

    getCatalogSub(clb: any){
        return this.http.get('app/categories')
        .map(res => res.json().data)
        .subscribe(data=>{clb(data)}, err=>{this.logError(err)})   
    }
    
- компонент


    ngOnInit() { 
            this.catalog.getCatalogSub(data=>{
                this.cats = data
            })         
    }
        
      
            
