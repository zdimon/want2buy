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

  announcements: any;
  pager: any;

  constructor(private _http: Http, private _service: AnnouncementService) { }


  ngOnInit() {

    this._service.getNewAnnoncements().subscribe(
      (data) => {
        this.announcements = data.results;
        this.pager = {
                      'offset': data.offset,
                      'count': data.count,
                      'limit': data.limit
        }
        console.log(this.pager);
      }

    );
    
   }

}