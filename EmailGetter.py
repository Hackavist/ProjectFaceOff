import wget
import pandas as pd
import os

PATH_OF_CSVS_FOLDER = '/home/hackavist/Desktop/m/'
files = os.listdir(PATH_OF_CSVS_FOLDER)

for i in files:
    data = pd.read_csv(PATH_OF_CSVS_FOLDER+'{}'.format(i))
    File_object = open("Emails","a+")

    #Skip the second Line 
    for x in range (1,len(data)):
         email = data.iloc[x,3]
         File_object.write(email + "\n")
File_object.close()