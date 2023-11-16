-- Crear tabla audioria_vida_marina para trigger --
create table if not exists auditoria_vida_marina
(
	ID int not null auto_increment,
	usuario varchar(30) not null,
    fecha datetime not null,
    primary key(ID)
);

-- Trigger para auditoria de Vida_marina --
delimiter //
create trigger auditoria_animal after insert on Vida_marina
for each row
begin
	insert into auditoria_vida_marina(usuario, fecha) value(current_user(), current_timestamp());
end //
delimiter ;

-- Trigger para verificar la compatibilidad del hábitat --
delimiter // 
create trigger verificar_habitat before insert on vida_marina
for each row
begin 
	declare tanque_habitat varchar(6);
    
	select habitat into tanque_habitat
    from tanque 
    where Numero_tanque = new.Numero_tanque;
    
    if new.habitat != tanque_habitat then 
		signal sqlstate '45000'
		set message_text = "Los habitats no coiciden. No se puede realizar la inserción";
    end if;
end // 
delimiter ;

-- Procedimiento para obtener los seres vivos que viven en cierto hábitat --
delimiter //
create procedure obtener_habitat(in habi varchar(6))
begin
	select ID
    from Vida_marina
    where habitat = habi;
end // 
delimiter ;