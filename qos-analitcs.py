from threading import Thread
import subprocess
import datetime
import time
import sys
import csv
import re
import os

_FILE_RTT_RESULTS = 'rttResults'
_FILE_SPEEDTEST_RESULTS = 'speedTestResults'

def getPingResults(_host, _nPackages, nExecution):
        print('\nrtt test n.'+str(nExecution))
        _process = subprocess.Popen(['ping', str(_host), '-c', str(_nPackages), '-i', '0.2'], stdout=subprocess.PIPE)
        _out, _err = _process.communicate()
        _resultsFormated = _out.split("--- "+ _host +" ping statistics ---")[1]
        _lossPercentage = re.findall("(\d)%", _resultsFormated)
        _rttValues = re.findall(r"(\d+\.\d+)", _resultsFormated)
        _formatedResults = _rttValues + _lossPercentage
        updateCsvArchive(_FILE_RTT_RESULTS, _formatedResults)

def getSpeedTest(serverId,nExecution):
        print('\nspeed test n.'+str(nExecution))
        _process = subprocess.Popen(['speedtest-cli.exe', '--simple', '--server', str(serverId) ], stdout=subprocess.PIPE)
        _out, _err = _process.communicate()
        _formatedResults = re.findall(r"(\d+\.\d+)", _out)
        updateCsvArchive(_FILE_SPEEDTEST_RESULTS, _formatedResults)

def createCsvArchive(_archiveName, _headers):
        with open(_archiveName+'.csv', 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow(_headers)

def updateCsvArchive(_archiveName, _arrayValues):
        with open(_archiveName+'.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow(_arrayValues)

def _init(args):
        _currentExecution = 0
        estimatedTime = int(args[3]) * int(args[4])
        
        print('---Initializing tests...')
        print('---Estimate duration: ' + str(datetime.timedelta(seconds=estimatedTime)))
        
        if(len(args) < 5):
                print('Arguments not found. all arguments are required EX.: qos-analitcs 8.8.8.8[host] 2000[nPackages] 100[nExecution] 1800[iBetweenTest] 7460[serverId]')
                pass

        createCsvArchive(_FILE_RTT_RESULTS, ['min', 'avg', 'max', 'mdev', 'loss'])
        createCsvArchive(_FILE_SPEEDTEST_RESULTS, ['ping', 'download', 'upload'])

        while(_currentExecution < int(args[3])):
                threadRtt = Thread(target=getPingResults,args=[args[1],args[2], _currentExecution])
                threadST = Thread(target=getSpeedTest, args=[args[4], _currentExecution])
                threadRtt.start()
                threadST.start()
                _currentExecution +=1
                time.sleep(float(args[4]))

        print('---End tests')

#python qos-analitcs 8.8.8.8 2000 100 1800 7460
_init(sys.argv)