import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';


@Component({
  template: '<h2>EditAnnouncementComponent {{ announcement_id }} </h2>'
})
export class EditAnnouncementComponent {

  announcement_id: string;

  constructor(private route: ActivatedRoute) { 
    
          }

  ngOnInit() {
    
            this.route.params.subscribe(
              params => this.announcement_id = params['announcement_id']
            )
    
          }

}