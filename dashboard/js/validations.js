document.addEventListener("DOMContentLoaded", () => {

    let url = window.location.pathname; //Obtenemos un array de la url

    //Las validaciones se hacen a tiempo real en el momento en el que el usuario ingrese los datos

    //Se realizan las validaciones respectivas al formulario de profile.html
    if (url.includes("profile.html")) { //Verificamos si en la url se encuentra el html que deseamos para validar
        const form = document.getElementById("profileForm")
        //Datos a validar
        const name = document.getElementById("fName");
        const lastNames = document.getElementById("fLnames");
        const email = document.getElementById("fEmail");
        const phoneNumber = document.getElementById("fPhone");
        const actualPsw = document.getElementById("fPsw");
        const newPsw = document.getElementById("fPsw2");
        const confirmNewPsw = document.getElementById("fPsw3");

        const Password = "111111111111";
        const newPassword = newPsw.value;

        //Función para mostrar el mensaje de error al usuario
        const showError = (inputElement, errorMessage) => {
            const errorElement = inputElement.nextElementSibling;
            errorElement.textContent = errorMessage;
        }   

        //Función para limpiar el mensaje si pasa las validaciones
        const clearError = (inputElement) => {
            const errorElement = inputElement.nextElementSibling;
            errorElement.textContent = "";
        }

        //Validación Nombre
        const checkName = (value) => {
            if (value.length < 3) {
                showError(name, "El nombre no es válido.");
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
        
        name.addEventListener("input", () => {
            checkName(name.value.trim());
        });
        //Fin validación nombre


        //Validación Apellidos
        const checkLastNames = (value) => {
            if (value.length < 4) {
                showError(lastNames, "Los apellidos no son válidos.");
                return false;
            } else if (value.charAt(0) != value.charAt(0).toUpperCase()) {
                showError(lastNames, "Los apellidos deben empezar por mayúscula.");
                return false;
            } else if (/\d/.test(value)) {
                showError(lastNames, "Los apellidos no pueden contener números");
                return false;
            } else {
                clearError(lastNames);
                return true;
            }
        }
        
        lastNames.addEventListener("input", () => {
            checkLastNames(lastNames.value.trim());
        });
        //Fin validación Apellidos


        //Validación Email
        const checkEmail = (value) => {
            if (value.length < 10) {
                showError(email, "El Email es inválido.");
                return false;
            }
        }

        email.addEventListener("input", () => {
           checkEmail(email.value); 
        });

        //Fin validación email


        //Validación número celular
        const checkPhone = (value) => {
            if (/\D/.test(value)) {
                showError(phoneNumber, "Número Celular inválido.");
            } else {
                clearError(phoneNumber);
            }
        }

        phoneNumber.addEventListener("input", () => {
            checkPhone(phoneNumber.value.trim())
        });
        //Fin validación número celular


        //Validación contraseña actual
        const checkPsw = (value) => {
            if (/\s/.test(value)) {
                showError(actualPsw, "La contraseña no puede contener espacios.");
                return false;
            } else if (value.length > 0 && value.length < 12) {
                showError(actualPsw, "La contraseña debe contener al menos 12 caracteres.");
                return false;
            } else {
                clearError(actualPsw);
                return true;
            }
        }

        
        //Se valida a tiempo real
        actualPsw.addEventListener("input", () => {
            checkPsw(actualPsw.value);

            //Si el usuario ingresa valores en contraseña actual
            //Se activa el input para ingresar una nueva contraseña
            if (actualPsw.value.length > 0) {
                newPsw.removeAttribute("disabled");
            } else {
                newPsw.setAttribute("disabled", "");
            }
        });
        //Fin valdiación contraseña actual


        //Validación nueva contraseña 
        const checkNewPsw = (value, pass) => {
            if (value === pass) {
                showError(newPsw, "Ingrese una contraseña diferente.");
                return false;
            } else if (/\s/.test(value)) {
                showError(newPsw, "La contraseña no puede contener espacios.");
                return false;
            } else if (value.length > 0 && value.length < 12) {
                showError(newPsw, "La contraseña debe contener al menos 12 caracteres.");
                return false;
            } else {
                clearError(newPsw);
                return true;
            }
        }

        newPsw.addEventListener("input", () => {
            checkNewPsw(newPsw.value, Password)
            //Si el usuario ingresa valores en nueva contraseña
            //Se activa el input para confirmar la nueva contraseña
            if (newPsw.value.length > 0) {
                confirmNewPsw.removeAttribute("disabled");
            } else {
                confirmNewPsw.setAttribute("disabled", "");
            }
        });
        //Fin validación nueva contraseña

        //Validación confirmar contraseña
         const checkConfNPsw = (value, newPass) => {
            if (value != newPass) {
                showError(confirmNewPsw, "Las contraseñas deben coincidir.");
            } else {
                clearError(confirmNewPsw);
            }
         }

         confirmNewPsw.addEventListener("input", () => {
            checkConfNPsw(confirmNewPsw.value);
         });
         //Fin validación confirmar contraseña

        form.addEventListener("submit", (event) => {
            if (!checkName(name.value.trim())) {
                event.preventDefault();
            }

            if (!checkLastNames(lastNames.value.trim())) {
                event.preventDefault();
            }

            if (!checkEmail(email.value)) {
                event.preventDefault();
            }
        })
    }
    //Fin validaciones profile.html
});