$(function () {

    lightbox();
    sticky();
    utils();

    demo();

});

/* for demo purpose only - can be deleted */

function demo() {

    $("#page").change(function () {

        if ($(this).val() !== '') {

            window.location.href = $(this).val();

        }

        return false;
    });
}

/* =========================================
 *  lightbox
 *  =======================================*/

function lightbox() {

    $(document).delegate('*[data-toggle="lightbox"]', 'click', function (event) {
        event.preventDefault();
        $(this).ekkoLightbox();
    });
}

/* =========================================
 *  sticky header 
 *  =======================================*/

function sticky() {

    $(".header").sticky();

}

function utils() {

    /* tooltips */

    $('[data-toggle="tooltip"]').tooltip();

    /* click on the box activates the radio */

    $('#checkout').on('click', '.box.shipping-method, .box.payment-method', function (e) {
        var radio = $(this).find(':radio');
        radio.prop('checked', true);
    });
    /* click on the box activates the link in it */

    $('.box.clickable').on('click', function (e) {

        window.location = $(this).find('a').attr('href');
    });
    /* external links in new window*/

    $('.external').on('click', function (e) {

        e.preventDefault();
        window.open($(this).attr("href"));
    });
    /* animated scrolling */

    /* animated scrolling */

    $('.scroll-to, #navigation a').click(function (event) {
        event.preventDefault();
        var full_url = this.href;
        var parts = full_url.split("#");
        var trgt = parts[1];

        $('body').scrollTo($('#' + trgt), 800, {offset: -40});

    });

}

$.fn.alignElementsSameHeight = function () {
    $('.same-height-row').each(function () {

        var maxHeight = 0;
        var children = $(this).find('.same-height');
        children.height('auto');
        if ($(window).width() > 768) {
            children.each(function () {
                if ($(this).innerHeight() > maxHeight) {
                    maxHeight = $(this).innerHeight();
                }
            });
            children.innerHeight(maxHeight);
        }

        maxHeight = 0;
        children = $(this).find('.same-height-always');
        children.height('auto');
        children.each(function () {
            if ($(this).innerHeight() > maxHeight) {
                maxHeight = $(this).innerHeight();
            }
        });
        children.innerHeight(maxHeight);
    });
}

$(window).load(function () {

    windowWidth = $(window).width();
    windowHeight = $(window).height();

    $(this).alignElementsSameHeight();

});
$(window).resize(function () {

    newWindowWidth = $(window).width();
    newWindowHeight = $(window).height();

    if (windowWidth !== newWindowWidth) {
        setTimeout(function () {
            $(this).alignElementsSameHeight();
        }, 100);
        windowWidth = newWindowWidth;
        windowHeight = newWindowHeight;
    }

});
