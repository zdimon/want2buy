import { Component, OnInit, Input, Output } from '@angular/core';
import { Announcement } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/announcement_detail.html'
})
export class AnnouncementDetailComponent {
  
  announcement: any;
  busy: Subscription;
  id: number;

  constructor(private _service: AnnouncementService, private route: ActivatedRoute) { }

  ngOnInit() {

    
        this.busy = this._service.getAnnoncement(this.route.snapshot.params['announcement_id']).subscribe(
          (data) => {
            this.announcement = data; 
            console.log(this.announcement);
          }
    
        );
        
       }  

}