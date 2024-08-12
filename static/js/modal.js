function muestraTelon(etiqueta) {
    let capa_telon = document.getElementById('telonCarga');
    capa_telon.style.display = "grid";
}

document.addEventListener('DOMContentLoaded', () => { 
    let formulario = document.getElementById('formu');

    formulario.addEventListener('submit', (envio) => {
        envio.preventDefault();

        muestraTelon(formulario);

        // aqui envio un formulario con fetch API
         // aqui envio un formulario con fetch API
          // aqui envio un formulario con fetch API
          
        fetch('/envioConsuPez', {
            method: 'POST',
            body: new FormData(formulario)
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                // Cambiar el círculo de carga por el chulo y cambiar el mensaje
                document.getElementById('cargando').style.display = 'none';
                document.getElementById('checkmark').style.display = 'block';
                document.getElementById('mensaje').textContent = 'Correo enviado correctamente';

                // Ocultar el telón después de unos segundos
                setTimeout(() => {
                    document.getElementById('telonCarga').style.display = 'none';
                }, 3000);
            } else {
                // Manejo de errores
                document.getElementById('mensaje').textContent = 'Error al enviar correo';
                setTimeout(() => {
                    document.getElementById('telonCarga').style.display = 'none';
                }, 3000);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('mensaje').textContent = 'Error al enviar correo';
            setTimeout(() => {
                document.getElementById('telonCarga').style.display = 'none';
            }, 3000);
        });

        formulario.reset();
    });
});
