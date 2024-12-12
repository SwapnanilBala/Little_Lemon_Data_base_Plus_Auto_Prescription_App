USE mydb;

ALTER TABLE booking RENAME TO Bookings;
ALTER TABLE staff RENAME TO Staffs ;
ALTER TABLE menus RENAME TO menu_items;
ALTER TABLE menu_table RENAME TO menu;

DESCRIBE bookings;
DESCRIBE menu_items;
DESCRIBE menu;
DESCRIBE orders;
DESCRIBE staffs;

ALTER TABLE menu_items MODIFY Price float;


DELIMITER //

CREATE PROCEDURE insert_menuitems(
    IN Item_ID INT, 
    IN Name VARCHAR(255), 
    IN Type VARCHAR(255), 
    IN Price FLOAT
)
BEGIN
    INSERT INTO menu_items (Item_ID, Name, Type, Price)
    VALUES (Item_ID, Name, Type, Price);
END //

DELIMITER ;

# we shall now move to using jupyter notebook

