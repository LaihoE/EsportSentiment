from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import os

# credits to https://www.geeksforgeeks.org/generating-word-cloud-python for most of the function

def wordcloudmaker(thispath,filename):

    df = pd.read_csv(thispath, encoding="UTF-8")
    print(df)

    "CHANGE THIS FOR DIFFERENT SENTIMENT CLOUDS"
    df.drop(df[df.compound > -0.8].index, inplace=True)
    comment_words = ''
    stopwords = set(STOPWORDS)
    # iterate through the csv file
    for val in df.comments:

        # typecaste each val to string
        val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens) + " "

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

directory = 'C:/Users/emill/PycharmProjects/reddit/cleancomments'
# Iterate trough all files in folder
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".csv"):
        thispath=os.path.join(directory, filename)

    wordcloudmaker(thispath,filename)