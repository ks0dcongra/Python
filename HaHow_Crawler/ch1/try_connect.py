import requests
from bs4 import BeautifulSoup


def main():
    # h1 = get_head_text('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html', 'h1','')
    # print(h1)
    # h2 = get_head_text('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html', 'h2','')
    # print(h2)
    web = get_head_text('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html','title','p')
    print(web)
def get_head_text(url, head_tag,para):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            a = soup.find(head_tag).text
            b = soup.find(para).text
            c = a + '\n'+b
            return c

    except Exception as e:
        return None


if __name__ == '__main__':
    main()