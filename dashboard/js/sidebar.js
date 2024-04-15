function openNav() {
  document.getElementById("content").style.transition = 'margin-left 0.5s';
  document.getElementById("mySidebar").style.width = "210px";
  document.getElementById("content").style.marginLeft = "210px";
}

function closeNav() {
  document.getElementById("content").style.transition = 'margin-left 0.5s';
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("content").style.marginLeft= "0";
}


document.addEventListener('DOMContentLoaded', function() {
  const sidebar = document.getElementById('mySidebar');
  const content = document.getElementById('content');

  if (sidebar && content) {
      console.log('Elementos encontrados:', sidebar, content);
    
      document.getElementById('sidebarCollapse').addEventListener('click', function() {
          console.log('Click en el botón de colapsar la barra lateral');
          sidebar.classList.toggle('show'); // Alternar la clase 'show' en la barra lateral
          if (sidebar.classList.contains('show')) {
            openNav();
            
          } else {
            closeNav();
          }
      });
  } else {
      console.error('No se encontraron elementos necesarios.');
  }
});
