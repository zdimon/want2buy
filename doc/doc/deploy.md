## Деплой проэкта на удаленную машину

deploy.sh

    #!/bin/bash
    cd client-app
    ng build -prod
    cd ..
    git add --all
    git commit -m "$(date)"
    git push
    ssh -t zdimon@gis.webmonstr.com "cd www/wezomlab; git pull"