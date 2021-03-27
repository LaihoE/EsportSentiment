import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def plotter(thispath,filename):
    df=pd.read_csv(thispath,encoding="UTF-8")
    # Drop rows with 0 compound score
    df.drop(df[df.compound == 0].index, inplace=True)
    filename=filename.replace('comments.csv','')
    filename=filename.replace('clean','')
    sns.histplot(df['compound']).set_title(filename)
    plt.ylabel('number of comments')
    plt.xlabel('compounded VADER score')
    plt.show()

directory = 'C:/Users/emill/PycharmProjects/reddit/cleancomments'
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".csv"):
        thispath=os.path.join(directory, filename)
    plotter(thispath,filename)