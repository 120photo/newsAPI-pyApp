from secrets import *
import requests
import json

source = 'https://newsapi.org/v1/articles?source=the-new-york-times&apiKey=' + NEWS_API_KEY
data = requests.get(source)
doc = json.loads(data.content)

for i in doc['articles']:
    print('|--> ' + i['title'])
