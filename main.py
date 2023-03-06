import requests
from bs4 import BeautifulSoup
import os

url = 'YOUR_WEBSITE'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.endswith('.pdf'):
        filename = href.split('/')[-1]
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'wb') as f:
            f.write(requests.get(url + href).content)
            print(f'Téléchargement de {filename} terminé.')
