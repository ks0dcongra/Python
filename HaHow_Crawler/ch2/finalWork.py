import requests
import re
from bs4 import BeautifulSoup


def main():
    URL = 'https://www.dcard.tw/f'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    articles = []
    dCard = soup.find_all('article',{'role':'article'})
    for div in dCard:
        title = div.find('h2').text
        lower_divs = div.find_all('div', recursive=False)
        try:
            excerpt = lower_divs[0].text.strip()
            actions = lower_divs[1].text.strip()
            nums = re.findall(r"\d+", actions)
            href = div.h2.a['href']
            articles.append({
                'title': title,
                'excerpt': excerpt,
                # 'bookmark': nums[0],
                # 'response': nums[1],
                'href': href
            })
        except Exception as e:
            return None
    print('共 %d 篇' % (len(articles)))
    for a in articles[:30]:
        print(a)
if __name__ == '__main__':
    main()
