-- CREATE DATABASE reservaVacacional;
USE reservaVacacional;

CREATE TABLE IF NOT EXISTS reservas (
    reservaId INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    creationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    phoneNumber VARCHAR(50),
    daysAmount INT NOT NULL DEFAULT 1,
    peopleAmount INT NOT NULL DEFAULT 1
)

select * from reservas;