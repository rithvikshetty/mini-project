import pandas as pd
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

class report:
    def __init__(self):
        #dir = './static'
        #filelist = glob.glob(os.path.join(dir, ".png"))
        #for f in filelist:
        #    os.remove(f)
        c=1

    def calc_escore(self):
        df=pd.read_csv("./project/reports/report.csv",index_col=None)
        y=df["Result"]
        ecount=0
        ncount=0
        y=y.to_numpy()
        for i in range(len(y)):
            if y[i] ==1:
                ecount=ecount+1
            else:
                ncount=ncount+1
        escore=ecount/(ecount+ncount)*100
        return (escore,y,ecount,ncount)

    def gen_report(self):
        (escore,y,ecount,ncount) = self.calc_escore()
        detail=pd.read_csv("./project/docs/uploaded/details/details.csv",index_col=None)
        sname=detail["Name"]
        smarks=detail["Marks"]
        stime=detail["Time"]
        sname=sname[0]
        smarks=smarks[0]
        stime=stime[0]

        fig = plt.figure(figsize = (20, 4))
        # creating the bar plot
        values=list(range(1,len(y)+1))
        plt.bar(values, y, color ='purple',width = 0.4)
        plt.xlabel("Frames")
        plt.ylabel("Engagement")
        plt.title(sname+"\'s Engagement")
        plt.savefig("./static/EngagementGraph.png",dpi=1000,bbox_inches="tight")
        plt.close()
        return (smarks,stime,sname)
    
    def perc_eng(self):
        (escore,y,ecount,ncount) = self.calc_escore()
        (smarks,stime,sname) = self.gen_report()

        #Visual Data
        labels = 'Engaged','Not Engaged'
        sizes = [ecount,ncount]
        colors = ['yellowgreen', 'red']
        plt.pie(sizes,labels=labels, colors=colors,autopct='%1.1f%%', startangle=140)
        plt.legend(labels, loc="best")
        plt.axis('equal')
        plt.title(sname+"\'s Engagement Score")
        plt.savefig("./static/EngagementScore.png",dpi=1000,bbox_inches="tight")
        plt.close()
        #Quiz Score
        labels = 'Correct','Wrong'
        sizes = [smarks,10-smarks]
        colors = ['skyblue', 'red']
        plt.pie(sizes,labels=labels, colors=colors,autopct='%1.1f%%', startangle=90)
        plt.legend(labels, loc="best")
        plt.axis('equal')
        plt.title(sname+"\'s Quiz Score")
        plt.savefig("./static/QuizScore.png",dpi=1000,bbox_inches="tight")
        plt.close()
        #Overall Score
        rscore=0
        qscore=smarks/10*100
        if(stime==0):
            rscore=escore*0.6+qscore*0.4
        elif(stime==1):
            rscore=escore*0.7+qscore*0.3
        elif(stime==2):
            rscore=escore*0.75+qscore*0.25
        # Data to plot
        labels = 'Engaged','Not Engaged'
        sizes = [rscore,100-rscore]
        colors = ['magenta', 'purple']
        plt.pie(sizes,labels=labels, colors=colors,autopct='%1.1f%%', startangle=90)
        plt.legend(labels, loc="best")
        plt.axis('equal')
        plt.title(sname+"\'s Overall Engagement")
        plt.savefig("./static/OverallScore.png",dpi=1000,bbox_inches="tight")
        plt.close()
        return