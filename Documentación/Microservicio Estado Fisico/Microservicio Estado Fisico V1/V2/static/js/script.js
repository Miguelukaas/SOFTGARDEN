const registerLink = document.querySelector('.register-link');
const registerForm = document.querySelector('.register-form');

registerLink.addEventListener('click', () => {
    registerForm.classList.toggle('hidden');
});

function mostrarFormulario() {
    document.getElementById('formulario').style.display = 'block';
}

function volverAlMenu() {
    document.getElementById('formulario').style.display = 'none';
}

function mostrarFormulario() {
    document.getElementById('formulario').style.display = 'block';
}

function mostrarFormularioPersonal() {
    document.getElementById('formularioPersonal').style.display = 'block';
}

function volverAlMenu() {
    document.getElementById('formulario').style.display = 'none';
    document.getElementById('formularioPersonal').style.display = 'none';
}

function toggleOpcionesAdministrador() {
    var opciones = document.getElementById("opcionesAdministrador");
    if (opciones.style.display === "none") {
        opciones.style.display = "block";
    } else {
        opciones.style.display = "none";
    }
}

function guardarCambios(button) {
    var fila = button.parentNode.parentNode;
    var celdas = fila.querySelectorAll('td[contenteditable="true"]');
    var nuevosDatos = [];

    celdas.forEach(function(celda) {
        nuevosDatos.push(celda.textContent);
    });

    // Aquí puedes enviar los nuevos datos a través de una solicitud AJAX o hacer lo que necesites con ellos

    alert("Los cambios se han guardado correctamente.");
}

// Verificar si hay datos almacenados en localStorage
if(localStorage.getItem("ninos")) {
    // Si hay datos, cargarlos en la tabla
    document.getElementById("tablaNinos").getElementsByTagName('tbody')[0].innerHTML = localStorage.getItem("ninos");
}

function agregarNiño() {
    // Obtener los valores del formulario
    var nombre = document.getElementById("nombre").value;
    var edad = document.getElementById("edad").value;
    var grupo = document.getElementById("grupo").value;
    var tipoSangre = document.getElementById("tipo_sangre").value;
    var sexo = document.getElementById("sexo").value;
    var padre = document.getElementById("nombrePadre").value;
    var correo = document.getElementById("correo").value;
    var telefono = document.getElementById("telefono").value;
    var comentarios = document.getElementById("comentarios").value;

    // Crear una nueva fila en la tabla
    var tabla = document.getElementById("tablaNinos").getElementsByTagName('tbody')[0];
    var nuevaFila = tabla.insertRow();

    // Insertar celdas con los valores del niño
    nuevaFila.innerHTML = `
        <td contenteditable="true">${nombre}</td>
        <td contenteditable="true">${edad}</td>
        <td contenteditable="true">${grupo}</td>
        <td contenteditable="true">${tipoSangre}</td>
        <td contenteditable="true">${sexo}</td>
        <td contenteditable="true">${padre}</td>
        <td contenteditable="true">${correo}</td>
        <td contenteditable="true">${telefono}</td>
        <td contenteditable="true">${comentarios}</td>
        <td><button onclick="guardarCambios(this)">Guardar</button></td>
    `;

    // Guardar los datos en localStorage
    localStorage.setItem("ninos", tabla.innerHTML);

    // Limpiar el formulario
    document.getElementById("nombre").value = "";
    document.getElementById("edad").value = "";
    document.getElementById("grupo").value = "";
    document.getElementById("tipo_sangre").value = "";
    document.getElementById("sexo").value = "";
    document.getElementById("nombrePadre").value = "";
    document.getElementById("correo").value = "";
    document.getElementById("telefono").value = "";
    document.getElementById("comentarios").value = "";
}
