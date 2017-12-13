## Routing

##Компонент Page

    ng generate component page
    
   
    import { Component, OnInit } from '@angular/core';
    import { ActivatedRoute } from '@angular/router';

    @Component({
      selector: 'app-page',
      templateUrl: './page.component.html',
      styleUrls: ['./page.component.css']
    })
    export class PageComponent implements OnInit {
    
      template: string;
      
      constructor(private route: ActivatedRoute) { 

      }

      ngOnInit() {

        this.route.params.subscribe(
          params => this.template = params['name']
        )

      }

    }
    
Вставляем директиву для вывода выхлопа от роутинга.  
    
 
    <router-outlet></router-outlet>  

    ng generate module router
    
Или создать руками в app/
    
    
    ///router.module.ts
      
    import { NgModule } from '@angular/core';
    import { RouterModule, Routes }  from '@angular/router';
    import { PageComponent } from './page/page.component';

    const routes: Routes = [
      { path: '', redirectTo: '/page/index', pathMatch: 'full' },
      { path: 'page/:name', component: PageComponent }
    ];

    @NgModule({
      imports: [
        RouterModule.forRoot(routes)
      ],
      exports: [
        RouterModule
      ]

    })
    export class AppRoutingModule { }
    
Используем в главном модуле app.module.ts.


    import { BrowserModule } from '@angular/platform-browser';
    import { NgModule } from '@angular/core';
    import { AppComponent } from './app.component';
    import { PageComponent } from './page/page.component';
    import { AppRoutingModule } from './router.module';




    @NgModule({
      declarations: [
        AppComponent,
        PageComponent
      ],
      imports: [
        BrowserModule,
        AppRoutingModule
      ],
      providers: [],
      bootstrap: [AppComponent]
    })
    export class AppModule { }


