import requests
import csv
import time

# Used for scraping post ID's
N = 0
last = ''
ids = []
subreddit=''
url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&fields=id,created_utc'

while N < 10000000:
    print(N)
    time.sleep(1)
    try:
        request = requests.get('{}&before={}'.format(url,last))
        json = request.json()
        for s in json['data']:
            with open('RocketLeague.csv', 'a', newline='\n') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([s['id']])
            N += 1
        last = int(s['created_utc'])
    except:
        print('fail')

