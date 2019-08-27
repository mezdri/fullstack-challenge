from django.shortcuts import render_to_response
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Books, Categories
from .serializer import BookSerializer

from bs4 import BeautifulSoup as bs
import requests


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class ScraperView(viewsets.ModelViewSet):
    books_queryset = Books.objects.all()
    categories_queryset = Categories.objects.all()
    serializer_class = BookSerializer

    def post(self, request):

        self.scrap_book('http://books.toscrape.com/catalogue/page-1.html')
        return Response({"Ingresamos"}, status=200)

    def scrap_book(self, url):
        """Metodo para realizar el scrappr a una url en especifica
        :param url: Url de la pagina.
        :type url: String
        """
        html = requests.get(url).text
        soup = bs(html, 'lxml')

        categories_raw = soup.find('div', {'class': 'side_categories'}).get_text()
        categories = categories_raw.split()

        self.save_categories(categories)

        # print(categories)

        pageNumbers = soup.find_all('ul', {"class": "pager"})[0].find_all('li', {'class': 'current'})[0].get_text()
        lastPages = [int(val) for val in pageNumbers.split() if self.is_number(val.replace(',', ''))]
        dic = {}
        lista = []

        for pageNumber in range(1):  # max(lastPages)):

            aux_index = url.find('-')
            new_url = url[:aux_index + 1] + str(pageNumber + 1) + ".html"

            page_html = requests.get(new_url).text.encode('utf-8').decode('iso-8859-1')
            page_soup = bs(page_html, 'lxml')
            books = soup.find('ol', {'class': 'row'}).find_all('li')
            for book in books:
                book_url = book.find('div', {'class': 'image_container'}).find_all('a')[0]['href']
                book_html = requests.get('http://books.toscrape.com/catalogue/' + book_url).text
                book_soup = bs(book_html, 'lxml')

                dic['Category'] = book_soup.find('ul', {'class': 'breadcrumb'}).find_all('li')[2].get_text().replace(
                    '\n', '')
                dic['Title'] = book_soup.find('ul', {'class': 'breadcrumb'}).find_all('li')[3].get_text()
                dic['Thumbnail'] = book_soup.find('div', {'class': 'item active'}).find('img')['src'].replace('../../',
                                                                                                              'http://books.toscrape.com/')
                dic['Price'] = float(book_soup.find('p', {'class': 'price_color'}).get_text()[2:])
                dic['Stock'] = \
                book_soup.find('p', {'class': 'instock availability'}).get_text().replace('(', '').split()[2]
                dic['Product_Description'] = book_soup.find('p', {'class': False})
                dic['UPC'] = book_soup.find('table', {'class': 'table table-striped'}).find_all('tr')[
                    0].get_text().replace('\n', '').strip()

                lista.append(dic.copy())
                dic = {}
        self.save_books(lista)

        return Response({'status': True, 'msg': 'Books are update'})

    def save_books(self, books):
        data = []
        for book in books:
            if not self.books_queryset.filter(title=book['Title']).first():
                category = self.categories_queryset.filter(name=book['Category']).first()
                if category:
                    print(category.id)
                    data.append(self.books_queryset.create(
                        category_id=category,
                        title=str(book['Title']),
                        thumbnail_url=str(book['Thumbnail']),
                        price=str(book['Price']),
                        stock=True if int(book['Stock']) else False,
                        product_description=str(book['Product_Description']),
                        upc=str(book['UPC'])
                    ))
        if data:
            for record in data:
                record.save()
        return True

    def save_categories(self, categories):
        data = []
        for category in categories:
            print(category)
            print(self.categories_queryset.filter(name=category).first())
            if not self.categories_queryset.filter(name=category).first():
                # data.append({'name': category})
                data.append(self.categories_queryset.create(name=category))
        if data:
            for record in data:
                record.save()
        return True

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
