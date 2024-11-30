-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 24-11-2024 a las 01:30:56
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `saludybienestar_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carnet_salud_bebe`
--

CREATE TABLE `carnet_salud_bebe` (
  `ID_Bebe` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Fecha_Nacimiento` date NOT NULL,
  `Peso` decimal(5,2) DEFAULT NULL,
  `Altura` decimal(5,2) DEFAULT NULL,
  `Medicamento` varchar(100) DEFAULT NULL,
  `Observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carnet_salud_bebe`
--

INSERT INTO `carnet_salud_bebe` (`ID_Bebe`, `Nombre`, `Fecha_Nacimiento`, `Peso`, `Altura`, `Medicamento`, `Observaciones`) VALUES
(1, 'Santiago Mora\r\n', '2024-03-20', 7.00, 59.00, 'Tempra infantil cada 12 horas, dramanine en caso de vomito ', 'EL bebe presento vomito una vez por lo que se le dio su medicamento y eventualmente no hubo malestar.'),
(2, 'Sofia Perez ', '2024-09-19', 4.00, 35.00, 'Motrin pediatrico(ibuprobefo)en caso de fiebre, gotas nasales para la congestion nasal y crema para ', 'presento congestion al dormir y se le administraron 3 gotas de su solucion en cada fosa nasal. se le aplico crema al cambiar el pañal. ');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carnet_salud_bebe`
--
ALTER TABLE `carnet_salud_bebe`
  ADD PRIMARY KEY (`ID_Bebe`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
