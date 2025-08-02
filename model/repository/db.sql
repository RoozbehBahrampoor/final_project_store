-- Save Admin
insert into admins
    (code, name, family, username, password, locked)
values (7, 'nima', 'akbari', 'parsa567', 'parsa567', 0);

-- Search - Find
select *
from admins
where code = 1;

select *
from admins
where username = 'parsa123'
  and password = 'parsa896';

-- Edit
update admins
set name=?,
    family=?,
    username=?,
    password=?,
    locked=?
where code = ?;
-- Delete
delete
from admins
where code = 2;

-- Delete
delete
from cars
where code = 1;

-- Save Car
insert into cars
    (code, name, model, color, year, price, locked)
values (105, 'quick', 'gxl', 'red', '2020', '17000', 0);
-- Search - Find
select *
from cars
where code = 105;
-- Edit
update cars
set name='quick',
    model='r',
    color='blue',
    year='2021',
    price='10000'
where code = 105;
-- Delete
delete
from cars
where code = 105;
-- Save Customer
insert into customers
    (code, name, family, username, password, phone_number, locked)
values(500,'kasra','aghayi','kasra12','kasra456','09194678291', 0);
-- Search - Find
select *
from customers
where code = 500;
-- Edit
update customers
set name=?, family=?, username=?, password=?, phone_number=?, locked=?
where code=?;
-- Delete
delete
from customers
where code = 500;
-- Save House
insert into houses
(code, region, address, floor, area, rooms, elevator, parking, storage, year, price,
locked)
values(1000,'azadi','saeed','7','5','2','0','2','6','2000','140000',0);
-- Search - Find
select *
from houses
where code = 1000;
-- Edit
update houses
set region=?, address=?, floor=?, area=?, rooms=?, elevator=?, parking=?, storage=?, year=?, price=?,locked=?
where code=?;
-- Delete
delete
from houses
where code = 1;