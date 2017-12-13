##Data binding

Вначале нужно подгрузить модуль форм для аппликухи.

    import { FormsModule } from '@angular/forms';
    
    
    @NgModule({
      declarations: [
        ...
      ],
      imports: [
        ...
        ....
        FormsModule
      ],
      
Теперь в шаблоне.


    <ul>
      <li *ngFor="let i of items"> {{i.name}} </li>
    </ul>

    <input *ngFor="let i of items" [(ngModel)]="i.name" />


Связки в одну сторону 


    <input *ngFor="let i of items" (input)="i.name = $event.target.value" />
    
    <input *ngFor="let i of items"  [ngModel]="i.name" />
    
    
    