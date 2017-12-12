import { NgModule } from '@angular/core';
import { RouterModule, Routes }  from '@angular/router';
import { EditAnnouncementComponent } from './edit.announcement.component'
import { IndexComponent } from './index.component'

const routes: Routes = [
  { path: '', redirectTo: 'index', pathMatch: 'full' },
  { path: 'edit/announcement/:announcement_id', component: EditAnnouncementComponent },
  { path: 'index', component: IndexComponent }
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