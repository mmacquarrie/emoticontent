$(document).ready(function() {
    var page = this.location.pathname;
    if (page != "/") page = page.substring(1);
    else page = 'index';
    $('#main-nav .navbar-nav a.nav-link[data-navlink="' + page + '"]').parent().addClass('active');
});
