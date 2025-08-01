-- Save Admin
insert into admins
    (code, name, family, username, password, locked)
values (2, 'parsa', 'akbari', 'parsa567', 'parsa567', 0);

-- Search - Find
select *
from admins
where code = 1;

select *
from admins
where username='parsa123' and password='parsa896';

-- Edit
update admins set name=?, family=?, username=?, password=?, locked=?
where code=?;

-- Delete
delete from cars where code =210;