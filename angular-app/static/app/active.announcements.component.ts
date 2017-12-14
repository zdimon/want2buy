import { Component } from '@angular/core';
import { AnnouncementService } from './service.module'
import { AnnouncementPager } from './models/announcement'
import {Subscription} from 'rxjs';



@Component({
  templateUrl: '/static/templates/announcement/active_announcement_list.html'
})
export class ActiveAnnouncementsComponent {

  announcements: {};
  pager = {};
  busy: Subscription;

  constructor(private _service: AnnouncementService) { }

  public goPage(page,limit){
    let offset = limit*page;
    this.busy = this._service.getActiveAnnoncementsPage(limit, offset).subscribe(
      (data) => {
        this.announcements = data.results;
        this.pager = {
          'offset': data.offset,
          'count': data.count,
          'limit': data.limit,
          'has_prev': data.has_prev,
          'has_next': data.has_next,
          'current': data.current
        }

      }

    );
  }


  ngOnInit() {

    this._service.getActiveAnnoncements().subscribe(
      (data) => {
        this.announcements = data.results;
        this.pager = {
          'offset': data.offset,
          'count': data.count,
          'limit': data.limit,
          'has_prev': data.has_prev,
          'has_next': data.has_next,
          'current': data.current
        }

      }

    );
    
   }

}