# Mitru Adina
# 343C1
import sys

import requests

url = 'http://server:5000/book'


def delete_book(book_id):
    response = requests.delete(
        url,
        data={'book_id': book_id})


def list_books():
    response = requests.post(
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


def operation_type():
    while True:
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


if __name__ == '__main__':
    operation_type()
