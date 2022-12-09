from Comment import Comment
from Driver import Driver
import threading
import csv
with open("src\\supply\\Targets.txt", "r") as f:
    targets = f.readlines()

for i in range(len(targets)):
    #Create a driver object
    d = Driver()
    driver = d.CreatDriver()
    #Multithreading bots
    bot = Comment()
    t = threading.Thread(target= bot.lauch, args=(driver,targets[i]))
    t.start()

    







