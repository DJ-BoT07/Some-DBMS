set serveroutput on;
declare
v_roll NUMBER;
v_name VARCHAR2(30);
v_marks NUMBER;
class VARCHAR2(30);
begin
v_roll := &roll;
v_name := '&name';
v_marks := &marks;
class := Fun2(v_roll, v_name, v_marks);
dbms_output.put_line(class);
end;
/
