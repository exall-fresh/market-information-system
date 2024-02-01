-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2024 at 08:04 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mis-python`
--

-- --------------------------------------------------------

--
-- Table structure for table `markets`
--

CREATE TABLE `markets` (
  `market_id` int(20) NOT NULL,
  `market_name` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `coordinates` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `markets`
--

INSERT INTO `markets` (`market_id`, `market_name`, `city`, `coordinates`) VALUES
(12, 'Chibavi Market', 'Mzuzu', '-13.374635671699615, 33.84049642938435'),
(13, 'Limbe market', 'Blantyre', '-15.81654186513036, 35.05411524983273'),
(14, 'Blantyre Market', 'Blantyre', '-15.790439169174508, 35.007322970993634'),
(15, 'Lilongwe Market', 'lilongwe', '-13.988062987458445, 33.7783089939577'),
(16, 'Chilinde market', 'lilongwe', '-13.994339535673424, 33.80805837186894');

-- --------------------------------------------------------

--
-- Table structure for table `market_images`
--

CREATE TABLE `market_images` (
  `market_image_id` int(20) NOT NULL,
  `market_id` varchar(255) NOT NULL,
  `image_location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `market_images`
--

INSERT INTO `market_images` (`market_image_id`, `market_id`, `image_location`) VALUES
(4, '14', 'app/static/uploads/13.jpg'),
(5, '15', 'app/static/uploads/12.jpg'),
(6, '16', 'app/static/uploads/13.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `scouts_products`
--

CREATE TABLE `scouts_products` (
  `scout_product_id` int(20) NOT NULL,
  `scout_id` varchar(255) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `price` int(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scouts_products`
--

INSERT INTO `scouts_products` (`scout_product_id`, `scout_id`, `product_name`, `price`, `date`) VALUES
(0, '3', 'maize', 900, '2024-01-01'),
(0, '3', 'mtedza', 90, '2024-01-01'),
(0, '3', 'mangoe', 100, '2024-01-01'),
(0, '5', 'maize', 90, '2024-01-02'),
(0, '6', 'maize', 56, '2024-01-02'),
(0, '6', 'tomatoe', 89, '2024-01-02'),
(0, '6', 'onions', 90, '2024-01-02');

-- --------------------------------------------------------

--
-- Table structure for table `scout_market`
--

CREATE TABLE `scout_market` (
  `scout_id` varchar(255) NOT NULL,
  `market_id` varchar(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scout_market`
--

INSERT INTO `scout_market` (`scout_id`, `market_id`, `date`) VALUES
('3', '14', '0000-00-00'),
('5', '13', '0000-00-00'),
('6', '16', '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `sellers_products`
--

CREATE TABLE `sellers_products` (
  `seller_product_id` int(11) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `price` int(255) NOT NULL,
  `date` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sellers_products`
--

INSERT INTO `sellers_products` (`seller_product_id`, `seller_id`, `product_name`, `price`, `date`) VALUES
(1, 2, 'maize', 234, 2023),
(2, 2, 'beans', 1200, 2023),
(6, 2, 'mzimbe', 900, 2023);

-- --------------------------------------------------------

--
-- Table structure for table `seller_market`
--

CREATE TABLE `seller_market` (
  `seller_market_id` int(255) NOT NULL,
  `market_id` varchar(255) NOT NULL,
  `seller_id` varchar(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `seller_market`
--

INSERT INTO `seller_market` (`seller_market_id`, `market_id`, `seller_id`, `date`) VALUES
(2, '12', '2', '2023-12-31');

-- --------------------------------------------------------

--
-- Table structure for table `trending_products`
--

CREATE TABLE `trending_products` (
  `trending_product_id` int(20) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `market_id` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `scout_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trending_products`
--

INSERT INTO `trending_products` (`trending_product_id`, `product_name`, `market_id`, `date`, `scout_id`) VALUES
(1, 'maize', '14', '2024-01-01', '3'),
(2, 'mtedza', '14', '2024-01-01', '3'),
(3, 'mangoe', '14', '2024-01-01', '3'),
(4, 'maize', '13', '2024-01-02', '5'),
(5, 'maize', '16', '2024-01-02', '6'),
(6, 'tomatoe', '16', '2024-01-02', '6'),
(7, 'maize', '16', '2024-01-02', '6');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(20) NOT NULL,
  `username` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `phone`, `email`, `password`, `role`) VALUES
(1, 'patrick', '777', 'patrick@gmail.com', 'scrypt:32768:8:1$f0R9FwmIdiecAl82$82d1b05351dc9a4ec45397808decae3f0a6c53d68a15644c5f05ab8cf6f620ffaec80f05f6f7a2e02f974f3fd0de06c14854b1fd127ec24251402853a75e0f69', 1),
(2, 'patrick seller', '90', 'patrickseller@gmail.com', 'scrypt:32768:8:1$3zY5rC1NqbVvwF7F$3955ca68e3e7bd49d251cc5186c208ddc1e4cc7049551149f5f824d751d24ef47913902f150bef4993e4a166fe2b6bd2acf0906875bea57baf4b47cbe49b0da4', 2),
(3, 'scout', '9000', 'scout@gmail.com', 'scrypt:32768:8:1$5w7WPziw3YiIrTbn$2391fcf4b24f7cc5a1d6ba15e412df2b47129cfb6421fd91d7398296a8fe6aa28485df25062f6484eec7ef5229b9d0f1ac4d11d5d987514fadb96b7db0cd0320', 3),
(5, 'scout limbe', '7777999', 'scout@limbe.com', 'scrypt:32768:8:1$oVnB2efPFSMRrl4r$5d7508147ce71b47455b547a61f4f559e685016b9ea8df303ee8882c725b00cfb799892cdd55477104135ed4002e5da4961a9f218934327f14008bf9eb2d0775', 3),
(6, 'scout chilinde', '2344', 'scout@chilinde.com', 'scrypt:32768:8:1$SX4YP4RSAPqs56mM$9d5c2ba481accd97dd548b085bf167298243b340fe7d5c18c3f1efaec96e39466c45449d2967b45a064102a79a6cd58c3429b9e0f554addd4963136404c384a8', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `markets`
--
ALTER TABLE `markets`
  ADD PRIMARY KEY (`market_id`);

--
-- Indexes for table `market_images`
--
ALTER TABLE `market_images`
  ADD PRIMARY KEY (`market_image_id`);

--
-- Indexes for table `sellers_products`
--
ALTER TABLE `sellers_products`
  ADD PRIMARY KEY (`seller_product_id`);

--
-- Indexes for table `seller_market`
--
ALTER TABLE `seller_market`
  ADD PRIMARY KEY (`seller_market_id`);

--
-- Indexes for table `trending_products`
--
ALTER TABLE `trending_products`
  ADD PRIMARY KEY (`trending_product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `markets`
--
ALTER TABLE `markets`
  MODIFY `market_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `market_images`
--
ALTER TABLE `market_images`
  MODIFY `market_image_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sellers_products`
--
ALTER TABLE `sellers_products`
  MODIFY `seller_product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `seller_market`
--
ALTER TABLE `seller_market`
  MODIFY `seller_market_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `trending_products`
--
ALTER TABLE `trending_products`
  MODIFY `trending_product_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
