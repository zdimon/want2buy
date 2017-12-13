import { Component } from '@angular/core';



@Component({
  selector: 'user-dashboard',
  templateUrl: '/static/templates/index.html'
})
export class AppComponent {


  public getActive($event){
    console.log('get activ ddddddd');
  }

  
}