# qos-analitcs

__Dependencies__
* python 2.3.x
* speedtest

__Install speedtest__
`$sudo apt-get instal speedtest-cli`

__Running__
Go to archive path and for run this program:
`$python qos-analitcs.py [interval] [times] [host]`

* interval - time between each tests, in seconds
* times - quantity of tests, int natural number
* host - destination ip host for test, exemple 8.8.8.8

When test are finalized, all results be saved in two archives `.csv`, `rttResults.csv` and `speedTestResults.csv`.
`rttResults.csv` contains `['min', 'avg', 'max', 'mdev', 'loss']`
`speedTestResults.csv` contains `['ping', 'download', 'upload']`