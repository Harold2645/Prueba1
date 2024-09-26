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
<<<<<<< HEAD
                const respuesta = await fetch('http://192.168.12.12:5004/consultarol', {
=======
                const respuesta = await fetch('http://192.168.211.166:5004/consultarol', {
>>>>>>> 91fdc61c5dc7bbfd5037df12f8e86224b59331d2
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
