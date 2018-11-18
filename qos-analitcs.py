from threading import Thread
import subprocess
import sys
import csv
import re
import os

def getPingResults(host, nPackages):
    process = subprocess.Popen(['ping', str(host), '-c', str(nPackages)], stdout=subprocess.PIPE)
    out, err = process.communicate()
    resultsFormated = out.split("--- "+ host +" ping statistics ---")[1]
    lossPercentage = re.findall("(\d)%", resultsFormated)
    rttValues = re.findall(r"(\d+\.\d+)", resultsFormated)
    return rttValues + lossPercentage

def getSpeedTest():
    process = subprocess.Popen(['speedtest-cli.exe', '--simple'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    return re.findall(r"(\d+\.\d+)", out)

def saveCsv(fileNAme):


def __init(args):
    print('Initializing...')
    print ('rtt values: ',getPingResults(args[1], 4))
    print ('speedtest: ',getSpeedTest())

__init(sys.argv)

import csv
import os

os.system('touch results.csv')

with open('results.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['min', 'avg', 'max', 'mdev'])