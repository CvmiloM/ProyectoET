document.addEventListener('DOMContentLoaded', () => {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    document.querySelectorAll('.btn-primary').forEach(button => {
        button.addEventListener('click', () => {
            const card = button.closest('.card');
            const nombre = card.querySelector('.card-title').textContent;
            const id = card.querySelector('img').alt;
            const producto = { id, nombre, cantidad: 1 };
            carrito.push(producto);
            localStorage.setItem('carrito', JSON.stringify(carrito));
            alert(`${nombre} agregado al carrito`);
        });
    });

    document.querySelector('#guardar-carrito').addEventListener('click', () => {
        fetch('/miapp/guardar_carrito/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({ carrito: carrito })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Carrito guardado exitosamente');
                localStorage.removeItem('carrito');
            } else {
                alert('Error al guardar el carrito');
            }
        });
    });
});
