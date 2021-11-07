import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
from plotly.offline.offline import plot

data=pd.read_csv('medium_data.csv')
listeddata=data['reading_time'].tolist()
populationmean=statistics.mean(listeddata)


def randomset(counter):
    Dataset=[]
    for i in range(0,counter):
        index=random.randint(0,len(listeddata)-1)
        value=listeddata[index]
        Dataset.append(value)
    mean=statistics.mean(Dataset)
    return mean     
    
def plot_fig(meanlist):
    df=meanlist
    mean=statistics.mean(meanlist)
    print('Mean of sampling distribution is:',mean)

    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name='MEAN'))
    fig.show()
    
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmean=randomset(100)
        meanlist.append(setofmean)
    plot_fig(meanlist)

print('The population mean is :',populationmean)
  
setup()  



