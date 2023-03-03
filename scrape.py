import requests
from bs4 import BeautifulSoup




def scrape(url):
    # url = "https://test-paint.surge.sh/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    p_tags = soup.find_all("p")
    text = ""
    for p in p_tags:
        text += str(p)
    return text


if __name__ == '__main__':
    scrape()
