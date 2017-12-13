##Bootstrap

    npm install bootstrap@4.0.0-alpha.4 --save
    
- add bootstrap to angular-cli.json

    "../node_modules/bootstrap/dist/css/bootstrap.min.css"
    
- template    
    
    <div class="container">


      <nav class="navbar navbar-toggleable-md navbar-light bg-faded">
          <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <a class="navbar-brand" href="#">WezoM-Lab</a>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item active">
               <a class="nav-link" routerLink="/page/about">About</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" routerLink="/page/index">Index</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" routerLink="/english">English</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" routerLink="/sandbox">Sandbox</a>
              </li>
            </ul>
            <auth-form></auth-form>
          </div>
      </nav>

      </div>
  
  
    
    
or    
    
    npm install ng2f-bootstrap --save
    
    "../node_modules/ng2f-bootstrap/dist/bootstrap.min.css"
    
    
    


    <div class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" >ngEvents</a>
        </div>

        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li>
              <a >All Events</a>
            </li>
            <li><a href="">Create Event</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" >
                Events
                <span class="caret"></span>
              </a>
              <ul class="dropdown-menu">
                <li >
                  <a href="">Angular Connect</a>
                </li>
              </ul>
            </li>
          </ul>
          <div class="navbar-header navbar-right">
            <ul class="nav navbar-nav">
              <li>
                <a>Welcome John</a>
              </li>
            </ul>
          </div>
          <form id="searchForm"  class="navbar-form navbar-right"  >
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Search Sessions" >
            </div>
            <button class="btn btn-default" >
              Search
            </button>
          </form>
        </div>
      </div>
    </div>

