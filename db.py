import cx_Oracle
con = cx_Oracle.connect('system/mayank12345@localhost/oracle')
print con.version
