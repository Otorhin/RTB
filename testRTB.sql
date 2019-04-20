-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Апр 20 2019 г., 19:22
-- Версия сервера: 10.0.38-MariaDB-0ubuntu0.16.04.1
-- Версия PHP: 7.0.33-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `testRTB`
--

-- --------------------------------------------------------

--
-- Структура таблицы `guild`
--

CREATE TABLE `guild` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `tag` text NOT NULL,
  `creator` text NOT NULL,
  `password` text NOT NULL,
  `gold` int(11) NOT NULL DEFAULT '0',
  `diamond` int(11) NOT NULL DEFAULT '0',
  `lvl` int(11) NOT NULL DEFAULT '1',
  `build1` int(11) NOT NULL DEFAULT '0',
  `build2` int(11) NOT NULL DEFAULT '0',
  `build3` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `guild`
--

INSERT INTO `guild` (`id`, `name`, `tag`, `creator`, `password`, `gold`, `diamond`, `lvl`, `build1`, `build2`, `build3`) VALUES
(1, 'пинус', 'хуй', '385224221', '66ec3305280b4745a7504e27e0326b7a', 346180173, 346339289, 1, 7, 2, 4),
(2, 'Porno', 'HUB', '439637823', 'a5aee93adb4a47409d8d8590ac3c9f47', 346200440, 346343705, 1, 17, 0, 5),
(3, 'lohblat', 'im', '301227622', '00cb014e3c684dc7854d4ff72337ddfb', 94176120, 346317505, 1, 25, 25, 15),
(4, 'Pidaras', 'YA', '406334867', '8fe008af81ef4796b5ea5d590a2b66ff', 345639733, 346318642, 1, 16, 12, 14),
(5, 'NOGAY', 'GAY', '314580963', 'f5bf91ccdf9c47a88ab9847dd8bc9c34', 98643750, 99971250, 1, 25, 25, 15);

-- --------------------------------------------------------

--
-- Структура таблицы `promocode`
--

CREATE TABLE `promocode` (
  `id` int(11) NOT NULL,
  `code` varchar(20) NOT NULL,
  `action` text NOT NULL,
  `number` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `quest`
--

CREATE TABLE `quest` (
  `user_id` int(11) NOT NULL,
  `quest` varchar(500) DEFAULT NULL,
  `monster` varchar(500) DEFAULT NULL,
  `item` varchar(500) DEFAULT NULL,
  `inv` varchar(25) DEFAULT NULL,
  `killed` int(11) DEFAULT NULL,
  `need` int(11) DEFAULT NULL,
  `allquest` int(11) NOT NULL DEFAULT '40',
  `lastquest` varchar(11) NOT NULL DEFAULT 'not_quest'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `quest`
--

INSERT INTO `quest` (`user_id`, `quest`, `monster`, `item`, `inv`, `killed`, `need`, `allquest`, `lastquest`) VALUES
(239955010, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest'),
(278330138, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest'),
(301227622, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest'),
(308111497, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest'),
(314580963, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest'),
(385224221, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest'),
(406334867, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest'),
(439637823, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest'),
(674697683, NULL, NULL, NULL, NULL, NULL, NULL, 40, 'not_quest');

-- --------------------------------------------------------

--
-- Структура таблицы `user`
--

CREATE TABLE `user` (
  `user_id` varchar(25) NOT NULL,
  `referal` varchar(25) DEFAULT NULL,
  `nick` text CHARACTER SET utf8mb4 NOT NULL,
  `emoji` text CHARACTER SET utf8mb4,
  `lvl` int(11) NOT NULL DEFAULT '1',
  `exp` int(11) NOT NULL DEFAULT '0',
  `new_exp` int(11) NOT NULL DEFAULT '15',
  `hp` int(11) NOT NULL DEFAULT '100',
  `guild_id` int(11) DEFAULT NULL,
  `city` text,
  `atk` int(11) NOT NULL DEFAULT '5',
  `def` int(11) NOT NULL DEFAULT '5',
  `karma` int(11) NOT NULL DEFAULT '0',
  `gold` int(11) NOT NULL DEFAULT '346346534',
  `diamond` int(11) NOT NULL DEFAULT '346346534',
  `buff` varchar(50) DEFAULT NULL,
  `ach` text,
  `bonus` int(1) NOT NULL DEFAULT '0',
  `rating` int(11) NOT NULL,
  `pizza` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `user`
--

INSERT INTO `user` (`user_id`, `referal`, `nick`, `emoji`, `lvl`, `exp`, `new_exp`, `hp`, `guild_id`, `city`, `atk`, `def`, `karma`, `gold`, `diamond`, `buff`, `ach`, `bonus`, `rating`, `pizza`) VALUES
('239955010', NULL, 'Reincor', NULL, 1, 7, 15, 250, NULL, NULL, 47, 38, 0, 111212414, 346345521, NULL, 'expect', 0, 9, 0),
('261825393', NULL, 'Аллия', NULL, 1, 0, 15, 100, NULL, NULL, 5, 5, 0, 346346534, 346346534, NULL, 'start', 0, 0, 0),
('278330138', NULL, 'Yoshinon', NULL, 1, 5, 15, 100, NULL, NULL, 5, 5, 0, 326142605, 346344174, NULL, 'start', 0, 6, 0),
('301227622', NULL, 'ПажилойХуила', NULL, 3, 50, 75, 250, 3, NULL, 52, 77, 0, 344, 5, NULL, 'start', 0, 66, 0),
('308111497', NULL, 'Ахъё', NULL, 1, 9, 15, 100, NULL, NULL, 21, 10, 0, 29910931, 346345851, NULL, 'start', 0, -2, 0),
('314580963', NULL, 'ТоряяяяяяяяяяяяяяяЯR', NULL, 1, 0, 15, 250, 5, NULL, 50, 75, 0, 246225248, 246340535, NULL, 'start', 0, 3, 0),
('385224221', NULL, 'Рикорин', NULL, 1, 0, 15, 250, 1, NULL, 50, 75, 0, 59, 0, NULL, 'start', 0, 304, 0),
('406334867', NULL, 'Сосалменяебали', NULL, 2, 15, 20, 250, 4, NULL, 51, 76, 0, 9464, 9728, NULL, 'start', 0, 64, 0),
('439637823', NULL, 'Оториноларинголог', NULL, 5, 127, 250, 180, 2, NULL, 25, 18, 0, 273276, 4664775, NULL, 'expect', 0, 76, 0),
('674697683', NULL, 'АнатолийСтепаныч', NULL, 1, 8, 15, 250, NULL, NULL, 50, 75, 0, 210091570, 346340924, NULL, 'start', 0, -2, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `user_equip`
--

CREATE TABLE `user_equip` (
  `user_id` varchar(25) NOT NULL,
  `head` text,
  `mask` text,
  `body` text,
  `gun` text,
  `legs` text,
  `shand` text,
  `amulet` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `user_equip`
--

INSERT INTO `user_equip` (`user_id`, `head`, `mask`, `body`, `gun`, `legs`, `shand`, `amulet`) VALUES
('239955010', NULL, '2', '2', '3', '2', NULL, NULL),
('261825393', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('278330138', '2', '2', '2', '4', '2', NULL, NULL),
('301227622', NULL, '2', NULL, '4', '2', NULL, NULL),
('308111497', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('314580963', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('385224221', '2', '2', '2', '3', '2', NULL, NULL),
('406334867', '2', '2', '2', '3', '2', NULL, NULL),
('439637823', '4', '4', '4', '6', '4', 'test', 'test'),
('674697683', '2', '2', '2', '4', '2', NULL, NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `user_inventory`
--

CREATE TABLE `user_inventory` (
  `user_id` varchar(25) NOT NULL,
  `stick` int(11) NOT NULL DEFAULT '0',
  `coal` int(11) NOT NULL DEFAULT '0',
  `iron` int(11) NOT NULL DEFAULT '0',
  `stone` int(11) NOT NULL DEFAULT '0',
  `stick2` int(11) NOT NULL DEFAULT '0',
  `wolfberri` int(11) NOT NULL DEFAULT '0',
  `thread` int(11) NOT NULL DEFAULT '0',
  `bone` int(11) NOT NULL DEFAULT '0',
  `ruby` int(11) NOT NULL DEFAULT '0',
  `blueberri` int(11) NOT NULL DEFAULT '0',
  `hallucberri` int(11) NOT NULL DEFAULT '0',
  `oldacorn` int(11) NOT NULL DEFAULT '0',
  `wildhops` int(11) NOT NULL DEFAULT '0',
  `chairleg` int(11) NOT NULL DEFAULT '0',
  `invigor` int(11) NOT NULL DEFAULT '0',
  `weakpotionber` int(11) NOT NULL DEFAULT '0',
  `babydoll` int(11) NOT NULL DEFAULT '0',
  `snowflower` int(11) NOT NULL DEFAULT '0',
  `blacksmithtools` int(11) NOT NULL DEFAULT '0',
  `logic` int(1) DEFAULT '0',
  `lost_cargo` int(11) NOT NULL DEFAULT '0',
  `leather` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `user_inventory`
--

INSERT INTO `user_inventory` (`user_id`, `stick`, `coal`, `iron`, `stone`, `stick2`, `wolfberri`, `thread`, `bone`, `ruby`, `blueberri`, `hallucberri`, `oldacorn`, `wildhops`, `chairleg`, `invigor`, `weakpotionber`, `babydoll`, `snowflower`, `blacksmithtools`, `logic`, `lost_cargo`, `leather`) VALUES
('239955010', 7, 1, 1, 2, 0, 2, 3, 21, 0, 2, 4, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 2),
('261825393', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
('278330138', 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
('301227622', 3, 8, 10, 7, 0, 1, 5, 54, 3, 0, 3, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 16),
('308111497', 1, 0, 0, 0, 0, 0, 2, 17, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4),
('314580963', 0, 1, 3, 2, 0, 4, 6, 6, 0, 2, 4, 2, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3),
('385224221', 0, 0, 0, 1, 0, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 2),
('406334867', 3, 8, 11, 26, 0, 2, 2, 44, 4, 1, 0, 2, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0),
('439637823', 516, 0, 0, 2, 6, 0, 1, 551, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 9828),
('674697683', 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `user_inventory_2`
--

CREATE TABLE `user_inventory_2` (
  `id` int(11) NOT NULL,
  `user_id` varchar(25) NOT NULL,
  `type` varchar(25) NOT NULL,
  `name` varchar(400) NOT NULL,
  `rname` varchar(40) DEFAULT NULL,
  `equipped` int(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `user_inventory_2`
--

INSERT INTO `user_inventory_2` (`id`, `user_id`, `type`, `name`, `rname`, `equipped`) VALUES
(7, '239955010', 'body', '2', NULL, 0),
(8, '239955010', 'legs', '1', NULL, 0),
(10, '239955010', 'head', '1', NULL, 0),
(11, '239955010', 'body', '2', NULL, 1),
(16, '385224221', 'mask', '2', NULL, 0),
(17, '385224221', 'mask', '2', NULL, 0),
(19, '385224221', 'body', '2', NULL, 0),
(20, '385224221', 'head', '2', NULL, 0),
(21, '385224221', 'body', '2', NULL, 0),
(24, '385224221', 'gun', '4', NULL, 0),
(25, '385224221', 'body', '2', NULL, 0),
(32, '406334867', 'legs', '2', NULL, 1),
(33, '406334867', 'mask', '2', NULL, 0),
(36, '406334867', 'mask', '2', NULL, 0),
(37, '406334867', 'mask', '2', NULL, 0),
(38, '406334867', 'body', '2', NULL, 0),
(39, '406334867', 'mask', '2', NULL, 0),
(40, '406334867', 'mask', '2', NULL, 0),
(41, '406334867', 'head', '2', NULL, 1),
(42, '406334867', 'body', '2', NULL, 0),
(43, '406334867', 'mask', '2', NULL, 1),
(59, '278330138', 'gun', '3', NULL, 0),
(77, '239955010', 'gun', '3', NULL, 1),
(78, '239955010', 'gun', '2', NULL, 0),
(79, '239955010', 'body', '1', NULL, 0),
(82, '439637823', 'mask', '1', 'Говнопалочная маска', 1),
(83, '439637823', 'legs', '1', 'Говнопалочные сапоги', 1),
(84, '301227622', 'legs', '2', NULL, 0),
(85, '301227622', 'head', '2', NULL, 0),
(86, '301227622', 'head', '2', NULL, 0),
(87, '301227622', 'head', '2', NULL, 1),
(88, '301227622', 'body', '2', NULL, 1),
(89, '301227622', 'legs', '2', NULL, 0),
(90, '301227622', 'legs', '2', NULL, 0),
(91, '301227622', 'mask', '2', NULL, 0),
(92, '301227622', 'body', '2', NULL, 0),
(93, '301227622', 'legs', '2', NULL, 0),
(94, '301227622', 'mask', '2', NULL, 1),
(95, '301227622', 'legs', '2', NULL, 0),
(96, '301227622', 'legs', '2', NULL, 1),
(98, '314580963', 'gun', '4', NULL, 1),
(107, '314580963', 'head', '2', NULL, 1),
(113, '314580963', 'mask', '2', NULL, 1),
(114, '314580963', 'legs', '2', NULL, 1),
(115, '314580963', 'body', '2', NULL, 1),
(117, '439637823', 'gun', 'ban', NULL, 1),
(121, '439637823', 'shand', 'test', NULL, 0),
(123, '406334867', 'mask', '2', NULL, 0),
(124, '406334867', 'mask', '2', NULL, 0),
(125, '406334867', 'legs', '2', NULL, 0),
(126, '406334867', 'body', '2', NULL, 1),
(127, '406334867', 'gun', '3', NULL, 1),
(129, '439637823', 'shand', 'test', NULL, 0),
(130, '439637823', 'amulet', 'test', NULL, 0),
(131, '439637823', 'body', '4', 'NULL', 1),
(132, '439637823', 'head', '4', 'NULL', 1),
(133, '439637823', 'amulet', 'collector', NULL, 0),
(134, '439637823', 'amulet', 'insight', NULL, 0),
(135, '439637823', 'amulet', 'otorhin', NULL, 0),
(136, '439637823', 'amulet', 'hunter', NULL, 0),
(137, '439637823', 'shand', 'knife', NULL, 0),
(138, '439637823', 'shand', 'shield', NULL, 0),
(139, '406334867', 'amulet', 'collector', NULL, 0),
(140, '406334867', 'amulet', 'insight', NULL, 0),
(141, '406334867', 'amulet', 'otorhin', NULL, 0),
(142, '406334867', 'amulet', 'hunter', NULL, 0),
(143, '406334867', 'shand', 'knife', NULL, 0),
(144, '406334867', 'shand', 'shield', NULL, 0),
(145, '301227622', 'amulet', 'collector', NULL, 0),
(146, '301227622', 'amulet', 'insight', NULL, 0),
(147, '301227622', 'amulet', 'otorhin', NULL, 0),
(148, '301227622', 'amulet', 'hunter', NULL, 0),
(149, '301227622', 'shand', 'knife', NULL, 0),
(150, '301227622', 'shand', 'shield', NULL, 0),
(151, '314580963', 'amulet', 'collector', NULL, 0),
(152, '314580963', 'amulet', 'insight', NULL, 0),
(153, '314580963', 'amulet', 'otorhin', NULL, 1),
(154, '314580963', 'amulet', 'hunter', NULL, 0),
(155, '314580963', 'shand', 'knife', NULL, 1),
(156, '314580963', 'shand', 'shield', NULL, 0),
(157, '239955010', 'amulet', 'collector', NULL, 0),
(158, '239955010', 'amulet', 'insight', NULL, 0),
(159, '239955010', 'amulet', 'otorhin', NULL, 0),
(160, '239955010', 'amulet', 'hunter', NULL, 0),
(161, '239955010', 'shand', 'knife', NULL, 1),
(162, '239955010', 'shand', 'shield', NULL, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `user_prof`
--

CREATE TABLE `user_prof` (
  `user_id` int(11) NOT NULL,
  `craft` int(11) NOT NULL DEFAULT '0',
  `craft_exp` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `user_prof`
--

INSERT INTO `user_prof` (`user_id`, `craft`, `craft_exp`) VALUES
(239955010, 0, 0),
(278330138, 0, 0),
(301227622, 0, 0),
(308111497, 0, 0),
(314580963, 0, 0),
(385224221, 0, 0),
(406334867, 0, 0),
(439637823, 0, 0),
(674697683, 0, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `user_skill`
--

CREATE TABLE `user_skill` (
  `user_id` varchar(50) NOT NULL,
  `gold` int(11) NOT NULL DEFAULT '0',
  `time` int(11) NOT NULL DEFAULT '30',
  `bag` int(11) DEFAULT '5',
  `crit` int(11) NOT NULL DEFAULT '0',
  `bleed` int(11) NOT NULL DEFAULT '0',
  `vamp` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `user_skill`
--

INSERT INTO `user_skill` (`user_id`, `gold`, `time`, `bag`, `crit`, `bleed`, `vamp`) VALUES
('239955010', 10, 30, 15, 4, 4, 4),
('261825393', 0, 30, 5, 0, 0, 0),
('278330138', 10, 30, 5, 5, 0, 20),
('301227622', 0, 30, 6, 0, 0, 0),
('308111497', 10, 30, 15, 1, 1, 1),
('314580963', 10, 30, 11, 20, 20, 20),
('385224221', 10, 30, 15, 20, 20, 20),
('406334867', 10, 30, 15, 20, 20, 20),
('439637823', 0, 30, 5, 5, 5, 5),
('674697683', 10, 30, 5, 20, 20, 20);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `guild`
--
ALTER TABLE `guild`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `promocode`
--
ALTER TABLE `promocode`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `quest`
--
ALTER TABLE `quest`
  ADD PRIMARY KEY (`user_id`);

--
-- Индексы таблицы `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `tg_id` (`user_id`);

--
-- Индексы таблицы `user_equip`
--
ALTER TABLE `user_equip`
  ADD PRIMARY KEY (`user_id`);

--
-- Индексы таблицы `user_inventory`
--
ALTER TABLE `user_inventory`
  ADD PRIMARY KEY (`user_id`);

--
-- Индексы таблицы `user_inventory_2`
--
ALTER TABLE `user_inventory_2`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `user_prof`
--
ALTER TABLE `user_prof`
  ADD PRIMARY KEY (`user_id`);

--
-- Индексы таблицы `user_skill`
--
ALTER TABLE `user_skill`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `guild`
--
ALTER TABLE `guild`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT для таблицы `promocode`
--
ALTER TABLE `promocode`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT для таблицы `quest`
--
ALTER TABLE `quest`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=674697684;
--
-- AUTO_INCREMENT для таблицы `user_inventory_2`
--
ALTER TABLE `user_inventory_2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=163;
--
-- AUTO_INCREMENT для таблицы `user_prof`
--
ALTER TABLE `user_prof`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=674697684;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
