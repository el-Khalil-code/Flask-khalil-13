-- Création de la base de données
CREATE DATABASE IF NOT EXISTS formulaire_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Utilisation de la base de données
USE formulaire_db;

-- Suppression de la table si elle existe déjà (pour réinitialisation)
DROP TABLE IF EXISTS inscriptions;

-- Création de la table inscriptions
CREATE TABLE inscriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_complet VARCHAR(100) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    date_inscription DATETIME NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insertion des données
INSERT INTO inscriptions (id, nom_complet, ville, email, date_inscription) VALUES
(1, 'khalil', 'tanger', 'khalil20003@gmail.com', '2025-03-03 10:06:19'),
(3, 'ghjhgj', 'rabat', 'vodevav763@ahieh.com', '2025-03-03 10:23:07'),
(4, 'amine', 'kenitra', 'tipepe1498@fincainc.com', '2025-03-03 10:27:54'),
(5, 'amine', 'Setat', 'tipepe1498@fincainc.com', '2025-03-03 10:28:06'),
(6, 'amine', 'canablanca', 'tipepe1498@fincainc.com', '2025-03-03 10:28:25'),
(7, 'amine', 'kenitra', 'tipepe1498@fincainc.com', '2025-03-03 10:28:41'),
(8, 'dsdsd', 'khalil', 'kobate7348@tupanda.com', '2025-03-03 11:04:47'),
(9, 'ayoub', 'df', 'vodevav763@ahieh.com', '2025-03-03 11:12:48');

-- Réinitialiser l'auto-increment pour correspondre au dernier ID
ALTER TABLE inscriptions AUTO_INCREMENT = 10;