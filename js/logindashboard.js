document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");

    const logUser = document.getElementById("lUser");
    
    //Función que devuelve true si el valor del usuario ingresado es "admin"
    const adminUser = (value) => {
        return value === "admin";
    }

    const logDashboard = () => {
        if (adminUser(logUser.value)) {
            loginForm.action = "../dashboard/dashboard.html";
        } else {
            loginForm.action = "indexLogin.html";
        }
    }

    //Al presionar el boton de submit, se inicia la función para validar si es admin o no
    loginForm.addEventListener("submit", logDashboard);
});