-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: bm9h8scsip6va76legry-mysql.services.clever-cloud.com    Database: bm9h8scsip6va76legry
-- ------------------------------------------------------
-- Server version	8.0.15-5

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'f41d366d-91e5-11e9-8525-cecd028ee826:1-92332802';

--
-- Table structure for table `categoriamueble`
--

DROP TABLE IF EXISTS `categoriamueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoriamueble` (
  `Nombre_Categoria` varchar(300) NOT NULL,
  `Direccion_Imagen_Categoria` varchar(300) DEFAULT NULL,
  `Descripcion_Categoria` varchar(600) DEFAULT NULL,
  `Titulo_Categoria` varchar(300) DEFAULT NULL,
  `Descuento_Categoria` int(11) DEFAULT NULL,
  PRIMARY KEY (`Nombre_Categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoriamueble`
--

LOCK TABLES `categoriamueble` WRITE;
/*!40000 ALTER TABLE `categoriamueble` DISABLE KEYS */;
INSERT INTO `categoriamueble` VALUES ('0-Otros','Etapas_Carga.png','Una categoria de prueba','Categoria Generica',NULL),('MESAS HOGAR','MESA_NORDICA_3.webp','Las mejores mesas para tu hogar, las mas duras y de confianza','MESAS PARA TU CASA!! DE LA MEJOR CALIDAD',NULL),('Sillas','SillasCategoria.jpg','Sillas que adornan tu hogar, pero ojo, solo para adornar','Sillas de 3 patas, lo ultimo de Europa Nordica',NULL);
/*!40000 ALTER TABLE `categoriamueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagenmueble`
--

DROP TABLE IF EXISTS `imagenmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imagenmueble` (
  `Nombre_Mueble` varchar(300) DEFAULT NULL,
  `Color_Mueble` varchar(300) DEFAULT NULL,
  `Direccion_Imagen_Mueble` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagenmueble`
--

LOCK TABLES `imagenmueble` WRITE;
/*!40000 ALTER TABLE `imagenmueble` DISABLE KEYS */;
INSERT INTO `imagenmueble` VALUES ('Silla Normal','AZUL','MESA_NORDICA_3.webp'),('Silla Normal','AZUL','sillas3Patas1.jpg'),('Silla Normal','AZUL','sillas3Patas2.jpg'),('Mesa Nordica','MARRON','MESA_NORDICA_1.webp'),('Mesa Nordica','MARRON','MESA_NORDICA_2.webp');
/*!40000 ALTER TABLE `imagenmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingresomueble`
--

DROP TABLE IF EXISTS `ingresomueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingresomueble` (
  `Nombre_Mueble` varchar(300) DEFAULT NULL,
  `Color_Mueble` varchar(300) DEFAULT NULL,
  `Cantidad_Ingreso` int(11) DEFAULT NULL,
  `Fecha_Ingreso` datetime NOT NULL,
  PRIMARY KEY (`Fecha_Ingreso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingresomueble`
--

LOCK TABLES `ingresomueble` WRITE;
/*!40000 ALTER TABLE `ingresomueble` DISABLE KEYS */;
INSERT INTO `ingresomueble` VALUES ('Silla Normal','AZUL',14,'2021-11-17 23:12:49'),('Mesa Nordica','MARRON',6,'2021-11-17 23:14:48');
/*!40000 ALTER TABLE `ingresomueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble`
--

DROP TABLE IF EXISTS `mueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mueble` (
  `Nombre_Mueble` varchar(300) NOT NULL,
  `Categoria_Mueble` varchar(300) DEFAULT NULL,
  `Precio_Mueble` float DEFAULT NULL,
  `Descuento_Mueble` int(11) DEFAULT NULL,
  `Descripcion_Corta_Mueble` varchar(300) DEFAULT NULL,
  `Descripcin_Larga_Mueble` varchar(600) DEFAULT NULL,
  `Cantidad_Disponible_Mueble` int(11) DEFAULT NULL,
  PRIMARY KEY (`Nombre_Mueble`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble`
--

LOCK TABLES `mueble` WRITE;
/*!40000 ALTER TABLE `mueble` DISABLE KEYS */;
INSERT INTO `mueble` VALUES ('Mesa Nordica','MESAS HOGAR',14000,15,'Buena mesa, dura 2 lunas rojas y una cuarta menguante','Buena mesa la mejor calidad y dureza, dura 2 lunas rojas y una cuarta menguante , garantia sujeta a solticios nocturnos',6),('Silla Normal','MESAS HOGAR',1400,0,'Sillas de la mejor calidad','Las mejores Sillas, de la mejor calidad, garantia de por vida',14);
/*!40000 ALTER TABLE `mueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `productos_vista_html`
--

DROP TABLE IF EXISTS `productos_vista_html`;
/*!50001 DROP VIEW IF EXISTS `productos_vista_html`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `productos_vista_html` AS SELECT 
 1 AS `Nombre_Mueble`,
 1 AS `Descripcion_Corta_Mueble`,
 1 AS `Descuento_Mueble`,
 1 AS `Precio_Mueble`,
 1 AS `Direccion_Imagen_Mueble`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `productos_vista_html`
--

/*!50001 DROP VIEW IF EXISTS `productos_vista_html`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`uejpo6trlzp13yjr`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `productos_vista_html` AS select `imagenmueble`.`Nombre_Mueble` AS `Nombre_Mueble`,`mueble`.`Descripcion_Corta_Mueble` AS `Descripcion_Corta_Mueble`,`mueble`.`Descuento_Mueble` AS `Descuento_Mueble`,`mueble`.`Precio_Mueble` AS `Precio_Mueble`,`imagenmueble`.`Direccion_Imagen_Mueble` AS `Direccion_Imagen_Mueble` from (`mueble` join `imagenmueble` on((`mueble`.`Nombre_Mueble` = `imagenmueble`.`Nombre_Mueble`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-20 23:55:02
