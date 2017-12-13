## Потоки данных

Template

    <profile-block [profile]="profile1"></profile-block>

    <profile-block *ngFor="let profile of profile_list" [profile]="profile"></profile-block>

Родительский компонент.

    
    
    export class SandboxComponent implements OnInit {
      
      profile1 = {name: 'Dimon'}

      profile_list = [{name: 'Dimon'},{name: 'Petro'}]
      
  
Дочерний компонент.

  
  
    import { Component, OnInit, Input, Output } from '@angular/core';

    @Component({
      selector: 'profile-block',
      template: '<h1> Profile {{ profile.name }}</h1>',
    })
    export class ProfileComponent{
      @Input() profile: any;

    }
      
      
## Output

Добавим кнопку с событием в шаблон дочернего компонента. 


      template: `<h1> Profile {{ profile.name }}</h1>
        <button (click)="DeleteMe()"> Delete </button>
      `,
  
Импортируем диспечер событий.

    import { ... EventEmitter }
    
Создадим его экземпляр с экспортом в родительский компонент.

    @Output() eventClick = new EventEmitter();
    
Добавим обрабочик  DeleteMe в котором запустим событие с передачей в него обьекта профиля.


  DeleteMe() {

    this.eventClick.emit(this.profile);

  }
  
  
Теперь можно в шаблоне родителя использовать конструкцию () для выуживания события и передачи данных из него внутрь компонента.


    <profile-block *ngFor="let profile of profile_list" [profile]="profile" (eventClick) = "handleEvent($event)"></profile-block>


Добавим обработчик handleEvent в котором удалим обьект из массива.


      profile_list = [{id: 1, name: 'Dimon'},{id: 2, name: 'Petro'}]

      ...

      handleEvent(evt){
        for (let p of this.profile_list){
          if (p.id == evt.id) {
              this.profile_list.splice(this.profile_list.indexOf(p), 1);
          } 
        }
      }
  
  
    