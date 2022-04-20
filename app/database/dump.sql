DROP DATABASE IF EXISTS who_got_next;
CREATE DATABASE who_got_next ENCODING 'utf8';
-- Need to convert to postgre
-- CREATE TABLE IF NOT EXISTS who_got_next.author (
--     id INT UNSIGNED NOT NULL AUTO_INCREMENT,
--     username VARCHAR(30) NOT NULL,
--     isAdmin BOOLEAN NOT NULL,
--     password VARCHAR(255) NOT NULL,
--     email VARCHAR(40) NOT NULL,
--     token VARCHAR(40) NOT NULL,
--     PRIMARY KEY (id)
--     );