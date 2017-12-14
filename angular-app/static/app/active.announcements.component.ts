import { Component } from '@angular/core';
import { AnnouncementService } from './service.module'
import { AnnouncementPager } from './models/announcement'

@Component({
  templateUrl: '/static/templates/announcement/active_announcement_list.html'
})
export class ActiveAnnouncementsComponent {

  announcements: {};
  pager = {};

  constructor(private _service: AnnouncementService) { }

  public goPage(page,limit){
    let offset = limit*page;
    this._service.getActiveAnnoncementsPage(limit, offset).subscribe(
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