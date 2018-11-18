from threading import Thread
import subprocess
import sys
import csv
import re
import os

FILE_RTT_RESULTS = 'rttResults'
FILE_SPEEDTEST_RESULTS = 'speedTestResults'

def getPingResults(host, nPackages):
        process = subprocess.Popen(['ping', str(host), '-c', str(nPackages)], stdout=subprocess.PIPE)
        out, err = process.communicate()
        resultsFormated = out.split("--- "+ host +" ping statistics ---")[1]
        lossPercentage = re.findall("(\d)%", resultsFormated)
        rttValues = re.findall(r"(\d+\.\d+)", resultsFormated)
        formatedResults = rttValues + lossPercentage
        updateCsvArchive(FILE_RTT_RESULTS, formatedResults)

def getSpeedTest():
        process = subprocess.Popen(['speedtest-cli.exe', '--simple'], stdout=subprocess.PIPE)
        out, err = process.communicate()
        formatedResults = re.findall(r"(\d+\.\d+)", out)
        updateCsvArchive(FILE_SPEEDTEST_RESULTS, formatedResults)

def createCsvArchive(archiveName, headers):
        os.system('touch '+archiveName+'.csv')
        updateCsvArchive(archiveName, headers)

def updateCsvArchive(archiveName, ArrayValues):
        with open(archiveName+'.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow(ArrayValues)

def __init(args):

        print('Initializing tests...')
        createCsvArchive(FILE_RTT_RESULTS, ['min', 'avg', 'max', 'mdev'])
        createCsvArchive(FILE_SPEEDTEST_RESULTS, ['ping', 'download', 'upload'])
        
        getPingResults(args[1], 4)
        getSpeedTest()

__init(sys.argv)