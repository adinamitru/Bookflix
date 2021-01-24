import json

import mysql.connector
import requests
from mysql.connector import Error, cursor
from flask import Flask, escape, request
from werkzeug.utils import redirect

app = Flask(__name__)

url_login = 'http://auth:6000/login'
url_createAcc = 'http://auth:6000/createAcc'


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
        print("DA")

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

        mySql_insert_query = """INSERT INTO book (title, author_name, publisher, language, genre,
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


@app.route('/createAcc', methods=['POST'])
def create_acc():
    name = request.values.get('name')
    user_name = request.values.get('user_name')
    password = request.values.get('password')
    print('Sunt in server in login')
    response = requests.post(
        url_createAcc,
        data={
            'name': name,
            'user_name': user_name,
            'password': password})


@app.route('/login', methods=['POST'])
def login():
    user_name = request.values.get('user_name')
    password = request.values.get('password')
    print('Sunt in server in login')
    response = requests.post(
        url_login,
        data={
            'user_name': user_name,
            'password': password})
    print(response.json())
    return json.dumps(response.text)


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
        sql_select_booking_query = "Select * from book where book_id = %s"
        cursor = conn.cursor()
        cursor.execute(sql_select_booking_query, (book_id,))
        exits = cursor.fetchone()
        if exits != "":
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









@app.route('/book', methods=['GET'])
def list_books():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        print("DA")
        sql_list_query = "Select * from book"
        cursor = conn.cursor()
        cursor.execute(sql_list_query)
        record = cursor.fetchall()
        print("DA")
        print(record)

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
    return json.dumps(record)


@app.route('/user', methods=['POST'])
def list_category():
    """ Connect to MySQL database """
    category_no = 0
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        category = request.values.get('category')
        cursor = conn.cursor()
        if category == "read":
            category_no = 1
        elif category == "started":
            category_no = 2
        elif category == "liked":
            category_no = 3
        elif category == "disliked":
            category_no = 4

        print(category_no)
        sql_list_query = "Select title, author_name from user_client natural join book where list_id = %s"
        cursor.execute(sql_list_query, (category_no,))
        record = cursor.fetchall()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
    return json.dumps(record)


@app.route('/books', methods=['POST'])
def get_book():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        category = request.values.get('category')
        category_type = request.values.get('category_type')
        sql_select_booking_query = """Select * from book where genre = %s"""
        cursor = conn.cursor()
        cursor.execute(sql_select_booking_query, (category_type,))
        record = cursor.fetchall()
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
    return json.dumps(record)


@app.route('/read', methods=['POST'])
def read_book():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        read_book_name = request.values.get('read_book_name')
        liked = request.values.get('liked')
        sql_select_booking_query = """Select * from book where title = %s"""
        cursor = conn.cursor()
        cursor.execute(sql_select_booking_query, (read_book_name,))
        record = cursor.fetchone()
        book_id = record[0]
        conn.commit()

        mySql_insert_read_query = """INSERT INTO user_client (book_id, list_id)
                                  VALUES (%s, 1) """
        cursor = conn.cursor()
        cursor.execute(mySql_insert_read_query, (book_id,))
        conn.commit()

        if liked == 'like':
            mySql_insert_liked_query = """INSERT INTO user_client (book_id, list_id)
                                      VALUES (%s, 3) """
            cursor = conn.cursor()
            cursor.execute(mySql_insert_liked_query, (book_id,))
            conn.commit()
        elif liked == 'dislike':
            mySql_insert_liked_query = """INSERT INTO user_client (book_id, list_id)
                                      VALUES (%s, 4) """
            cursor = conn.cursor()
            cursor.execute(mySql_insert_liked_query, (book_id,))
            conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
    return ""


@app.route('/start', methods=['POST'])
def start_book():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        stat_book_name = request.values.get('stat_book_name')
        sql_select_booking_query = """Select * from book where title = %s"""
        cursor = conn.cursor()
        cursor.execute(sql_select_booking_query, (stat_book_name,))
        record = cursor.fetchone()
        book_id = record[0]
        genre = record[5]
        print(genre)
        conn.commit()

        mySql_insert_started_query = """INSERT INTO user_client (book_id, list_id)
                                          VALUES (%s, 2) """
        cursor = conn.cursor()
        cursor.execute(mySql_insert_started_query, (book_id,))
        conn.commit()

        sql_select_suggest_query = """Select * from book where genre = %s and not(book_id=%s)"""
        cursor = conn.cursor()
        cursor.execute(sql_select_suggest_query, (genre, book_id,))
        record_suggest = cursor.fetchall()
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
    return json.dumps(record_suggest)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
