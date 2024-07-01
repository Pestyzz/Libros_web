document.addEventListener("DOMContentLoaded", () => {
    const paymentForm = document.getElementById("paymentForm");

    //Datos a validar payment.html
    const payName = document.getElementById("pName");
    const payEmail = document.getElementById("pEmail");
    const payAddress = document.getElementById("fAddress");
    const payPhone = document.getElementById("pPhone");
    const payCardPropetary = document.getElementById("pProp");
    const payCardNumber = document.getElementById("pCardNumb");
    const payCardExpDate = document.getElementById("pCardExpDate");
    const payCardCvv = document.getElementById("pCardCvv");

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

    //Validación Pago Nombre
    const checkPayName = (value) => {
        if (value.length < 3) {
            showError(payName, "El nombre no es válido.");
            return false;
        } else if (value.charAt(0) != value.charAt(0).toUpperCase()) {
            showError(payName, "El nombre debe empezar por mayúscula.");
            return false;
        } else if (/\d/.test(value)) {
            showError(payName, "El nombre no puede contener números.");
            return false;
        } else {
            clearError(payName);
            return true;
        }
    }
    //Validación pago nombre en tiempo real
    payName.addEventListener("input", () => {
        checkPayName(payName.value);
    });
    //Fin Validación Pago Nombre

    //Validación Pago Email
    const checkPayEmail = (value) => {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(value) || value.length < 10) {
            showError(payEmail, "El Email es inválido.")
        } else {
            clearError(payEmail);
            return true;
        }
    }
    //Validación pago email en tiempo real
    payEmail.addEventListener("input", () => {
        checkPayEmail(payEmail.value);
    });
    //Fin Validación Pago Email

    //Validación Pago Dirección
    const checkPayAddress = (value) => {
        if (value.length < 1) {
            showError(payAddress, "Ingrese una dirección válida.");
            return false;
        } else {
            clearError(payAddress);
            return true;
        }
    }
    //Validación pago dirección en tiempo real
    payAddress.addEventListener("input", () => {
        checkPayAddress(payAddress.value);
    });
    //Fin Validación Pago Dirección

    //Validación Pago Número Celular
    const checkPayPhone = (value) => {
        const phonePattern = /^\d{9}$/;

        if (!phonePattern.test(value)) {
            showError(payPhone, "Teléfono inválido.");
        } else {
            clearError(payPhone);
            return true;
        }
    }
    //Validación pago número celular en tiempo real
    payPhone.addEventListener("input", () => {
        checkPayPhone(payPhone.value.trim());
    });
    //Fin Validación Pago Número Celular

    //Validación Tarjeta Propietario
    const checkCardPropetary = (value) => {
        if (value.length < 3) {
            showError(payCardPropetary, "El nombre no es válido.");
            return false;
        } else if (value.charAt(0) != value.charAt(0).toUpperCase()) {
            showError(payCardPropetary, "El propietario debe empezar por mayúscula.");
            return false;
        } else if (/\d/.test(value)) {
            showError(payCardPropetary, "El nombre no puede contener números.");
            return false;
        } else {
            clearError(payCardPropetary);
            return true;
        }
    }
    //Validación tarjeta propietario en tiempo real
    payCardPropetary.addEventListener("input", () => {
        checkCardPropetary(payCardPropetary.value);
    });
    //Fin Validación Tarjeta Propietario

    //Validación Tarjeta Número
    const checkCardNumber = (value) => {
        const cardNumber = value.replace(/\s+/g, '').replace(/-/g, '');

        // Verificar si el número de tarjeta contiene solo dígitos
        if (!/^\d+$/.test(cardNumber) || cardNumber.length !== 16 ) {
            showError(payCardNumber, "Tarjeta Inválida.");
            return false;
        } else {
            clearError(payCardNumber)
            return true;
        }
    }
    //Validación tarjeta número en tiempo real
    payCardNumber.addEventListener("input", () => {
        checkCardNumber(payCardNumber.value);
    });
    //Fin Validación Tarjeta Número

    //Validación Tarjeta Fecha Expiración
    const checkCardExpDate = (value) => {
        // Eliminar espacios en blanco
        const expDate = value.replace(/\s+/g, '');

        // Verificar si la longitud es correcta
        if (expDate.length > 7) {
            showError(payCardExpDate, "La fecha de expiración es inválida.");
            return false;
        }

        const formattedExpDate = expDate
            .replace(/\//g, '')
            .replace(/^(\d{2})/, '$1/'); // Añadir una barra después de los primeros dos dígitos (mes)
        
        // Actualizar el valor del campo de entrada con el formato
        payCardExpDate.value = formattedExpDate;

        clearError(payCardExpDate);
        return true;
    }
    //Validación tarjeta fecha expiración en tiempo real
    payCardExpDate.addEventListener("input", () => {
        checkCardExpDate(payCardExpDate.value);
    });
    //Fin Validación Tarjeta Fecha Expiración

    //Validación Tarjeta CVV
    const checkCardCvv = (value) => {
        const cvvPattern = /^[0-9]{3}$/;

        if (!cvvPattern.test(value)) {
            showError(payCardCvv, "El CVV es inválido.");
            return false;
        } else {
            clearError(payCardCvv);
            return true;
        }
    }
    //Validación tarjeta cvv en tiempo real
    payCardCvv.addEventListener("input", () => {
        checkCardCvv(payCardCvv.value);
    });
    //Fin Validación Tarjeta CVV

    const validatePayForm = (event) => {
        let isValid = true;


        if (!checkPayName(payName.value)) {
            isValid = false;
        }

        if (!checkPayEmail(payEmail.value)) {
            isValid = false;
        }

        if (!checkPayAddress(payAddress.value)) {
            isValid = false;
        }

        if (!checkPayPhone(payPhone.value.trim())) {
            isValid = false;
        }

        if (!checkCardPropetary(payCardPropetary.value)) {
            isValid = false;
        }

        if (!checkCardNumber(payCardNumber.value)) {
            isValid = false;
        }

        if (!checkCardExpDate(payCardExpDate.value)) {
            isValid = false;
        }

        if (!checkCardCvv(payCardCvv.value)) {
            isValid = false;
        }


        if (!isValid) {
            event.preventDefault();
        }
    }

    if (paymentForm) {
        paymentForm.addEventListener("submit", validatePayForm);
    }
});