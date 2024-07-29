from bs4 import BeautifulSoup
import requests
import html2text as ht
import re


def getUrl():
    url = input("请输入URL：")
    html = requests.get(url)
    html.encoding = "utf-8"
    print(html)
    # get_md(html)
    get_image(html)

def get_image(html):
    # count = 0
    # soup = BeautifulSoup(html.text, "html.parser")
    # images = soup.find_all(name="img", attrs={"loading": "lazy"})
    # length = len(images)
    # for image in images:
    #     # print(image.attrs['src'])
    #     url = f"https://www.threeyear.com.cn{image.attrs['src']}"
    #     filename = str(image.attrs['src']).split("/")[2]
    #     bImage = requests.get(url).content
    #     with open(f"./upload/{filename}", "wb") as fb:
    #         fb.write(bImage)
    #         count += 1
    #         print(f"{count}/{length}下载成功")
    count = 0
    soup = BeautifulSoup(html.text, "html.parser")
    figure = soup.find_all(name="figure", attrs={"class": "wp-block-image"})
    length = len(figure)
    for f in figure:
        url = str(f).split("src=")[1].split("\"")[1]
        filename = url.split("/")[7]
        bImage = requests.get(url).content
        with open(f"./{filename}", "wb") as fb:
            fb.write(bImage)
            count += 1
            print(f"{count}/{length}下载成功")


if __name__ == "__main__":
    getUrl()