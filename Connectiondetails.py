import mysql.connector
cnx =mysql.connector.connect(user='root', password='root', host='localhost', port='3306')
print(cnx.get_server_info())