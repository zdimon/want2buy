import { Component, OnInit, Input, Output } from '@angular/core';
import { Announcement } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/offer_detail.html'
})
export class OfferDetailComponent {
  
  offer: any = {};
  busy: Subscription;
 
  public messageForm = this.fb.group({
    message: ["", Validators.required]
  });

  constructor(private _service: AnnouncementService, private route: ActivatedRoute, public fb: FormBuilder) { }

  

  

  doSaveMessage(event) {
    
    
  }

  ngOnInit() {

    
        
        
       }  

}