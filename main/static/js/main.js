(function () {
    'use strict';

    $('ul.header-menu li')
        .click(function(){
            window.sessionStorage.currentMenuItem = this.id;
    });
    $('ul.footer-menu li')
        .click(function(){
            window.sessionStorage.currentMenuItem = this.id;
    });
    $('h1.site-title a')
        .click(function () {
            sessionStorage.currentMenuItem = "hnHome";
    });
    switch (sessionStorage.currentMenuItem)
    {
        case 'fnHome':
            sessionStorage.currentMenuItem = 'hnHome';
            break;
        case 'fnAbout':
            sessionStorage.currentMenuItem = 'hnAbout';
            break;
        case 'fnRules':
            sessionStorage.currentMenuItem = 'hnRules';
            break;
        case 'fnFeedback':
            sessionStorage.currentMenuItem = 'hnFeedback';
            break;
    }
    $("#"+sessionStorage.currentMenuItem)
        .addClass('current-menu-item menu-item-has-children');


})();