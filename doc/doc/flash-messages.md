# Flash messages.

## Custom messages

    mkdir messages
    cd messages
    touch message.component.ts
    touch message.service.ts
    
Простой компонент.

    import { Component, OnInit } from '@angular/core';

    @Component({
        selector: 'mymessages',
        templateUrl: '<h1>{{ message }}</h1>'
    })

    export class NameComponent implements OnInit {
        message: string;
        constructor() { }

        ngOnInit() { 

            this.message = 'Hello!';

        }
    }

Подключим в главном модуле.

    import { MymessageComponent } from './messages/message.component';


    @NgModule({
      declarations: [
        ...
        MymessageComponent,
        ...

Вставим в шаблон.

    <mymessages></mymessages>
    
    
Создадим сервис.

    import { Injectable, EventEmitter } from '@angular/core';

    @Injectable()
    export class MymessageService {
        public evt: EventEmitter<string>;
        constructor() { 
            this.evt = new EventEmitter();
        }
        sendMessage(mes: string){
            this.evt.emit(mes);
        }


    }   
        
Подключим его  корневом модуле.

    import { MymessageService } from './messages/message.service';
    
    @NgModule({
      declarations: [
       ...
      ],
      imports: [
        ...
      ],
      providers: [
        ...
        MymessageService,
        ...
      ],  
        
Подпишемся на событие в компоненте.

    import { Component, OnInit } from '@angular/core';
    import { MymessageService } from './message.service';


    @Component({
        selector: 'mymessages',
        template: '<h1>{{ message }}</h1>'
    })

    export class MymessageComponent implements OnInit {
        message: string;
        constructor(private msgservice: MymessageService) { 
            this.message = '';
         }

        ngOnInit() { 

            this.msgservice.evt.subscribe(mes=>{
                this.message = mes;
              })
          

        }
    }
    
Инициируем событие в произвольном месте любого компонента.

    import { MymessageService } from './../messages/message.service';
                
    ...        
    constructor(private _mymess: MymessageService) { }     
    ...
    registerUser(form: NgForm){
        this._mymess.sendMessage('Test message');       
        
## Пакет angular2-flash-messages

    npm install angular2-flash-messages --save
    
Add to root module.

    import { FlashMessagesModule } from 'angular2-flash-messages';  


    @NgModule({
      declarations: [
        ...
      ],
      imports: [
        ...
        FlashMessagesModule
      ],
      
      
Using in the component or service.

    import { FlashMessagesService } from 'angular2-flash-messages';
    
   
    constructor(private _flashMessagesService: FlashMessagesService) { }


      registerUser(form: NgForm){
        this.Auth.Login(form.value).subscribe(data => {
          if(data.status == 0){
             this.user.is_auth = true;
             this.is_auth = true;
             this._flashMessagesService.show('Welcome!', { cssClass: 'alert-success', timeout: 10000 });

          } else {
            this._flashMessagesService.show('Login or password is incorrect!', { cssClass: 'alert-danger', timeout: 10000 });
          }
        }, err=>{
          this._flashMessagesService.show(`Service is temporary unvailable! ${err}`, { cssClass: 'alert-danger', timeout: 10000 });
        });
      }
      
      
## Toastr service.


    npm install toastr --save
      
      "styles": [
        "styles.css",
        "../node_modules/toastr/build/toastr.min.css"
      ],      
      "scripts": [
        "../myfunc.js",
        "../node_modules/jquery/dist/jquery.min.js",
        "../node_modules/toastr/build/toastr.min.js"
      ],      
      
   
Создаем сервис.

    import { Injectable } from '@angular/core';

    declare let toastr: any;

    @Injectable()
    export class ToastrService {

        constructor() { }

        alert(mess: string, title: string){
            toastr.success(mess, title)
        }

    }

Добавляем в главный модуль.      
              
              
    import { ToastrService } from './toastr.service';

     
    @NgModule({
      declarations: [
        AppComponent,
        GameComponent,
        CardComponent,
        RemoveQuotes
      ],
      imports: [
        BrowserModule
      ],
      providers: [
        CardService,
        ToastrService,
        JQUERY_PROVIDER
      ],          
          
          
Используем.

    import { ToastrService } from '../toastr.service';        
    
    constructor(private toastr: ToastrService) { }

    ngOnInit() {  
       this.toastr.alert('Hello','everybody');
    } 
          
          
*** дз ***          
добавить таймаут

    alert(mess: string, title: string){
        toastr.success(mess, title, {'timeOut': 2000})
    }

          
          
          
