document.addEventListener("DOMContentLoaded", () => {
    const findMyAddress = () => {
        const status = document.querySelector(".status");
        const addressInput = document.getElementById("fAddress");
        const regionInput = document.getElementById("fRegion");
        const cityInput = document.getElementById("fCity");

        const success = (position) => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            const geoAPIUrl = `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=es`;

            fetch(geoAPIUrl)
            .then(res => res.json())
            .then(data => {
                const country = data.countryName;
                const region = data.localityInfo.administrative[1].name;
                const city = data.localityInfo.administrative[2].name
                const locality = data.localityInfo.administrative[3].name;
                addressInput.value = country + ", " + region +  ", " + city + ", " + locality; // Actualiza el valor del input con el nombre del país
                regionInput.value = region;
                cityInput.value = locality;

                // Eliminar el event listener después de actualizar los campos
                addressInput.removeEventListener("click", findMyAddress);
            })
            .catch(error => {
                console.error("Error al obtener los datos de ubicación:", error);
                status.textContent = "No se pudo encontrar tu dirección.";
            });
        }

        const error = (err) => {
            console.error("Error de geolocalización:", err);
            status.textContent = "No se pudo encontrar tu dirección.";
        }

        navigator.geolocation.getCurrentPosition(success, error);
    } 

    document.querySelector("#fAddress").addEventListener("click", findMyAddress);
});