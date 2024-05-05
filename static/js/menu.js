document.addEventListener('DOMContentLoaded', () =>{

    const botns_n01 = document.querySelectorAll('.btn-n01');

    function mostrarNiveles (segundo_menu){

        if (segundo_menu == "btn_productos"){

            let menu_prod = document.getElementById('menu_prod');

            if (menu_prod.style.display == "" || menu_prod.style.display == "none") {
                menu_prod.style.display = "block";
            } else {
                menu_prod.style.display = "none";
            }
        }

        if (segundo_menu == "btn_servicios"){

            let menu_serv = document.getElementById('menu_serv');

            if (menu_serv.style.display == "" || menu_serv.style.display == "none") {
                menu_serv.style.display = "block";
            }else{
                menu_serv.style.display = "none";
            }
        }
    }

    botns_n01.forEach(boton => {
        boton.addEventListener('click', (objeto) => {
            console.log(objeto.target.id)

            if (objeto.target.id == "btn_productos"){
                mostrarNiveles (objeto.target.id);
            }

            if (objeto.target.id == "btn_servicios"){
                mostrarNiveles (objeto.target.id);
            }
        });
    });
    

})