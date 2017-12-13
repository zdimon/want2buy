## Запрос авторизации с формы.

    ng generate component auth
    
Импортируем модуль для работы с формами.


    import { NgForm } from '@angular/forms';
    
    
Добавим шаблон с обработкой формы.


      selector: 'auth-form',
      template: `<form #signupForm="ngForm" (ngSubmit)="registerUser(signupForm)" class="navbar-form navbar-right" role="search">
                        <div class="form-group">
                            <input type="text" class="form-control" name="username" placeholder="Username" ngModel>
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" name="password" placeholder="Password" ngModel>
                        </div>
                        <button type="submit" class="btn btn-default">Sign In</button>
          </form>`,
    })
    
Создадим обработчик в который передадим объект формы.

  registerUser(form: NgForm){
    console.log(form.value);
  }
  
  
Добавим компонент в родительский шаблон.

    ...
    <auth-form></auth-form> 
    
## Делаем http запрос.


Импортируем провайдер в приложение.

    import { HttpModule } from '@angular/http';

      imports: [
        ...
        HttpModule
      ],
  
  
    import {Http, Response, Headers, RequestOptions} from '@angular/http';
    import {Observable} from 'rxjs/Rx';
    
get запрос
        
      registerUser(form: NgForm){
        console.log(form.value);
        let url = 'http://localhost/login';
        return this._http.get(url)
       .subscribe((res) => { 
          console.log(res);
       });
      }
      
post запрос
        
      registerUser(form: NgForm){
        console.log(form.value);

        var headers = new Headers();
        headers.append('Content-Type', 'json-content-type');

        let url = 'http://localhost/login';
        var body = JSON.stringify(form.value);
        return this._http.post(url,body,{ headers: headers, method: "post" })
        .subscribe((res) => { 
          console.log(res);
       });
      }
    
