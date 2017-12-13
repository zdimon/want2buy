System.register(["@angular/core", "@angular/http", "rxjs/add/operator/map", "./service.module"], function (exports_1, context_1) {
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
    var core_1, http_1, service_module_1, IndexComponent;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (_1) {
            },
            function (service_module_1_1) {
                service_module_1 = service_module_1_1;
            }
        ],
        execute: function () {
            IndexComponent = /** @class */ (function () {
                function IndexComponent(_http, _service) {
                    this._http = _http;
                    this._service = _service;
                }
                IndexComponent.prototype.getActive = function () {
                    console.log('get active');
                };
                IndexComponent.prototype.ngOnInit = function () {
                    var _this = this;
                    this._service.getNewAnnoncements().subscribe(function (data) {
                        _this.announcements = data;
                        console.log(_this.announcements);
                    });
                };
                IndexComponent = __decorate([
                    core_1.Component({
                        templateUrl: '/static/templates/announcement/new_announcement_list.html'
                    }),
                    __metadata("design:paramtypes", [http_1.Http, service_module_1.AnnouncementService])
                ], IndexComponent);
                return IndexComponent;
            }());
            exports_1("IndexComponent", IndexComponent);
        }
    };
});
//# sourceMappingURL=/home/zdimon/www/want2buy/static/app/index.component.js.map