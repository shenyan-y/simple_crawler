# crawler.py
import requests
from bs4 import BeautifulSoup


def crawl(url):
    """
    爬取指定URL的网页内容，并解析返回BeautifulSoup对象。

    参数:
        url (str): 要爬取的网页地址

    返回:
        soup (BeautifulSoup对象): 解析后的网页内容；如果请求失败则返回None
    """
    # 设置HTTP请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 发起GET请求
        response = requests.get(url, headers=headers, timeout=10)
        # 如果响应状态码为200，则表示请求成功
        if response.status_code == 200:
            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            print(f"爬取失败，状态码: {response.status_code}")
            return None
    except requests.RequestException as e:
        print("请求异常:", e)
        return None


def main():
    # 待爬取的网页地址，此处以示例网站为例
    url = "https://www.example.com"
    print(f"开始爬取: {url}")

    # 调用爬虫函数获取网页解析对象
    soup = crawl(url)

    if soup:
        # 提取网页标题
        title_tag = soup.find("title")
        if title_tag:
            print("网页标题:", title_tag.get_text().strip())
        else:
            print("未找到网页标题")
    else:
        print("爬虫未能成功获取网页内容")


if __name__ == "__main__":
    main()
