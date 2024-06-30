document.addEventListener("DOMContentLoaded", () => {
    // Capturar el input de tipo archivo
    const fileInput = document.getElementById('file-input');
    // Capturar la imagen de vista previa
    const previewImage = document.getElementById('preview-image');

    // Escuchar el evento de cambio en el input de tipo archivo
    fileInput.addEventListener('change', function(event) {
        // Obtener el archivo seleccionado
        const file = event.target.files[0];
        // Crear un objeto URL para la vista previa de la imagen
        const imageUrl = URL.createObjectURL(file);
        // Actualizar la fuente de la imagen de vista previa
        previewImage.src = imageUrl;
    });
});