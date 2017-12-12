import { IndexComponent } from './index.component';
import { EditAnnouncementComponent } from './edit.announcement.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component'
import { AppRoutingModule } from './router.module';
import { HttpModule } from '@angular/http';


@NgModule({
declarations: [
  /// here we need to add every new component
  AppComponent,
  EditAnnouncementComponent,
  IndexComponent
],
imports: [ BrowserModule, AppRoutingModule, HttpModule ],
providers: [],
bootstrap: [AppComponent]
})
export class AppModule { }