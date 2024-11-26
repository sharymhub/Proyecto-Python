-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-11-2024 a las 23:21:16
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `giebd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `n° identificación` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Fecha nacimiento` date NOT NULL,
  `Lugar nacimiento` varchar(50) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Genero` text NOT NULL,
  `Direccion` varchar(60) NOT NULL,
  `Grupo sanguineo` varchar(10) NOT NULL,
  `NombreMadre` varchar(50) NOT NULL,
  `TelefonoMadre` int(11) NOT NULL,
  `CorreoMadre` varchar(50) NOT NULL,
  `OcupacionMadre` varchar(30) NOT NULL,
  `DireccionMadre` varchar(60) NOT NULL,
  `NombrePadre` varchar(50) NOT NULL,
  `TelefonoPadre` int(11) NOT NULL,
  `CorreoPadre` varchar(50) NOT NULL,
  `OcupacionPadre` varchar(30) NOT NULL,
  `DireccionPadre` varchar(50) NOT NULL,
  `Grado` int(11) NOT NULL,
  `Alergias` varchar(30) NOT NULL,
  `Discapacidad fisica` varchar(30) NOT NULL,
  `Discapacidad mental` varchar(30) NOT NULL,
  `Medicamentos` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grados`
--

CREATE TABLE `grados` (
  `Numero` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `grados`
--

INSERT INTO `grados` (`Numero`, `Nombre`) VALUES
(1, 'Primero'),
(2, 'Segundo'),
(3, 'Tercero'),
(4, 'Cuarto'),
(5, 'Quinto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horarios`
--

CREATE TABLE `horarios` (
  `idhorarios` int(11) NOT NULL,
  `hora` time DEFAULT NULL,
  `Lunes` int(11) DEFAULT NULL,
  `Martes` int(11) DEFAULT NULL,
  `Miércoles` int(11) DEFAULT NULL,
  `Jueves` int(11) DEFAULT NULL,
  `Viernes` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horarios`
--

INSERT INTO `horarios` (`idhorarios`, `hora`, `Lunes`, `Martes`, `Miércoles`, `Jueves`, `Viernes`) VALUES
(1, '07:00:00', 3, 5, 6, 1, 4),
(2, '07:00:00', 11, 12, 7, 10, 8),
(3, '07:00:00', 18, 13, 16, 14, 15),
(4, '08:00:00', 2, 3, 5, 6, 1),
(5, '08:00:00', 9, 11, 12, 7, 10),
(6, '08:00:00', 17, 18, 13, 16, 14),
(7, '09:00:00', 4, 2, 3, 5, 6),
(8, '09:00:00', 8, 9, 11, 12, 7),
(9, '09:00:00', 15, 17, 18, 13, 16),
(10, '10:30:00', 1, 4, 2, 3, 5),
(11, '10:30:00', 10, 8, 9, 11, 12),
(12, '10:30:00', 14, 15, 17, 18, 13),
(13, '11:30:00', 6, 1, 4, 2, 3),
(14, '11:30:00', 7, 10, 8, 9, 11),
(15, '11:30:00', 16, 14, 15, 17, 18);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `m-g`
--

CREATE TABLE `m-g` (
  `idmg` int(11) NOT NULL,
  `grado` int(11) NOT NULL,
  `materia` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `m-g`
--

INSERT INTO `m-g` (`idmg`, `grado`, `materia`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 2, 1),
(8, 2, 2),
(9, 2, 3),
(10, 2, 4),
(11, 2, 5),
(12, 2, 6),
(13, 3, 1),
(14, 3, 2),
(15, 3, 3),
(16, 3, 4),
(17, 3, 5),
(18, 3, 6),
(19, 4, 1),
(20, 4, 2),
(21, 4, 3),
(22, 4, 4),
(23, 4, 5),
(24, 4, 6),
(25, 5, 1),
(26, 5, 2),
(27, 5, 3),
(28, 5, 4),
(29, 5, 5),
(30, 5, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `idmateria` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `idProfesor` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`idmateria`, `Nombre`, `idProfesor`) VALUES
(1, 'Ciencias Naturales', 'loren4@gmail.com'),
(2, 'Ciencias Sociales', 'susana@gmail.com'),
(3, 'Matemáticas', 'juan_dcastroc@soy.sena.edu.co'),
(4, 'Lenguaje', 'Fulan00@gmail.com'),
(5, 'Inglés', 'FulanaM@gmail.com'),
(6, 'Educación Física', 'pepita@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `Nombre` varchar(30) NOT NULL,
  `Correo_electronico` varchar(50) NOT NULL,
  `Tipo de documento` varchar(10) NOT NULL,
  `N° documento` int(11) NOT NULL,
  `Telefono` double NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `Fecha nacimiento` date NOT NULL,
  `Grado a cargo` int(11) DEFAULT NULL,
  `Materia a cargo` int(11) DEFAULT NULL,
  `Contrato` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`Nombre`, `Correo_electronico`, `Tipo de documento`, `N° documento`, `Telefono`, `Direccion`, `Fecha nacimiento`, `Grado a cargo`, `Materia a cargo`, `Contrato`) VALUES
('Fulano Mantilla', 'Fulan00@gmail.com', 'C.C', 1058465212, 44878755, 'Tangamandapio', '2000-05-23', 4, 4, '2024-11-25'),
('Fulana Mantilla', 'FulanaM@gmail.com', 'C.C', 1059447855, 54454541, 'Sapo', '2000-05-24', 5, 5, '2024-11-25'),
('Juan David Castro', 'juan_dcastroc@soy.sena.edu.co', 'C.C', 1095421120, 14523214, 'Molinos Bajos', '2004-08-11', 3, 3, '2024-11-25'),
('Lorena Torres ', 'loren4@gmail.com', 'C.C', 1005336365, 4654821, 'nose', '1999-05-23', 2, 1, '2021-11-25'),
('Pepa Suarez ', 'pepita@gmail.com', 'C.C', 1060211252, 15454544, 'Sapa', '1995-06-15', NULL, 6, '2024-11-25'),
('Susana Pérez', 'susana@gmail.com', 'C.C', 1002345585, 1324567, 'Quinta Porra', '1998-10-17', 1, 2, '2024-11-12');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `Correo` varchar(50) NOT NULL,
  `Nombreusuario` varchar(30) NOT NULL,
  `Contraseña` varchar(20) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Rol` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Correo`, `Nombreusuario`, `Contraseña`, `Telefono`, `Rol`) VALUES
('Fulan00@gmail.com', 'Fun00', '1245', 77875451, 'Profesor'),
('FulanaM@gmail.com', 'Fully', '9512', 12145457, 'Profesor'),
('juan_dcastroc@soy.sena.edu.co', 'MrRacoon', '7894', 14523214, 'Profesor'),
('loren4@gmail.com', 'LoRe', '1597', 22542101, 'Profesor'),
('pepita@gmail.com', 'Pepa', '7534', 21321245, 'Profesor'),
('pepito@gmail.com', 'Pepe', '1234', 20054854, 'Administrador'),
('susana@gmail.com', 'SuSi', '4567', 31021321, 'Profesor');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`n° identificación`),
  ADD KEY `GradoEstudiantes` (`Grado`);

--
-- Indices de la tabla `grados`
--
ALTER TABLE `grados`
  ADD PRIMARY KEY (`Numero`);

--
-- Indices de la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`idhorarios`),
  ADD KEY `fklunes_idx` (`Lunes`),
  ADD KEY `fkmartes_idx` (`Martes`),
  ADD KEY `fkmiercoles_idx` (`Miércoles`),
  ADD KEY `fkjueves_idx` (`Jueves`),
  ADD KEY `fkviernes_idx` (`Viernes`);

--
-- Indices de la tabla `m-g`
--
ALTER TABLE `m-g`
  ADD PRIMARY KEY (`idmg`),
  ADD KEY `fkgrados_idx` (`grado`),
  ADD KEY `fkmaterias_idx` (`materia`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`idmateria`),
  ADD KEY `fkprofe_idx` (`idProfesor`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`Correo_electronico`),
  ADD KEY `fkmateriacargo_idx` (`Materia a cargo`),
  ADD KEY `fkgradocargo_idx` (`Grado a cargo`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `grados`
--
ALTER TABLE `grados`
  MODIFY `Numero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `horarios`
--
ALTER TABLE `horarios`
  MODIFY `idhorarios` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `idmateria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `GradoEstudiantes` FOREIGN KEY (`Grado`) REFERENCES `grados` (`Numero`);

--
-- Filtros para la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD CONSTRAINT `fkjueves` FOREIGN KEY (`Jueves`) REFERENCES `m-g` (`idmg`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fklunes` FOREIGN KEY (`Lunes`) REFERENCES `m-g` (`idmg`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkmartes` FOREIGN KEY (`Martes`) REFERENCES `m-g` (`idmg`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkmiercoles` FOREIGN KEY (`Miércoles`) REFERENCES `m-g` (`idmg`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkviernes` FOREIGN KEY (`Viernes`) REFERENCES `m-g` (`idmg`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `m-g`
--
ALTER TABLE `m-g`
  ADD CONSTRAINT `fkgrados` FOREIGN KEY (`grado`) REFERENCES `grados` (`Numero`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkmaterias` FOREIGN KEY (`materia`) REFERENCES `materias` (`idmateria`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `materias`
--
ALTER TABLE `materias`
  ADD CONSTRAINT `fkprofe` FOREIGN KEY (`idProfesor`) REFERENCES `profesores` (`Correo_electronico`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD CONSTRAINT `fkgradocargo` FOREIGN KEY (`Grado a cargo`) REFERENCES `grados` (`Numero`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkmateriacargo` FOREIGN KEY (`Materia a cargo`) REFERENCES `materias` (`idmateria`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkusuario` FOREIGN KEY (`Correo_electronico`) REFERENCES `usuarios` (`Correo`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
