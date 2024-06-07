document.addEventListener("DOMContentLoaded", () => {

    //Las validaciones se hacen a tiempo real en el momento en el que el usuario ingrese los datos.
    //Se realizan diferentes validaciones dependiendo de si se está en el formulario de profile.html o addauthor.html.

    const form = document.getElementById("productForm");

    //Datos a validar
    const isbn = document.getElementById("fIsbn");
    const bookName = document.getElementById("fBname");
    const author = document.getElementById("fAuthor");
    const publisher = document.getElementById("fPub");
    const language = document.getElementById("fLng");
    const category = document.getElementById("fCateg");
    const price = document.getElementById("fPrice");

    //Función para mostrar el mensaje de error al usuario
    const showError = (inputElement, errorMessage) => {
        const errorElement = inputElement.nextElementSibling;
        errorElement.textContent = errorMessage;
    }   

    //Función para limpiar el mensaje de error si pasa las validaciones
    const clearError = (inputElement) => {
        const errorElement = inputElement.nextElementSibling;
        errorElement.textContent = "";
    }

    //Validación ISBN-13
    const checkIsbn = (value) => {
        const isbnPattern = /^\d{13}$/;

        if (!isbnPattern.test(value)) {
            showError(isbn, "ISBN Inválido. (13 dígitos)");
            return false;
        } else {
            clearError(isbn);
            return true;
        }
    }

    //Validación isbn-13 en tiempo real
    isbn.addEventListener("input", () => {
        if (!isbn.getAttribute("disabled")) {
            checkIsbn(isbn.value);
        }
    });
    //Fin Validación ISBN-13

    //Validación Nombre Libro
    const checkBookName = (value) => {
        const MIN_BOOK_NAME_LENGTH = 3;
        const MAX_BOOK_NAME_LENGTH = 50;
    
        // Permitir letras Unicode, espacios y caracteres especiales, pero no números
        const bookNamePattern = new RegExp(`^[A-Za-zÀ-ÖØ-öø-ÿ0-9\\s',.()!\\-]{${MIN_BOOK_NAME_LENGTH},${MAX_BOOK_NAME_LENGTH}}$`);
    
        if (!bookNamePattern.test(value)) {
            showError(bookName, "Nombre de Libro Inválido.");
            return false;
        } else {
            clearError(bookName);
            return true;
        }
    }
    
    
    
     
    //Validación nombre libro en tiempo real
    bookName.addEventListener("input", () => {
        checkBookName(bookName.value);
    })
    //Fin Validación Nombre Libro

    //Validación Autor
    const checkAuthor = (value) => {
        if (value.length < 2) {
            showError(author, "El nombre del autor es demasiado corto. (Mínimo 2 caracteres)");
            return false;
        } else if (value.length > 30) {
            showError(author, "El nombre del autor es demasiado largo. (Máximo 30 caracteres)");
            return false;
        } else {
            clearError(author);
            return true;
        }
    }
    //Validación autor en tiempo real
    author.addEventListener("input", () => {
        if (!author.getAttribute("disabled")) {
            checkAuthor(author.value);
        }
    });
    //Fin Validación Autor

    //Validación Editorial
    const checkPublisher = (value) => {
        if (value.length < 3) {
            showError(publisher, "El nombre de la editorial es demasiado corto. (Mínimo 3 caracteres)");
            return false;
        } else if (value.length > 15) {
            showError(publisher, "El nombre de la editorial es demasiado largo. (Máximo 15 caracteres)");
            return false;
        } else {
            clearError(publisher);
            return true;
        }
    }
    //Validación editorial en tiempo real
    publisher.addEventListener("input", () => {
        checkPublisher(publisher.value);
    });
    //Fin Validación Editorial

    //Validación Idioma
    const checkLng = (value) => {
        if (value === "0") {
            showError(language, "Selecciona un idioma.")
            return false;
        } else {
            clearError(language);
            return true;
        }
    }
    //Validación idioma en tiempo real
    language.addEventListener("change", () => {
        checkLng(language.value)
    });
    //Fin Validación Idioma

    //Validación Categoría
    const checkCategory = (value) => {
        if (value === "none") {
            showError(category, "Selecciona una categoría.")
            return false;
        } else {
            clearError(category);
            return true;
        }
    }
    //Validación categoría en tiempo real
    category.addEventListener("change", () => {
        checkCategory(category.value)
    });
    //Fin Validación Categoría

    //Formatear Precio
    const checkPrice = (value) => {
        const cleanedValue = value.replace(/\D/g, '');
        //Formatear el precio con un punto cada tres dígitos
        const formattedValue = cleanedValue.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
        //Establecer el valor formateado en el input
        price.value = formattedValue;

        return true;
    }
    //Formatear precio en tiempo real
    price.addEventListener("input", () => {
        checkPrice(price.value);
    });
    //Fin Formatear Precio

    //Función que valida el formulario para poder enviarlo
    const validateForm = (event) => {
        let isValid = true;

        if (!isbn.getAttribute("disabled")) {
            if (!checkIsbn(isbn.value)) {
                isValid = false;
            }
        }
        
        if (!checkBookName(bookName.value)) {
            isValid = false;
        }

        if (!author.getAttribute("disabled")) {
            if (!checkAuthor(author.value)) {
                isValid = false;
            }
        }

        if (!checkPublisher(publisher.value)) {
            isValid = false;
        }

        if (!checkLng(language.value)) {
            isValid = false;
        }

        if (!checkCategory(category.value)) {
            isValid = false;
        }

        if (!checkPrice(price.value)) {
            isValid = false;
        }
        
        if (!isValid) {
            event.preventDefault();
        }
    };

    //Si se encuentra el formulario de profile.html, se realizan las validaciones para ese formulario
    //Si se encuentra el formulario de addauthor.html, se realizan las validaciones para ese formulario

    if (form) {
        form.addEventListener("submit", validateForm);
    }
});