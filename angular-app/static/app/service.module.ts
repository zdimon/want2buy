import { Injectable } from '@angular/core'; 
import {Http, Response, Headers, RequestOptions} from '@angular/http';
import {Observable} from 'rxjs/Rx';
import 'rxjs/add/operator/map'; 
import { Announcement, AnnouncementPager } from './models/announcement';

 
 @Injectable()
 export class AnnouncementService {  

    constructor (private http: Http) {}
     
    public getNewAnnoncements(): Observable<AnnouncementPager> { 
        return this.http
        .get('/api/new_announcement')
        .map((res:Response) => res.json())
        
    }

    public getActiveAnnoncementsPage(limit,offset): Observable<AnnouncementPager> { 
        
        return this.http
        .get('/api/announcement/?limit='+limit+'&offset='+offset)
        .map((res:Response) => res.json())
        
    }    
 
    public getActiveAnnoncements(): Observable<AnnouncementPager> { 
        
        return this.http
        .get('/api/announcement')
        .map((res:Response) => res.json())
        
    }

    public getAnnoncement(id): any { 
        
        return this.http
        .get('/api/announcement/detail/'+id)
        .map((res:Response) => res.json())
        
    }    

    public getUser(id): any { 
        
        return this.http
        .get('/api/user/detail/'+id)
        .map((res:Response) => res.json())
        
    }     

    public saveMessage(obj): any { 
        
        return this.http
        .post('/api/offer/save/message/',obj)
        .map((res:Response) => res.json())
        
    }  
    
    
    public getOfferPage(limit,offset): Observable<AnnouncementPager> { 
        
        return this.http
        .get('/api/offer/?limit='+limit+'&offset='+offset)
        .map((res:Response) => res.json())
        
    }    
 
    public getOffer(id): any { 
        
        return this.http
        .get('/api/offer/detail/'+id)
        .map((res:Response) => res.json())
        
    }     


    public setCurrentOffer(id): any { 
        
        return this.http
        .get('/api/offer/'+id+'/set/current')
        .map((res:Response) => res.json())
        
    }  

    public setCurrentOfferInAnnouncement(announcement_id,offer_id): any { 
        
        return this.http
        .get('/api/announcement/'+announcement_id+'/offer/'+offer_id+'/set/current')
        .map((res:Response) => res.json())
        
    }     
    
 } 