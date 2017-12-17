import { Component, OnInit, Input, Output } from '@angular/core';
import { Announcement } from './models/announcement'

@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/announcement_detail.html'
})
export class AnnouncementDetailComponent {
  @Input() announcements: Announcement[];
}