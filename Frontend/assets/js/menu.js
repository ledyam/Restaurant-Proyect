document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');

    // Inicializar Isotope después de que el DOM cargue
    const menuContainer = document.querySelector('.isotope-container');
    let iso = new Isotope(menuContainer, {
        itemSelector: '.menu-item',
        layoutMode: 'masonry'
    });

    // Obtener los platillos desde el backend
    fetch('http://localhost:8000/menu')
        .then(response => response.json())
        .then(data => {
            console.log('Platillos obtenidos:', data);
            agregarPlatillos(data, iso);
        })
        .catch(error => console.error('Error obteniendo los platillos:', error));

    // Activar filtrado al hacer clic en un botón
    const filterButtons = document.querySelectorAll('.menu-filters li');
    filterButtons.forEach(button => {
        button.addEventListener('click', function () {
            const filterValue = this.getAttribute('data-filter');
            console.log('Filtro aplicado:', filterValue);
            iso.arrange({ filter: filterValue });

            // Cambiar la clase activa
            filterButtons.forEach(btn => btn.classList.remove('filter-active'));
            this.classList.add('filter-active');
        });
    });
});

function agregarPlatillos(platillos, iso) {
    console.log("Agregando platillos:", platillos);

    const menuContainer = document.querySelector('.isotope-container');

    platillos.forEach(item => {
        const categoria = `filter-${item.categoria.toLowerCase().replace(/\s+/g, '-')}`;
        const imagePath = `assets/img/menu/${item.nombre.toLowerCase().replace(/\s+/g, '-')}.jpg`;

        const menuItem = document.createElement('div');
        menuItem.classList.add('col-lg-6', 'menu-item', 'isotope-item', categoria);

        menuItem.innerHTML = `
            <img src="${imagePath}" class="menu-img" alt="${item.nombre}">
            <div class="menu-content">
                <a href="#">${item.nombre}</a><span>${item.precio}</span>
            </div>
            <div class="menu-ingredients">
                ${item.descripcion}
            </div>
        `;

        menuContainer.appendChild(menuItem);
        iso.appended(menuItem); // 🚀 Agregar el nuevo elemento a Isotope
    });

    iso.layout(); // 🚀 Recalcular el diseño
}
