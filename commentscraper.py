import praw
import time
import pandas as pd
import csv


# Used for scraping comments from the ids
reddit = praw.Reddit(
    user_agent="",
    client_id="",
    client_secret="",
    username="",
    password="",
)
subreddits=['']
for i in subreddits:
    df=pd.read_csv(f'{i}.csv')
    for x in range(10010):
        time.sleep(1)
        idredd=df['id'].iloc[x]
        print(x)
        post = reddit.submission(id=idredd)  # if you have the ID
        # Iterate over all of the top-level comments on the post:
        try:
            for comment in post.comments:
                with open(f'{i}comments.csv', 'a', newline='\n') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow([comment.body])
                for reply in comment.replies:
                    with open(f'{i}comments.csv', 'a', newline='\n') as f:
                        thewriter = csv.writer(f)
                        thewriter.writerow([reply.body])
        except:
            print('fail')