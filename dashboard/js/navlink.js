$(document).ready(function () {
    let url = window.location;
    $('ul.navbar-nav a[href="' + url + '"]').addClass('active');
    $('ul.navbar-nav a').filter(function() {
        return this.href == url;
    }).addClass('active');
 });