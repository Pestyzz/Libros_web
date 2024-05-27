document.addEventListener("DOMContentLoaded", () => {

    //Las validaciones se hacen a tiempo real en el momento en el que el usuario ingrese los datos.

    const registerForm = document.getElementById("registerForm");

    //Datos a validar register.html
    const user = document.getElementById("fUser");
    const name = document.getElementById("fName");
    const lastNames = document.getElementById("fLnames");
    const email = document.getElementById("fEmail");
    const phoneNumber = document.getElementById("fPhone");
    const psw = document.getElementById("fPsw");
    const confirmNewPsw = document.getElementById("fPsw2");
    const address = document.getElementById("fAddress");

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

    //Validación Nombre de Usuario
    const checkUser = (value) => {
        if (value.length < 5) {
            showError(user, "El nombre de usuario es demasiado corto. (Mínimo 5 caracteres)");
            return false;
        } else if (value.length > 16) {
            showError(user, "El nombre de usuario es demasiado largo. (Máximo 16 caracteres)");
            return false;
        } else if (/\s/.test(value)) {
            showError(user, "El nombre de usuario no puede contener espacios.");
            return false;
        } else {
            clearError(user);
            return true;
        }
    }

    //Validación nombre de usuario en tiempo real
    user.addEventListener("input", () => {
        checkUser(user.value);
        console.log(checkUser(user.value))
    });
    //Fin Validación nombre de usuario

    //Validación Nombre
    const checkName = (value) => {
        if (value.length < 3) {
            showError(name, "El nombre ingresado no es válido.");
            return false;
        } else if (value.charAt(0) != value.charAt(0).toUpperCase()) {
            showError(name, "El nombre debe empezar por mayúscula.");
            return false;
        } else if (/\d/.test(value)) {
            showError(name, "El nombre no puede contener números.");
            return false;
        } else {
            clearError(name);
            return true;
        }
    }
    
    //Validación nombre en tiempo real
    name.addEventListener("input", () => {
        checkName(name.value);
    });
    //Fin validación nombre

    //Validación Apellidos
    const checkLastNames = (value) => {

        const lastNamesArray = value.trim().split(" ");

        if (lastNamesArray.length !== 2) {
            showError(lastNames, "Debe ingresar uno o ambos apellidos")
            return false;
        } 

        for (const lastName of lastNamesArray) {
            if (lastName.charAt(0) !== lastName.charAt(0).toUpperCase()) {
                showError(lastNames, "Los apellidos deben empezar por mayúscula.");
                return false;
            } else if (/\d/.test(lastName)) {
                showError(lastNames, "Los apellidos no pueden contener números");
                return false;
            }
        }

        clearError(lastNames);
        return true;
    }
    
    //Validación apellidos en tiempo real
    lastNames.addEventListener("input", () => {
        checkLastNames(lastNames.value);
    });
    //Fin validación Apellidos

    //Validación Email
    const checkEmail = (value) => {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(value) || value.length < 10) {
            showError(email, "El formato Email ingresado es inválido.")
        } else {
            clearError(email);
            return true;
        }
    }

    //Validación email en tiempo real
    email.addEventListener("input", () => {
    checkEmail(email.value); 
    });

    //Fin validación email

    //Validación número celular
    const checkPhone = (value) => {
        const phonePattern = /^\d+$/;

        if (!phonePattern.test(value) || value.trim().length < 9 || value.trim().length > 9) {
            showError(phoneNumber, "Número Celular ingresado inválido.");
        } else {
            clearError(phoneNumber);
            return true;
        }
    }

    //Validación número celular en tiempo real
    phoneNumber.addEventListener("input", () => {
        checkPhone(phoneNumber.value.trim())
    });
    //Fin validación número celular

    //Validación contraseña
    const checkPsw = (value) => {
        if (/\s/.test(value)) {
            showError(psw, "La contraseña no puede contener espacios.");
            return false;
        } else if (value.length === 0) {
            showError(psw, "Debe ingresar una contraseña.")
            return false;
        } else if (value.length > 0 && value.length < 12) {
            showError(psw, "La contraseña debe contener al menos 12 caracteres.");
            return false;
        } else {
            clearError(psw);
            return true;
        }
    }

    //Validación contraseña en tiempo real
    psw.addEventListener("input", () => {
        checkPsw(psw.value);
        checkConfNPsw(confirmNewPsw.value, psw.value);
    });
    //Fin valdiación contraseña

    //Validación confirmar contraseña
    const checkConfNPsw = (value, newPass) => {
        if (value.length === 0) {
            showError(confirmNewPsw, "Debe ingresar una contraseña.");
            return false;
        } else if (value != newPass) {
            showError(confirmNewPsw, "Ambas  contraseñas deben coincidir.");
            return false;
        } else {
            clearError(confirmNewPsw);
            return true;
        }
    }

    //Validación confirmar contraseña en tiempo real
    confirmNewPsw.addEventListener("input", () => {
        checkConfNPsw(confirmNewPsw.value, psw.value)
    });
    //Fin validación confirmar contraseña

    const checkAddress = (value) => {
        if (value.length === 0) {
            showError(address, "Debe ingresar una dirección válida.");
            return false;
        } else {
            clearError(address);
            return true;
        }
    }
    address.addEventListener("input", () => {
        checkAddress(address.value);
    });


    const validateForm = (event) => {
        let isValid = true;

        //Validación del nombre de usuario
        if (!checkUser(user.value)) {
            isValid = false;
        }

        // Validación del nombre
        if (!checkName(name.value)) {
            isValid = false;
        }
    
        // Validación de los apellidos
        if (!checkLastNames(lastNames.value)) {
            isValid = false;
        }
    
        // Validación del correo electrónico
        if (!checkEmail(email.value)) {
            isValid = false;
        }
    
        // Validación del número de teléfono
        if (!checkPhone(phoneNumber.value.trim())) {
            isValid = false;
        }

        if (!checkPsw(psw.value)) {
            isValid = false;
        }

        if (!checkConfNPsw(confirmNewPsw.value, psw.value)) {
            isValid = false;
        }

        if (!checkAddress(address.value)) {
            isValid = false;
        }
    
        if (!isValid) {
            event.preventDefault();
        }
    };

    if (registerForm) {
        registerForm.addEventListener("submit", validateForm);
    }
});