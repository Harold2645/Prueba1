document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("alerta_acpm_modal");
    var span = document.getElementsByClassName("close")[0];

   

    span.onclick = function() {
        modal.style.display = "none"; 
        document.querySelector("form").submit();
    }

    
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    
    document.querySelector("form").addEventListener("submit", function(event) {
        var cantidadInput = document.getElementById("cantidadt");
        var cantidad = parseInt(cantidadInput.value);
        var nivelACPM = parseInt(document.getElementById("nivel_acpm").value); 

     
        if (cantidad <= 20 || nivelACPM <= 15) {
            event.preventDefault(); 
            modal.style.display = "block"; 
        }
    });
});