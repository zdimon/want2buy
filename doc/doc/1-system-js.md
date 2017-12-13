##SystemJS

### app.ts

    import { MyApp } from "./classapp";

    var app = new MyApp();
    app.go();

### mylib/classapp.ts

    class MyApp{
        
        constructor(){
        };
        
        go(){
            alert('GOOOO')
        };
        
    }

echo '{  "compilerOptions": { "module": "commonjs"  }  }' >> tsconfig.json
### !!!!If you specify input files, tsconfig.json is ignored.!!!!!


### index.html

    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>My first app</title>
      <script src="static/app.js"> </script>
    </head>
    <body>
      <h1> My first app </h1>
    </body>
    </html>    
    
    
**app.js:1 Uncaught ReferenceError: require is not defined**


We need to use SystemJS

    npm init
    npm install systemjs --save
    cd static
    ln -s ../node_modules lib
    
    
    <script src="static/lib/systemjs/dist/system.js"> </script>
    
    <script>
          SystemJS.config({})
          SystemJS.import('app.js').then(function(m){
          }, function(error){
             console.log(error);
          });
    </script>    
    
    
**http://localhost:8080/static/classapp 404 (File not found)**    


We need to explaine to SystemJS what the extension we want tot use.

      <script>
            SystemJS.config({

              packages: {
                '.': { defaultExtension: 'js' }
              }         
             
            })
            SystemJS.import('static/app').then(function(m){
            }, function(error){
               console.log(error);
            });
      </script>
      
      
## Jquery


    npm install jquery @types/jquery --save
    
    <script src="static/lib/jquery/dist/jquery.min.js"> </script>


    export class MyApp{

        app: any;

        constructor(){
            this.app = $('#myapp');
        };
        
        go(){
            this.app.html('App content');
            return true;
        };
        
    }

    
    
    
    
    
    
    
    
    
