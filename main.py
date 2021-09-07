from bs4 import BeautifulSoup
import requests


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com'


def find_keywords(text, keywords):
    for keyword in keywords:
        if keyword in text:
            # < дата > - < заголовок > - < ссылка >
            date = post.find('time').attrs.get('title').split(',')[0]
            title = post.find('a', class_='tm-article-snippet__title-link')
            href = URL + title.attrs.get('href')

            return f'{date} - {title.text} - {href}'
    return ''


if __name__ == '__main__':
    response = requests.get('https://habr.com/ru/all/')
    soup = BeautifulSoup(response.text, features='html.parser')
    posts = soup.find_all(class_='tm-article-snippet')
    print(len(posts))
    for post in posts:
        text = post.find(class_='article-formatted-body').text
        info = find_keywords(text, KEYWORDS)

        if info:
            print('Предпросмотр ' + info)
            continue
        else:
            '''
            Выполнение дополнительного задания 
            '''
            href = URL + post.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
            inner_response = requests.get(href)
            inner_soup = BeautifulSoup(inner_response.text, features='html.parser')
            text = inner_soup.find(class_='tm-article-body').text

            info = find_keywords(text, KEYWORDS)
            if info:
                print('Полная статья ' + info)
