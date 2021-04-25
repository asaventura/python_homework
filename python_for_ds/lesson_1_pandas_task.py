import pandas as pd
import numpy as np


authors_dict = {'author_id': [1, 2, 3],
                'author_name': ['Тургенев', 'Чехов', 'Островский']}
books_dict = {'author_id': [1, 1, 1, 2, 2, 3, 3],
              'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий',
                             'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
              'price': [450, 300, 350, 500, 450, 370, 290]}
authors = pd.DataFrame(authors_dict)
books = pd.DataFrame(books_dict)
authors_price = pd.merge(authors, books, on='author_id', how='outer')
authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
authors_stat = authors_price.groupby('author_name').agg({'price': [('min_price', 'min'),
                                                                   ('max_price', 'max'),
                                                                   ('mean_price', 'mean')]})
book_info = pd.pivot_table(data=authors_price, values='price', index='author_name',
                           columns='cover', aggfunc=np.sum, fill_value=0)
print(authors)
print(books)
print(authors_price)
print(authors_price.nlargest(5, 'price'))
print(authors_stat)
print(book_info)
