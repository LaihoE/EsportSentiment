#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import re
import os

# Vader sentiment score

sid = SentimentIntensityAnalyzer()
def vader(game,filename):
    df=pd.read_csv(game,encoding="UTF-8",error_bad_lines=False)
    # Make all comments lower case
    df['comments'] = df['comments'].str.lower()
    # Remove comments with '/s', indicating that the person is sarcastic
    df=df[df.comments.str.contains("/s") == False]
    # Remove links
    df['comments'] = df['comments'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
    # Drop empty rows
    df = df.dropna()

    # VADER
    df['compound'] = [sid.polarity_scores(v)['compound'] for v in df['comments']]
    df['neg'] = [sid.polarity_scores(v)['neg'] for v in df['comments']]
    df['neu'] = [sid.polarity_scores(v)['neu'] for v in df['comments']]
    df['pos'] = [sid.polarity_scores(v)['pos'] for v in df['comments']]

    df.to_csv(f'C:/Users/emill/PycharmProjects/reddit/cleancomments/clean{filename}',encoding="UTF-8")


directory = 'C:/Users/emill/PycharmProjects/reddit/rawcomments'
# Iterate trough all files in folder
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".csv"):
        thispath=os.path.join(directory, filename)
    vader(thispath,filename)
