import { Component, OnInit, Input, Output, ElementRef, ViewChild } from '@angular/core';
import { Announcement, Test } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';
import { ChangeDetectorRef } from '@angular/core';
import { FileUploader, FileSelectDirective  } from 'ng2-file-upload';

//console.log(FileUploader);

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
  public uploader:FileUploader = new FileUploader({
    url: 'api/announcement/file/upload/'
  });


 
  

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

  acceptOffer(offer_id) {
    if(confirm("Вы уверены что вы хотите предать ваши контактные данные продавцу?")) {
      this.busy = this._service.acceptOffer(offer_id).subscribe(
          (data) => {
            console.log (data); 
          }
        );
      }
  };

  deniteOffer(offer_id) {

  };
  


  setCurrentOffer(id){

    this.announcement.offers.forEach( (element,index) => {
      if(element.id==id){
        this.announcement.offers[index].status = 'active';
        this.current_offer = element;
        this.messageForm.controls.offer_id.setValue(id);
        this.uploader.setOptions({url: 'api/announcement/file/upload/'+id});
        this.uploader.onCompleteItem = (item, response, status, header) => {
          if (status === 200) {
            console.log(response);
            let res_json = JSON.parse(response);
            let obj_message = {
              'user': {
                'name': res_json.name,
                'thumbnail': res_json.thumbnail,
              },
              'offer_id': res_json.offer_id,
              'file': res_json.file,
              'created_at': '2018-01-01'
            };
            this.current_offer.messages.push(obj_message);

          }  
        }
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