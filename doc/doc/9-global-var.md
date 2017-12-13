#Global variable

###global.ts    

    export const SERVER_URL = 'http://localhost:8080'
    
    
###Imploing

    
        
    import { SERVER_URL } from './global';

    @Injectable()
    export class AuthService {

      headers = new Headers(); 
      
      url = `${SERVER_URL}/login`;    
      
      ...
      
## Class.

    export class User {
        is_auth: boolean = false 
        permissions = {
            "admin": false
        } 
    }
    
    
    import { User } from '../global'
    
    ...
    constructor(private Auth: AuthService,private user: User) { }
    
    ...
