-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-11-2024 a las 16:02:19
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
(5, 'Quinto'),
(6, 'Sexto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario primero`
--

CREATE TABLE `horario primero` (
  `día` varchar(30) NOT NULL,
  `hora1` int(11) DEFAULT NULL,
  `hora2` int(11) DEFAULT NULL,
  `hora3` int(11) DEFAULT NULL,
  `hora4` int(11) DEFAULT NULL,
  `hora5` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horario primero`
--

INSERT INTO `horario primero` (`día`, `hora1`, `hora2`, `hora3`, `hora4`, `hora5`) VALUES
('04Jueves', 1, 6, 5, 3, 2),
('01Lunes', 3, 2, 4, 1, 6),
('05Viernes', 4, 1, 6, 5, 3),
('02Martes', 5, 3, 2, 4, 1),
('03Miercoles', 6, 5, 3, 2, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horariosegundo`
--

CREATE TABLE `horariosegundo` (
  `dia` varchar(30) NOT NULL,
  `horarioseg1` int(11) DEFAULT NULL,
  `horarioseg2` int(11) DEFAULT NULL,
  `horarioseg3` int(11) DEFAULT NULL,
  `horarioseg4` int(11) DEFAULT NULL,
  `horarioseg5` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horariosegundo`
--

INSERT INTO `horariosegundo` (`dia`, `horarioseg1`, `horarioseg2`, `horarioseg3`, `horarioseg4`, `horarioseg5`) VALUES
('1Lunes', 11, 9, 8, 10, 7),
('2Martes', 12, 11, 9, 8, 10),
('3Miercoles', 7, 12, 11, 9, 8),
('4Jueves', 10, 7, 12, 11, 9),
('5Viernes', 8, 10, 7, 12, 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horariotercero`
--

CREATE TABLE `horariotercero` (
  `día` varchar(30) NOT NULL,
  `hora1ter` int(11) DEFAULT NULL,
  `hora2ter` int(11) DEFAULT NULL,
  `hora3ter` int(11) DEFAULT NULL,
  `hora4ter` int(11) DEFAULT NULL,
  `hora5ter` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horariotercero`
--

INSERT INTO `horariotercero` (`día`, `hora1ter`, `hora2ter`, `hora3ter`, `hora4ter`, `hora5ter`) VALUES
('01Lunes', 18, 17, 15, 14, 16),
('02Martes', 13, 18, 17, 15, 14),
('03Miercoles', 16, 13, 18, 17, 15),
('04Jueves', 14, 16, 13, 18, 17),
('05Viernes', 15, 14, 16, 13, 18);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `m-g`
--

CREATE TABLE `m-g` (
  `idm-g` int(11) NOT NULL,
  `grado` int(11) NOT NULL,
  `materia` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `m-g`
--

INSERT INTO `m-g` (`idm-g`, `grado`, `materia`) VALUES
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
(30, 5, 6),
(31, 6, 1),
(32, 6, 2),
(33, 6, 3),
(34, 6, 4),
(35, 6, 5),
(36, 6, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `idmateria` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Horas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`idmateria`, `Nombre`, `Horas`) VALUES
(1, 'Ciencias Naturales', 1),
(2, 'Ciencias Sociales', 1),
(3, 'Matemáticas', 1),
(4, 'Lenguaje', 1),
(5, 'Inglés', 1),
(6, 'Educación Física', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `Nombre` varchar(30) NOT NULL,
  `Correo electronico` varchar(50) NOT NULL,
  `Tipo de documento` varchar(30) NOT NULL,
  `N° documento` int(11) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `Fecha nacimiento` date NOT NULL,
  `Grado a cargo` int(11) NOT NULL,
  `Materia a cargo` int(11) NOT NULL,
  `Contrato` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
-- Indices de la tabla `horario primero`
--
ALTER TABLE `horario primero`
  ADD PRIMARY KEY (`día`),
  ADD KEY `fkhorario1_idx` (`hora1`,`hora2`,`hora3`,`hora4`,`hora5`),
  ADD KEY `fkfranja2_idx` (`hora2`),
  ADD KEY `fkfranja31_idx` (`hora3`),
  ADD KEY `fkfranja41_idx` (`hora4`),
  ADD KEY `fkfranja51_idx` (`hora5`);

--
-- Indices de la tabla `horariosegundo`
--
ALTER TABLE `horariosegundo`
  ADD PRIMARY KEY (`dia`),
  ADD KEY `fkfranja21_idx` (`horarioseg1`),
  ADD KEY `fkfanja22_idx` (`horarioseg2`),
  ADD KEY `fkfranja32_idx` (`horarioseg3`),
  ADD KEY `fkfranja42_idx` (`horarioseg4`),
  ADD KEY `fkfranja52_idx` (`horarioseg5`);

--
-- Indices de la tabla `horariotercero`
--
ALTER TABLE `horariotercero`
  ADD PRIMARY KEY (`día`),
  ADD KEY `fkfranja13_idx` (`hora1ter`),
  ADD KEY `fkfranja23_idx` (`hora2ter`),
  ADD KEY `fkfranja33_idx` (`hora3ter`),
  ADD KEY `fkfranja43_idx` (`hora4ter`),
  ADD KEY `fkfranja53_idx` (`hora5ter`);

--
-- Indices de la tabla `m-g`
--
ALTER TABLE `m-g`
  ADD PRIMARY KEY (`idm-g`),
  ADD KEY `fkgrados_idx` (`grado`),
  ADD KEY `fkmaterias_idx` (`materia`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`idmateria`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`Correo electronico`),
  ADD KEY `Materia a cargo` (`Materia a cargo`),
  ADD KEY `Grado a cargo` (`Grado a cargo`);

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
-- AUTO_INCREMENT de la tabla `m-g`
--
ALTER TABLE `m-g`
  MODIFY `idm-g` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

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
-- Filtros para la tabla `horario primero`
--
ALTER TABLE `horario primero`
  ADD CONSTRAINT `fkfranja11` FOREIGN KEY (`hora1`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja21` FOREIGN KEY (`hora2`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja31` FOREIGN KEY (`hora3`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja41` FOREIGN KEY (`hora4`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja51` FOREIGN KEY (`hora5`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `horariosegundo`
--
ALTER TABLE `horariosegundo`
  ADD CONSTRAINT `fkfranja12` FOREIGN KEY (`horarioseg1`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja22` FOREIGN KEY (`horarioseg2`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja32` FOREIGN KEY (`horarioseg3`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja42` FOREIGN KEY (`horarioseg4`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja52` FOREIGN KEY (`horarioseg5`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `horariotercero`
--
ALTER TABLE `horariotercero`
  ADD CONSTRAINT `fkfranja13` FOREIGN KEY (`hora1ter`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja23` FOREIGN KEY (`hora2ter`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja33` FOREIGN KEY (`hora3ter`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja43` FOREIGN KEY (`hora4ter`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkfranja53` FOREIGN KEY (`hora5ter`) REFERENCES `m-g` (`idm-g`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `m-g`
--
ALTER TABLE `m-g`
  ADD CONSTRAINT `fkgrados` FOREIGN KEY (`grado`) REFERENCES `grados` (`Numero`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fkmaterias` FOREIGN KEY (`materia`) REFERENCES `materias` (`idmateria`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD CONSTRAINT `profesores_ibfk_1` FOREIGN KEY (`Materia a cargo`) REFERENCES `materias` (`idmateria`),
  ADD CONSTRAINT `profesores_ibfk_2` FOREIGN KEY (`Grado a cargo`) REFERENCES `grados` (`Numero`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
