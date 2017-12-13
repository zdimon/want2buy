##Внедрение зависимостей

# Dependency Injection DI.

Важный паттерн проектирования, решающий задачи внедрения зависимых библиотек для повторного изпользования.

Рассмотрим класс.

    export class Car {
     
      public engine: Engine;
      public tires: Tires;
      public description = 'No DI';
     
      constructor() {
        this.engine = new Engine();
        this.tires = new Tires();
      }

      drive() {
        return `${this.description} car with ` +
          `${this.engine.cylinders} cylinders and ${this.tires.make} tires.`;
      }
    }

Класс создает все что ему необходимо внутри конструктора вместо того чтоб их запрашивать.
Проблема в том что этим он легко ломается не гибок, и трудно тестируеться.
К примеру если будет изменяться сигнатура конструктора зависимого класса - ломка.
Еще хуже если мы хотим использовать разные типы обьектов Tires.
Мы фактически привязаны к одному типу - не гибкость.
Также класс не может разделить внутренние обьекты с другими классами.
Тестирование затруднено тем что мы в ручную должны создавать все необходимое для внутренних обьектов обеспечивая их корректное ф-ие.

Как улучшить ситуацию.

    public description = 'DI';

    constructor(public engine: Engine, public tires: Tires) { }
    
Теперь класс не создает что ему необходимо а запрашивает в конструкторе.
И при создании экземпляра нужно эти обьекты передать.


    let car = new Car(new Engine(), new Tires());
    
Теперь если кто то изменит класс Engine это уже не проблема для класса Car.
Но проблема остается в клиенском коде.

    class Engine2 {
      constructor(public cylinders: number) { }
    }
    // Super car with 12 cylinders and Flintstone tires.
    let bigCylinders = 12;
    let car = new Car(new Engine2(bigCylinders), new Tires());

Тестирование.


    class MockEngine extends Engine { cylinders = 8; }
    class MockTires  extends Tires  { make = 'YokoGoodStone'; }

    // Test car with 8 cylinders and YokoGoodStone tires.
    let car = new Car(new MockEngine(), new MockTires());

Суть паттерна в том что класс получает все необходимое из вне.

Для того чтоб убрать проблему с клиентским кодом необходимо написать класс фабрику, унифицирующую создание объектов Car.


    import { Engine, Tires, Car } from './car';
     
    // BAD pattern!
    export class CarFactory {
      createCar() {
        let car = new Car(this.createEngine(), this.createTires());
        car.description = 'Factory';
        return car;
      }
     
      createEngine() {
        return new Engine();
      }
     
      createTires() {
        return new Tires();
      }
    }
    
Но при росте приложения поддержка этого кода будет напрягать и он будет усложняться.
Было бы неплохо просто перечислить все что нужно не заботясь о том как его обеспечить свими зависимостями.
Сдесь вступает в игру DI фреймворк Ангуляра.
Представим что у нас есть универсальный обьект injector который о бо всем позаботится.

    let car = injector.get(Car);

Создаем сервис который можно внедрить.

    import { Injectable } from '@angular/core';

    import { HEROES }     from './mock-heroes';

    @Injectable()
    export class HeroService {
      getHeroes() { return HEROES; }
    }

Добавляем его в главный модуль в секцию providers (будет доступен всем модулям).
Либо в дочерний модуль.
Либо в компонент (убрано!!!).


    import { Component }          from '@angular/core';

    import { HeroService }        from './hero.service';

    @Component({
      selector: 'my-heroes',
      providers: [HeroService],
      
    ....

Регистрируем провайдера в компоненте.


    import { Component }   from '@angular/core';
     
    import { Hero }        from './hero';
    import { HeroService } from './hero.service';
     
    @Component({
      selector: 'hero-list',
      template: `
      <div *ngFor="let hero of heroes">
        {{hero.id}} - {{hero.name}}
      </div>
      `
    })
    export class HeroListComponent {
      heroes: Hero[];
     
      constructor(heroService: HeroService) {
        this.heroes = heroService.getHeroes();
      }
    }

Логгер.

    import { Injectable } from '@angular/core';

    @Injectable()
    export class Logger {
      logs: string[] = []; // capture logs for testing

      log(message: string) {
        this.logs.push(message);
        console.log(message);
      }
    }

При создании провайдера в модуле его просто подменить на другой класс.


    providers: [Logger]
    
    [{ provide: Logger, useClass: Logger }]
    
Первый - токен (ключ для поиска).
Второй - способ создания провайдера.

    [{ provide: Logger, useClass: BetterLogger }]

Алиасы.

    [ NewLogger,
      // Not aliased! Creates two instances of `NewLogger`
      { provide: OldLogger, useClass: NewLogger}]

    [ NewLogger,
      // Alias OldLogger w/ reference to NewLogger
      { provide: OldLogger, useExisting: NewLogger}]

Иногда удобно использовать в качестве провайдера уже готовые объекты вместо классов.


    // An object in the shape of the logger service
    let silentLogger = {
      logs: ['Silent logger says "Shhhhh!". Provided via "useValue"'],
      log: () => {}
    };

    [{ provide: Logger, useValue: silentLogger }]

