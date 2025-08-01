import sqlite3

connection = sqlite3.connect("store_db.sqlite")


# cursor = connection.cursor()


# cursor.execute("SQL")


# connection.commit()


# coursor.close()
connection.close()
