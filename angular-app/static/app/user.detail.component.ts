import { Component, OnInit, Input, Output } from '@angular/core';
import { Announcement } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/user_detail.html'
})
export class UserDetailComponent {
  
  user: any = {};
  busy: Subscription;

  constructor(private _service: AnnouncementService, private route: ActivatedRoute) { }

  

 
  ngOnInit() {

    
        this.busy = this._service.getUser(this.route.snapshot.params['user_id']).subscribe(
          (data) => {
            this.user = data; 
           
          }
    
        );
        
       }  

}