create or replace Procedure pro1(
    roll in number,
    name in varchar2,
    marks in number
) as
BEGIN
    if(marks <= 1500 and marks >= 1000) THEN
    dbms_output.put_line('Distinction');
    insert into result(roll, name, class) 
    values
    (roll, name, 'Distinction');
    elsif(marks < 999 and marks >= 800) THEN
    dbms_output.put_line('First Class');
    insert into result(roll, name, class)
    values
    (roll, name, 'First Class');
    elsif(marks < 799 and marks >= 600) THEN
    dbms_output.put_line('Second Class');
    insert into result(roll, name, class)
    values
    (roll, name, 'Second Class');
    else
    dbms_output.put_line('Fail');
    insert into result(roll, name, class)
    values
    (roll, name, 'Fail');
    end if;

    commit;
END;
/
