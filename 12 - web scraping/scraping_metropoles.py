import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/javascript'
resposta = requests.get(url)
html = BeautifulSoup(resposta.text, 'html.parser')

for perguntar in html.select('.question-summary'):
    titulo = perguntar.select_one('.question-hyperlink')
    data = perguntar.select_one('.relativetime')
    autor = perguntar.select_one('.user-details a')

    print(data.text, titulo.text, autor.text, sep='\t')