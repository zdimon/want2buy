import { Component } from '@angular/core';
import {Subscription} from 'rxjs';



@Component({
  templateUrl: '/static/templates/announcement/offer_list.html'
})
export class OfferListComponent {

  offers: any = [];
  pager = {};
  busy: Subscription;

  constructor() { }

  public goPage(page,limit){
    
  }


  ngOnInit() {

    this.offers =[ {
      'title': 'title',
      'thumbnail': '<img src="/static/images/noimage.png" />',
      'id': 12,
      'region': 'Киеваский',
      'city': 'Киев',
      'created_at': '2018-01-01',
      'price': 123
    }];
    
   }

}