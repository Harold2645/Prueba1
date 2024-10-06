document.addEventListener('DOMContentLoaded', () => { 
    const documento = document.getElementById('documento');
    let contra = document.getElementById('cajacontra');
    const noregistrado = document.getElementById('noregistrado');
    const siregistrado = document.getElementById('siregistrado');

        documento.addEventListener('keyup', async (etiqueta)=>{

            console.log(etiqueta.target.value)
            consu = etiqueta.target.value
            if (consu.length > 6 && consu.length < 16){

                // const respuesta = await fetch('http://85.31.231.136:5004/consultarol', {
                const respuesta = await fetch('http://192.168.194.222:5004/consultarol', {
                //const respuesta = await fetch('http://10.206.81.27:5004/consultarol', {
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
                    
                }else if(result == "Instructor" || result == "Aprendiz" || result == "Trabajador"){
                    contra.style.display = "none"
                    noregistrado.style.display = "none"
                    siregistrado.style.display = "block"


                }else if(result == "No existe"){
                    contra.style.display = "none"
                    siregistrado.style.display = "none"
                    noregistrado.style.display = "block"
                }
        }

        })
        
    })
