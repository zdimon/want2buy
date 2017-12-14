System.register([], function (exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var Announcement, AnnouncementPager;
    return {
        setters: [],
        execute: function () {
            Announcement = /** @class */ (function () {
                function Announcement(id, title, user, category, sub_category, sub_sub_category, new_category, new_bu, opt_roznica, type, once, price, thumbnail, region, city, creted_at) {
                    this.id = id;
                    this.title = title;
                    this.user = user;
                    this.category = category;
                    this.sub_category = sub_category;
                    this.sub_sub_category = sub_sub_category;
                    this.new_category = new_category;
                    this.new_bu = new_bu;
                    this.opt_roznica = opt_roznica;
                    this.type = type;
                    this.once = once;
                    this.price = price;
                    this.thumbnail = thumbnail;
                    this.region = region;
                    this.city = city;
                    this.creted_at = creted_at;
                }
                return Announcement;
            }());
            exports_1("Announcement", Announcement);
            AnnouncementPager = /** @class */ (function () {
                function AnnouncementPager(count, offset, limit, current, pager, has_prev, has_next, results) {
                    this.count = count;
                    this.offset = offset;
                    this.limit = limit;
                    this.current = current;
                    this.pager = pager;
                    this.has_prev = has_prev;
                    this.has_next = has_next;
                    this.results = results;
                }
                return AnnouncementPager;
            }());
            exports_1("AnnouncementPager", AnnouncementPager);
        }
    };
});
//# sourceMappingURL=/home/zdimon/www/want2buy/static/app/models/announcement.js.map