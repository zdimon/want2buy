import { IndexComponent } from './index.component';
import { EditAnnouncementComponent } from './edit.announcement.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component'
import { AppRoutingModule } from './router.module';
import { HttpModule } from '@angular/http';
import { NewAnnouncementTableComponent } from './new.announcement.table.component'
import { AnnouncementService } from './service.module'
import { ActiveAnnouncementsComponent } from './active.announcements.component'

@NgModule({
declarations: [
  /// here we need to add every new component
  AppComponent,
  EditAnnouncementComponent,
  IndexComponent,
  NewAnnouncementTableComponent,
  ActiveAnnouncementsComponent
],
imports: [ BrowserModule, AppRoutingModule, HttpModule ],
providers: [ AnnouncementService ],
bootstrap: [AppComponent]
})
export class AppModule { }