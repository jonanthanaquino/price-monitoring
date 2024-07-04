#carregamento das bibliotecas e obtenção da pag html
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from requests.exceptions import MissingSchema, RequestException
import pandas as pd

# url = 'https://www.sefaz.mt.gov.br/nfce/consultanfce?p=51230809477652008502651080000343851912768157|2|1|1|BE090D965611C41F345B1B6CF45050D1DB7EF805'
url ='https://www.sefaz.mt.gov.br/nfce/consultanfce?p=51240117226232002702650060000800991660419100|2|1|1|C22AE3E7BAFC889737E51EA38167C4067DD01BC4'
print(url)


def carregamento_inicial(url):

  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

  try:
    requisicao = requests.get(url, headers= headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    return site

  except MissingSchema as e:
    return "Nan"

  except requests.RequestException as e:
    return "Nan"

