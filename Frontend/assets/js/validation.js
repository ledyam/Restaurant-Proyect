document.addEventListener("DOMContentLoaded", function () {
    const dateInput = document.getElementById('date');
    
    // Obtener la fecha de hoy en formato YYYY-MM-DD
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = (today.getMonth() + 1).toString().padStart(2, '0'); // Asegura que el mes tenga dos dígitos
    const dd = today.getDate().toString().padStart(2, '0'); // Asegura que el día tenga dos dígitos
    
    const currentDate = `${yyyy}-${mm}-${dd}`; // Fecha mínima (hoy)
    
    // Establecer la fecha mínima en el input
    dateInput.setAttribute('min', currentDate);
    
    // Establecer la fecha máxima (31 de diciembre del año actual)
    const maxDate = `${yyyy}-12-31`;
    dateInput.setAttribute('max', maxDate);
    dateInput.setAttribute('placeholder',"Fecha")
});
