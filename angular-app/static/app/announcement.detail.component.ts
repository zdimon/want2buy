import { Component, OnInit, Input, Output } from '@angular/core';
import { Announcement } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';

declare var $: any;

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
    new_price: [""],
    offer_id: [""],
    file: [""]
  });

  constructor(private _service: AnnouncementService, private route: ActivatedRoute, public fb: FormBuilder) { 

   
  }

  

  selectOffer(id){

    this.announcement.offers.forEach( (element) => {
      if(element.id==id){
        this.current_offer = element;
        this.messageForm.controls.offer_id.setValue(id);
      }
    });
    
  }

  scrollMessages(){

    var box = $('#announcement_block').find('#comments');
    var h = box[0].scrollHeight + 400;
    //alert(h);

    //box.scrollTop( 20000000 );  

  }

  doSaveMessage(event) {
    console.log(this.announcement.current_user);
    //console.log(this.messageForm.value);
    let obj_message = {
      'user': {
        'name': this.announcement.current_user.name,
        'thumbnail': this.announcement.current_user.thumbnail,
      },
      'new_price': this.messageForm.value.new_price,
      'offer_id': this.messageForm.value.offer_id,
      'message': this.messageForm.value.message,
      'created_at': '2018-01-01'
    };
    this.current_offer.messages.push(obj_message);
    this.messageForm.reset({
      'message': '',
      'offer_id': this.messageForm.value.offer_id
    });

    this.scrollMessages();


    this._service.saveMessage(obj_message).subscribe(
      function (data) {
        console.log($('#announcement_block').find('#comments'));

      


      }
    );

  }

  ngOnInit() {

    
        this.busy = this._service.getAnnoncement(this.route.snapshot.params['announcement_id']).subscribe(
          (data) => {
            this.announcement = data; 
            setTimeout(this.scrollMessages(),1000);
            
            if(parseInt(this.announcement.cnt_offers)>0){
              this.current_offer = this.announcement.offers[0];
              this.messageForm.controls.offer_id.setValue(this.announcement.offers[0].id);

            } else {

            }

          }
    
        );
        
       }  

}