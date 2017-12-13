##Фасадная загрузка модулей.

Для того чтобы иметь возможность переносить модули внутри файловой системы без необходимости изменения пути импорта во многих частях приложения, создается фасадный модуль загрузки.
Из которого импортируются все ваши классы.


    import { SERVER_URL, User } from './global';
    import {AuthService} from './auth/auth.service'

    export {
        SERVER_URL,
        AuthService,
        User
    }
    
Импортируем.

    
    import {AuthService, User} from '../importer'
    
## Правила импорта.

По умолчанию импортируют так.

    import A from '/A'
   
Это работает только когда определен экспорт по умолчанию.

    export default 42
    
Причем не важно какое имя использовать.

    import A from './A'
    import MyA from './A'
    import Something from './A'

    
Если дефолтный экспорт не определен.
	
    export const A = 42
    export const myA = 43
    export const Something = 44
    
То импорт нужно производить внутри скобок (именованый импорт).

    import {A} from './A'
    import {MyA} from './A'
    import {Something} from './A'
    
    
 Смешанный вариант.
 
    export default 42
    export const myA = 43
    export const Something = 44   
        
    import A, { myA, Something } from './A'        
    
    import X, { myA as myX, Something as XSomething } from './A'
    
