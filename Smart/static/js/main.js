$(document).ready(function() {
    $("#carousel-header").owlCarousel({
        items: 1,
        nav: true,
        navText: [],
        loop: true,
        autoplay: true,
        autoplayTimeout: 4000
    });
});

$(document).ready(function() {
    $("#carousel-product").owlCarousel({
        items: 1,
        nav: true,
        navText: [],
        loop: true,
        autoplay: false,
        autoplayTimeout: 4000
    });
});