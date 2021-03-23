import requests
import re
from bs4 import BeautifulSoup


def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    divs = soup.find_all('div', 'card-image')
    count = 0
    for div in divs:
        count =count+1
    print(count)

    countCrawler = 0

    haveCrawler = soup.find_all('img')
    for apple in haveCrawler:
            if 'src' in apple.attrs:
                if 'crawler' in apple['src']:
                    countCrawler += 1
    print(countCrawler)

    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/table/table.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    count = 0
    rows = soup.find('table', 'table').tbody.find_all('tr')
    for row in rows:
        all_tds = row.find_all('td.a')  # 方法一: find_all('td)
        # all_tds = [td for td in row.children]  # 方法二: 找出 row (tr) 所有的直接 (下一層) children
        # 以下執行時會報錯, 因為最後一列的 <a> 沒有 'href' 屬性
        # print(all_tds[0].text, all_tds[1].text, all_tds[2].text, all_tds[3].a['href'], all_tds[3].a.img['src'])
        # 取得 href 屬性前先檢查其是否存在
        count +=1
    print(count)
if __name__ == '__main__':
    main()
