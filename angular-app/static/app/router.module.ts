import { NgModule } from '@angular/core';
import { RouterModule, Routes }  from '@angular/router';
import { EditAnnouncementComponent } from './edit.announcement.component'
import { IndexComponent } from './index.component'
import { ActiveAnnouncementsComponent } from './active.announcements.component'

const routes: Routes = [
  { path: '', redirectTo: 'announcements', pathMatch: 'full' }, 
  { path: 'edit/announcement/:announcement_id', component: EditAnnouncementComponent },
  { path: 'index', component: IndexComponent },
  { path: 'announcements', component: ActiveAnnouncementsComponent }
];

@NgModule({
    imports: [
      RouterModule.forRoot(routes)
    ],
    exports: [
      RouterModule
    ]

  })
  export class AppRoutingModule { }