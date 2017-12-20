import { Component } from '@angular/core';
import {Subscription} from 'rxjs';
import { AnnouncementService } from './service.module'


@Component({
  templateUrl: '/static/templates/announcement/offer_list.html'
})
export class OfferListComponent {

  offers: any = [];
  pager = {};
  busy: Subscription;

  constructor(private _service: AnnouncementService) { }

  public goPage(page,limit){
    
  }


  ngOnInit() {

    this.busy = this._service.getOfferPage(10, 0).subscribe(
      (data) => {
        this.offers = data;
        console.log(this.offers);
      }
    );    

    
    
   }

}