#pip3 install wget
#pip3 install pandas
import wget
import pandas as pd
import os

PATH_OF_CSVS_FOLDER = '/home/hackavist/Desktop/Source/'
PATH_OF_SAVE_IMAGES_DOWNLOADED = '/home/hackavist/Desktop/Result/'

#The Folder that contains All the CSVs
files = os.listdir(PATH_OF_CSVS_FOLDER)
#print(files)
#Selecting all the Files
for i in files:
    data = pd.read_csv(PATH_OF_CSVS_FOLDER+'{}'.format(i))
    #Skip the second Line 
    for x in range (1,len(data)):
        try:

            url = data.iloc[x,9]
            #Save the Downloaded Images to Specific Folder with Their Names
            wget.download(url, PATH_OF_SAVE_IMAGES_DOWNLOADED+'{}.jpg'.format(data.iloc[x,0]))

        except:

            #this will Display the names with no Photos 
            print("Photo with name {} not found".format(data.iloc[x,9]))
