#Phaser

    npm install phaser --save
    
    
    
      "scripts": [
        "../node_modules/jquery/dist/jquery.min.js",
        "../node_modules/phaser/build/phaser.min.js"
      ],
      
      
  Import
  
      import * as Phaser from "phaser";    
          
    export class AppComponent {
      title = 'app';
      game: any;
      constructor(){
        this.game =  new Phaser.Game(800,600, 
          Phaser.CANVAS, 'game', {'preload': this.preload, 'create': this.create});
      }
      preload() {
        this.game.load.image('preloader', 'assets/images/loading_bar.png');
        
      }

      create(){
        console.log('creates');
      };
       
    }
    
    
        
    import { Component } from '@angular/core';
    import * as $ from "jquery";
    import * as Phaser from "phaser";

    @Component({
      selector: 'app-root',
      templateUrl: './app.component.html',
      styleUrls: ['./app.component.css']
    })
    export class AppComponent {
      title = 'app';
      game: any;
      cat: any;
      constructor(){
        this.game =  new Phaser.Game(800,600, 
          Phaser.CANVAS, 'game', {'preload': this.preload, 'create': this.create, 'update': this.update});
       // this.game.state.add('preload', this.preload);
        
      }
      preload() {
        this.game.load.image('cat', 'assets/cat.png');
        
      }

      create(){
        console.log('creates');
        this.cat = this.game.add.sprite(40, 30, 'cat');
      };

      update(){
         if (this.game.input.keyboard.isDown(Phaser.Keyboard.LEFT)){
            this.cat.x -= 5;
          }
          if (this.game.input.keyboard.isDown(Phaser.Keyboard.RIGHT)){
            this.cat.x += 5;
          }
      }
       
    }    
