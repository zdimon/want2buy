import { Component } from '@angular/core';
import {Http, Response, Headers, RequestOptions} from '@angular/http';
import {Observable} from 'rxjs/Rx';
import 'rxjs/add/operator/map';
import { AnnouncementService } from './service.module'
import { Announcement } from './models/announcement'

@Component({
  templateUrl: '/static/templates/announcement/new_announcement_list.html'
})
export class IndexComponent {

  announcements: Announcement[];

  constructor(private _http: Http, private _service: AnnouncementService) { }

  public getActive(){
    console.log('get active');
  }

  ngOnInit() {

    this._service.getNewAnnoncements().subscribe(
      (data) => {
        this.announcements = data;
        console.log(this.announcements);
      }

    );
    
   }

}