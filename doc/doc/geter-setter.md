# Гетеры сетеры

Используют синтаксис ActionScript3.

    class foo {
        private _bar:boolean = false;
        get bar():boolean {
            return this._bar;
        }
        set bar(theBar:boolean) {
            this._bar = theBar;
        }
    }
    
Обертка над Object.defineProperty() ES5.

Object.defineProperty(obj, prop, descriptor)

Аргументы:

obj
Объект, в котором объявляется свойство.

prop
Имя свойства, которое нужно объявить или модифицировать.

descriptor
Дескриптор – объект, который описывает поведение свойства.

    Object.defineProperty(user, "name", {
      value: "Вася",
      writable: false, // запретить присвоение "user.name="
      configurable: false // запретить удаление "delete user.name"
    });
    
        
    var foo = (function () {
        function foo() {
            this._bar = false;
        }
        Object.defineProperty(foo.prototype, "bar", {
            get: function () {
                return this._bar;
            },
            set: function (theBar) {
                this._bar = theBar;
            },
            enumerable: true,
            configurable: true
        });
        return foo;
    })();
        
