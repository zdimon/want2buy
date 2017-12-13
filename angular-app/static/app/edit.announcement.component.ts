import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';


@Component({
  template: `
  
  <div class="row">
    <div class="col-md-12">
           
    </div>
  </div>
  `
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