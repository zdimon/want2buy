import { Component, OnInit, Input, Output } from '@angular/core';
import { Announcement } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/announcement_detail.html'
})
export class AnnouncementDetailComponent {
  
  announcement: any = {'offers':[], current_user: {}};
  current_offer: any = {user: {}};
  busy: Subscription;
  id: number;
  public messageForm = this.fb.group({
    message: ["", Validators.required],
    price: [""],
    file: [""]
  });

  constructor(private _service: AnnouncementService, private route: ActivatedRoute, public fb: FormBuilder) { }

  

  selectOffer(id){

    this.announcement.offers.forEach( (element) => {
      if(element.id==id){
        this.current_offer = element;
      }
    });
    
  }

  doSaveMessage(event) {
    //console.log(event);
    //console.log(this.messageForm.value);
    let obj_message = {
      'user': {
        'name': this.announcement.current_user.name,
        'price': this.messageForm.value.price,
        'thumbnail': '/static/images/nouser.png'
      },
      'message': this.messageForm.value.message,
      'created_at': '2018-01-01'
    };
    this.current_offer.messages.push(obj_message);
    this.messageForm.reset({
      'message': ''
    });

    this.busy = this._service.saveMessage(obj_message).subscribe(
      function (data) {
        console.log(data);
      }
    );

  }

  ngOnInit() {

    
        this.busy = this._service.getAnnoncement(this.route.snapshot.params['announcement_id']).subscribe(
          (data) => {
            this.announcement = data; 
            console.log(this.announcement);

            if(parseInt(this.announcement.cnt_offers)>0){
              this.current_offer = this.announcement.offers[0];
              console.log(this.current_offer);
            } else {

            }

          }
    
        );
        
       }  

}