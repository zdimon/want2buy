import { Component, OnInit, Input, Output, ElementRef, ViewChild } from '@angular/core';
import { Announcement, Test } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';
import { ChangeDetectorRef } from '@angular/core';
import { FileUploader  } from 'ng2-file-upload';


declare var $: any;

@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/announcement_detail.html'
})
export class AnnouncementDetailComponent {
  
  @ViewChild('scrollMe') private myScrollContainer: ElementRef;

  announcement: any = {'offers':[], current_user: {}};
  current_offer: any = {user: {}};
  busy: Subscription;
  id: number;
  test: Test = new Test();
  public uploader:FileUploader = new FileUploader({url: 'announcement/file/upload'});

  

  public messageForm = this.fb.group({
    message: ["", Validators.required],
    new_price: [""],
    offer_id: [""],
    file: [""]
  });

  constructor(private _service: AnnouncementService, private route: ActivatedRoute, public fb: FormBuilder, private cdRef:ChangeDetectorRef) { 

   
  }

  ngAfterViewChecked() {
    this.scrollToBottom();
  }

  private scrollToBottom(): void {
    try {
        this.myScrollContainer.nativeElement.scrollTop = this.myScrollContainer.nativeElement.scrollHeight;
    } catch(err) { }
  }

  setCurrentOffer(id){

    this.announcement.offers.forEach( (element) => {
      if(element.id==id){
        this.current_offer = element;
        this.messageForm.controls.offer_id.setValue(id);
      }
    });

  }

  selectOffer(id){

    this.setCurrentOffer(id);
    this._service.setCurrentOfferInAnnouncement(this.announcement.id,id).subscribe(
      (data) => {
        console.log (data);
      }
    );
    
  }



  doSaveMessage(event) {
    //console.log(this.announcement.current_user);
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


    this._service.saveMessage(obj_message).subscribe(
      function (data) {
       

      }
    );

  }

  ngOnInit() {

    
        this.busy = this._service.getAnnoncement(this.route.snapshot.params['announcement_id']).subscribe(
          (data) => {
            this.announcement = data; 
           
            
            if(parseInt(this.announcement.cnt_offers)>0){
              this.setCurrentOffer(this.announcement.current_offer);
            } else {

            }

          }
    
        );
        
       }  

}