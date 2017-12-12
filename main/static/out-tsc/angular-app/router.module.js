System.register(["@angular/core", "@angular/router", "./edit.announcement.component", "./index.component"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __moduleName = context_1 && context_1.id;
    var core_1, router_1, edit_announcement_component_1, index_component_1, routes, AppRoutingModule;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (edit_announcement_component_1_1) {
                edit_announcement_component_1 = edit_announcement_component_1_1;
            },
            function (index_component_1_1) {
                index_component_1 = index_component_1_1;
            }
        ],
        execute: function () {
            routes = [
                { path: '', redirectTo: 'index', pathMatch: 'full' },
                { path: 'edit/announcement/:announcement_id', component: edit_announcement_component_1.EditAnnouncementComponent },
                { path: 'index', component: index_component_1.IndexComponent }
            ];
            AppRoutingModule = /** @class */ (function () {
                function AppRoutingModule() {
                }
                AppRoutingModule = __decorate([
                    core_1.NgModule({
                        imports: [
                            router_1.RouterModule.forRoot(routes)
                        ],
                        exports: [
                            router_1.RouterModule
                        ]
                    })
                ], AppRoutingModule);
                return AppRoutingModule;
            }());
            exports_1("AppRoutingModule", AppRoutingModule);
        }
    };
});
//# sourceMappingURL=/home/zdimon/storage1/www/want2buy/angular-app/router.module.js.map