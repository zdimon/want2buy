import { IndexComponent } from './index.component';
import { EditAnnouncementComponent } from './edit.announcement.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component'
import { AppRoutingModule } from './router.module';
import { HttpModule } from '@angular/http';
import { AnnouncementService } from './service.module'
import { ActiveAnnouncementsComponent } from './active.announcements.component'
import {BusyModule, BusyConfig} from 'angular2-busy';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'
import { AnnouncementDetailComponent } from './announcement.detail.component'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
declarations: [
  /// here we need to add every new component
  AppComponent,
  EditAnnouncementComponent,
  IndexComponent,
  AnnouncementDetailComponent,
  ActiveAnnouncementsComponent
],
imports: [ 
  BrowserModule, 
  AppRoutingModule, 
  HttpModule, 
  FormsModule,
  ReactiveFormsModule,
  BusyModule.forRoot(
    new BusyConfig({
        message: 'Подождите идет загрузка...',
          backdrop: false,
          //template: '<div>{{message}}</div>',
          //delay: 0,
          minDuration: 600
          //wrapperClass: 'my-class'
      })
  ),
  BrowserAnimationsModule 
],
providers: [ AnnouncementService ],
bootstrap: [AppComponent]
})
export class AppModule { }