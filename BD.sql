-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: lojadiscos
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

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

--
-- Table structure for table `Artists`
--

DROP TABLE IF EXISTS `Artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Artists` (
  `artist_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `Country` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`artist_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Artists`
--

LOCK TABLES `Artists` WRITE;
/*!40000 ALTER TABLE `Artists` DISABLE KEYS */;
INSERT INTO `Artists` VALUES (1,'The Beatles','England'),(2,'The Dave Brubeck Quartet','United States'),(3,'Piotr Ilitch Tchaikovsky','Russia'),(4,'David Bowie','England'),(5,'Alcest','France'),(6,'Miles Davis','United States'),(7,'Johannes Brahms','Germany'),(8,'Tangerine Dream','Germany'),(9,'Tom Jobim','Brazil'),(10,'Museo Rosenbach','Italy'),(11,'Led Zeppelin','England'),(12,'Herbie Hancock','United States'),(13,'Igor Stravinsky','Russia'),(14,'Gong','France'),(15,'Pink Floyd','England'),(16,'John Coltrane','United States'),(17,'Ludwig van Beethoven','Germany'),(18,'Kraftwerk','Germany'),(19,'Michael Jackson','United States'),(20,'Yes','England');
/*!40000 ALTER TABLE `Artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Clients`
--

DROP TABLE IF EXISTS `Clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Clients` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `address` varchar(50) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clients`
--

LOCK TABLES `Clients` WRITE;
/*!40000 ALTER TABLE `Clients` DISABLE KEYS */;
INSERT INTO `Clients` VALUES (1,'John Doe','123-456-7890','123 Main St, Anytown','johndoe@email.com'),(2,'Jane Smith','234-567-8901','456 Elm St, Othertown','janesmith@email.com'),(3,'Alice Johnson','345-678-9012','789 Oak St, Anycity','alicej@email.com'),(4,'Bob Brown','456-789-0123','012 Maple St, Othercity','bobbrown@email.com'),(5,'Carol White','567-890-1234','345 Pine St, Somewhere','carolwhite@email.com'),(6,'David Green','678-901-2345','678 Cedar St, Nowhere','davidgreen@email.com'),(7,'Eve Black','789-012-3456','901 Birch St, Anywhere','eveblack@email.com'),(8,'Frank Gray','890-123-4567','234 Spruce St, Everywhere','frankgray@email.com'),(9,'Grace Lee','901-234-5678','567 Ash St, Someplace','gracelee@email.com'),(10,'Henry Ford','012-345-6789','890 Willow St, Thisplace','henryford@email.com');
/*!40000 ALTER TABLE `Clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Discs`
--

DROP TABLE IF EXISTS `Discs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Discs` (
  `disc_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `artist_id` int NOT NULL,
  `genre_id` int NOT NULL,
  `format_id` int NOT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`disc_id`),
  KEY `artist_id` (`artist_id`),
  KEY `genre_id` (`genre_id`),
  KEY `format_id` (`format_id`),
  CONSTRAINT `Discs_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `Artists` (`artist_id`),
  CONSTRAINT `Discs_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `Genres` (`genre_id`),
  CONSTRAINT `Discs_ibfk_3` FOREIGN KEY (`format_id`) REFERENCES `Formats` (`format_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Discs`
--

LOCK TABLES `Discs` WRITE;
/*!40000 ALTER TABLE `Discs` DISABLE KEYS */;
INSERT INTO `Discs` VALUES (1,'Let It Be',1,1,1,119.9),(2,'A Hard Days Night',1,1,1,109.9),(3,'Time Out',2,2,2,64.9),(4,'Swan Lake Suite',3,3,2,34.88),(5,'Stone Flower',9,2,2,69.99),(6,'Wave',9,2,1,89.9),(7,'Zarathustra',10,5,1,19.99),(8,'The Virgin Years',8,4,3,499.99),(9,'Bitches Brew',6,2,1,169.9),(10,'Yellow Submarine',1,1,2,50.5),(11,'Time Further Out',2,2,2,19.77),(12,'The Nutcracker',3,3,2,25.85),(13,'Head Hunters',12,1,1,83.65),(14,'Thriller',19,6,2,45.5),(15,'Animals',15,5,1,119.9),(16,'Low',4,1,5,89.9),(17,'Low',4,1,2,49.9),(18,'Fragile',20,1,2,49.8),(19,'Les Noches',13,3,2,25.55),(20,'Kodama',5,1,5,109.9);
/*!40000 ALTER TABLE `Discs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Formats`
--

DROP TABLE IF EXISTS `Formats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Formats` (
  `format_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`format_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Formats`
--

LOCK TABLES `Formats` WRITE;
/*!40000 ALTER TABLE `Formats` DISABLE KEYS */;
INSERT INTO `Formats` VALUES (1,'Vinyl'),(2,'CD'),(3,'Box'),(4,'Cassette Tape'),(5,'Blueray Audio');
/*!40000 ALTER TABLE `Formats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Genres`
--

DROP TABLE IF EXISTS `Genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Genres` (
  `genre_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Genres`
--

LOCK TABLES `Genres` WRITE;
/*!40000 ALTER TABLE `Genres` DISABLE KEYS */;
INSERT INTO `Genres` VALUES (1,'Rock'),(2,'Jazz'),(3,'Classical'),(4,'Electronic'),(5,'Progressive Rock'),(6,'Pop'),(7,'Hip Hop'),(8,'Blues'),(9,'Reggae'),(10,'Country'),(11,'Folk'),(12,'Latin'),(13,'R&B'),(14,'Metal'),(15,'Funk'),(16,'Soul');
/*!40000 ALTER TABLE `Genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `disc_id` int DEFAULT NULL,
  `client_id` int DEFAULT NULL,
  `date_order` date DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `disc_id` (`disc_id`),
  KEY `client_id` (`client_id`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`disc_id`) REFERENCES `Discs` (`disc_id`),
  CONSTRAINT `Orders_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `Clients` (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES (1,5,10,'2023-11-27'),(2,20,8,'2023-11-28'),(3,14,7,'2023-11-29'),(4,7,2,'2023-11-30'),(5,18,4,'2023-12-01');
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stock`
--

DROP TABLE IF EXISTS `Stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Stock` (
  `disc_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `stock_id` int NOT NULL AUTO_INCREMENT,
  `supplier_id` int DEFAULT NULL,
  PRIMARY KEY (`stock_id`),
  KEY `supplier_id` (`supplier_id`),
  KEY `disc_id` (`disc_id`),
  CONSTRAINT `Stock_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `Suppliers` (`supplier_id`),
  CONSTRAINT `Stock_ibfk_2` FOREIGN KEY (`disc_id`) REFERENCES `Discs` (`disc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stock`
--

LOCK TABLES `Stock` WRITE;
/*!40000 ALTER TABLE `Stock` DISABLE KEYS */;
INSERT INTO `Stock` VALUES (10,17,5,1),(13,19,8,1),(5,1,10,2),(11,16,12,2),(6,2,15,3),(12,3,18,3),(3,15,20,3),(14,20,22,2),(7,9,25,1),(2,6,30,2),(15,5,33,3),(8,18,35,2),(4,7,40,1),(9,4,45,3),(1,12,50,1);
/*!40000 ALTER TABLE `Stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suppliers`
--

DROP TABLE IF EXISTS `Suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Suppliers` (
  `supplier_id` int NOT NULL AUTO_INCREMENT,
  `phone` varchar(12) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `cnpj` char(14) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suppliers`
--

LOCK TABLES `Suppliers` WRITE;
/*!40000 ALTER TABLE `Suppliers` DISABLE KEYS */;
INSERT INTO `Suppliers` VALUES (1,'123-456-7890','supplier1@example.com','123 Main Street, Cityville','12345678901234','Supplier One'),(2,'987-654-3210','supplier2@example.com','456 Oak Avenue, Townsville','56789012345678','Supplier Two'),(3,'555-123-7890','supplier3@example.com','789 Pine Lane, Villageton','90123456789012','Supplier Three'),(4,'111-222-3333','supplier4@example.com','999 Elm Street, Hamletville','34567890123456','Supplier Four'),(5,'777-888-9999','supplier5@example.com','234 Cedar Road, Boroughburg','78901234567890','Supplier Five');
/*!40000 ALTER TABLE `Suppliers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-28 14:36:49
