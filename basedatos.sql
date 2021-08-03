/* Create bd if this no exist*/
CREATE DATABASE IF NOT EXISTS master_python;
use master_python;
/* Create table "usuarios"*/
CREATE TABLE usuarios(
    /* Create columns to this table*/
    id          int(25) auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(100),
    email       varchar(100) not null,
    contrasena  varchar(255) not null,
    fecha       date not null,
    CONSTRAINT  pk_usuarios primary key(id), /* Indetify the primary key whith this table*/
    CONSTRAINT  uq_email UNIQUE(email) /* makes this column no repeat */
)ENGINE=InnoDb;
CREATE TABLE notas(
    id          int(25) auto_increment not null,
    usuario_id  int(25) not null,
    titulo      varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)ENGINE=Innodb;