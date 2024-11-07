set serveroutput on
declare 
v_book_name Borrower.NameofBook%TYPE;
v_roll Borrower.Rollin%TYPE;
v_days NUMBER;
v_fine NUMBER;

BEGIN
v_roll := &roll_on;
v_book_name := '&NameofBook';

select TRUNC(SYSDATE) - DateofIssue into v_days from Borrower where Rollin = v_roll and NameofBook = v_book_name;

IF v_days > 30 THEN
v_fine := (v_days) * 50;
ELSIF v_days between 15 and 30 THEN
v_fine := (v_days) * 5;
END IF;

IF v_fine > 0 THEN
 insert into Fine (Roll_No, FineDate, Amt) values (v_roll, SYSDATE, v_fine);
END IF;

UPDATE Borrower set Status  = 'R' where Rollin = v_roll and NameofBook = v_book_name;

COMMIT;

EXCEPTION
WHEN NO_DATA_FOUND THEN
    dbms_output.put_line('No such record found');
WHEN OTHERS THEN
    dbms_output.put_line('Error');
END;
/
