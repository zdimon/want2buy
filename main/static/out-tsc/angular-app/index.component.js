System.register(["@angular/core", "@angular/http", "rxjs/add/operator/map"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var __moduleName = context_1 && context_1.id;
    var core_1, http_1, IndexComponent;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (_1) {
            }
        ],
        execute: function () {
            IndexComponent = /** @class */ (function () {
                function IndexComponent(_http) {
                    this._http = _http;
                }
                IndexComponent.prototype.ngOnInit = function () {
                    var _this = this;
                    var url = 'http://localhost:8080/static/test/users.json';
                    this._http
                        .get(url)
                        .map(function (res) { return res.json(); })
                        .subscribe(function (res) {
                        console.log(res);
                        _this.users = res;
                    });
                };
                IndexComponent = __decorate([
                    core_1.Component({
                        template: "<h2>IndexComponent {{ announcement_id }} </h2>\n    <ul>\n    <li *ngFor=\"let u of users\"> {{u.username}} </li>\n  </ul>\n  "
                    }),
                    __metadata("design:paramtypes", [http_1.Http])
                ], IndexComponent);
                return IndexComponent;
            }());
            exports_1("IndexComponent", IndexComponent);
        }
    };
});
//# sourceMappingURL=/home/zdimon/storage1/www/want2buy/angular-app/index.component.js.map