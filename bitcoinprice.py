import urllib.request
from bs4 import BeautifulSoup as Bs

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Windows i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

pedido = urllib.request.Request('http://markets.businessinsider.com/currencies/btc-usd', headers=headers)
resposta = urllib.request.urlopen(pedido)
conteudo = resposta.read().decode(errors='ignore')

conteudo = Bs(conteudo, 'lxml')
conteudo = conteudo.find('span', {'class': 'push-data '}).contents[0]
print('O PREÇO DO BITCOIN É DE ${}'.format(conteudo))
conteudo = conteudo.replace(',', '')
conteudo = float(conteudo)
bitcoins = float(input('Quantas bitcoins você tem? '))
print('Você tem ${}'.format(conteudo * bitcoins))
