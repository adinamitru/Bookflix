CREATE DATABASE bookflix;
use bookflix;


CREATE TABLE book (
    book_id int NOT NULL AUTO_INCREMENT,
    title VARCHAR(100),
    author_name VARCHAR(20),
    publisher VARCHAR(20),
    language VARCHAR(20),
    genre VARCHAR(20),
    short_description TEXT,
    publishing_year INT(5),
    no_pages INT(5),  
    no_readers INT(7),
    rate INT(2),	
    awards INT(2) default 0,
    PRIMARY KEY (book_id)
);

CREATE TABLE user_client (
    book_id INT(6),
    list_id INT(6)
);

CREATE TABLE user_info (
    user_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(20),
    user_name VARCHAR(20),
    password VARCHAR(20),
    PRIMARY KEY (user_id)
);



CREATE TABLE book_user (
    user_id INT UNSIGNED NOT NULL,
    book_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (user_id, book_id),
    --CONSTRAINT `Constr_book_user_user_id_fk`
        FOREIGN KEY (user_id) REFERENCES user_info(user_id)
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (book_id) REFERENCES book(book_id)
             ON DELETE CASCADE ON UPDATE CASCADE
)

INSERT INTO book (title, author_name, publisher, language, genre, short_description, publishing_year, no_pages, no_readers, rate, awards)
VALUES ('The Fellowship of the Ring', 'J. R. R. Tolkien', 'Allen & Unwin', 'English', 'fantasy', 'The title of the novel refers to the storys main antagonist, the Dark Lord Sauron,[a] who had in an earlier age created the One Ring to rule the other Rings of Power as the ultimate weapon in his campaign to conquer and rule all of Middle-earth', 1954, 427, 552, 9.2, 5);

INSERT INTO book (title, author_name, publisher, language, genre, short_description, publishing_year, no_pages, no_readers, rate, awards)
VALUES ('c', 'Irving Stone', 'Allen & Unwin', 'English', 'biographical novel', 'It is Stones first major publication and is largely based on the collection of letters between Vincent van Gogh and his younger brother, art dealer Theo van Gogh. They lay the foundation for most of what is known about the thoughts and beliefs of the artist.', 1934, 576, 241, 8.7, 1);

INSERT INTO book (title, author_name, publisher, language, genre, short_description, publishing_year, no_pages, no_readers, rate, awards)
VALUES ('Harry Potter and the Goblet of Fire', 'J. K. Rowling', 'Scholastic', 'English', 'fantasy', 'It follows Harry Potter, a wizard in his fourth year at Hogwarts School of Witchcraft and Wizardry, and the mystery surrounding the entry of Harrys name into the Triwizard Tournament, in which he is forced to compete.', 2000, 636, 562, 8.9, 2);

INSERT INTO user_info VALUES ('Ana Popescu', 'ana', 'pass');

