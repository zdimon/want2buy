import { Component, OnInit, Input, Output } from '@angular/core';
import { Announcement } from './models/announcement'
import { AnnouncementService } from './service.module'
import {Subscription} from 'rxjs';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/offer_detail.html'
})
export class OfferDetailComponent {
  
  offer: any = {};
  offers: any = {};
  busy: Subscription;
  id: number;
 
  public messageForm = this.fb.group({
    message: ["", Validators.required]
  });

  constructor(private _route: Router, private _service: AnnouncementService, private route: ActivatedRoute, public fb: FormBuilder) { }

  
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
      }
    );    
    
   
    
  }
  

  doSaveMessage(event) {
    
    
  }

  ngOnInit() {


      this.busy = this._service.getOffer(this.route.snapshot.params['offer_id']).subscribe(
        (data) => {
          this.offer = data;
        }
      );    
      

      this._service.setCurrentOffer(this.route.snapshot.params['offer_id']).subscribe(
        (data) => {
          console.log(data);
        }
      );      
      
      this.busy = this._service.getOfferPage(10, 0).subscribe(
        (data) => {
          this.offers = data;
          console.log(this.offers);
        }
      ); 

        
        
       }  

}