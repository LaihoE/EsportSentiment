import pandas as pd
import numpy as np
import os
import csv
import plotly.express as px
# Main comparison of subreddits

gamelist = []
def toxic(thispath,filename):
    df=pd.read_csv(thispath,encoding='UTF-8')
    # Drop rows with compound score 0
    #df.drop(df[df.compound == 0].index, inplace=True)
    thismean=np.average(df['compound'])
    filename = filename.replace('comments.csv', '')
    filename = filename.replace('clean', '')
    with open('graphdata.csv','a',newline='\n')as f:
        thewriter = csv.writer(f)
        thewriter.writerow([filename,thismean])


directory = 'C:/Users/emill/PycharmProjects/reddit/cleancomments'
# Iterate trough all files in folder
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        thispath=os.path.join(directory, filename)
    toxic(thispath,filename)

df=pd.read_csv('graphdata.csv')
df=df.sort_values(by=['vader_score'])
fig = px.histogram(df,x='game',y='vader_score',title='Sentiment scores of Esport subreddits (VADER)',histfunc='avg')
fig.show()