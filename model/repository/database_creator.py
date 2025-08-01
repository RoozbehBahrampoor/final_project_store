import sqlite3


def create_connection():
    connection = sqlite3.connect("store_db.sqlite")

    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS ADMINS
                   (
                       code     integer primary key autoincrement,
                       name     text not null,
                       family   text not null,
                       username text not null unique,
                       password text not null,
                       locked   tinyint default 0

                   )

                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS CUSTOMERS
                   (
                       code         integer primary key autoincrement,
                       name         text not null,
                       family       text not null,
                       username     text not null unique,
                       password     text not null,
                       phone_number text not null,
                       locked       tinyint default 0
                   )

                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS CARS
                   (
                       code   integer primary key autoincrement,
                       name   text    not null,
                       model  text    not null,
                       color  text    not null,
                       year   integer not null,
                       price  integer not null,
                       locked tinyint default 0
                   )

                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS HOUSES
                   (
                       code     integer primary key autoincrement,
                       region   text    not null,
                       address  text    not null,
                       floor    text    not null,
                       area     text    not null,
                       rooms    text    not null,
                       elevator text    not null,
                       parking  text    not null,
                       storage  text    not null,
                       year     integer not null,
                       price    integer not null,
                       locked   tinyint default 0
                   )

                   """)
    connection.commit()

    cursor.close()
    connection.close()



