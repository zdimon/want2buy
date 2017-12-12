import { Component } from '@angular/core';
import {Http, Response, Headers, RequestOptions} from '@angular/http';
import {Observable} from 'rxjs/Rx';
import 'rxjs/add/operator/map';

@Component({
  template: `<h2>IndexComponent {{ announcement_id }} </h2>
    <ul>
    <li *ngFor="let u of users"> {{u.username}} </li>
  </ul>
  `
})
export class IndexComponent {

  users: any;

  constructor(private _http: Http) { }

  ngOnInit() {
    let url = 'http://localhost:8080/static/test/users.json';
    this._http
      .get(url)
      .map((res:Response) => res.json())
      .subscribe(
      (res)=> {
        console.log(res);
        this.users = res;
      }
    ) 

   }

}