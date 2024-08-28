<?php

include("db.php");

if(isset($_POST['iniciar_sesion'])){
    $usuario = $_POST['usuario'];
    $contrasena = $_POST['contrasena'];
    
    $cadena = "SELECT * FROM usuario WHERE usuario='$usuario' AND contrasena='$contrasena'";
    $result = $conn->query($cadena);

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if ($row['id_cargo'] == 1) {
            header('Location: indexAdmin.html'); // Administrador
        } elseif ($row['id_cargo'] == 2) {
            header('Location: indexNinera.html'); // Niñera
        } elseif ($row['id_cargo'] == 3) {
            header('Location: indexUser.html'); // Padres
        } elseif ($row['id_cargo'] == 4) {
            header('Location: indexRH.html'); // RH
        } elseif ($row['id_cargo'] == 5) {
            header('Location: indexContabilidad.html'); // Contabilidad
        } elseif ($row['id_cargo'] == 6) {
            header('Location: indexGerente.html'); // Gerente
        } elseif ($row['id_cargo'] == 7) {
            header('Location: indexSecretaria.html'); // Secretaria
        } else {
            echo "Error: Tipo de usuario no reconocido";
        }
    } else {
        echo "Nombre de usuario o contraseña incorrectos";
    }
    // Consulta SQL para obtener el nombre de un usuario específico
$sql = "SELECT nombre FROM usuario WHERE id=10 "; // Cambia "1" por el ID del usuario que quieras mostrar

$resultado = $conexion->query($user);

if ($resultado->num_rows > 0) {
    // Mostrar el nombre en HTML
    $fila = $resultado->fetch_assoc();
    $nombre = $fila["nombre"];
    echo "<p>El nombre es: $nombre</p>";
} else {
    echo "No se encontraron resultados";
}
}

?>