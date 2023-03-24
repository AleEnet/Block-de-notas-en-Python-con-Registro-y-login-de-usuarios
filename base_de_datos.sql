CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLA usuarios (
    id  int(255) auto_ increment not null,
    nombre  varchar(100),
    apellido    varchar(255),
    email   varchar(255) not null,
    password    varchar(255) not null,
    fecha   date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE = InnoDB

CREATE TABLE notas (
    id INT(255) AUTO_INCREMENT NOT NULL,
    usuario_id INT(25) NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY (id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
) ENGINE = InnoDB;