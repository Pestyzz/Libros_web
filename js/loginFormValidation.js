document.addEventListener("DOMContentLoaded", () => {

    const loginForm = document.getElementById("loginForm");

    const  loginUser = document.getElementById("lUser");
    const  loginPass = document.getElementById("lPass");

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

    const checkLogUser = (value) => {
        if (value.length < 5 || value.length > 16 || /\s/.test(value)) {
            showError(loginUser, "Usuario Inválido");
            return false;
        } else {
            clearError(loginUser);
            return true;
        }
    }

    loginUser.addEventListener("input", () => {
        checkLogUser(loginUser.value);
    });

    const checkLogPass = (value) => {
        if (/\s/.test(value)) {
            showError(loginPass, "Contraseña Inválida");
            return false;
        } else if (value.length > 0 && value.length < 12) {
            showError(loginPass, "Contraseña Inválida");
            return false;
        } else {
            clearError(loginPass);
            return true;
        }
    }

    loginPass.addEventListener("input", () => {
        checkLogPass(loginPass.value);
    });

    const validateForm = (event) => {
        let isValid = true;

        if (!checkLogUser(loginUser.value)) {
            isValid = false;
        }

        if (!checkLogPass(loginPass.value)) {
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    }

    if (loginForm) {
        loginForm.addEventListener("submit", validateForm)
    }
});