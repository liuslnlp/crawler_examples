from bs4 import BeautifulSoup

import requests
import lxml


def getLinks(url):
    """
    Receive a URL and return a BeautifulSoup object
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
    try:
        html = requests.get(url, headers=headers)
    except:
        print("Get links error!")
        return
    soup = BeautifulSoup(html.text, "lxml")
    return soup


def crawlCompany(bsObj):
    """
    Crwal companies
    """
    data = bsObj.find_all("ul", {"class": "list-main-icnset"})
    infos = []
    try:
        for one in data[1].find_all("li"):
            name = one.find("p", {"class": "title"}).get_text()

            introduce = one.find("p", {"class": "des"}).get_text()

            date = one.find("i", {"class": "cell date"}).get_text().replace(
                "\n", "").replace("\t", "").replace(" ", "")

            roundOfFin = one.find("i", {"class": "cell round"}).get_text(
            ).replace("\n", "").replace("\t", "").replace(" ", "")

            info = {"name": name, "introduce": introduce,
                    "date": date, "roundOfFin": roundOfFin}

            infos.append(info)
    except:
        print("Crawl company error")
        pass
    return infos


def crawlEvent(bsObj):
    """
    Crawl investment events
    """
    data = bsObj.find_all("ul", {"class": "list-main-eventset"})
    infos = []
    try:
        for one in data[1].find_all("li"):
            name = one.find("p", {"class": "title"}).get_text().replace(
                "\n", "").replace("\t", "").replace(" ", "")
            date = one.find_all("i", {"class": "cell round"})[0].get_text(
            ).replace("\n", "").replace("\t", "").replace(" ", "")
            roundOfFin = one.find_all("i", {"class": "cell round"})[1].get_text(
            ).replace("\n", "").replace("\t", "").replace(" ", "")
            fina = one.find("i", {"class": "cell fina"}).get_text().replace(
                "\n", "").replace("\t", "").replace(" ", "")
            _investorset = one.find("span", {"class": "investorset"}).get_text(
            ).replace("\n", ",").replace("\t", "").replace(" ", "")
            investorset = _investorset[1:]

            info = {"name": name, "date": date, "roundOfFin": roundOfFin,
                    "fina": fina, "investorset": investorset}

            infos.append(info)
    except:
        print("crawl event error")
        pass
    return infos
