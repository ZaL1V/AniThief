import requests
import re
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('syncing anime ...')
        play = Anime_parser()
        play.anime_colection()


from bs4 import BeautifulSoup
import requests
import re


class Anime_parser:
    def __init__(self):
        self.page = 1
        self.headers = {
                "Accept":
                "/",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0"
            }



     #reads all anime
    def anime_colection(self):

        while True:
            url = "https://jut.su/anime/page-" + str(self.page)

            req = requests.get(url, headers= self.headers, timeout=None)
            src = req.text
            soup = BeautifulSoup(src, "lxml")

            all_anime_href  = soup.find_all( class_ = "all_anime_global")

            if not all_anime_href:
                break

            for item in all_anime_href:
                self.parse_anime_data(item)


            self.page += 1


    def parse_anime_data(self, anime_card):

        a = anime_card.a

        anime_name = a.find('div', class_= 'aaname').text
        anime_href = "https://jut.su" + a.get('href')
        anime_series = a.find('div', class_='aailines').text
        anime_images = a.find('div', class_='all_anime_image').get('style')
        anime_image = re.findall(r"(?<=\(').*?(?='\))",anime_images)[0]
        # print(anime_image)
        self.series_colection(anime_href)


    def series_colection(self, url):
        req = requests.get(url, headers= self.headers, timeout=None)
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        card = soup.find('div', class_='watch_l')

        self.parse_series_data(card)



    def parse_series_data(self, series_card):
        btn = series_card.find_all('a', class_='short-btn')

        descriptions = series_card.find('p', class_='under_video uv_rounded_bottom the_hildi').find('span').text

        print(descriptions)
        for series in btn:
            num = series.text
