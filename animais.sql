-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Tempo de geração: 11-Set-2024 às 23:41
-- Versão do servidor: 10.6.5-MariaDB
-- versão do PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `petshop`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `animais`
--

DROP TABLE IF EXISTS `animais`;
CREATE TABLE IF NOT EXISTS `animais` (
  `COD_ANIMAL` int(11) NOT NULL AUTO_INCREMENT,
  `animal` varchar(40) NOT NULL,
  `especie` varchar(40) NOT NULL,
  `raca` varchar(40) NOT NULL,
  `cor_predom` varchar(40) NOT NULL,
  `nascimento` date NOT NULL,
  `observacao` varchar(1000) NOT NULL,
  `foto_animal` varchar(500) NOT NULL,
  `tutor` varchar(40) NOT NULL,
  `fone` varchar(15) NOT NULL,
  PRIMARY KEY (`COD_ANIMAL`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `animais`
--

INSERT INTO `animais` (`COD_ANIMAL`, `animal`, `especie`, `raca`, `cor_predom`, `nascimento`, `observacao`, `foto_animal`, `tutor`, `fone`) VALUES
(2, 'Simba', 'Cachorro', 'Chow-Chow', 'Branco', '2024-09-11', 'Teimoso e preguiçoso', 'C:\\Users\\si\\Desktop\\pedro\\2°Semestre\\LAB_CONF\\projeto1 - pet shop\\imagens\\chow_chow_branco.jpg', 'Pedro', '(14)98172-2145');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
