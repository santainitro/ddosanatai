import mysql.connector
py_my = mysql.connector.connect(
  	host = "localhost",
  	user = "nitro",
  	password = "nitro@fe",
  	database = "db_server"
)
py_cur = py_my.cursor()
py_cur.execute("SELECT * FROM db_table WHERE stud_name = %B;", (stud_name,))

