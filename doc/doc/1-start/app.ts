import { NgModule } from '@angular/core';
import { Component } from "@angular/core";
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { BrowserModule } from '@angular/platform-browser';

@Component({
    selector: 'hello-angular',
    template: '<h1>{{ title }}</h1>'
})

class HelloAngular{
    title: string;
    constructor(){
        this.title = 'Hello bro!!'
    }
} 

@NgModule({
  declarations: [
    HelloAngular
  ],
  imports: [ BrowserModule ],
  providers: [],
  bootstrap: [HelloAngular]
})
export class AppModule { }


platformBrowserDynamic().bootstrapModule(AppModule);