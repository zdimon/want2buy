import { Component, OnInit, Input, Output } from '@angular/core';
import { Announcement } from './models/announcement'

@Component({
  selector: 'announcement',
  templateUrl: '/static/templates/announcement/new_announcement_list.html'
})
export class NewAnnouncementTableComponent {
  @Input() announcements: Announcement[];
}