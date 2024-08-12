
// document.addEventListener('DOMContentLoaded', function() {
    
//     var modal = document.getElementById("alerta_acpm_modal");
//     var span = document.getElementsByClassName("close")[0];

    
//     var alerta = "{{ session.get('alerta_acpm') }}";
//     if (alerta) {
//         modal.style.display = "block";
//     }


//     // if ("{{ session.get('alerta_acpm') }}") {
//     //     modal.style.display = "block";
//     // }

//     //cierra el modal
//     span.onclick = function() {
//         modal.style.display = "none";
//     }

//     // Cuando el usuario haga clic en cualquier parte fuera del modal, cierra el modal
//     window.onclick = function(event) {
//         if (event.target == modal) {
//             modal.style.display = "none";
//         }
//     }
// });



document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("alerta_acpm_modal");
    var span = document.getElementsByClassName("close")[0];

    // Solo muestra el modal si 'alerta_acpm' está presente en la sesión
    if (modal) {
        modal.style.display = "block";
    }

    // Cierra el modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Cuando el usuario haga clic en cualquier parte fuera del modal, cierra el modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});