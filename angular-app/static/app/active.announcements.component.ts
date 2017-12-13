import { Component } from '@angular/core';
import { AnnouncementService } from './service.module'
import { Announcement } from './models/announcement'

@Component({
  templateUrl: '/static/templates/announcement/active_announcement_list.html'
})
export class ActiveAnnouncementsComponent {

  announcements: Announcement[];

  constructor(private _service: AnnouncementService) { }


  ngOnInit() {

    this._service.getActiveAnnoncements().subscribe(
      (data) => {
        this.announcements = data;
        console.log(this.announcements);
      }

    );
    
   }

}