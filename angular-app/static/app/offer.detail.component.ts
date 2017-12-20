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
  id: number;
 
  public messageForm = this.fb.group({
    message: ["", Validators.required]
  });

  constructor(private _service: AnnouncementService, private route: ActivatedRoute, public fb: FormBuilder) { }

  

  

  doSaveMessage(event) {
    
    
  }

  ngOnInit() {


      this.busy = this._service.getOffer(this.route.snapshot.params['offer_id']).subscribe(
        (data) => {
          this.offer = data;
          console.log(this.offer);
        }
      );       
        
        
       }  

}