document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("alerta_acpm_modal");
    var span = document.getElementsByClassName("close")[0];
    var form = document.querySelector("form");

    span.onclick = function() {
        modal.style.display = "none"; 
        form.submit(); // Enviar formulario al cerrar el modal
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    form.addEventListener("submit", function(event) {
        var cantidadInput = document.getElementById("cantidadt");
        var cantidad = parseInt(cantidadInput.value);
        var nivelACPM = parseInt(document.getElementById("nivel_acpm").value); 

        if (cantidad <= 20 || nivelACPM <= 15) {
            event.preventDefault(); 
            modal.style.display = "block"; 
        }
    });

   
    document.querySelector(".btn-solicitar").addEventListener("click", function(event) {
        event.preventDefault();
        modal.style.display = "none"; 
        form.submit(); 
    });
});
