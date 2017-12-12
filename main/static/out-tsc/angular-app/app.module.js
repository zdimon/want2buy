System.register(["./index.component", "./edit.announcement.component", "@angular/platform-browser", "@angular/core", "./app.component", "./router.module", "@angular/http"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __moduleName = context_1 && context_1.id;
    var index_component_1, edit_announcement_component_1, platform_browser_1, core_1, app_component_1, router_module_1, http_1, AppModule;
    return {
        setters: [
            function (index_component_1_1) {
                index_component_1 = index_component_1_1;
            },
            function (edit_announcement_component_1_1) {
                edit_announcement_component_1 = edit_announcement_component_1_1;
            },
            function (platform_browser_1_1) {
                platform_browser_1 = platform_browser_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (app_component_1_1) {
                app_component_1 = app_component_1_1;
            },
            function (router_module_1_1) {
                router_module_1 = router_module_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            }
        ],
        execute: function () {
            AppModule = /** @class */ (function () {
                function AppModule() {
                }
                AppModule = __decorate([
                    core_1.NgModule({
                        declarations: [
                            /// here we need to add every new component
                            app_component_1.AppComponent,
                            edit_announcement_component_1.EditAnnouncementComponent,
                            index_component_1.IndexComponent
                        ],
                        imports: [platform_browser_1.BrowserModule, router_module_1.AppRoutingModule, http_1.HttpModule],
                        providers: [],
                        bootstrap: [app_component_1.AppComponent]
                    })
                ], AppModule);
                return AppModule;
            }());
            exports_1("AppModule", AppModule);
        }
    };
});
//# sourceMappingURL=/home/zdimon/storage1/www/want2buy/angular-app/app.module.js.map