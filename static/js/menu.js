document.addEventListener('DOMContentLoaded', () => { 
    const btns_n01 = document.querySelectorAll('.btn-n01');
    const btns_n02 = document.querySelectorAll('.btn-n02');
    
    const menu_n02 = document.querySelectorAll('.menu-n02');
    const menu_n03 = document.querySelectorAll('.menu-n03');

    function mostrarNiveles(boton_activado) {
        switch (boton_activado) {
            case "btn_usuarios":
                let menu_usuarios = document.getElementById('menu_usuarios');
                if (menu_usuarios.style.display == "" || menu_usuarios.style.display == "none") {
                    menu_n03.forEach(elemento_03 => {
                        elemento_03.style.display = "none";
                    });
                    menu_n02.forEach(elemento_02 => {
                        elemento_02.style.display = "none";
                    });
                    menu_usuarios.style.display = "block";
                } else {
                    menu_usuarios.style.display = "none";
                }
                break;

            case "btn_tractores":
                    let menu_tractores = document.getElementById('menu_tractores');
                    if (menu_tractores.style.display == "" || menu_tractores.style.display == "none") {
                        menu_n03.forEach(elemento_03 => {
                            elemento_03.style.display = "none";
                        });
                        menu_n02.forEach(elemento_02 => {
                            elemento_02.style.display = "none";
                        });
                        menu_tractores.style.display = "block";
                    } else {
                        menu_tractores.style.display = "none";
                    }
                    break;

            case "btn_herramienta":
                    let menu_herramienta = document.getElementById('menu_herramienta');
                    if (menu_herramienta.style.display == "" || menu_herramienta.style.display == "none") {
                        menu_n03.forEach(elemento_03 => {
                            elemento_03.style.display = "none";
                        });
                        menu_n02.forEach(elemento_02 => {
                            elemento_02.style.display = "none";
                        });
                        menu_herramienta.style.display = "block";
                    } else {
                        menu_herramienta.style.display = "none";
                    }
                    break;

                case "btn_categoria":
                        let menu_categorias = document.getElementById('menu_categorias');
                        if (menu_categorias.style.display == "" || menu_categorias.style.display == "none") {
                            menu_n03.forEach(elemento_03 => {
                                elemento_03.style.display = "none";
                            });
                            menu_n02.forEach(elemento_02 => {
                                elemento_02.style.display = "none";
                            });
                            menu_categorias.style.display = "block";
                        } else {
                            menu_categorias.style.display = "none";
                        }
                        break;

                case "btn_novedad":
                    let menu_novedad = document.getElementById('menu_novedad');
                    if (menu_novedad.style.display == "" || menu_novedad.style.display == "none") {
                        menu_n03.forEach(elemento_03 => {
                            elemento_03.style.display = "none";
                        });
                        menu_n02.forEach(elemento_02 => {
                            elemento_02.style.display = "none";
                        });
                        menu_novedad.style.display = "block";
                    } else {
                        menu_novedad.style.display = "none";
                    }
                    break;

                    case "btn_servicios":
                        let menu_servicios = document.getElementById('menu_servicios');
                        if (menu_servicios.style.display == "" || menu_servicios.style.display == "none") {
                            menu_n03.forEach(elemento_03 => {
                                elemento_03.style.display = "none";
                            });
                            menu_n02.forEach(elemento_02 => {
                                elemento_02.style.display = "none";
                            });
                            menu_servicios.style.display = "block";
                        } else {
                            menu_servicios.style.display = "none";
                        }
                        break;


                    case "btn_insumo":
                        let menu_insumo = document.getElementById('menu_insumo');
                        if (menu_insumo.style.display == "" || menu_insumo.style.display == "none") {
                            menu_n03.forEach(elemento_03 => {
                                elemento_03.style.display = "none";
                            });
                            menu_n02.forEach(elemento_02 => {
                                elemento_02.style.display = "none";
                            });
                            menu_insumo.style.display = "block";
                        } else {
                            menu_insumo.style.display = "none";
                        }
                        break;
                        
                    case "btn_liquido":
                        let menu_liquidos = document.getElementById('menu_liquidos');
                        if (menu_liquidos.style.display == "" || menu_liquidos.style.display == "none") {
                            menu_n03.forEach(elemento_03 => {
                                elemento_03.style.display = "none";
                            });
                            menu_liquidos.style.display = "block";
                        } else {
                            menu_liquidos.style.display = "none";
                        }
                        break;

            default:
                break;
        }
    }

    btns_n01.forEach(boton => {
        boton.addEventListener('click', (objeto) => {
            mostrarNiveles(objeto.target.id);
        });
    });

    btns_n02.forEach(boton => {
        boton.addEventListener('click', (objeto) => {
            mostrarNiveles(objeto.target.id);
        });
    });


const nav = document.querySelector("#menu_cont");
const abrir = document.querySelector("#disparador");
const cerrar = document.querySelector("#close")
const notscroll = document.querySelector('body')

abrir.addEventListener("click", () => {
    nav.classList.add("visible");
    if(nav.className = "visible"){
        notscroll.style.overflow = "hidden"
    }
})

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
    nav.classList.add("remove")

    if(nav.className = "remove"){
        notscroll.style.overflow = "scroll"
    }
})
    

});
