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