-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 3.7.198.191    Database: bu-training
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',2,'add_permission'),(2,'Can change permission',2,'change_permission'),(3,'Can delete permission',2,'delete_permission'),(4,'Can view permission',2,'view_permission'),(5,'Can add group',3,'add_group'),(6,'Can change group',3,'change_group'),(7,'Can delete group',3,'delete_group'),(8,'Can view group',3,'view_group'),(9,'Can add user',4,'add_user'),(10,'Can change user',4,'change_user'),(11,'Can delete user',4,'delete_user'),(12,'Can view user',4,'view_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can view content type',5,'view_contenttype'),(17,'Can add category_ hari',8,'add_category_hari'),(18,'Can change category_ hari',8,'change_category_hari'),(19,'Can delete category_ hari',8,'delete_category_hari'),(20,'Can view category_ hari',8,'view_category_hari'),(21,'Can add products_ hari',7,'add_products_hari'),(22,'Can change products_ hari',7,'change_products_hari'),(23,'Can delete products_ hari',7,'delete_products_hari'),(24,'Can view products_ hari',7,'view_products_hari'),(25,'Can add log entry',1,'add_logentry'),(26,'Can change log entry',1,'change_logentry'),(27,'Can delete log entry',1,'delete_logentry'),(28,'Can view log entry',1,'view_logentry'),(29,'Can add session',6,'add_session'),(30,'Can change session',6,'change_session'),(31,'Can delete session',6,'delete_session'),(32,'Can view session',6,'view_session'),(33,'Can add cart_hari',9,'add_cart_hari'),(34,'Can change cart_hari',9,'change_cart_hari'),(35,'Can delete cart_hari',9,'delete_cart_hari'),(36,'Can view cart_hari',9,'view_cart_hari'),(37,'Can add favourite_hari',10,'add_favourite_hari'),(38,'Can change favourite_hari',10,'change_favourite_hari'),(39,'Can delete favourite_hari',10,'delete_favourite_hari'),(40,'Can view favourite_hari',10,'view_favourite_hari'),(41,'Can add book_project',11,'add_book_project'),(42,'Can change book_project',11,'change_book_project'),(43,'Can delete book_project',11,'delete_book_project'),(44,'Can view book_project',11,'view_book_project'),(45,'Can add order',12,'add_order'),(46,'Can change order',12,'change_order'),(47,'Can delete order',12,'delete_order'),(48,'Can view order',12,'view_order'),(49,'Can add order item',13,'add_orderitem'),(50,'Can change order item',13,'change_orderitem'),(51,'Can delete order item',13,'delete_orderitem'),(52,'Can view order item',13,'view_orderitem'),(53,'Can add product image',14,'add_productimage'),(54,'Can change product image',14,'change_productimage'),(55,'Can delete product image',14,'delete_productimage'),(56,'Can view product image',14,'view_productimage'),(57,'Can add wishlist',15,'add_wishlist'),(58,'Can change wishlist',15,'change_wishlist'),(59,'Can delete wishlist',15,'delete_wishlist'),(60,'Can view wishlist',15,'view_wishlist'),(61,'Can add wishlist item',16,'add_wishlistitem'),(62,'Can change wishlist item',16,'change_wishlistitem'),(63,'Can delete wishlist item',16,'delete_wishlistitem'),(64,'Can view wishlist item',16,'view_wishlistitem'),(65,'Can add rest_products',17,'add_rest_products'),(66,'Can change rest_products',17,'change_rest_products'),(67,'Can delete rest_products',17,'delete_rest_products'),(68,'Can view rest_products',17,'view_rest_products'),(69,'Can add book project',18,'add_bookproject'),(70,'Can change book project',18,'change_bookproject'),(71,'Can delete book project',18,'delete_bookproject'),(72,'Can view book project',18,'view_bookproject'),(73,'Can add book images',19,'add_bookimages'),(74,'Can change book images',19,'change_bookimages'),(75,'Can delete book images',19,'delete_bookimages'),(76,'Can view book images',19,'view_bookimages');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `unique_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$ANPpcK1NJQ9o51r8sy7pT2$5e7o6Jo0TWOGFzTJ8C3vMe7ZY7WR6s4EqCxFManf/Hc=','2024-08-26 04:53:36.722021',1,'hari','','','hari@gmail.com',1,1,'2024-07-01 09:02:37.911768'),(3,'pbkdf2_sha256$720000$EVhKXZL0IweegkzxXpVqaT$faEn3+asCGpVEgrexZlKMKUpxX4oLlXkVzT8nCgDiw4=','2024-08-26 04:54:43.443152',0,'buvi','','','buvi@gmail.com',0,1,'2024-07-09 05:38:39.717418'),(5,'pbkdf2_sha256$720000$TiX8ksB09fKCmXpLUyrfQ9$NX4BgPagxPnn0/EZKquszDgKoA3hve2nk6zHf357/eo=','2024-07-30 12:15:59.282105',0,'kaviya','','','kaviya@gmail.com',0,1,'2024-07-22 10:05:03.040020'),(7,'pbkdf2_sha256$720000$dUWWGeMO9QpPrFYJibXLP4$7uBiLBB7WyQUqpBnBKx/i7xuZTUTRwN+up4o/g3kxvs=','2024-08-13 12:01:23.622629',0,'ragavi','','','ragavi@gmail.com',0,1,'2024-08-01 07:26:25.279786'),(9,'pbkdf2_sha256$720000$iC0MDmNJkX705wkoEbKOrD$iq/6D4KvjDYeLGn+qnx3jZPGXklWfiV3qPNYQ84xNFw=','2024-08-01 07:35:55.541892',0,'priya','','','Priya@gmail.com',0,1,'2024-08-01 07:35:31.617049'),(11,'pbkdf2_sha256$720000$LmatLFLje309NmuTXLazwX$sSAVLusAoA6C/Pg6EIhuXvPFKQV1aYlvX3/ypWXrYJg=','2024-08-16 05:03:45.559307',0,'Hariharan','','','hariharan2445@gmail.com',0,1,'2024-08-07 06:45:27.214733');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-07-29 08:14:13.294598','34','Shirt for men',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Shirt for men\"}}]',7,1),(2,'2024-07-29 08:15:16.473825','33','Saree',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Saree\"}}]',7,1),(3,'2024-07-29 08:19:36.506694','32','lehanga',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for lehanga\"}}]',7,1),(4,'2024-07-29 08:19:47.958004','31','van heusen suit for men',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for van heusen suit for men\"}}]',7,1),(5,'2024-07-29 08:37:51.577081','30','crompton water heater',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for crompton water heater\"}}]',7,1),(6,'2024-07-29 08:39:13.038415','29','Sony Bravia tv',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Sony Bravia tv\"}}]',7,1),(7,'2024-07-29 08:39:45.344240','28','LG oven',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for LG oven\"}}]',7,1),(8,'2024-07-29 08:39:46.506557','28','LG oven',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for LG oven\"}}]',7,1),(9,'2024-07-29 08:40:09.209625','27','samsung refrigerator',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for samsung refrigerator\"}}]',7,1),(10,'2024-07-29 08:41:02.709504','28','LG oven',2,'[{\"deleted\": {\"name\": \"product image\", \"object\": \"Image for LG oven\"}}]',7,1),(11,'2024-07-29 08:42:42.558481','26','samsung washing machine',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for samsung washing machine\"}}]',7,1),(12,'2024-07-29 08:42:57.876300','25','maggi',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for maggi\"}}]',7,1),(13,'2024-07-29 08:43:30.627419','24','kissan tomato ketchup',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for kissan tomato ketchup\"}}]',7,1),(14,'2024-07-29 08:43:45.097099','23','wheat flour',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for wheat flour\"}}]',7,1),(15,'2024-07-29 08:43:58.026882','22','Spices',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Spices\"}}]',7,1),(16,'2024-07-29 08:44:14.438078','21','Sunflower Oil 5 Ltr',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Sunflower Oil 5 Ltr\"}}]',7,1),(17,'2024-07-29 08:44:32.194234','20','RPM Wireless Mouse',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for RPM Wireless Mouse\"}}]',7,1),(18,'2024-07-29 08:44:54.890940','18','ThinkPad X1',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for ThinkPad X1\"}}]',7,1),(19,'2024-07-29 08:45:06.832187','19','Zebronics Keyboard',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Zebronics Keyboard\"}}]',7,1),(20,'2024-07-29 08:45:26.042042','17','GoPro HERO12',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for GoPro HERO12\"}}]',7,1),(21,'2024-07-29 08:45:40.038547','16','Noise Smart Watch',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Noise Smart Watch\"}}]',7,1),(22,'2024-07-29 08:45:52.458748','15','samsung powerbank',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for samsung powerbank\"}}]',7,1),(23,'2024-07-29 08:46:23.372899','14','Apple Magsafe',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Apple Magsafe\"}}]',7,1),(24,'2024-07-29 08:46:38.700274','13','boAt Type C Charger',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for boAt Type C Charger\"}}]',7,1),(25,'2024-07-29 08:46:53.802651','12','AirPods Pro',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for AirPods Pro\"}}]',7,1),(26,'2024-07-29 08:47:13.168803','11','Skullcandy Dime 3 earbuds',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Skullcandy Dime 3 earbuds\"}}]',7,1),(27,'2024-07-29 08:47:29.351340','10','Huawei Pura 70 Ultra 5G',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Huawei Pura 70 Ultra 5G\"}}]',7,1),(28,'2024-07-29 08:47:43.630296','9','Honor X9b',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Honor X9b\"}}]',7,1),(29,'2024-07-29 08:48:02.009103','8','OnePlus 12',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for OnePlus 12\"}}]',7,1),(30,'2024-07-29 08:48:16.677228','7','iPhone 15 Pro Max',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for iPhone 15 Pro Max\"}}]',7,1),(31,'2024-07-29 08:48:35.950012','6','Oppo Reno 10 Pro',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Oppo Reno 10 Pro\"}}]',7,1),(32,'2024-07-29 08:48:52.875861','5','Samsung s24 ultra',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Samsung s24 ultra\"}}]',7,1),(33,'2024-07-29 08:49:09.847806','4','vivo X100 Pro',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for vivo X100 Pro\"}}]',7,1),(34,'2024-07-29 08:49:24.235755','3','Nokia X30 5G',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Nokia X30 5G\"}}]',7,1),(35,'2024-07-29 08:49:41.171811','2','realme 12 Pro 5G',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for realme 12 Pro 5G\"}}]',7,1),(36,'2024-07-29 08:49:51.151078','1','REDMI 9i Sport',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for REDMI 9i Sport\"}}]',7,1),(37,'2024-07-31 09:35:46.440758','1','REDMI 9i Sport',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for REDMI 9i Sport\"}}]',7,1),(38,'2024-07-31 09:38:24.057969','1','REDMI 9i Sport',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for REDMI 9i Sport\"}}]',7,1),(39,'2024-07-31 09:41:47.510959','1','REDMI 9i Sport',2,'[{\"deleted\": {\"name\": \"product image\", \"object\": \"Image for REDMI 9i Sport\"}}]',7,1),(40,'2024-07-31 09:44:52.771639','2','realme 12 Pro 5G',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for realme 12 Pro 5G\"}}]',7,1),(41,'2024-07-31 09:45:08.091855','3','Nokia X30 5G',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Nokia X30 5G\"}}]',7,1),(42,'2024-07-31 09:50:00.415013','4','vivo X100 Pro',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for vivo X100 Pro\"}}]',7,1),(43,'2024-07-31 09:53:38.688253','5','Samsung s24 ultra',2,'[{\"added\": {\"name\": \"product image\", \"object\": \"Image for Samsung s24 ultra\"}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(11,'book_app','book_project'),(19,'book_app','bookimages'),(18,'book_app','bookproject'),(5,'contenttypes','contenttype'),(17,'rest_app','rest_products'),(6,'sessions','session'),(9,'shop_app','cart_hari'),(8,'shop_app','category_hari'),(10,'shop_app','favourite_hari'),(12,'shop_app','order'),(13,'shop_app','orderitem'),(14,'shop_app','productimage'),(7,'shop_app','products_hari'),(15,'shop_app','wishlist'),(16,'shop_app','wishlistitem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (19,'shop_app','0001_initial','2024-07-01 08:01:26.027482'),(21,'contenttypes','0001_initial','2024-07-10 07:10:35.001643'),(22,'auth','0001_initial','2024-07-10 07:11:41.306020'),(26,'contenttypes','0002_remove_content_type_name','2024-07-10 07:17:02.477564'),(38,'sessions','0001_initial','2024-07-10 07:18:14.052055'),(39,'shop_app','0002_cart_hari','2024-07-10 07:19:46.444350'),(40,'shop_app','0003_favourite_hari','2024-07-10 07:19:53.817197'),(41,'shop_app','0004_alter_favourite_hari_product','2024-07-18 07:13:10.516182'),(42,'book_app','0001_initial','2024-07-19 09:19:55.686587'),(47,'auth','0002_alter_permission_name_max_length','2024-07-29 07:42:14.867980'),(48,'auth','0003_alter_user_email_max_length','2024-07-29 07:42:14.908409'),(49,'auth','0004_alter_user_username_opts','2024-07-29 07:42:14.952408'),(50,'auth','0005_alter_user_last_login_null','2024-07-29 07:42:14.991873'),(51,'auth','0006_require_contenttypes_0002','2024-07-29 07:42:15.033689'),(52,'auth','0007_alter_validators_add_error_messages','2024-07-29 07:42:15.075829'),(53,'auth','0008_alter_user_username_max_length','2024-07-29 07:42:15.114722'),(54,'auth','0009_alter_user_last_name_max_length','2024-07-29 07:42:15.153081'),(55,'auth','0010_alter_group_name_max_length','2024-07-29 07:42:15.192616'),(56,'auth','0011_update_proxy_permissions','2024-07-29 07:42:15.231866'),(57,'auth','0012_alter_user_first_name_max_length','2024-07-29 07:42:15.273428'),(58,'admin','0001_initial','2024-07-29 07:51:53.167761'),(59,'admin','0002_logentry_remove_auto_add','2024-07-29 07:51:53.230899'),(60,'admin','0003_logentry_add_action_flag_choices','2024-07-29 07:51:53.286502'),(61,'shop_app','0002_cart_hari_favourite_hari','2024-07-29 07:51:54.082897'),(62,'shop_app','0003_order_orderitem','2024-07-29 07:51:54.728438'),(63,'shop_app','0004_order_name','2024-07-29 07:51:54.916643'),(64,'shop_app','0005_remove_products_hari_product_image_productimage','2024-07-29 07:51:55.300985'),(65,'book_app','0002_bookproject_delete_book_project','2024-08-08 15:21:16.994895'),(69,'shop_app','0006_wishlist_wishlistitem','2024-08-12 05:17:18.766294'),(70,'rest_app','0001_initial','2024-08-14 09:52:09.506010');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('68fq3n69euheqwhguwiea8ti9fx8701b','.eJxVjDEOwjAMRe-SGUVxQI7LyM4ZIsdxSAGlUtNOiLtDpQ6w_vfef5nI61Lj2nWOYzZnA-bwuyWWh7YN5Du322Rlass8JrspdqfdXqesz8vu_h1U7vVbO2F1BQowahBkxhSGQTRj8gSZMBMcT-iL8wiU2AkpSVERD0oazPsDBQ44wg:1sOyEH:4bYl63FXklZZ7XAL61MAUEwcTJfq5B5A2llfet29N4o','2024-07-17 11:32:53.752799'),('gnwybrvbwb87wh0opu8e8pomgu01p1dl','.eJxVjMsOwiAQRf-FtSHg8HTp3m8gMAxSNZCUdmX8d9ukC93ec859sxDXpYZ10BymzC4M2Ol3SxGf1HaQH7HdO8felnlKfFf4QQe_9Uyv6-H-HdQ46lYXLzZZEGkLBjI6iAZiEsJbiQmlxaKSRKeM9uCktAoJrDyD1cVrodjnC-pMNz0:1sR9Xe:3p7o5vfwv_yPc7lTpDJLFIvImjPe8I3Q7HMp5IRYk1Q','2024-07-23 12:01:54.612648'),('ncodw60ple3wgbtizycbnqsdn5dec44u','.eJxVjDEOwjAMRe-SGUVxQI7LyM4ZIsdxSAGlUtNOiLtDpQ6w_vfef5nI61Lj2nWOYzZnA-bwuyWWh7YN5Du322Rlass8JrspdqfdXqesz8vu_h1U7vVbO2F1BQowahBkxhSGQTRj8gSZMBMcT-iL8wiU2AkpSVERD0oazPsDBQ44wg:1sYJov:BIcFsEmUAytt04iLdEflMMhUK65qkPk-JZPAGrC_mPA','2024-08-12 06:25:21.027291'),('47hkqqidlyxzz70602fs1ry7kh4m9jgq','.eJxVjMEKwjAQRP8l5xKSKNttj979ApGy2WxsVRpIUi_iv9tCD3obZt68txpoqeOwFMnDFFSvrGp-O0_8kHkbwp3mW9Kc5ponrzdE72vR5xTkedrZP8FIZVzfhklMtNESSMtABL7tOpYA3qENCAHt4QguGgcWPRlGQY7C7KygtKs00isteapSVH-5Noop1y19vj0gQXg:1sYKlf:py3vOVX_HlwVB_rQXSoCihGvUXBVofg9dGqglmoKNrY','2024-08-12 07:26:03.893660'),('dgiwkne74u41xzfwztmilg05zkwugn13','.eJxVjE0OgjAYRO_SNWlKkVJcuvcExpDvr4IamrTFjfHuQsJCd5OZN--tBljKOCxZ0jCxOqpaVb8dAj1k3ga-w3yLmuJc0oR6Q_S-Zn2OLM_Tzv4JRsjj-g4d9TUZct45OIiz3Jo21F1jbBBBtrZDZIPkvaPGAAjapiViBumt96s0wCsuaSqS1fFyrRRBKlv6fAEpx0Fs:1sari0:urLB8U7GEeTzICjVsLhoTGFTEJRixsbovQKm92gl5WU','2024-08-19 07:00:44.542612'),('2eblvbbq4f7qa27lgshdiie2gpg1cwvd','eyJzaGFyZWRfd2lzaGxpc3RfYWNjZXNzZWQiOnRydWV9:1sdpLI:kRJom6QxqGxoa8txDdttrm8f6NTgiJK1gpLvYQo0LqM','2024-08-27 11:05:32.055412'),('j6j03d69k0l679vyx6lli3wuekenkkhq','.eJxVjMEOgjAQRP-lZ9KwlULh6J0vMIZsu4ugpk3a4sX475aEg95m5s3MW0y45WXaEsdpJTEIENVvZtE92O-A7uhvQbrgc1yt3CvyoEmOgfh5Prp_BwumpawVKVat0rNGZyxYJlNc07cdQN1zR60jIuhBY3HG4okUuLluWHdkmMvpjK-wxTVzEsPlWgmHMe_q8wUONEDy:1sdqFL:XHBbxeIdYP87Q5FmyDrw8N6pKVRgl4RqyC4UKAKXQmI','2024-08-27 12:03:27.515748'),('tetht0spha4h5dc6g7fnmfohez9iwhzm','.eJxVjEEOwiAURO_CuiGUXwp26b4nMKb5fMBWDSRA3Rjvbpt0obvJzJv3ZhOudZ7W4vO0ODawljW_nUV6-LgP7o7xljilWPNi-Y7wYy18TM4_zwf7J5ixzNvbeKGtlOhP0gnogdBa0go0OAIFoDS2YQMgkKauV9CLLnTGBBmMElpu0oCvtOal-sKGy7VhhLnu6fMF6_k_8Q:1sfweP:RtF0w5v6ya9IXmS4OaOz0bYrrpZMfqxzI46QlKrP3T4','2024-09-02 07:18:01.388211'),('mtukh1py4nwsg7gs9pr83wa38kypvuiq','.eJxVjMsOwiAQRf-FtSHg8HTp3m8gMAxSNZCUdmX8d9ukC93ec859sxDXpYZ10BymzC4M2Ol3SxGf1HaQH7HdO8felnlKfFf4QQe_9Uyv6-H-HdQ46lYXLzZZEGkLBjI6iAZiEsJbiQmlxaKSRKeM9uCktAoJrDyD1cVrodjnC-pMNz0:1siRkZ:Q_6mQ73_W0yilv8IGyidZc2mE-R4fmRG0eLXZTJSbv8','2024-09-09 04:54:43.519339');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_app_category_hari`
--

DROP TABLE IF EXISTS `shop_app_category_hari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_category_hari` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_category_hari`
--

LOCK TABLES `shop_app_category_hari` WRITE;
/*!40000 ALTER TABLE `shop_app_category_hari` DISABLE KEYS */;
INSERT INTO `shop_app_category_hari` VALUES (1,'Mobiles','uploads/20240701144546mobiles.webp','All Kinds Of Mobiles',0,'2024-07-01 09:15:46.026314'),(2,'Electronics','uploads/20240703120049electronics.jpg','All kinds of Electronic products',0,'2024-07-03 06:30:49.852935'),(3,'Grocery','uploads/20240703120331grocery.jpg','All kinds of Grocery Items.',0,'2024-07-03 06:33:31.267546'),(4,'Home','uploads/20240703120659home_prod.jpg','All Kinds of Home Accessories',0,'2024-07-03 06:36:59.480764'),(5,'Fashion','uploads/20240703120853fashion.webp','Fashion products of Men and Women.',0,'2024-07-03 06:38:53.472949');
/*!40000 ALTER TABLE `shop_app_category_hari` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_app_products_hari`
--

DROP TABLE IF EXISTS `shop_app_products_hari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_products_hari` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `vendor` varchar(150) NOT NULL,
  `quantity` int NOT NULL,
  `original_price` double NOT NULL,
  `selling_price` double NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `trending` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_app_products_ha_category_id_06a80453_fk_shop_app_` (`category_id`),
  CONSTRAINT `shop_app_products_ha_category_id_06a80453_fk_shop_app_` FOREIGN KEY (`category_id`) REFERENCES `shop_app_category_hari` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_products_hari`
--

LOCK TABLES `shop_app_products_hari` WRITE;
/*!40000 ALTER TABLE `shop_app_products_hari` DISABLE KEYS */;
INSERT INTO `shop_app_products_hari` VALUES (1,'REDMI 9i Sport','MH mobiles',0,9999,8999,'MI REDMI 9i Sport (Coral Green, 64 GB) (4 GB RAM)',0,1,'2024-07-01 09:28:45.164450',1),(2,'realme 12 Pro 5G','Double-H mobiles',0,31999,24799,'realme 12 Pro 5G (Submarine Blue, 8GB RAM 256 GB Storage)',0,1,'2024-07-03 06:45:47.573770',1),(3,'Nokia X30 5G','Double-H mobiles',3,45999,39999,'Nokia X30 5G, 6.43” FHD+ AMOLED PureDisplay, 90Hz refresh rate, 3 years Android OS and monthly security updates, 50MP PureView OIS camera | Blue, 8+256GB',0,0,'2024-07-03 06:53:46.686438',1),(4,'vivo X100 Pro','Double-H mobiles',2,96999,89999,'vivo X100 Pro (Asteroid Black, 512 GB)  (16 GB RAM)',0,1,'2024-07-03 06:56:23.983641',1),(5,'Samsung s24 ultra','MH mobiles',19,134999,124999,'Samsung Galaxy S Series S24 Ultra 5G Dual Sim Smartphone (12GB RAM,256GB Storage) 6.8 inch QHD+ AMOLED Display| Snapdragon 8 Gen 3 (Titanium Violet)',0,1,'2024-07-03 06:59:53.112602',1),(6,'Oppo Reno 10 Pro','MH mobiles',11,35999,27999,'Oppo Reno 10 Pro Dual-SIM 256gb ROM + 12gb RAM Factory Unlocked 5G Smartphone',0,1,'2024-07-03 07:03:05.518946',1),(7,'iPhone 15 Pro Max','Double-H mobiles',12,159999,150999,'Apple iPhone 15 Pro Max (256 GB) - Black Titanium',0,1,'2024-07-03 07:05:10.172400',1),(8,'OnePlus 12','Double-H mobiles',3,75999,68999,'OnePlus 12 (Flowy Emerald, 16GB RAM, 512GB Storage)',0,1,'2024-07-03 07:06:52.365589',1),(9,'Honor X9b','Double-H mobiles',2,30999,19999,'Honor X9b (Midnight Black, 256 GB)  (8 GB RAM)',0,0,'2024-07-03 07:09:31.064064',1),(10,'Huawei Pura 70 Ultra 5G','Double-H mobiles',1,130999,120999,'Huawei Pura 70 Ultra 5G 6.8\"OLED 16/512GB Kirin 9010 GLOBAL VERSION By FedEx',0,1,'2024-07-03 07:12:36.112003',1),(11,'Skullcandy Dime 3 earbuds','Vp mobiles',28,10000,2997,'Skullcandy Dime 3 in-Ear Wireless Earbuds,Multipoint Pairing, 20 Hr Battery, Microphone, Works with iPhone Android and Bluetooth Devices - Black',0,1,'2024-07-03 09:09:44.215371',2),(12,'AirPods Pro','Vp mobiles',10,24999,20999,'AirPods Pro (2nd generation) with MagSafe Charging Case (USB‑C)',0,1,'2024-07-03 09:14:42.925159',2),(13,'boAt Type C Charger','Vp gadgets',35,600,450,'boAt WCD 18W Type C Fast Charger',0,0,'2024-07-03 09:17:59.582224',2),(14,'Apple Magsafe','Vp gadgets',20,5000,4000,'MagSafe Charger',0,1,'2024-07-03 09:20:35.920238',2),(15,'samsung powerbank','Vp gadgets',20,2000,1799,'Samsung 10000 mAh Power Bank',0,0,'2024-07-03 09:23:30.107992',2),(16,'Noise Smart Watch','Vp gadgets',25,5000,4499,'Noise Newly Launched ColorFit Pro 5 Max 1.96\" AMOLED Display Smart Watch, BT Calling, Post Training Workout Analysis, VO2 Max, Rapid Health, 5X Faster Data Transfer - Space Blue',0,1,'2024-07-03 09:27:03.081882',2),(17,'GoPro HERO12','Vp gadgets',5,70000,65000,'GoPro HERO12 Black Creator Edition Waterproof Action Camera with 5.3K60 Ultra HD Video, 27MP Photos, 1080p Live Streaming, Enduro Battery (Black)',0,1,'2024-07-03 09:28:33.536129',2),(18,'ThinkPad X1','Vp gadgets',5,160000,154000,'ThinkPad X1 Carbon Gen 12',0,1,'2024-07-03 10:18:48.669375',2),(19,'Zebronics Keyboard','Vp gadgets',10,1999,1099,'Zebronics Transformer Gaming Keyboard and Mouse Combo,Braided Cable,Durable Al body,Multimedia keys and Gaming Mouse with 6 Buttons, Multi-Color LED Lights, High-Resolution Sensor with 3200 DPI(Black)',0,1,'2024-07-03 10:20:37.729330',2),(20,'RPM Wireless Mouse','Vp gadgets',10,1000,599,'RPM Euro Games Wireless Gaming Mouse Rechargeable 500 mAh Battery DPI Upto 3200',0,1,'2024-07-03 10:22:15.077941',2),(21,'Sunflower Oil 5 Ltr','pandian store',50,600,550,'Mr. Gold Refined Sunflower Oil 5 Ltr Can Sunflower Oil Can  (5 L)',0,1,'2024-07-03 11:04:38.620322',3),(22,'Spices','pandian store',59,1400,1200,'All Spice Combo: Green Cardamom + Black Cardamom + Cloves + Black Pepper + Coriander Whole + Cumin Whole + Red Chilli Powder + Cumin Powder + Coriander Powder + Kashmiri Chilli Powder',0,1,'2024-07-03 11:06:40.900627',3),(23,'wheat flour','pandian store',75,75,61,'Aashirvaad Superior MP Atta, 1kg Pack',0,0,'2024-07-03 11:08:14.637935',3),(24,'kissan tomato ketchup','pandian store',29,230,195,'Kissan Fresh Tomato Ketchup 2 kg Pouch, Sweet & Tangy Sauce Real Tomatoes - Super Saver Offer Pack',0,1,'2024-07-03 11:10:05.700776',3),(25,'maggi','pandian store',100,175,158,'Maggi 2-Minute Noodles Masala 420G',0,1,'2024-07-03 11:11:41.323543',3),(26,'samsung washing machine','rags home appliances',5,41599,34999,'8.0 kg AI Ecobubble™ Front Load Washing Machine with SmartThings & Wi-Fi, WW80T504DAX1',0,1,'2024-07-03 11:16:57.819568',4),(27,'samsung refrigerator','rags home appliances',3,120000,110999,'633 L Convertible 5in1 Side by Side Refrigerator RS78CG8543S9',0,1,'2024-07-03 11:19:16.884400',4),(28,'LG oven','rags home appliances',5,9999,6999,'LG 20 Ltr Solo Microwave Oven with Glass Door',0,1,'2024-07-03 11:21:42.025380',4),(29,'Sony Bravia tv','rags home appliances',1,80000,73000,'Sony Bravia 139 cm (55 inches) 4K Ultra HD Smart LED Google TV KD-55X74L (Black)',0,1,'2024-07-03 11:23:17.823024',4),(30,'crompton water heater','rags home appliances',6,10000,5799,'Crompton Arno Neo 15-L 5 Star Rated Storage Water Heater (Geyser) with Advanced 3 Level Safety (White) National Energy Conservation Award Winner 2023',0,0,'2024-07-03 11:24:38.232084',4),(31,'van heusen suit for men','bhu\'s Fashion',11,9999,7999,'MEN NAVY TEXTURED SKINNY FIT PARTY THREE PIECE SUIT',0,1,'2024-07-03 11:28:35.114451',5),(32,'lehanga','bhu\'s Fashion',1,20000,19999,'Light Pink Stone Work Lehenga',0,1,'2024-07-03 11:31:04.349597',5),(33,'Saree','bhu\'s Fashion',8,5000,4000,'Beige Saree In Organza With Lace Trims And Unstitched Blouse Piece',0,1,'2024-07-03 11:35:59.078992',5),(34,'Shirt for men','bhu\'s Fashion',9,1500,1200,'Raymond Men Orange Slim Fit Solid Regular Collar Shirt',0,1,'2024-07-03 11:37:26.573260',5);
/*!40000 ALTER TABLE `shop_app_products_hari` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `shop_app_productimage`
--

DROP TABLE IF EXISTS `shop_app_productimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_productimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_app_productimag_product_id_ed678c68_fk_shop_app_` (`product_id`),
  CONSTRAINT `shop_app_productimag_product_id_ed678c68_fk_shop_app_` FOREIGN KEY (`product_id`) REFERENCES `shop_app_products_hari` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_productimage`
--

LOCK TABLES `shop_app_productimage` WRITE;
/*!40000 ALTER TABLE `shop_app_productimage` DISABLE KEYS */;
INSERT INTO `shop_app_productimage` VALUES (1,'uploads/2024072913441320240703170726shirt.webp','2024-07-29 08:14:13.251022',34),(2,'uploads/2024072913451620240703170559saree.webp','2024-07-29 08:15:16.438166',33),(3,'uploads/202407291349362024072516033720240703170104lehanga.webp','2024-07-29 08:19:36.469131',32),(4,'uploads/202407291349472024072516035420240703165835suit.jpg','2024-07-29 08:19:47.920284',31),(5,'uploads/2024072914075120240703165438water_heater.jpg','2024-07-29 08:37:51.537906',30),(6,'uploads/2024072914091220240703165317sony_tv.jpg','2024-07-29 08:39:12.957069',29),(7,'uploads/2024072914094520240703165142oven.jfif','2024-07-29 08:39:45.306042',28),(9,'uploads/2024072914100920240703164916fridgr.png','2024-07-29 08:40:09.159119',27),(10,'uploads/2024072914124220240703164657washing_machine.webp','2024-07-29 08:42:42.501069',26),(11,'uploads/2024072914125720240703164141maggi.webp','2024-07-29 08:42:57.840201',25),(12,'uploads/2024072914133020240703164005ketchup.jpg','2024-07-29 08:43:30.583375',24),(13,'uploads/2024072914134520240703163814atta.jpg','2024-07-29 08:43:45.062108',23),(14,'uploads/2024072914135720240703163640spices.webp','2024-07-29 08:43:57.983386',22),(15,'uploads/2024072914141420240703163438sunoil.webp','2024-07-29 08:44:14.393208',21),(16,'uploads/2024072914143220240703155215mouse.webp','2024-07-29 08:44:32.154330',20),(17,'uploads/2024072914145420240703154848laptop.jpg','2024-07-29 08:44:54.847866',18),(18,'uploads/2024072914150620240703155037keyboard.jpg','2024-07-29 08:45:06.789997',19),(19,'uploads/2024072914152520240703145833go_pro.jpg','2024-07-29 08:45:25.988073',17),(20,'uploads/2024072914153920240703145703smartwatch.jpg','2024-07-29 08:45:40.001637',16),(21,'uploads/2024072914155220240703145330powerbank.webp','2024-07-29 08:45:52.414710',15),(22,'uploads/2024072914162320240703145035apple-charger.jfif','2024-07-29 08:46:23.337424',14),(23,'uploads/2024072914163820240703144759charger-C.webp','2024-07-29 08:46:38.651368',13),(24,'uploads/2024072914165320240703144442airpods_apple.jfif','2024-07-29 08:46:53.768672',12),(25,'uploads/2024072914171320240703143944earbuds.jpg','2024-07-29 08:47:13.131954',11),(26,'uploads/2024072914172920240703124236huawei.webp','2024-07-29 08:47:29.306325',10),(27,'uploads/2024072914174320240703123931honor.webp','2024-07-29 08:47:43.584783',9),(28,'uploads/2024072914180120240703123652one_plus.webp','2024-07-29 08:48:01.959726',8),(29,'uploads/2024072914181620240703123510iphone_15.jfif','2024-07-29 08:48:16.627557',7),(30,'uploads/2024072914183520240703123305oppo_reno.jpg','2024-07-29 08:48:35.911395',6),(31,'uploads/2024072914185220240703122953samsung_s24.jpg','2024-07-29 08:48:52.839762',5),(32,'uploads/2024072914190920240703122623vivo_x100_pro.jpg','2024-07-29 08:49:09.803941',4),(33,'uploads/2024072914192420240703122346Nokia_m.jpg','2024-07-29 08:49:24.190304',3),(34,'uploads/2024072914194120240703121547M_realme.webp','2024-07-29 08:49:41.121679',2),(35,'uploads/2024072914195120240701145845redmi_9i.jfif','2024-07-29 08:49:51.116249',1),(37,'uploads/20240731150824realme3.jpg','2024-07-31 09:38:24.020884',1),(38,'uploads/20240731151452realme3.jpg','2024-07-31 09:44:52.728257',2),(39,'uploads/20240731151508nokia_2.jfif','2024-07-31 09:45:08.050213',3),(40,'uploads/20240731152000vivo2.png','2024-07-31 09:50:00.378195',4),(41,'uploads/20240731152338samsung2.jfif','2024-07-31 09:53:38.656779',5);
/*!40000 ALTER TABLE `shop_app_productimage` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `shop_app_cart_hari`
--

DROP TABLE IF EXISTS `shop_app_cart_hari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_cart_hari` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_qty` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_app_cart_hari_product_id_59f4382c_fk_shop_app_` (`product_id`),
  KEY `shop_app_cart_hari_user_id_63404ae0_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shop_app_cart_hari_product_id_59f4382c_fk_shop_app_` FOREIGN KEY (`product_id`) REFERENCES `shop_app_products_hari` (`id`),
  CONSTRAINT `shop_app_cart_hari_user_id_63404ae0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_cart_hari`
--

LOCK TABLES `shop_app_cart_hari` WRITE;
/*!40000 ALTER TABLE `shop_app_cart_hari` DISABLE KEYS */;
INSERT INTO `shop_app_cart_hari` VALUES (4,1,'2024-07-29 11:23:57.410737',4,3),(8,3,'2024-07-31 08:43:38.701648',7,5),(9,2,'2024-07-31 08:44:30.535608',2,5),(13,1,'2024-08-02 05:07:20.007191',3,1),(14,1,'2024-08-12 12:40:05.635463',23,1);
/*!40000 ALTER TABLE `shop_app_cart_hari` ENABLE KEYS */;
UNLOCK TABLES;



--
-- Table structure for table `shop_app_favourite_hari`
--

DROP TABLE IF EXISTS `shop_app_favourite_hari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_favourite_hari` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_app_favourite_h_product_id_0ad1bc00_fk_shop_app_` (`product_id`),
  KEY `shop_app_favourite_hari_user_id_3e94350d_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shop_app_favourite_h_product_id_0ad1bc00_fk_shop_app_` FOREIGN KEY (`product_id`) REFERENCES `shop_app_products_hari` (`id`),
  CONSTRAINT `shop_app_favourite_hari_user_id_3e94350d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_favourite_hari`
--

LOCK TABLES `shop_app_favourite_hari` WRITE;
/*!40000 ALTER TABLE `shop_app_favourite_hari` DISABLE KEYS */;
INSERT INTO `shop_app_favourite_hari` VALUES (3,'2024-08-16 05:03:45.665331',11,11);
/*!40000 ALTER TABLE `shop_app_favourite_hari` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_app_order`
--

DROP TABLE IF EXISTS `shop_app_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `total_price` double NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `user_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_app_order_user_id_5587e9b1_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shop_app_order_user_id_5587e9b1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_order`
--

LOCK TABLES `shop_app_order` WRITE;
/*!40000 ALTER TABLE `shop_app_order` DISABLE KEYS */;
INSERT INTO `shop_app_order` VALUES (1,28799,'chennai','1234567890','2024-07-29 10:31:36.148053','Pending',1,'hari'),(2,1200,'tirupur','1234567890','2024-07-29 10:38:08.791485','Pending',5,'kaviya'),(3,4800,'chennai','1234567890','2024-07-29 11:41:43.101170','Pending',1,'hari'),(4,39999,'chennai','1234567890','2024-07-30 08:54:26.697940','Pending',1,'hari'),(5,39999,'chennai','1234567890','2024-07-30 08:56:49.561185','Pending',1,'hari'),(6,24799,'chennai','1234567890','2024-07-30 08:57:03.297901','Pending',1,'hari'),(7,68999,'chennai','1234567890','2024-07-30 09:01:37.220957','Pending',1,'hari'),(8,68999,'chennai','1234567890','2024-07-30 09:07:42.881932','Pending',1,'ragavi'),(9,4000,'coimbatore','1234567890','2024-07-30 12:24:01.204780','Pending',5,'priya'),(10,24799,'chennai','1234567890','2024-08-01 07:42:18.622069','Pending',1,'hari'),(11,24799,'chennai','1234567890','2024-08-01 07:42:19.169733','Pending',1,'hari'),(12,24799,'chennai','1234567890','2024-08-01 07:42:19.456501','Pending',1,'hari'),(13,24799,'chennai','1234567890','2024-08-01 07:42:19.487061','Pending',1,'hari'),(14,24799,'chennai','1234567890','2024-08-01 07:42:19.668119','Pending',1,'hari'),(15,24799,'chennai','1234567890','2024-08-01 07:42:37.275276','Pending',1,'hari'),(16,24799,'chennai','1234567890','2024-08-01 07:42:37.432605','Pending',1,'hari'),(17,24799,'chennai','1234567890','2024-08-01 07:42:37.596677','Pending',1,'hari'),(18,89999,'tirupur','1234567890','2024-08-01 07:46:19.686155','Pending',1,'hari'),(19,89999,'tirupur','1234567890','2024-08-01 07:46:20.923696','Pending',1,'hari'),(20,89999,'chennai','1234567890','2024-08-01 07:57:23.310199','Pending',1,'salem'),(21,195,'chennai','1234567890','2024-08-07 09:46:52.998978','Pending',11,'Hariharan'),(22,2997,'Kanyakumari','1234567890','2024-08-13 10:32:19.136029','Pending',1,'buvi');
/*!40000 ALTER TABLE `shop_app_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_app_orderitem`
--

DROP TABLE IF EXISTS `shop_app_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `price` double NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_app_orderitem_order_id_96bb41a6_fk_shop_app_order_id` (`order_id`),
  KEY `shop_app_orderitem_product_id_2b33c773_fk_shop_app_` (`product_id`),
  CONSTRAINT `shop_app_orderitem_order_id_96bb41a6_fk_shop_app_order_id` FOREIGN KEY (`order_id`) REFERENCES `shop_app_order` (`id`),
  CONSTRAINT `shop_app_orderitem_product_id_2b33c773_fk_shop_app_` FOREIGN KEY (`product_id`) REFERENCES `shop_app_products_hari` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_orderitem`
--

LOCK TABLES `shop_app_orderitem` WRITE;
/*!40000 ALTER TABLE `shop_app_orderitem` DISABLE KEYS */;
INSERT INTO `shop_app_orderitem` VALUES (1,1,4000,1,33),(2,1,24799,1,2),(3,1,1200,2,22),(4,4,4800,3,34),(5,1,39999,4,3),(6,1,39999,5,3),(7,1,24799,6,2),(8,1,68999,7,8),(9,1,68999,8,8),(10,1,4000,9,33),(11,1,24799,10,2),(12,1,24799,11,2),(13,1,24799,12,2),(14,1,24799,13,2),(15,1,24799,14,2),(16,1,24799,15,2),(17,1,24799,16,2),(18,1,24799,17,2),(19,1,89999,18,4),(20,1,89999,19,4),(21,1,89999,20,4),(22,1,195,21,24),(23,1,2997,22,11);
/*!40000 ALTER TABLE `shop_app_orderitem` ENABLE KEYS */;
UNLOCK TABLES;



--
-- Table structure for table `shop_app_wishlist`
--

DROP TABLE IF EXISTS `shop_app_wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_wishlist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `shareable_link` char(32) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `shareable_link` (`shareable_link`),
  KEY `shop_app_wishlist_user_id_c71950a5_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shop_app_wishlist_user_id_c71950a5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_wishlist`
--

LOCK TABLES `shop_app_wishlist` WRITE;
/*!40000 ALTER TABLE `shop_app_wishlist` DISABLE KEYS */;
INSERT INTO `shop_app_wishlist` VALUES (4,'My Wishlist','2fb02128e06b400ca16604701e02ea9a','2024-08-12 09:08:17.202803',1),(5,'My view Wishlist','0c35c5477e7249a3a230190fcca3eaf7','2024-08-12 09:13:37.572865',1),(6,'My Wishlist','1ef78b3050a64674a58397a3244ed10e','2024-08-13 05:40:53.602923',3),(7,'My Wishlist','3b240c239a93455ab49d40e6a79748b4','2024-08-13 12:01:35.897247',7),(8,'My Wishlist','4f489cdd3a774e178fa7a793df028faa','2024-08-16 05:03:54.412088',11);
/*!40000 ALTER TABLE `shop_app_wishlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_app_wishlistitem`
--

DROP TABLE IF EXISTS `shop_app_wishlistitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_app_wishlistitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `added_at` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `wishlist_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_app_wishlistite_product_id_2df9f35b_fk_shop_app_` (`product_id`),
  KEY `shop_app_wishlistite_wishlist_id_b16cfbbd_fk_shop_app_` (`wishlist_id`),
  CONSTRAINT `shop_app_wishlistite_product_id_2df9f35b_fk_shop_app_` FOREIGN KEY (`product_id`) REFERENCES `shop_app_products_hari` (`id`),
  CONSTRAINT `shop_app_wishlistite_wishlist_id_b16cfbbd_fk_shop_app_` FOREIGN KEY (`wishlist_id`) REFERENCES `shop_app_wishlist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_app_wishlistitem`
--

LOCK TABLES `shop_app_wishlistitem` WRITE;
/*!40000 ALTER TABLE `shop_app_wishlistitem` DISABLE KEYS */;
INSERT INTO `shop_app_wishlistitem` VALUES (7,'2024-08-13 08:52:52.417607',11,4),(9,'2024-08-13 10:47:13.090174',11,6),(10,'2024-08-13 12:01:35.999406',11,7),(11,'2024-08-13 12:02:14.074792',21,7);
/*!40000 ALTER TABLE `shop_app_wishlistitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-28 11:25:38
