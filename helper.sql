-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Июн 05 2024 г., 11:28
-- Версия сервера: 5.7.38
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `helper`
--

-- --------------------------------------------------------

--
-- Структура таблицы `food_drinks`
--

CREATE TABLE `food_drinks` (
  `id_food` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `food_drinks`
--

INSERT INTO `food_drinks` (`id_food`, `name`, `price`) VALUES
(0, 'Чай', 50),
(1, 'Кола', 150),
(2, 'Морс', 50),
(3, 'Салат', 250),
(4, 'Суп', 250),
(5, 'Сэндвич', 150);

-- --------------------------------------------------------

--
-- Структура таблицы `order_food`
--

CREATE TABLE `order_food` (
  `id_order` int(11) NOT NULL,
  `id_food` int(11) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  `counts` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `order_food`
--

INSERT INTO `order_food` (`id_order`, `id_food`, `id_user`, `counts`) VALUES
(1, 0, 0, 1),
(2, 0, 0, 2),
(3, 1, 0, 1),
(4, 2, 0, 1),
(5, 4, 0, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `order_services`
--

CREATE TABLE `order_services` (
  `id_order` int(11) NOT NULL,
  `id_services` int(11) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  `counts` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `order_services`
--

INSERT INTO `order_services` (`id_order`, `id_services`, `id_user`, `counts`) VALUES
(1, 1, 0, 1),
(2, 4, 0, 1),
(3, 3, 0, 1),
(4, 3, 0, 2),
(5, 5, 0, 1),
(6, 5, 0, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `services`
--

CREATE TABLE `services` (
  `id_services` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `services`
--

INSERT INTO `services` (`id_services`, `name`) VALUES
(0, 'Подушка'),
(1, 'Одеяло'),
(2, 'Приборы'),
(3, 'Наушники'),
(4, 'Телефон'),
(5, 'Проводник');

-- --------------------------------------------------------

--
-- Структура таблицы `user_helper`
--

CREATE TABLE `user_helper` (
  `id_user` int(11) NOT NULL,
  `report` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `user_helper`
--

INSERT INTO `user_helper` (`id_user`, `report`) VALUES
(0, ''),
(1, ''),
(2, ''),
(3, '');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `food_drinks`
--
ALTER TABLE `food_drinks`
  ADD PRIMARY KEY (`id_food`);

--
-- Индексы таблицы `order_food`
--
ALTER TABLE `order_food`
  ADD PRIMARY KEY (`id_order`),
  ADD KEY `id_food` (`id_food`),
  ADD KEY `id_user` (`id_user`);

--
-- Индексы таблицы `order_services`
--
ALTER TABLE `order_services`
  ADD PRIMARY KEY (`id_order`),
  ADD KEY `id_services` (`id_services`),
  ADD KEY `id_user` (`id_user`);

--
-- Индексы таблицы `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id_services`);

--
-- Индексы таблицы `user_helper`
--
ALTER TABLE `user_helper`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `order_food`
--
ALTER TABLE `order_food`
  MODIFY `id_order` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `order_services`
--
ALTER TABLE `order_services`
  MODIFY `id_order` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `order_food`
--
ALTER TABLE `order_food`
  ADD CONSTRAINT `order_food_ibfk_1` FOREIGN KEY (`id_food`) REFERENCES `food_drinks` (`id_food`),
  ADD CONSTRAINT `order_food_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user_helper` (`id_user`);

--
-- Ограничения внешнего ключа таблицы `order_services`
--
ALTER TABLE `order_services`
  ADD CONSTRAINT `order_services_ibfk_1` FOREIGN KEY (`id_services`) REFERENCES `services` (`id_services`),
  ADD CONSTRAINT `order_services_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user_helper` (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
