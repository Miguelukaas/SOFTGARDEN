<?php

include("db.php");

if(isset($_POST['guardar_usr'])){
    $nombre = $_POST['nombre'];
    $correo = $_POST['correo'];
    $contrasena = $_POST['contrasena'];
    $usuario = $_POST['usuario'];

    $query = "INSERT INTO usuario(nombre,correo,contrasena,id_cargo) VALUES('$usuario''$nombre','$correo','$contrasena','3')";
    $result = mysqli_query($conn,$query);

    if(!$result){
            die("ERROR");
    }else{
        header("Location: indexUser.html");
    }

}
?>