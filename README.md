# qos-analitcs

#####__Description__
Command-line tool for qos analytics, Speed and Round-Trip time.
Four arguments are be passed to tool: `host`, `nPackages`, `nExecution` and `iBetweenExecution`. 
Based in this values, `nPackages` are be sended to `host` with 0.2s interval between each request in a test. The interval between each test are defined in `iBetweenExecution`(in seconds). Tests are be executed `nExecution` times.

#####__Dependencies__

* python 2.3.x
* speedtest

#####__Install speedtest__

`$sudo apt-get instal speedtest-cli`

#####__Running__

Go to archive path and for run this program:
`$python qos-analytics.py [host] [nPackages] [nExecution] [iBetweenExecution]`

* host - destination ip host for test, ex: 8.8.8.8
* nPackages - number of packages are sended peer test, ex: 2000
* nExecution - number of tests, ex: 100
* iBetweenExecution - interval between each test(in seconds), ex: 1800

When test are finalized, all results be saved in two archives `.csv`, `rttResults.csv` and `speedTestResults.csv`.
`rttResults.csv` contains `['min', 'avg', 'max', 'mdev', 'loss']` and
`speedTestResults.csv` contains `['ping', 'download', 'upload']`