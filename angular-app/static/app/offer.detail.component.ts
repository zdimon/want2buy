import { Component, OnInit, Input, Output, ElementRef, ViewChild } from '@angular/core';
import { Announcement } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';
import { FileUploader, FileSelectDirective  } from 'ng2-file-upload';

@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/offer_detail.html'
})
export class OfferDetailComponent {
  
  @ViewChild('scrollMe') private myScrollContainer: ElementRef;

  offer: any = {};
  offers: any = {};
  busy: Subscription;
  id: number;
  public uploader:FileUploader = new FileUploader({
    url: 'api/announcement/file/upload/'
  });
 
  public messageForm = this.fb.group({
    message: ["", Validators.required],
    new_price: [""],
    offer_id: [""],
    file: [""]
  });

  constructor(private _route: Router, private _service: AnnouncementService, private route: ActivatedRoute, public fb: FormBuilder) { }

  
  ngAfterViewChecked() {
    this.scrollToBottom();
  }

  private scrollToBottom(): void {
    try {
        this.myScrollContainer.nativeElement.scrollTop = this.myScrollContainer.nativeElement.scrollHeight;
    } catch(err) { }
  }

  public goToPage(page,limit){
    let offset = limit*page;
    this.busy = this._service.getOfferPage(limit, offset).subscribe(
      (data) => {
        this.offers = data;
        console.log(this.offers);
      }
    ); 
  }


  selectOffer(id) {

    this.busy = this._service.getOffer(id).subscribe(
      (data) => {
        this.offer = data; 
        this._service.setCurrentOffer(id).subscribe();  
        this._route.navigate(['offer/detail/'+id]);
        this.messageForm.controls.offer_id.setValue(id);

        this.uploader.setOptions({url: 'api/announcement/file/upload/'+id});
        this.uploader.onCompleteItem = (item, response, status, header) => {
          if (status === 200) {
            let res_json = JSON.parse(response);
            console.log(res_json);
            let obj_message = {
              'user': {
                'name': res_json.name,
                'thumbnail': res_json.thumbnail,
              },
              'offer_id': res_json.offer_id,
              'file': res_json.file,
              'created_at': '2018-01-01'
            };
            this.offer.messages.push(obj_message);

          }  
        }


      }
    );    
    
   
    
  }
  

  doSaveMessage(event) {
    //console.log(this.announcement.current_user);
    console.log(this.offer);

    let obj_message = {
      'user': {
        'name': this.offer.user.name,
        'thumbnail': this.offer.user.thumbnail,
      },
      'new_price': this.messageForm.value.new_price,
      'offer_id': this.messageForm.value.offer_id,
      'message': this.messageForm.value.message
    };
    this.offer.messages.push(obj_message);
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

      this.selectOffer(this.route.snapshot.params['offer_id']);
     
      
      this.busy = this._service.getOfferPage(10, 0).subscribe(
        (data) => {
          this.offers = data;
          //console.log(this.offers);
        }
      ); 

        
        
       }  

}