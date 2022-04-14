import os
from tkinter import Y
from py_llu_tu import pyllutu

PATH = os.path.dirname(os.path.abspath(__file__))

ytdl = pyllutu()

ytdl.setSkipDownload(True)
ytdl.setWriteThumbnail(True)
with open(PATH+ '/new.txt',"w") as w:
    with open(PATH + '/url.txt') as f:
        for line in f:
            temp = line.strip().split("\t")
            ytdl.setURL(temp[0])
            ytdl.setName(temp[1])
            ytdl.setPath(PATH+"/downloads/")
            fileName = ytdl.runCommand()
            print(ytdl.buildCommand())
            print("File created: " + fileName) 
            print("-----------------")
            w.write(line.strip()+"\t" + fileName + "\n")
            


       