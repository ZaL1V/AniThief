import requests, json
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('syncing anime ...')
        play = Anime_parser()
        play.anime_colection()


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
        anime_url = {}

        while True:
            url = "https://jut.su/anime/page-" + str(self.page)

            req = requests.get(url, headers= self.headers)
            src = req.text
            soup = BeautifulSoup(src, "lxml")
            all_anime  = soup.find_all(class_ = "the_invis")


            if len(all_anime):
                for item in all_anime:
                    item_a = item.next
                    item_name = (''.join(item_a.text.split('смотреть')[-1:])).strip()
                    item_href = "https://jut.su" + item_a.get("href")
                    anime_url[item_name] = item_href
                    print(f"{item_name} : {item_href}")

                self.page += 1
            else:
                with open("anime_url.json", "w", encoding='utf-8') as file:
                    json.dump(anime_url, file, indent=4, ensure_ascii=False)
                break


    #reads all series
    def anime_series(self, url):
        req = requests.get(url, headers= self.headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        series  = soup.find_all("a", class_="short-btn")
        anime_series = {}
        # print(series)

        for item in series:
            item_name = item.text
            item_href = "https://jut.su" + item.get("href")
            anime_series[item_name] = item_href
            print(f"{item_name} : {item_href}")
            with open("anime_series.json", "w", encoding='utf-8') as file:
                json.dump(anime_series, file, indent=4, ensure_ascii=False)


    #reads all video
    def anime_video(self, url):
        req = requests.get(url, headers= self.headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        video  = soup.find("video").find_all('source')

        for item in video:
            item_quality = item.get('res')
            item_video = item.get('src')
            print(f"{item_quality} : {item_video}")
