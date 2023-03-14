import requests
import re
from anime.models import Anime, Series, Genre
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('syncing anime ...')
        play = Anime_parser()
        play.anime_collection()
        animes = play.anime_collection()

        for anime in animes:
            anime_db = Anime.objects.filter(title = anime['title']).first()

            if not anime_db:
                anime_db = Anime(
                    title = anime['title'],
                    img_url = anime['image'],
                    description = anime['description']
                )
                anime_db.save()
            else:
                anime_db.img_url = anime['image']
                anime_db.description = anime['description']

            seasons = anime['seasons']
            for season_number, series in seasons.items():
                for series_number, series_data in series.items():
                    season_n = int(season_number)
                    series_n = int(series_number)
                    s = Series.objects.filter(
                        season = season_n,
                        series_number = series_n,
                        anime = anime_db
                    ).first()
                    if not s:
                        s = Series(
                            name = series_data['title'],
                            preview = series_data['preview'],
                            season = season_n,
                            series_number = series_n,
                            video_360 = series_data['video_360'],
                            video_480 = series_data['video_480'],
                            video_720 = series_data['video_720'],
                            video_1080 = series_data['video_1080'],
                            anime = anime_db,
                        )
                        s.save()
                    else:
                        s.name = series_data['title']
                        s.preview = series_data['preview']
                        s.video_360 = series_data['video_360']
                        s.video_480 = series_data['video_480']
                        s.video_720 = series_data['video_720']
                        s.video_1080 = series_data['video_1080']
                        s.save()








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
    def anime_collection(self):
        anime = []
        while True:
            url = "https://jut.su/anime/page-" + str(self.page)

            req = requests.get(url, headers= self.headers, timeout=None)
            src = req.text
            soup = BeautifulSoup(src, "lxml")

            all_anime_href  = soup.find_all( class_ = "all_anime_global")

            if not all_anime_href:
                break

            for item in all_anime_href:
                anime.append(self.parse_anime_data(item))


            self.page += 1
        return anime


    def parse_anime_data(self, anime_card):
        anime_data = {}
        a = anime_card.a

        anime_name = a.find('div', class_= 'aaname').text
        anime_href = "https://jut.su" + a.get('href')
        anime_series = a.find('div', class_='aailines').text
        anime_images = a.find('div', class_='all_anime_image').get('style')
        anime_image = re.findall(r"(?<=\(').*?(?='\))",anime_images)[0]
        anime_data['title'] = anime_name
        anime_data['image'] = anime_image

        anime_data  = self.series_collection(anime_href, anime_data)
        return anime_data


    def series_collection(self, url, anime_data):
        req = requests.get(url, headers= self.headers, timeout=None)
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        card = soup.find('div', class_='watch_l')

        anime_data = self.parse_series_data(card, anime_data)
        return anime_data




    def parse_series_data(self, series_card, anime_data):
        seasons = series_card.find_all('div', class_ = 'the_invis')


        descriptions = series_card.find('p', class_='under_video uv_rounded_bottom the_hildi').find('span').text
        type_anime = series_card.find('div', class_='under_video_additional the_hildi').text

        anime_data['description'] = descriptions
        anime_data['seasons'] = {}

        for season in seasons:
            season_text = season.text
            season_url = 'https://jut.su/' + season.next.get('href')

            season_num = re.findall(r'\d+',season_text)[0]
            anime_data['seasons'][season_num]= self.parse_series_url(season_url)

        return anime_data



    def parse_series_url(self, url):
        req = requests.get(url, headers= self.headers, timeout=None)
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        series_nums = soup.find_all('a', class_ = 'short-btn')
        series = {}
        for series_number, item in enumerate(series_nums,1):
            url_series = 'https://jut.su/' + item.get('href')
            series_name = item.text
            series[series_number] = {
                'title' : series_name
            }
            series[series_number].update(self.parse_video_url(url_series))
        return series





    def parse_video_url(self, url):

        req = requests.get(url, headers= self.headers, timeout=None)
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        video = soup.find('video').find_all('source')
        poster = soup.find('video').get('poster')

        video_data = {
            'preview' : poster,
            'video_360' : None,
            'video_480' : None,
            'video_720' : None,
            'video_1080' : None
        }

        for item in video:
            quality = item.get('res')
            href = item.get('src')
            if quality == '360':
                video_data['video_360'] = href
            if quality == '480':
                video_data['video_480'] = href
            if quality == '720':
                video_data['video_720'] = href
            if quality == '1080':
                video_data['video_1080'] = href
        return video_data
