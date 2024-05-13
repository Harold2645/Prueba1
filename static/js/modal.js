document.addEventListener('DOMContentLoaded', () => { 

    document.getElementById('openModalBtn').addEventListener('click', function() {
        // Fetching the modal content from the server
        fetch('/modal')
        .then(response => response.text())
        .then(data => {
            // Adding the modal content to the modal container
            document.getElementById('modalContainer').innerHTML = data;

            // Displaying the modal
            document.getElementById('myModal').style.display = 'grid';

            let boton_cerrar = document.querySelector ('#myModal span.close');

            boton_cerrar.addEventListener('click', function (){
                let ventana = document.querySelector ('#myModal')
                ventana.style.display = "none";
            })

        });
    });

});
