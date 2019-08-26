#concerned eith storing into a a csv file


def add_book(name, author):
    with open('books.txt', 'a') as file:
        file.write(f'{name}, {author}, 0\n')

def list_book():
    with open('books.txt', 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        return [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
        ]

def mark_book(name):
    # with open('books.txt', 'r') as file
    #     lines = [line.strip().split(',') for line in file.readlines()]
    #     books = [
    #         {'name': line[0], 'author': line[1], 'read': line[2]}
    #         for line in lines
    #     ]
    books = list_book()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'

    with open('book.txt', 'w') as file:
        for book in books:
            file.write(f"{book['name']}, {book['author']}, {book['read']}\n")



# def del_book(name):
#     for book in books:
#        if book['name'] == name:
#            books.remove(book)

def del_book(name):
    books = list_book()
    new_book = []
    for book in books:
        if book['name'] != name:
            new_book.append(book)
    with open('book.txt', 'w') as file:
        for book in new_book:
            for book in new_book:
                file.write(f"{book['name']}, {book['author']}, {book['read']}\n")








