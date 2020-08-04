import json
import requests
from bs4 import BeautifulSoup
import pymysql

url = "https://movie.douban.com/subject/26794435/comments?start=20&limit=20&sort=new_score&status=P"
headers = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'Cookie': '_pk_id.100001.4cf6=95a6a4811cef5fa3.1596286133.1.1596286133.1596286133.;__utmb=223695111.0.10.1596286133;__utmb=30149280.0.10.1596286133;__utmz=30149280.1596286133.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);__utmc=	30149280;__utmz=223695111.1596286133.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);__utma=30149280.1712636964.1596286133.1596286133.1596286133.1;ap_v=0,6.0;__utmc=223695111;__utma=223695111.1549464510.1596286133.1596286133.1596286133.1;bid=78RQLqq1pgg;'
}

web_page = requests.get(url, headers=headers)
soup = BeautifulSoup(web_page.text, 'lxml')

short_contents = soup.select('#comments > div > div.comment > p > span.short')
short_stars = soup.select(
    '#comments > div > div.comment > h3 > span.comment-info > span.rating')  # .allstar10
short_dates = soup.select(
    '#comments > div > div.comment > h3 > span.comment-info > span.comment-time')
movie_type = soup.select_one(
    '#content > div > div.aside > div.indent > div > span > p:nth-child(3)').get_text().split('\n')[2].strip()
movie_name = soup.select_one('#content > h1').get_text().split(' ')[0]
movie_date = soup.select_one(
    '#content > div > div.aside > div.indent > div > span > p:nth-child(6)').get_text().split(', ')[1].split('(')[0]

short_db = {'movie_name': movie_name, 'movie_date': movie_date, 'movie_type': movie_type, 'movie_shorts': [{'short_content': c.string.replace(
    '\n', ''), 'short_star': s['class'][0].split('r')[-1], 'short_title': s['title'], 'short_date': d.string.strip()} for c, s, d in zip(short_contents, short_stars, short_dates)]}


class MagicMySQL:
    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            db='douban',
            user='root',
            password='Tango0079410',
            charset='utf8mb4'
        )
        self.cursor = self.connect.cursor()

    # CREATE TABLE shorts(movie_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #                     name char(20),
    #                     type char(20),
    #                     show_time char(20),
    #                     commits JSON);
    # /usr/local/mysql/bin/mysqldump -u root -h 127.0.0.1 -p douban shorts > shorts.sql
    def process_item(self, item):
        try:
            self.cursor.execute("INSERT INTO shorts(name, type, show_time, commits) VALUES (%s, %s, %s, %s)", (
                item['movie_name'], item['movie_type'], item['movie_date'], json.dumps(item['movie_shorts'])))
            self.connect.commit()
        except Exception as e:
            print(e)

    def close_spider(self):
        self.cursor.close()
        self.connect.close()

if __name__ == "__main__":
    print(short_db)
    my_sql = MagicMySQL()
    my_sql.process_item(short_db)
    my_sql.close_spider()