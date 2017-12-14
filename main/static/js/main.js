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


    var dropdown_counter=0;
    function dropdown_open_close(){
        if (dropdown_counter==0) {
            $('#header-dropdown-caret-down').hide("fast");
            $('.header-links').show("fast");
            $('#header-dropdown-caret-left').show("fast");
            dropdown_counter=1;
        }
        else {
            $('#header-dropdown-caret-down').show("fast");
            $('#header-dropdown-caret-left').hide("fast");
            $('.header-links').hide("fast");
            dropdown_counter=0;
        }
    }
    $('#header-dropdown')
        .click(dropdown_open_close);
})();