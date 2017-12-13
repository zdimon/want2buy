# Animation

Включаем анимацию в главном модуле.

    import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

Импортируем все нужное в компоненте.


    import {
      trigger,
      state,
      style,
      animate,
      transition
    } from '@angular/animations';


    animations: [
        trigger('cardState', [
          state('close', style({
            width: '0px',
            overflow: 'hidden'
          })),
          state('open',   style({
            width: '*',
            overflow: 'hidden'
          })),
          transition('* => *', animate('1s  ease-in-out')),
        ])
      ]
      
      
Шаблон.
      
       <div class="card back" *ngIf="card.isHidden" [@cardState]="status_cover">*</div>
