// script.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".login100-form"); // Seleccionamos el formulario
    const userInput = document.querySelector("input[name='user']"); // Seleccionamos el campo de correo electrónico
    const passwordInput = document.querySelector("input[name='pass']"); // Seleccionamos el campo de contraseña
    
    form.addEventListener("submit", async (event) => {
        event.preventDefault();  // Evita que el formulario se envíe de forma tradicional

        // Verifica si los campos existen
        if (!userInput || !passwordInput) {
            console.error("Campos de entrada no encontrados.");
            return;
        }

        const username = userInput.value.trim();
        const password = passwordInput.value.trim();

        if (!username || !password) {
            alert("Por favor, ingrese el correo electrónico y la contraseña.");
            return;
        }


        try {
            const response = await fetch(`http://127.0.0.1:8000/user-exists/${username}/${password}`, {

                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                }
            });

            if (response.ok) {
                const data = await response.json();
                if (data.exists) {
                    alert("El usuario existe.");
                    // Redirigir al usuario a la página de inicio o dashboard
                    window.location.href = "http://127.0.0.1:5500/Frontend/pages/dashboard-sb-admin/index.html"; // Cambia esto por la URL deseada
                }
            } else {
                const error = await response.json();
                alert(error.detail);  // Muestra el detalle del error (por ejemplo, usuario no encontrado)
            }
        } catch (error) {
            console.error("Error al intentar consumir la API:", error);
            alert("Hubo un error al contactar con la API.");
        }
    });
});
