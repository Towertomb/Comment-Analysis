import pandas as pd
from snownlp import SnowNLP
import urllib.request
import json
from urllib.error import HTTPError

LANGUAGES = {
    '简体中文': 'cn',
    '繁体中文': 'tw',
    '英语': 'us',
    '日语': 'jp',
    '法语': 'fr',
    '德语': 'de',
    '西班牙语': 'es',
    '葡萄牙语': 'pt',
    '韩语': 'kr',
    '阿拉伯语': 'sa'
}

def get_reviews(appid, page, country):
    url = "https://itunes.apple.com/{}/rss/customerreviews/page={}/id={}/sortby=mostrecent/json".format(country, page, appid)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    if "entry" in data["feed"]:
        return data["feed"]["entry"]
    else:
        return []
    
def sentiment_analysis(rating):
    if rating > 3:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"
    
def fetch_reviews_all(appid, language, page_mode=False, start_page=1, end_page=10):
    page = 1
    result = []
    reviews = get_reviews(appid, page, language)

    def page_fetch(appid, page, language):
        print(f"fetching page {page}, appid: {appid}, language: {language}...")
        try:
            reviews = get_reviews(appid, page, language)
        except HTTPError as e:
                if e.code == 400:
                    return result, [], page
                else:
                    raise
        reviews = get_reviews(appid, page, language)
        page += 1
        for review in reviews:
            if isinstance(review, dict):
                date = review["updated"]["label"]
                content = review['content']['label']
                rating = review['im:rating']['label']
                version = review['im:version']['label']
                author = review['author']['name']['label']
                sentiment = sentiment_analysis(rating)
                result.append({
                    'updated': date,
                    'content': content,
                    'rating': rating,
                    'version': version,
                    'author': author,
                    'sentiment': sentiment
                })
        return result, reviews, page
    
    if page_mode == False:
        while reviews != []:
            result, reviews, page = page_fetch(appid, page, language)
    else:
        for page in range(start_page, end_page + 1):
            result, reviews, page = page_fetch(appid, page, language)
    
    # 将评论数据保存为Excel文件
    df = pd.DataFrame(result)
    df.to_csv(f'{appid}_{language}.csv')

if __name__ == '__main__':
    fetch_reviews_all(1484302191, 'us')
    fetch_reviews_all(1536111825, 'us') #Giant RideControl
    fetch_reviews_all(1609966547, 'us') #Trek Central
    fetch_reviews_all(1437969979, 'us') #Shimano E-TUBE
    fetch_reviews_all(1094591345, 'us', page_mode=True, start_page=1, end_page=20) #Pokemon Go