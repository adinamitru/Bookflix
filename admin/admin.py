# Mitru Adina
# 343C1
import json
import sys

import requests

url = 'http://server:5000/book'
url_login = 'http://server:5000/login'
url_createAcc = 'http://server:5000/createAcc'


def delete_book(book_id):
    response = requests.delete(
        url,
        data={'book_id': book_id})


def list_books():
    response = requests.get(
        url)
    return response.text


def add_book(title, author_name, publisher, language, genre, short_description, publishing_year,
             no_pages, no_readers, rate, awards):
    response = requests.post(url,
                             data={'title': title,
                                   'author_name': author_name,
                                   'publisher': publisher,
                                   'language': language,
                                   'genre': genre,
                                   'short_description': short_description,
                                   'publishing_year': publishing_year,
                                   'no_pages': no_pages,
                                   'no_readers': no_readers,
                                   'rate': rate,
                                   'awards': awards})


def read_add_details():
    book_id = int(input("Add book_id: "))
    title = input("Add title: ")
    author_name = input("Add author name: ")
    publisher = (input("Add publisher: "))
    language = (input("Add language: "))
    genre = (input("Add the genre of the book: "))
    short_description = (input("Add a short description: "))
    publishing_year = int(input("Add the publishing year: "))
    no_pages = int(input("Add the number of pages: "))
    no_readers = int(input("Add the number of readers: "))
    rate = float(input("Add the rate: "))
    awards = int(input("Add the awards number: "))
    recordTuple = (title, author_name, publisher, language, genre, short_description, publishing_year,
                   no_pages, no_readers, rate, awards, book_id)

    return recordTuple


def login(user_name, password):
    response = requests.post(
        url_login,
        data={
            'user_name': user_name,
            'password': password})
    return response.text


def create_account(name, user_name, password):
    response = requests.post(
        url_createAcc,
        data={'name': name,
              'user_name': user_name,
              'password': password})


def read_create_account_details():
    name = input("Name: ")
    user_name = input("User_name: ")
    password = (input("Password: "))
    recordTuple = (name, user_name, password)

    return recordTuple


def operation_type():
    while True:
        print("Choose operation ('Create account' or 'Login'): ")
        line = sys.stdin.readline()
        ok = 5
        if line == "Create account\n":
            recordTuple = read_create_account_details()
            create_account(recordTuple[0], recordTuple[1], recordTuple[2])
            print("User added successfully!\n" + "Do you want you login?")
            yes_no = input("Y/N :  ")
            if yes_no == "Y":
                ok = 0
        if line == "Login\n":
            user_name = input("user_name:  ")
            password = input("password:  ")
            record = json.loads(login(user_name, password))
            print(record)
            if record != "":
                ok = 0
            else:
                ok = 1
        if ok == 0:
            print("Choose operation ('Add book' or 'Delete book'): ")
            line = sys.stdin.readline()
            if line == "Add book\n":
                recordTuple = read_add_details()
                add_book(recordTuple[0], recordTuple[1], recordTuple[2], recordTuple[3], recordTuple[4], recordTuple[5],
                         recordTuple[6], recordTuple[7], recordTuple[8], recordTuple[9], recordTuple[10])
                print("Book added successfully!")
            if line == "Delete book\n":
                book_id = input("Insert the book id for cancellation:  ")
                delete_book(book_id)
                print("Book deleted successfully!")
            if line == "List books\n":
                list = list_books()
                print(list)
        elif ok == 1:
            print("Wrong password or username, please try again ")
        elif ok == 2:
            print("You do not have account, please create account ")


if __name__ == '__main__':
    operation_type()
