from threading import Thread
import subprocess
import time
import sys
import csv
import re
import os

_FILE_RTT_RESULTS = 'rttResults'
_FILE_SPEEDTEST_RESULTS = 'speedTestResults'

def getPingResults(_host, _nPackages):
        _process = subprocess.Popen(['ping', str(_host), '-c', str(_nPackages)], stdout=subprocess.PIPE)
        _out, _err = _process.communicate()
        _resultsFormated = _out.split("--- "+ _host +" ping statistics ---")[1]
        _lossPercentage = re.findall("(\d)%", _resultsFormated)
        _rttValues = re.findall(r"(\d+\.\d+)", _resultsFormated)
        _formatedResults = _rttValues + _lossPercentage
        updateCsvArchive(_FILE_RTT_RESULTS, _formatedResults)

def getSpeedTest():
        _process = subprocess.Popen(['speedtest-cli.exe', '--simple'], stdout=subprocess.PIPE)
        _out, _err = _process.communicate()
        _formatedResults = re.findall(r"(\d+\.\d+)", _out)
        updateCsvArchive(_FILE_SPEEDTEST_RESULTS, _formatedResults)

def createCsvArchive(_archiveName, _headers):
        os.system('touch '+_archiveName+'.csv')
        updateCsvArchive(_archiveName, _headers)

def updateCsvArchive(_archiveName, _arrayValues):
        with open(_archiveName+'.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow(_arrayValues)

def handlerRttTest(_interval, _times, _host, _nPackages):
        _currentExecution = 0

        print( 'rtt tests being executed..')

        while (True):
                getPingResults(_host, _nPackages)
                _currentExecution +=1
                time.sleep(float(_interval))
                if (_currentExecution < _times): 
                        pass

        print( 'rtt tests were terminated')

def handlerSpeedTest(_interval, _times):
        _currentExecution = 0

        print( 'speedtest tests being executed..')
        
        while (True):
                getSpeedTest()
                _currentExecution +=1
                time.sleep(float(_interval))
                if (_currentExecution < _times): 
                        pass

        print( 'speedtest tests were terminated')

def _init(args):

        print('Initializing tests...')
        print('Estimate duration: ' + time.strftime('%H:%M:%S', time.gmtime(int(args[1]) * int(args[2]))))
        if(len(args) < 4):
                print('Arguments not found. all arguments are required EX.: qos-analitcs.py 60[interval] 10[times] 8.8.8.8[host]')
                pass

        createCsvArchive(_FILE_RTT_RESULTS, ['min', 'avg', 'max', 'mdev'])
        createCsvArchive(_FILE_SPEEDTEST_RESULTS, ['ping', 'download', 'upload'])

        threadRtt = Thread(target=handlerRttTest,args=[args[1],args[2],args[3], 5])
        threadST = Thread(target=handlerSpeedTest,args=[args[1],args[2]])
        
        threadRtt.start()
        threadST.start()

_init(sys.argv)