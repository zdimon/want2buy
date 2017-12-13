## Каркас

Создадим каталог для модуля

    mkdir catalog
    
Создадим файлы.
    
    
- модуль
    
    touch catalog.module.ts
    
- корневой компонент

    touch catalog.main.component.ts
  
- форма поиска

    touch catalog.search.component.ts
    
- навигация

    touch catalog.nav.component.ts
  
- список элементов

    touch catalog.list.component.ts
    
- элемент

    touch catalog.item.component.ts
    

Главный модуль.

    import { NgModule } from '@angular/core';

    import { CatalogMainComponent } from './catalog.main.component';

    @NgModule({
        imports: [ ],
        declarations: [ CatalogMainComponent ],
    })
    export class CatalogModule{ }
    
    
    
Главный компонент catalog.main.component.ts.
    
    
        
    import { Component, OnInit } from '@angular/core';

    @Component({
        selector: 'catalog-module',
        templateUrl: 'index.html'
    })
    export class CatalogMainComponent implements OnInit {

        constructor() { }

        ngOnInit() { 

        }

    }    
       
- включим в модуль приложения (app.module)       
       
       
    import { CatalogModule } from './catalog/catalog.module'
    
    ...       

    @NgModule({
      ...
      imports: [
        ...
        CatalogModule
      ],       
           
       
- включим в роутинг

    { path: 'catalog', component: CatalogMainComponent },
        
        
- поставим ссылку


      <li class="nav-item">
        <a class="nav-link" routerLink="/catalog">Catalog</a>
      </li>
      
- базовая разметка


<h1> Catalog </h1>


<div class="container">

        <div class="row">

            <div class="col-md-3">
                <div class="form-group">
                  <label for="">Search</label>
                  <input type="text" class="form-control">
                </div>            

                <div class="card">
                    <ul class="list-group">
                        <li class="list-group-item active">Active item</li>
                        <li class="list-group-item">Item</li>
                        <li class="list-group-item disabled">Disabled item</li>
                    </ul>
                </div>
            </div>

            <div class="col-md-9">
                   <table class="table">
                       <thead>
                           <tr>
                               <th>#</th>
                               <th>Name</th>
                               <th>Action</th>
                           </tr>
                       </thead>
                       <tbody>
                           <tr>
                               <td scope="row">1</td>
                               <td>One</td>
                               <td><a name="" id="" class="btn btn-primary" href="#" role="button">Show</a></td>
                           </tr>
                           <tr>
                               <td scope="row">2</td>
                               <td>Two</td>
                               <td><a name="" id="" class="btn btn-primary" href="#" role="button">Show</a></td>
                           </tr>
                       </tbody>
                   </table>
            </div>

        </div>
        
</div>


- поиск (catalog.search.component)

    import { Component, OnInit } from '@angular/core';

    @Component({
        selector: 'catalog-search',
        templateUrl: 'tpl/search.html'
    })

    export class CatalogSearchComponent implements OnInit {
        constructor() { }

        ngOnInit() { }
    }

- включаем его в модуль каталога.

    ...
    import { CatalogSearchComponent } from './catalog.search.component';

    @NgModule({
        imports: [ ],
        declarations: [ 
            CatalogMainComponent,
            CatalogSearchComponent 
        ],
    })
    ...  
    
- навигация

    import { Component, OnInit } from '@angular/core';

    @Component({
        selector: 'catalog-nav',
        templateUrl: 'tpl/nav.html'
    })

    export class CatalogNavComponent implements OnInit {
        constructor() { }

        ngOnInit() { }
    }    
        
    
- список

    import { Component, OnInit } from '@angular/core';

    @Component({
        selector: 'catalog-list',
        templateUrl: 'tpl/list.html'
    })

    export class CatalogListComponent implements OnInit {
        constructor() { }

        ngOnInit() { }
    }
    
- главный шаблон


    <h1> Catalog </h1>

    <div class="container">
        <div class="row">
            <div class="col-md-3">
                <catalog-search></catalog-search>
                <catalog-nav></catalog-nav>
            </div>
            <div class="col-md-9">
                <catalog-list></catalog-list>
            </div>
        </div>
    </div>


    
    
    
