import pandas as pd


authors_dict = {'author_id': [1, 2, 3], 'author_name': ['Тургенев', 'Чехов', 'Островский']}
books_dict = {'author_id': [1, 1, 1, 2, 2, 3, 3],
              'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий',
                             'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
              'price': [450, 300, 350, 500, 450, 370, 290]}
authors = pd.DataFrame(authors_dict)
books = pd.DataFrame(books_dict)
authors_price = pd.merge(authors, books, on='author_id', how='outer')
print(authors)
print(books)
print(authors_price)
