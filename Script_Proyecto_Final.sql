-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema PROYECTO_FINAL
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema PROYECTO_FINAL
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `PROYECTO_FINAL` DEFAULT CHARACTER SET utf8 ;
USE `PROYECTO_FINAL` ;

-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Acuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Acuario` (
  `Numero_RUT` VARCHAR(10) NOT NULL COMMENT 'Código de indentificación encontrado en el RUT.',
  `Coste_mantenimento` DOUBLE NOT NULL COMMENT 'El coste de mantenimiento general del acuario.',
  PRIMARY KEY (`Numero_RUT`),
  UNIQUE INDEX `Numero de RUT_UNIQUE` (`Numero_RUT` ASC) VISIBLE)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información general del acuario.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Trabajador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Trabajador` (
  `ID_trabajador` INT NOT NULL COMMENT 'Este es el ID de cada trabajador.',
  `Numero_RUT` VARCHAR(10) NOT NULL COMMENT 'Clave foránea que indica el código de indentificación encontrado en el RUT del acuario.',
  `Nombres` VARCHAR(30) NOT NULL COMMENT 'Aquí se guarda los nombres del trabajador.',
  `Apellidos` VARCHAR(30) NOT NULL COMMENT 'Aquí se guardan los apellidos de los trabajadores.',
  `Celular` VARCHAR(15) NOT NULL,
  `Salario` DOUBLE NOT NULL COMMENT 'Aquí se guarda el salario de cada trabajador.',
  `Numero_cuenta_bancaria` INT NOT NULL COMMENT 'Aquí se guarda el número de cuenta bancaria de cada trabajador.',
  `Direccion` VARCHAR(30) NULL COMMENT 'Aquí se guarda la dirección de cada trabajado (opcional).',
  `Edad` VARCHAR(45) NULL COMMENT 'Aquí se guarda la edad del trabajador (opcional).',
  `Tipo_trabajador` VARCHAR(30) NOT NULL COMMENT 'Atributo donde se sabe que tipo de trabajador es: biólogo, cuidador o de roles varios.',
  `Hora-Entradaa` TIME NOT NULL,
  `Hora-Salida` TIME NOT NULL,
  PRIMARY KEY (`ID_trabajador`),
  UNIQUE INDEX `ID_trabajador_UNIQUE` (`ID_trabajador` ASC) VISIBLE,
  UNIQUE INDEX `Numero_cuenta_bancaria_UNIQUE` (`Numero_cuenta_bancaria` ASC) VISIBLE,
  INDEX `FK_Trabajador_Acuario_idx` (`Numero_RUT` ASC) VISIBLE,
  CONSTRAINT `FK_Trabajador_Acuario`
    FOREIGN KEY (`Numero_RUT`)
    REFERENCES `PROYECTO_FINAL`.`Acuario` (`Numero_RUT`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de cada trabajador.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Biologo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Biologo` (
  `ID_trabajador` INT NOT NULL COMMENT 'Clave foránea que indica el ID del trabajador.',
  `Puesto_especifico` VARCHAR(45) NOT NULL COMMENT 'Puesto específico del Biólogo. ',
  INDEX `FK_Biologo_Trabajador_idx` (`ID_trabajador` ASC) VISIBLE,
  PRIMARY KEY (`ID_trabajador`),
  CONSTRAINT `FK_Biologo_Trabajador`
    FOREIGN KEY (`ID_trabajador`)
    REFERENCES `PROYECTO_FINAL`.`Trabajador` (`ID_trabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de un tipo de tarbajador: Biólogo.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Roles_varios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Roles_varios` (
  `ID_trabajador` INT NOT NULL COMMENT 'Clave foránea que indica el ID de cada trabajador de roles varios.',
  `Cargo_especifico` VARCHAR(30) NOT NULL COMMENT 'Cargo específico en el que se desempeña el trabajador.',
  `Empresa_origen` VARCHAR(45) NULL COMMENT 'Empresa a la que pertenece el trabajador (opçional).',
  INDEX `FK_Roles_varios_Trabajador_idx` (`ID_trabajador` ASC) VISIBLE,
  PRIMARY KEY (`ID_trabajador`),
  CONSTRAINT `FK_Roles_varios_Trabajador`
    FOREIGN KEY (`ID_trabajador`)
    REFERENCES `PROYECTO_FINAL`.`Trabajador` (`ID_trabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de un tipo de tarbajador: Roles varios.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Grupo_investigacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Grupo_investigacion` (
  `Codigo_grupo` INT NOT NULL COMMENT 'Clave primaria que indica el código del grupo de investigación. ',
  `Area_investigacion` VARCHAR(30) NOT NULL COMMENT 'Área que investiga el grupo. ',
  `Presupuesto` DOUBLE NOT NULL COMMENT 'Presupuesto general de grupo.',
  PRIMARY KEY (`Codigo_grupo`),
  UNIQUE INDEX `Codigo_grupo_UNIQUE` (`Codigo_grupo` ASC) VISIBLE)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de cada grupo de investigación.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Biologo_grupo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Biologo_grupo` (
  `ID_trabajador` INT NOT NULL COMMENT 'Clave foránea que indica el ID del Biólogo.',
  `Codigo_grupo` INT NOT NULL COMMENT 'Clave foránea que indica el código del grupo al que pertenece el Biólogo.',
  `Fecha_inicio` DATE NOT NULL COMMENT 'Fecha en la que se unió el Biólogo al grupo de investigación.',
  `Fecha_final` DATE NULL COMMENT 'Fecha en la que se salió, el Biólogo, del grupo de investigación (este es opcional por si el trabajador sigue en el grupo).',
  UNIQUE INDEX `Codigo_grupo_UNIQUE` (`Codigo_grupo` ASC) VISIBLE,
  INDEX `FK_Biologo_grupo_Biologo_idx` (`ID_trabajador` ASC) VISIBLE,
  CONSTRAINT `FK_Biologo_grupo_Biologo`
    FOREIGN KEY (`ID_trabajador`)
    REFERENCES `PROYECTO_FINAL`.`Biologo` (`ID_trabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Biologo_grupo_Grupo_investigacion`
    FOREIGN KEY (`Codigo_grupo`)
    REFERENCES `PROYECTO_FINAL`.`Grupo_investigacion` (`Codigo_grupo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de la relación entre un biólogo y su grupo de investigación.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Experiencia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Experiencia` (
  `ID_trabajador` INT NOT NULL COMMENT 'Clave foránea que indica el ID del trabajador.',
  `Area` VARCHAR(20) NOT NULL COMMENT 'Area de experticia. ',
  `Annos` INT NOT NULL COMMENT 'Aquí se guardan los años de experiencia que tiene el trabajador en la determinada área.',
  `Descripcion` VARCHAR(45) NOT NULL COMMENT 'Una breve descripción de la experiencia en el determinado campo.',
  CONSTRAINT `FK_Experiencia_Trabajador`
    FOREIGN KEY (`ID_trabajador`)
    REFERENCES `PROYECTO_FINAL`.`Trabajador` (`ID_trabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de la experiencia de cada trabajador.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Tanque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Tanque` (
  `Numero_tanque` INT NOT NULL AUTO_INCREMENT COMMENT 'Numero de identificación del tanque, el cual empieza desde el 0.',
  `Numero_RUT` VARCHAR(10) NOT NULL COMMENT 'Clave foránea que se relaciona con el RUT del acuario.',
  `Habitat` VARCHAR(6) NOT NULL COMMENT 'Tipo de agua que contiene el tanque, ya sea agua dulce o salada.',
  `Tamano` VARCHAR(10) NOT NULL COMMENT 'Se refiere al tamaño que el tanque dispone para albergar animales y plantas marinas, (recordar que los animales estan entre el tamaño pequeño y mediano).',
  PRIMARY KEY (`Numero_tanque`),
  INDEX `fk_Tanque_Acuario1_idx` (`Numero_RUT` ASC) VISIBLE,
  CONSTRAINT `fk_Tanque_Acuario1`
    FOREIGN KEY (`Numero_RUT`)
    REFERENCES `PROYECTO_FINAL`.`Acuario` (`Numero_RUT`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de cada tanque, donde viven los distintos seres vivos.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Vida_marina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Vida_marina` (
  `ID` INT NOT NULL AUTO_INCREMENT COMMENT 'Numero de identificación de cada ser vivo, empezando desde cero.',
  `Numero_tanque` INT NOT NULL COMMENT 'Clave foránea que indica a que tanque pertence cada ser vivo.',
  `Habitat` VARCHAR(6) NOT NULL COMMENT 'Tipo de habitat en la que se puede encontrar la especie, puede ser agua dulce o salada.',
  `Alimento` VARCHAR(15) NOT NULL COMMENT 'Tipo de comida que el acuario le suministra a los animales, por ejemplo gusanos o peces pequeños.',
  `Tipo_vida_marina` VARCHAR(15) NOT NULL COMMENT 'Atributo que indica si es un animal o una planta.',
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE,
  INDEX `FK_Vida_marina_Tanque_idx` (`Numero_tanque` ASC) VISIBLE,
  CONSTRAINT `FK_Vida_marina_Tanque`
    FOREIGN KEY (`Numero_tanque`)
    REFERENCES `PROYECTO_FINAL`.`Tanque` (`Numero_tanque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Aquí se guardarán los datos relacionados a las diferentes especies de seres vivos encontrados en el acuario.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Animal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Animal` (
  `ID_animal` INT NOT NULL COMMENT 'Numero de identificación de los animales, empezando desde el 0.',
  `Comportamiento` VARCHAR(15) NOT NULL COMMENT 'Se refiere al comportamiento general o la naturaleza del animal, es decir si es agresivo, pasivo, nervioso, etc.',
  PRIMARY KEY (`ID_animal`),
  CONSTRAINT `FK_Animal_Vida_Marina`
    FOREIGN KEY (`ID_animal`)
    REFERENCES `PROYECTO_FINAL`.`Vida_marina` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Especies pertenecientes al reino animal las cuales se albergan dentro de los acuarios, hereda de Vida_Marina y tiene un solo atributo llamada comportamiento.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Planta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Planta` (
  `ID_planta` INT NOT NULL COMMENT 'Numero de identificación de cada planta, empezando desde el 0.\n',
  `Funcion` VARCHAR(15) NOT NULL COMMENT 'La función exacta que cumple dentro del acuario, este puede abarcar trabajos como, decoración, alimento para algunos animales, control, entre otras.',
  PRIMARY KEY (`ID_planta`),
  CONSTRAINT `fk_Plantas_vida marina`
    FOREIGN KEY (`ID_planta`)
    REFERENCES `PROYECTO_FINAL`.`Vida_marina` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Especies pertenecientes al reino vegetal y al reino protista las cuales se albergan dentro de los acuarios, hereda de Vida_Marina y tiene un solo atributo llamado función.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Taquilla`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Taquilla` (
  `Numero_taquilla` INT NOT NULL AUTO_INCREMENT COMMENT 'El numero de identificación de taquilla que va desde el 0.',
  `Numero_RUT` VARCHAR(10) NOT NULL COMMENT 'Código de indentificación encontrado en el RUT.',
  `ID_trabajador` INT NOT NULL COMMENT 'ID de los trabajadores encargado de operar los diferentes puesto de taquilla.',
  PRIMARY KEY (`Numero_taquilla`),
  INDEX `FK_Taquilla_Acuario_idx` (`Numero_RUT` ASC) VISIBLE,
  INDEX `FK_Taquillla_RolesVarios_idx` (`ID_trabajador` ASC) VISIBLE,
  CONSTRAINT `FK_Taquilla_Acuario`
    FOREIGN KEY (`Numero_RUT`)
    REFERENCES `PROYECTO_FINAL`.`Acuario` (`Numero_RUT`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Taquillla_Roles_varios`
    FOREIGN KEY (`ID_trabajador`)
    REFERENCES `PROYECTO_FINAL`.`Roles_varios` (`ID_trabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Punto de entrada de los visitantes, lugar donde se paga para la entrada del acuario.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Venta_taquilla`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Venta_taquilla` (
  `ID_Venta` INT NOT NULL AUTO_INCREMENT COMMENT 'Numero de identificación de la venta.',
  `Numero_taquilla` INT NOT NULL COMMENT 'Clave foránea que indicada en que taquilla se hizo la venta.',
  `Precio_entrada` DOUBLE NOT NULL COMMENT 'Precio de la entrada (precio predeterminado).',
  `Hora_entrada` DATETIME NOT NULL COMMENT 'Hora de la entrada al acuario.',
  `Hora_salida` DATETIME NOT NULL,
  PRIMARY KEY (`ID_Venta`),
  INDEX `fk_Venta_Taquilla_idx` (`Numero_taquilla` ASC) VISIBLE,
  CONSTRAINT `FK_Venta_taquilla_Taquilla`
    FOREIGN KEY (`Numero_taquilla`)
    REFERENCES `PROYECTO_FINAL`.`Taquilla` (`Numero_taquilla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de cada venta que se haga en cada taquilla.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Cuidador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Cuidador` (
  `ID_trabajador` INT NOT NULL COMMENT 'Clave foránea que indica el ID de cada Cuidador.',
  `Numero de tanque` INT NOT NULL COMMENT 'El tanque en cuestión que el cuidador tiene asiganado para cuidar de los animales albergados adentro.',
  `Especialización` VARCHAR(45) NOT NULL COMMENT 'Se refiere al tipo de seres vivos en los que este cuidador se especializa en atender, por ejemplo, plantas, peces pequeños, etc.',
  PRIMARY KEY (`ID_trabajador`),
  INDEX `fk_Cuidador_Tanque_idx` (`Numero de tanque` ASC) VISIBLE,
  CONSTRAINT `FK_Cuidador_Trabajador`
    FOREIGN KEY (`ID_trabajador`)
    REFERENCES `PROYECTO_FINAL`.`Trabajador` (`ID_trabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Cuidador_Tanque`
    FOREIGN KEY (`Numero de tanque`)
    REFERENCES `PROYECTO_FINAL`.`Tanque` (`Numero_tanque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de cada Cuidador.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Local`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Local` (
  `Numero_local` INT NOT NULL AUTO_INCREMENT COMMENT 'Número del local.',
  `Numero_RUT` VARCHAR(10) NOT NULL COMMENT 'Clave foránea que indica el código de indentificación encontrado en el RUT del acuario.',
  `Empresa_afiliada` VARCHAR(45) NULL COMMENT 'Empresa a la cual está afiliado el local (esto es opcional).',
  PRIMARY KEY (`Numero_local`),
  INDEX `fk_Local_Acuario1_idx` (`Numero_RUT` ASC) VISIBLE,
  UNIQUE INDEX `RUT_UNIQUE` (`Numero_local` ASC) VISIBLE,
  CONSTRAINT `FK_Local_Acuario`
    FOREIGN KEY (`Numero_RUT`)
    REFERENCES `PROYECTO_FINAL`.`Acuario` (`Numero_RUT`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de cada local en el acuario.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Producto` (
  `Nombre_producto` VARCHAR(45) NOT NULL COMMENT 'Nombre del producto.',
  `Precio_producto` DOUBLE NOT NULL COMMENT 'Precio del producto.',
  `Cantidad` INT ZEROFILL NOT NULL COMMENT 'La cantidad total que se tiene de cada producto en un local.',
  PRIMARY KEY (`Nombre_producto`))
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de cada producto que se tiene en un local.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Local_roles_varios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Local_roles_varios` (
  `Numero_local` INT NOT NULL,
  `ID_trabajador` INT NOT NULL COMMENT 'Clave foránea que indica el ID de cada Trabajador.',
  `Hora_entrada` TIME NOT NULL COMMENT 'Hora de entrada del trabador al local. ',
  `Hora_salida` TIME NOT NULL COMMENT 'Hora de salida del trabajador del local.',
  INDEX `fk_local roles varios_Local1_idx` (`Numero_local` ASC) VISIBLE,
  CONSTRAINT `FK_Local_roles_varios_Local`
    FOREIGN KEY (`Numero_local`)
    REFERENCES `PROYECTO_FINAL`.`Local` (`Numero_local`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Local_roles_varios_Roles_varios`
    FOREIGN KEY (`ID_trabajador`)
    REFERENCES `PROYECTO_FINAL`.`Roles_varios` (`ID_trabajador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de la relación entre un trabajador de roles varios con un local.';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Venta_local`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Venta_local` (
  `ID_venta` INT NOT NULL AUTO_INCREMENT COMMENT 'ID de cada venta del local.',
  `Numero_local` INT NOT NULL COMMENT 'Clave foránea que indica el número del local donde se hizo la compra.',
  `Nombre_producto` VARCHAR(45) NOT NULL COMMENT 'Nombre del producto.',
  `Cantidad` INT NOT NULL COMMENT 'Cantidad del mismo producto que se hizo en la compra.',
  PRIMARY KEY (`ID_venta`),
  INDEX `fk_ventas locales_Local1_idx` (`Numero_local` ASC) VISIBLE,
  INDEX `FK_Venta_local_Producto_idx` (`Nombre_producto` ASC) VISIBLE,
  CONSTRAINT `FK_Venta_local_Local`
    FOREIGN KEY (`Numero_local`)
    REFERENCES `PROYECTO_FINAL`.`Local` (`Numero_local`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Venta_local_Producto`
    FOREIGN KEY (`Nombre_producto`)
    REFERENCES `PROYECTO_FINAL`.`Producto` (`Nombre_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de cada venta que se hace en un local. ';


-- -----------------------------------------------------
-- Table `PROYECTO_FINAL`.`Importacion_producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`Importacion_producto` (
  `Codigo_importacion` INT NOT NULL AUTO_INCREMENT COMMENT 'Este el código de cada importación que se hace en un local. No puede ser menor de 0.',
  `Numero_local` INT NOT NULL COMMENT 'Clave foránea que indica el local donde se hace la importación.',
  `Nombre_producto` VARCHAR(45) NOT NULL COMMENT 'Clave foránea que indica el nombre del producto importado.',
  `Cantidad` INT NOT NULL COMMENT 'Cantidad total del producto en la importación.',
  `Precio_unitario` DOUBLE NOT NULL COMMENT 'Precio de importación del producto.',
  `Fecha_importacion` DATE NOT NULL COMMENT 'Fecha de la importación.',
  PRIMARY KEY (`Codigo_importacion`),
  INDEX `fk_Importación de producto_Local1_idx` (`Numero_local` ASC) VISIBLE,
  INDEX `FK_Importacion_producto_Producto_idx` (`Nombre_producto` ASC) VISIBLE,
  CONSTRAINT `FK_Importacion_producto_Local`
    FOREIGN KEY (`Numero_local`)
    REFERENCES `PROYECTO_FINAL`.`Local` (`Numero_local`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Importacion_producto_Producto`
    FOREIGN KEY (`Nombre_producto`)
    REFERENCES `PROYECTO_FINAL`.`Producto` (`Nombre_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'En esta tabla se guarda la información de la importación que se hacen de productos a un local.';

USE `PROYECTO_FINAL` ;

-- -----------------------------------------------------
-- Placeholder table for view `PROYECTO_FINAL`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO_FINAL`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `PROYECTO_FINAL`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `PROYECTO_FINAL`.`view1`;
USE `PROYECTO_FINAL`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
