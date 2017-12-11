/*
 * Indigo v1.0.0
 */
(function ($) {
    'use strict';

    /*--------------------------------
     * Scroll to Top
     *-------------------------------*/
    $("#scroll-to-top").on('click', function () {
        $("html, body").animate({scrollTop: 0}, "fast");
        return false;
    });

    /*--------------------------------
     * Tabs
     *-------------------------------*/
    var $indigoTabsContainer = $(".indigo-tabs-container");
    if ($indigoTabsContainer) {
        $indigoTabsContainer.find(".indigo-tabs > li").on('click', function () {
            var $this = $(this),
                $indigoTabs = $this.parents(".indigo-tabs");
            $indigoTabs.find("li").removeClass('active');
            $(this).addClass('active');
            $indigoTabsContainer.find(".indigo-tab-content").removeClass('active').hide();
            $indigoTabsContainer.find(".indigo-tab-content").eq($this.index()).show().addClass('active');
        });
    }

    /*--------------------------------
     * Slick Nav
     * http://slicknav.com/
     *-------------------------------*/
    if (jQuery().slicknav) {
        var headerNavigation = $("#header-navigation"),
            headerMenu = headerNavigation.find(".header-menu");
        headerMenu.slicknav({
            label: "",
            prependTo: '.site-branding-wrap'
        });
    }

    var extendedBg = function () {
        var $extendedBg = $("#extended-bg");
        if ($(window).width() > 991) {
            var header = $("#header"),
                extendBG = 15 + ( ( header.width() - header.find(".container").width() ) / 2);
            $extendedBg.css({
                paddingRight: extendBG,
                marginRight: -extendBG
            })
        } else {
            $extendedBg.css({
                paddingRight: 0,
                marginRight: -0
            })
        }
    };

    extendedBg();
    $(window).on('resize', function () {
        extendedBg();
    });

    /*--------------------------------
     * Chosen
     * https://harvesthq.github.io/chosen/
     *-------------------------------*/
  //  if (jQuery().chosen) {
        $(".indigo-select").chosen({
            width: "100%",
            disable_search_threshold: 10000
        })
 //   }

    /*--------------------------------
     * Light Case
     * http://cornel.bopp-art.com/lightcase/documentation/
     *-------------------------------*/
    if (jQuery().lightcase) {
        $('a[data-rel^=lightcase]').lightcase({
            swipe: true
        });
    }

    /*--------------------------------
     * Facts
     * Waypoints : http://imakewebthings.com/waypoints/
     * jquery-countTo : https://github.com/mhuggins/jquery-countTo
     *-------------------------------*/
    if (jQuery().waypoint) {

        var $facts = $('#facts');
        $facts.waypoint({
            handler: function (direction) {
                if ('down' == direction) {
                    if (jQuery().countTo) {
                        $('.fact-figure > span').countTo();
                    }
                }
            },
            offset: '80%'
        });
    }

    /*--------------------------------
     * Carousel
     * https://owlcarousel2.github.io/OwlCarousel2/docs/started-welcome.html
     *-------------------------------*/
    if (jQuery().owlCarousel) {
        $(".clients-items-carousel").owlCarousel({
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                500: {
                    items: 2
                },
                991: {
                    items: 3,
                    margin: 30
                },
                1199: {
                    items: 4
                }
            }
        });
    }

    /*--------------------------------
     * Form Validation
     * http://malsup.com/jquery/form/
     * http://jqueryvalidation.org/
     *-------------------------------*/
    if (jQuery().validate && jQuery().ajaxSubmit) {
        var errorsContainer = $("#contact-form .errors-container"),
            ajaxLoader = $("#contact-form #loader");

        $("#contact-form").validate({
            errorLabelContainer: errorsContainer,
            submitHandler: function (form) {
                $(form).ajaxSubmit({
                    beforeSubmit: function () {
                        errorsContainer.hide();
                        ajaxLoader.show();
                    },
                    success: function (result, status, xhr, form) {
                        var data = $.parseJSON(result);
                        ajaxLoader.hide();
                        errorsContainer.show();
                        if (data.response == "success") {
                            errorsContainer.html(data.message);
                        }
                    },
                    complete: function (xhr, status, form) {
                        form.resetForm();
                    }
                });
            }
        });
    }

})(jQuery);