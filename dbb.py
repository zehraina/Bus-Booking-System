import sqlite3
# con=sqlite3.connect('test_db')
con=sqlite3.connect('database_211b140')
# print(con.execute('select* from operator').fetchall())
# print(con.execute('select* from bus_details').fetchall())
# # # print(con.execute('delete from operator where id=10'))
# print(con.execute('select* from passenger').fetchall())
# # print(con.execute('select name from passenger where phone=111222333444').fetchall())
# print(con.execute('select* from runs').fetchall())
# print(con.execute('select *from bus_details').fetchall())
val=50
# val2=70
# con.execute(f"UPDATE  BUS_DETAILS SET capacity={val} WHERE bus_id=2")
# con.execute(f"UPDATE  BUS_DETAILS SET capacity={val2} WHERE capacity=10")
# con.commit()