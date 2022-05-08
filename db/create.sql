CREATE DATABASE siwusers;
use siwusers;

CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `user`(`name`,`email`,`login`,`password`,`role`) values 
('Soumitra Roy','sroy@gmail.com','user1','123456','user'),
('Rahul Kumar','rahul@gmail.com','admin','topsecret','admin');

CREATE TABLE `blog` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `createdate` varchar(50) NOT NULL,
  `login` varchar(100) NOT NULL,
  `text` varchar(400) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `blog`(`createdate`,`login`,`text`) values 
('2022-03-18T11:08:53.423559', 'Rahul Kumar','Welcome to that very cool blog. Enjoy!');
