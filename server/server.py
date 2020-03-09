# Mitru Adina
# 343C1

import json

import mysql.connector
from mysql.connector import Error, cursor
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/book', methods=['POST'])
def add_book():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        # details give by the admin for the flight
        title = request.values.get('title')
        author_name = request.values.get('author_name')
        publisher = request.values.get('publisher')
        language = request.values.get('language')
        genre = request.values.get('short_description')
        short_description = request.values.get('short_description')
        publishing_year = request.values.get('publishing_year')
        no_pages = request.values.get('no_pages')
        no_readers = request.values.get('no_readers')
        rate = request.values.get('rate')
        awards = request.values.get('awards')

        mySql_insert_query = """INSERT INTO flights (title, author_name, publisher, language, genre,
         short_description, publishing_year, no_pages, no_readers, rate, awards)
                                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        recordTuple = (title, author_name, publisher, language, genre, short_description, publishing_year,
                       no_pages, no_readers, rate, awards)
        cursor = conn.cursor()
        cursor.execute(mySql_insert_query, recordTuple)
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
        return ""


@app.route('/book', methods=['DELETE'])
def delete_book():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        book_id = request.values.get('book_id')
        sql_Delete_query = "Delete from book where book_id = %s"
        cursor = conn.cursor()
        cursor.execute(sql_Delete_query, (book_id,))
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
        return ""


@app.route('/book', methods=['POST'])
def list_books():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        sql_list_query = "Select from * book"
        cursor = conn.cursor()
        cursor.execute(sql_list_query)
        conn.commit()
        record = cursor.fetchone()
        recordTuple = (record[0], record[1], record[2], record[3], record[4], record[5],
                     record[6], record[7], record[8], record[9], record[10])

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
    return json.dumps(recordTuple)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
