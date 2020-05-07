# Mitru Adina
# 343C1
import json
import sys

import requests

url = 'http://server:5000/book'
url_books = 'http://server:5000/books'
url_read = 'http://server:5000/read'
url_category = 'http://server:5000/user'
url_start = 'http://server:5000/start'


def list_books():
    response = requests.get(
        url)
    return response.text


def get_book(category, category_type):
    response = requests.post(
        url_books,
        data={
            'category': category,
            'category_type': category_type})

    return response.text


def read_book(read_book_name, liked):
    response = requests.post(
        url_read,
        data={
            'read_book_name': read_book_name,
            'liked': liked})


def list_category(category):
    response = requests.post(
        url_category,
        data={
            'category': category})
    return response.text


def start_book(stat_book_name):
    response = requests.post(
        url_start,
        data={
            'stat_book_name': stat_book_name})
    return response.text


def operation_type():
    while True:
        print("Choose operation ('Recommend a book = 1', 'Mark a book as read = 2', 'Start a new book = 3', "
              "'Continue reading = 4', 'List books = 5', 'List category ""= 6'): ")
        line = sys.stdin.readline()
        if line == "1\n":
            category = input("Please provide the category:  ")
            category_type = input("Please provide the  " + category + " you would like: ")
            recommendations = json.loads(get_book(category, category_type))
            print("The recommendations: ", recommendations)
        if line == "2\n":
            read_book_name = input("Please provide the name of the book:  ")
            liked = input("Please say if you like or dislike: ")
            read_book(read_book_name, liked)
            print("The book " + liked + " has been marked as read and " + liked)
        if line == "3\n":
            stat_book_name = input("Please provide the name of the book:  ")
            suggestion = start_book(stat_book_name)
            print("The book has been added to started list and you might also like: " + suggestion)
        if line == "4\n":
            list = json.loads(list_category("started"))
            print(list)
            read_book_name = input("Which one would you like to continue reading: ")
        if line == "5\n":
            list = json.loads(list_books())
            print(list)
        if line == "6\n":
            category = input("Please provide the category: ")
            list = json.loads(list_category(category))
            print(list)


if __name__ == '__main__':
    operation_type()
