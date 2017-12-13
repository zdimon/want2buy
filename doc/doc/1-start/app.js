System.register(["@angular/core", "@angular/platform-browser-dynamic", "@angular/platform-browser"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __moduleName = context_1 && context_1.id;
    var core_1, core_2, platform_browser_dynamic_1, platform_browser_1, HelloAngular, AppModule;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
            },
            function (platform_browser_dynamic_1_1) {
                platform_browser_dynamic_1 = platform_browser_dynamic_1_1;
            },
            function (platform_browser_1_1) {
                platform_browser_1 = platform_browser_1_1;
            }
        ],
        execute: function () {
            HelloAngular = (function () {
                function HelloAngular() {
                    this.title = 'Hello bro!!';
                }
                return HelloAngular;
            }());
            HelloAngular = __decorate([
                core_2.Component({
                    selector: 'hello-angular',
                    template: '<h1>{{ title }}</h1>'
                })
            ], HelloAngular);
            AppModule = (function () {
                function AppModule() {
                }
                return AppModule;
            }());
            AppModule = __decorate([
                core_1.NgModule({
                    declarations: [
                        HelloAngular
                    ],
                    imports: [platform_browser_1.BrowserModule],
                    providers: [],
                    bootstrap: [HelloAngular]
                })
            ], AppModule);
            exports_1("AppModule", AppModule);
            platform_browser_dynamic_1.platformBrowserDynamic().bootstrapModule(AppModule);
        }
    };
});
//# sourceMappingURL=app.js.map