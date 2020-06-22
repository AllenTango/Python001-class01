import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://m.maoyan.com/films?showType=3#movie/classic"

headers = {
    "Cookie": "uuid_n_v=v1; iuuid=3D5B1F90B48A11EAB726418169972B1D660DA419116B40DA8241C22175BD138A; webp=true; ci=20%2C%E5%B9%BF%E5%B7%9E; _last_page=c_dmLad; selectci=; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172dd6cfe0b800-014f93f432f6b-621e1d31-230400-172dd6cfe0c85e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172dd6cfe0b800-014f93f432f6b-621e1d31-230400-172dd6cfe0c85e%22%7D; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592831543; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592852808; _lxsdk_cuid=172dc2886dbc8-0efd0bd91ea5c9-30667700-384000-172dc2886dbc8; _lxsdk=3D5B1F90B48A11EAB726418169972B1D660DA419116B40DA8241C22175BD138A; __mta=46921240.1592831543617.1592852808500.1592852808519.5; _lxsdk_s=172dd6cf547-229-788-1f2%7C%7C4",
    "Host": "m.maoyan.com",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Mobile Safari/537.36"
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
movie_list = soup.find_all("div", attrs={"class": "movie-info"})
movie_data = []

for movie in movie_list:
    title = movie.select('div.title')[0].get_text()
    actors = movie.select('div.actors')[0].get_text()
    show_time = movie.select('div.show-info')[0].get_text()
    movie_data.append((title, actors,show_time))

movies = pd.DataFrame(data=movie_data)
movies.to_csv('./week01/maoyan_movies1.csv', encoding='utf-8', index=False, header=False)