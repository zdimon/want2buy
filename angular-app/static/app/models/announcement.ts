export class Announcement {
    constructor(
        public id: Number, 
        public title: string, 
        public user: Number,
        public category: string,
        public sub_category: string,
        public sub_sub_category: string,
        public new_category: string,
        public new_bu: string,
        public opt_roznica: string,
        public type: string,
        public once: string,
        public price: Number,
        public thumbnail: string,
        public region: string,
        public city: string,
        public creted_at: string,
        ){}
}

export class AnnouncementPager {
    constructor(
        public count: Number, 
        public offset: Number,
        public limit: Number,
        public current: Number,
        public pager: any,
        public has_prev: Boolean,
        public has_next: Boolean,
        public results: Announcement[],
        ){}
}