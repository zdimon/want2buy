# Generic

При написании кода вы всегда встаёте перед выбором, имеющим как минимум две ветви решения. Первый путь приводит вас к копированию существующего кода с нужным вам типом, что также приводит к «распуханию» кода и необходимости думать при рефакторинге. Второй путь – унификация, что подразумевает под собой параметрический полиморфизм, в основе которого лежит использование одного и того же кода, но с разными типами. Получается, что обобщённые типы нужны для написания кода, который можно многократно использовать вне зависимости от типов.
 

interface IAnimal{
    color: string;
    voice();
}

class Dog implements IAnimal{
    color: string;
    voice(){
      console.log('gav');
    }
  }

class Cat{
    color: string;
    voice(){
      console.log('mya');
    }
  }
  


  var d = new Dog();
  var c = new Cat();
  
Можем так.

    function say(d: Dog){
        d.voice();
    }
    function say(d: Cat){
        d.voice();
    }

Можем так.


  function say<T extends IAnimal>(d: T){
    d.voice()
  }
  
Попробуем с классом.

  
  
   class Box<T>{
        content: Array<T> = [];

        put(animal: T){
            this.content.push(animal);
        }
    }

    var d = new Dog();
    var c = new Cat();

    var box = new Box<Dog>();
    box.put(с);
  
  
Так как классы Dog и Cat одинаковы то ошибки не возникает.

Добавим доп поле.


    class Dog implements IAnimal{
        color: string;
        size: number;
        voice(){
          console.log('gav');
        }
      }
      
Получим.


    message: 'Argument of type 'Cat' is not assignable to parameter of type 'Dog'.


      
  


