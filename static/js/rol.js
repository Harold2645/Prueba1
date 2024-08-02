document.addEventListener('DOMContentLoaded', () => { 
    const documento = document.getElementById('documento');
    let contra = document.getElementById('cajacontra');
    const noregistrado = document.getElementById('noregistrado');
    const registrado = document.getElementById('registrado');
    const siregistrado = document.getElementById('siregistrado');

        documento.addEventListener('keyup', async (etiqueta)=>{

            console.log(etiqueta.target.value)
            consu = etiqueta.target.value
            if (consu.length > 7 && consu.length < 16){

                const respuesta = await fetch('http://localhost:5004/consultarol', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(consu), // Convierte el objeto a JSON
                    
                });
                
                const result = await respuesta.text();
                console.log("Respuesta:", result)
                
                if(result == "Practicante" || result == "Admin" ){
                    
                    noregistrado.style.display = "none"
                    siregistrado.style.display = "none"
                    contra.style.display = "block"
                    registrado.style.display = "block"
                    
                }else if(result == "Instructor" || result == "Aprendiz" || result == "Trabajador"){
                    contra.style.display = "none"
                    noregistrado.style.display = "none"
                    registrado.style.display = "none"
                    siregistrado.style.display = "block"


                }else if(result == "No existe"){
                    contra.style.display = "none"
                    siregistrado.style.display = "none"
                    registrado.style.display = "none"
                    noregistrado.style.display = "block"
                }
        }

        })
        
    })
