create or replace FUNCTION Fun2(
    r in NUMBER,
    n in VARCHAR2,
    m in NUMBER
) return varchar2 as
BEGIN
pro1(r, n, m);
return 'Success';
END;
/