document.addEventListener("DOMContentLoaded", () => { 
    const recoverForm = document.getElementById("recoverForm");

    const recoverEmail = document.getElementById("rEmail");

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

    const checkRecoverEmail = (value) => {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(value) || value.length < 10) {
            showError(recoverEmail, "El formato Email ingresado es inválido.")
            return false;
        } else {
            clearError(recoverEmail);
            return true;
        }
    }

    recoverEmail.addEventListener("input", () => {
        checkRecoverEmail(recoverEmail.value);
        console.log(checkRecoverEmail(recoverEmail.value));
    });

    const validateForm = (event) => {
        let isValid = true;

        if (!checkRecoverEmail(recoverEmail.value)) {
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    }

    recoverForm.addEventListener("submit", validateForm)
});