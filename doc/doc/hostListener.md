## HostListener

Слушает события компоненты или директивы.


    @HostListener('click', ['$event.target']) flipOver(crd){
        console.log(crd);
    }
    
