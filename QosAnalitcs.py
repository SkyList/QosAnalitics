import re
import sys
import subprocess
from threading import Thread

def getPingResults(host, nPackages):
    process = subprocess.Popen(['ping', str(host), '-c', str(nPackages)], stdout=subprocess.PIPE)
    out, err = process.communicate()
    resultsFormated = out.split("--- "+ host +" ping statistics ---")[1]
    lossPercentage = re.findall("(\d)%", resultsFormated)
    rttValues = re.findall(r"(\d+\.\d+)", resultsFormated)
    return rttValues + lossPercentage



def __init(args):
    print getPingResults(args[1], 4)

__init(sys.argv)