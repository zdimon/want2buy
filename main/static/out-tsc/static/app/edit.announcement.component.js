System.register(["@angular/core", "@angular/router"], function (exports_1, context_1) {
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
    var core_1, router_1, EditAnnouncementComponent;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            }
        ],
        execute: function () {
            EditAnnouncementComponent = /** @class */ (function () {
                function EditAnnouncementComponent(route) {
                    this.route = route;
                }
                EditAnnouncementComponent.prototype.ngOnInit = function () {
                    var _this = this;
                    this.route.params.subscribe(function (params) { return _this.announcement_id = params['announcement_id']; });
                };
                EditAnnouncementComponent = __decorate([
                    core_1.Component({
                        template: "\n  \n  <div class=\"row\">\n    <div class=\"col-md-12\">\n           \n    </div>\n  </div>\n  "
                    }),
                    __metadata("design:paramtypes", [router_1.ActivatedRoute])
                ], EditAnnouncementComponent);
                return EditAnnouncementComponent;
            }());
            exports_1("EditAnnouncementComponent", EditAnnouncementComponent);
        }
    };
});
//# sourceMappingURL=/home/zdimon/www/want2buy/static/app/edit.announcement.component.js.map