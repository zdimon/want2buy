import { Injectable } from '@angular/core'; 
import {Http, Response, Headers, RequestOptions} from '@angular/http';
import {Observable} from 'rxjs/Rx';
import 'rxjs/add/operator/map'; 
import { Announcement } from './models/announcement'

 
 @Injectable()
 export class AnnouncementService {  

    constructor (private http: Http) {}
     
    public getNewAnnoncements(): Observable<Announcement[]> { 
        return this.http
        .get('/api/new_announcement')
        .map((res:Response) => res.json())
        
    }
 
    public getActiveAnnoncements(): Observable<Announcement[]> { 
        return this.http
        .get('/api/announcement')
        .map((res:Response) => res.json())
        
    }
    
 } 