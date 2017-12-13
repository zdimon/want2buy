## Настройка Nginx 

    server {
        listen 80 ;
        server_name study.webmonstr.com;
        index index.html;

            root /home/zdimon/www/wezomlab/client-app/dist;

            location / {
            
                    try_files $uri$args $uri$args/ /index.html;
                    
            }
    }
