import { NgModule } from '@angular/core';
import { RouterModule, Routes }  from '@angular/router';
import { EditAnnouncementComponent } from './edit.announcement.component'
import { AnnouncementDetailComponent } from './announcement.detail.component'
import { IndexComponent } from './index.component'
import { ActiveAnnouncementsComponent } from './active.announcements.component'
import { OfferListComponent } from './offer.list.component'; 
import { OfferDetailComponent } from './offer.detail.component';
import { UserDetailComponent } from './user.detail.component'

const routes: Routes = [
  { path: '', redirectTo: 'announcements', pathMatch: 'full' }, 
  { path: 'edit/announcement/:announcement_id', component: EditAnnouncementComponent },
  { path: 'announcement/detail/:announcement_id', component: AnnouncementDetailComponent },
  { path: 'index', component: IndexComponent },
  { path: 'announcements', component: ActiveAnnouncementsComponent },
  { path: 'offer/list', component: OfferListComponent },
  { path: 'offer/detail/:offer_id', component: OfferDetailComponent },
  { path: 'user/detail/:user_id', component: UserDetailComponent },


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