import requests
from bs4 import BeautifulSoup


def main():
    try:
        resp = requests.get('https://im.mgt.ncu.edu.tw/')
    except:
        resp = None
    if resp and resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        try:
            h2 = soup.find('h2')
        except:
            h2 = None
        try:
            h1 = soup.find('h2')
        except:
            h1 = None
        if h2:
            print(h2.text)
        if h1:
            print(h1.text)
if __name__ == '__main__':
    main()
