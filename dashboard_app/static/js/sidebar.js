$(document).ready(function() {
  $('#sidebarCollapse').click(function() {
    $('#mySidebar').toggleClass('show'); // Alternar la clase 'show' en la barra lateral
    if ($('#mySidebar').hasClass('show')) {
      openNav();
    } else {
      closeNav();
    }
  });

  function openNav() {
    $('#content').css('transition', 'margin-left 0.5s');
    $('#mySidebar').css('width', '210px');
    $('#content').css('margin-left', '210px');
  }

  function closeNav() {
    $('#content').css('transition', 'margin-left 0.5s');
    $('#mySidebar').css('width', '0');
    $('#content').css('margin-left', '0');
  }
});