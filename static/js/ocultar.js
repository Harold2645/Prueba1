
function mensaje(){
    alert("Espera 12 horas a ser activado")
}

document.addEventListener("DOMContentLoaded", ()=>{

    const rol = document.getElementById('rol');
    let ficha = document.getElementById('cajaFicha');

    rol.addEventListener('change', (etiqueta)=>{

        if(etiqueta.target.value == "Aprendiz"){

            console.log("Si paso", ficha)
            ficha.style.display = "flex"
            
            }else{
                console.log("No paso")
                ficha.style.display = "none"
        }

    })

})