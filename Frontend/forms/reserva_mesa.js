
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("php-email-form");

    if (!form) {
        console.error("Formulario no encontrado. Verifica el ID.");
        return;
    }

    form.removeAttribute("action");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        // Asegurar que todos los elementos existen antes de acceder a ellos
        const nameInput = document.getElementById("name");
        const carnetInput = document.getElementById("carnet");
        const phoneInput = document.getElementById("phone");
        const dateInput = document.getElementById("date");
        const timeInput = document.getElementById("time");
        const peopleInput = document.getElementById("people");
        const messageInput = document.getElementById("message");

        if (!nameInput || !carnetInput || !phoneInput || !dateInput || !timeInput || !peopleInput) {
            console.error("Uno o más elementos del formulario no existen.");
            return;
        }

        const formData = {
            name: nameInput.value.trim(),
            identification: carnetInput.value.trim(),
            phone: phoneInput.value.trim(),
            date: dateInput.value,
            time: timeInput.value,
            people: parseInt(peopleInput.value, 10),
            message: document.querySelector("textarea[name='message']").value
        };

        if (!formData.name || !formData.identification || !formData.phone || !formData.date || !formData.time || isNaN(formData.people)) {
            document.querySelector(".error-message").textContent = "Por favor, completa todos los campos.";
            document.querySelector(".error-message").style.display = "block";
            return;
        }

        try {
            const response = await fetch("http://localhost:8000/reserva", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            const result = await response.json();
            console.log("Reserva exitosa:", result);

            document.querySelector(".sent-message").style.display = "block";
            document.querySelector(".error-message").style.display = "none";
            form.reset();
        } catch (error) {
            console.error("Error al enviar la reserva:", error);
            document.querySelector(".error-message").textContent = "Error al enviar la reserva. Intenta de nuevo.";
            document.querySelector(".error-message").style.display = "block";
        }
    });
});