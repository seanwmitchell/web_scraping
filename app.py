from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():

    BASE_URL = 'https://vnexpress.net/'
    response = requests.get(BASE_URL)

    try:
        BASE_URL = 'https://vnexpress.net/'
        response = requests.get(BASE_URL)
    except Exception as err:
        print(f'ERROR: {err}')

    soup = BeautifulSoup(response.text, features="html.parser")

    articles = soup.find_all('article', class_='list_news')

    titles, images, descriptions = [], [], []
    for i in range(len(articles)):
        try:
            images.append(articles[i].img['src'])
            titles.append(articles[i].a.string.strip())
            descriptions.append(articles[i].p.text.strip())
        except:
            print('pass')

            import json

    final_articles = list(zip(titles, images, descriptions))

    return render_template('index.html', final_articles=final_articles)

if __name__ == '__main__':
    app.run(debug=True)
