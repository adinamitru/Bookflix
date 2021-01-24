import json
import sys

import requests
import mysql.connector
from mysql.connector import Error, cursor
from flask import Flask, escape, request
from werkzeug.utils import redirect

app = Flask(__name__)

# url_createAcc = 'http://server:5000/createAcc'


# url_login = 'http://server:5000/login'


@app.route('/login', methods=['POST'])
def login():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')

        user_name = request.values.get('user_name')
        password = request.values.get('password')
        sql_list_query = "Select * from user_info WHERE user_name = %s AND password = %s"
        cursor = conn.cursor()
        cursor.execute(sql_list_query, (user_name, password,))
        record = cursor.fetchone()
        print(record)
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
    return json.dumps(record)


@app.route('/createAcc', methods=['POST'])
def create_acc():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='db',
                                       port='3306',
                                       database='bookflix',
                                       user='root',
                                       password='root')
        print("DA")

        name = request.values.get('name')
        user_name = request.values.get('user_name')
        password = request.values.get('password')

        mySql_insert_query = """INSERT INTO user_info (name, user_name, password)
                                  VALUES (%s, %s, %s) """
        recordTuple = (name, user_name, password)
        cursor = conn.cursor()
        cursor.execute(mySql_insert_query, recordTuple)
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
        # return json.dumps(recordTuple)
        return ""


# def create_account(name, user_name, password):
#     response = requests.post(
#         url_createAcc,
#         data={'name': name,
#               'user_name': user_name,
#               'password': password})


# def list_users():
#     response = requests.get(
#         url_createAcc)
#     return response.text


# def login(user_name, password):
#     response = requests.get(url_createAcc, )
#     return response.text


# def operation_type():
#     while True:
#         print("Choose operation ('Create account' or 'Log in'): ")
#         line = sys.stdin.readline()
#         if line == "Create account\n":
#             recordTuple = read_add_details()
#             create_account(recordTuple[0], recordTuple[1], recordTuple[2])
#             print("User added successfully!")
#         if line == "Login\n":
#             user_name = input("user_name:  ")
#             password = input("password:  ")
#             login(user_name, password)
#             # print("Book deleted successfully!")
#         # if line == "List users\n":
#         #     list = list_users()
#         #     print(list)


# if __name__ == '__main__':
#     operation_type()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
