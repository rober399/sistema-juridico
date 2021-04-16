-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-11-2019 a las 20:12:50
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `despacho`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `DUI` int(11) NOT NULL,
  `Nombres` varchar(20) NOT NULL,
  `Apellidos` varchar(20) NOT NULL,
  `Telefono` int(12) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `NombreUsuario` varchar(20) NOT NULL,
  `Contraseña` varchar(20) NOT NULL,
  `Correo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `administradores`
--

INSERT INTO `administradores` (`DUI`, `Nombres`, `Apellidos`, `Telefono`, `Direccion`, `NombreUsuario`, `Contraseña`, `Correo`) VALUES
(1211, 'Roberto', 'Orellana', 65453, 'sensuntepeque', 'Rober', '123', 'roberssmelendez@live'),
(1212, 'Luis', 'Zavala', 12121, 'sensuntepeque', 'luis', 'admin', 'luis@gmail.com'),
(32312, 'Jonathan ', 'Arce', 342342, 'Sensuntepeque', 'Jonathan', '1234', 'jonathan28josue@gmai'),
(54232, 'Miguel', 'Rodriguez', 5342, 'Sensuntepeque', 'Miguel', '123456', 'migue@gmail.com'),
(52432658, 'jose roberto', 'orellana rodriguez ', 60168645, 'guacotecti', 'joserober', '987', 'roberore99@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `ID` int(11) NOT NULL,
  `Fecha_cita` date NOT NULL,
  `Hora_Cita` varchar(8) NOT NULL,
  `Dui_cliente` int(11) NOT NULL,
  `Dui_admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `citas`
--

INSERT INTO `citas` (`ID`, `Fecha_cita`, `Hora_Cita`, `Dui_cliente`, `Dui_admin`) VALUES
(1, '2019-11-23', '9:00 am', 1231, 1211),
(2, '2019-11-30', '10:00 am', 23422, 1212),
(3, '2019-11-25', '2:00PM', 121212, 1211),
(4, '2019-11-26', '9:30 am', 23121, 1211),
(5, '2019-11-26', '9:00 am', 1231, 54232);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `Dui` int(11) NOT NULL,
  `Nombres` varchar(20) NOT NULL,
  `Apellidos` varchar(20) NOT NULL,
  `Telefono` int(10) NOT NULL,
  `Dui_Admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`Dui`, `Nombres`, `Apellidos`, `Telefono`, `Dui_Admin`) VALUES
(1231, 'Luis', 'Zavala', 53342, 1211),
(23121, 'Jonathan', 'Arce', 2323, 1212),
(23422, 'Roberto', 'Orellana', 4243523, 1212),
(121212, 'Miguel', 'Rodriguez', 2212, 1212),
(1243322, 'Luis', 'Zavala', 7534232, 52432658);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `Id` int(11) NOT NULL,
  `DescripcionS` varchar(40) NOT NULL,
  `Costo` int(3) NOT NULL,
  `DUI_Admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `servicios`
--

INSERT INTO `servicios` (`Id`, `DescripcionS`, `Costo`, `DUI_Admin`) VALUES
(1, 'Asesoria', 100, 1211),
(2, 'Herencias pues', 200, 1211),
(3, 'Otra herencias ', 233, 1212),
(4, 'Hacete cargo del cipote', 500, 1211),
(5, 'compra venta', 100, 52432658);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio_cliente`
--

CREATE TABLE `servicio_cliente` (
  `Id` int(11) NOT NULL,
  `Dui_cliente` int(11) NOT NULL,
  `Id_sevicio` int(11) NOT NULL,
  `Estado_pago` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `servicio_cliente`
--

INSERT INTO `servicio_cliente` (`Id`, `Dui_cliente`, `Id_sevicio`, `Estado_pago`) VALUES
(1, 1231, 1, 'Pago pendiente'),
(2, 23121, 2, 'Pago pendiente'),
(3, 23422, 3, 'Pago cancelado'),
(4, 1231, 1, 'Pago cancelado'),
(9, 1231, 1, 'Pago pendiente'),
(10, 1231, 4, 'Pago cancelado');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`DUI`);

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Dui_cliente` (`Dui_cliente`),
  ADD KEY `Dui_admin` (`Dui_admin`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`Dui`),
  ADD KEY `Dui_Admin` (`Dui_Admin`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `DUI_Admin` (`DUI_Admin`);

--
-- Indices de la tabla `servicio_cliente`
--
ALTER TABLE `servicio_cliente`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Dui_cliente` (`Dui_cliente`),
  ADD KEY `Id_sevicio` (`Id_sevicio`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `servicio_cliente`
--
ALTER TABLE `servicio_cliente`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citas`
--
ALTER TABLE `citas`
  ADD CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`Dui_cliente`) REFERENCES `cliente` (`Dui`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`Dui_admin`) REFERENCES `administradores` (`DUI`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`Dui_Admin`) REFERENCES `administradores` (`DUI`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD CONSTRAINT `servicios_ibfk_1` FOREIGN KEY (`DUI_Admin`) REFERENCES `administradores` (`DUI`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `servicio_cliente`
--
ALTER TABLE `servicio_cliente`
  ADD CONSTRAINT `servicio_cliente_ibfk_1` FOREIGN KEY (`Dui_cliente`) REFERENCES `cliente` (`Dui`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `servicio_cliente_ibfk_2` FOREIGN KEY (`Id_sevicio`) REFERENCES `servicios` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
