#Тестирование.

    ng test
    
## Jasmin

    describe - описание блока тестов
    it - описание теста
    
Инструкции beforeEach и afterEach в блоках.

    describe("A spec", function() {
      var foo;

      beforeEach(function() {
        foo = new Object;
      });

      afterEach(function() {
        foo = null;
      });
      
    })

### Наблюдатели.

    beforeEach(function() {
        spyOn(foo, 'setBar');
        foo.setBar(123);
        foo.setBar(456, 'another param');
      });

    ....
    expect(foo.setBar).toHaveBeenCalled();
    expect(foo.setBar.calls.length).toEqual(2);
    expect(foo.setBar).toHaveBeenCalledWith(123);
    expect(foo.setBar).toHaveBeenCalledWith(456, 'another param');
    expect(foo.setBar.mostRecentCall.args[0]).toEqual(456);
    expect(foo.setBar.calls[0].args[0]).toEqual(123);

### Задержка
    
    beforeEach(function() {
       
        jasmine.Clock.useMock();
      });

    it("causes a timeout to be called synchronously", function() {
        setTimeout(function() {
          timerCallback(); // это функция выполнится через 100мс
        }, 100);

        jasmine.Clock.tick(101); // ждем 101 мс

        ...
      });
      
### Асинхронные тесты.

    describe("Asynchronous specs", function() {
        var value, flag;

        it("async test", function() {
            runs(function() {
                flag = false;  // начальные значения
                value = 0;
                asynchFunc(value, function(x){
                    value = x;
                    flag = true;  // указывает на то что тест выполнен
                });
            });

            waitsFor(function() {
                return flag; // ждет когда флаг переключится в true
            }, "Message for timeout case", 750);
            // после выполняет следующий блок кода
            runs(function() {
                expect(value).toBeGreaterThan(0);
            });
        });
    });      
      
Синтаксис waitsFor.

    waitsFor(conditionCallback, TimeOutMessage, TimeOut)
    conditionCallback - функция возвращающая true/false, она постоянно вызывается методом waitsFor пока не вернет true либо наступит TimeOut
    TimeOut - максимально время работы метода в мс
    TimeOutMessage - сообщение по приходу TimeOut

### Проверки на истинность

    expect(...).toBe(151); (=== ссылочное сравнение)
    expect(true).not.toBe(true);
    expect().toBeTruthy() (coercion !!"hello" = true)
    expect(a).toEqual(b); (сравнение по содержимому a = {}, b = {} = true)   
 
### Подстроки 
   
    var message = 'foo bar baz';
    expect(message).toMatch(/bar/);
    expect(message).toMatch('bar');
    expect(message).not.toMatch('bar');   
   
### Свойства в объекте.   
   
    expect(a.foo).toBeDefined();
    expect(a.bar).not.toBeDefined();   
    
### Null & undefined    
    
    
    expect(a).toBeNull();
    expect(b).not.toBeNull(); 
    
### Имя класса конструктора       

    expect({}).toEqual(jasmine.any(Object));
    expect(12).toEqual(jasmine.any(Number));
    
### Проверка исключений.    
    
    var foo = function() {
      return 1 + 2;
    };
    var bar = function() {
      return a + 1;
    };

    expect(foo).not.toThrow();
    expect(bar).toThrow();       
           
       
       
Равенство

    let c = new Card(name,face, 1);
    expect(c.name).toEqual(name);


Can't bind to 'card' since it isn't a known property of 'card'.

	import { DebugElement, NO_ERRORS_SCHEMA } from '@angular/core';

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GameComponent ],
      schemas: [NO_ERRORS_SCHEMA]
    })
    .compileComponents();
  }));

    
    
## e2e

    ng e2e
    
##Изначальные настройки и тесты.

###app.po.ts
    
    import { browser, by, element } from 'protractor';

    export class CardPage {
      navigateTo() {
        return browser.get('/');
      }

      getParagraphText() {
        return element(by.css('app-root h1')).getText();
      }
    }
        
 
### app.e2e-spec.ts 
        
    import { CardPage } from './app.po';

    describe('card App', () => {
      let page: CardPage;

      beforeEach(() => {
        page = new CardPage();
      });

      it('should display welcome message', () => {
        page.navigateTo();
        expect(page.getParagraphText()).toEqual('Welcome to app!!');
      });
    });
 
### Оснофные ф-ции.

- получение ОДНОГО элемента

    let greenParagraph = element(by.css('p.green'));
 
- получение КОЛЛЕКЦИИ элементов и их подсчет, получение первого элемента         
    
    let greenParagraphs = element.all(by.css('p.green'));    
    let count = greenParagraphs.count();  
    let first = greenParagraphs.first(); 
    
- получение текста элемента

    let greenParagraph = element(by.css('p.green'));  
    let text = greenParagraph.getText(); 

- клик на элементе

    let submitButton = element(by("form .submit-button"));  
    submitButton.click(); 
    
- ввод значений в форму

    let newTodoInput = element(by.css(".add-todo input[type=text]"));
    newTodoInput.sendKeys("Todo 4");
    
- получение значения из эл-та формы

    let inputFieldText = element(by.css("todo input[type=text]")).getAttribute("value"); 
    
- дополнительно 

    newTodoSubmitButton.isEnabled()  
    
               

Тест на наличие элемента


  it('Кнопка раздачи', () => {
    page.navigateTo();
    expect(element(by.id('deal-button')).getText()).toEqual('Get 6 cards');
  });
  
  
### Сценарии тестирования.

- формы

    it("should be able to add a new todo", () => {  
        browser.get("/");
        let newTodoInput = element(
              by.css(".add-todo input[type=text]"));
        newTodoInput.sendKeys("Todo 4");

        let newTodoSubmitButton = element(
              by.css(".add-todo input[type=submit]"));
        newTodoSubmitButton.click();

        let todos = element.all(by.css(".todos .todo"));
        expect(todos.count()).toEqual(4);
    })



  
    

##Ошибка     

    Uncaught ReferenceError: require is not defined
    
Из за отсутствия поддержки require в браузере. 
Мы собираемся прокрутить тесты через karma-browserify перед запуском.   
    
    npm install karma-browserify --save-dev



    Failed: Template parse errors:
    'app-game' is not a known element:
    
Необходимо добавлять дочерние компоненты в тест.

    import { GameComponent } from './game/game.component';
    
      beforeEach(async(() => {
        TestBed.configureTestingModule({
          declarations: [
            AppComponent,
            GameComponent
          ],
        }).compileComponents();
      }));    

