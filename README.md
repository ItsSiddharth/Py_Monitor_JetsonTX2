# Context-Search

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/ItsSiddharth/context_search/blob/master/LICENSE)   [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

## About
Optimisation has become a need of the hour. Gpu usage, CPU usage, GPU temperature, CPU temperature, Power comsumption are a great indicator of how a process can be optimised further. This project allows you to run a process analysing algorithm in a parallel thread while you are running your block of code in python that needs to be monitored. A graph will be generated once the process completes and will be saved in the same folder as your python script.

## For source code 
This the my <a href="https://github.com/ItsSiddharth/Py_Monitor_JetsonTX2">Github repo. </a>
Contact me for support and PRs are welcome.

## Usage 
1. Pip install the package.
```
$ pip3 install Py-Monitor-JetsonTX2
```
* **NOTE** : Please note that the package is specific to NVIDIA JETSON TX2.

> The use of package will result in an image and a txt file in the same directory as your python code.

## Syntax 
1. Import the library.
```
>> import Py_Monitor_JetsonTX2 as pm
```
2. Create an object of the class, pm.Analyser(). Say, `analyser`.
```
>> analyser = pm.Analyser()
```
3. Now place a start trigger at that point in your code where you want to start recording the resources being used
```
>> analyser.start_recording()
```
* **NOTE** : This initiates another thread parallel to the script that is being executed.
4. Once the process you want to monitor is over place another trigger telling the package to stop monitoring resource consumption.
```
>> analyser.stop_recording()
```
5. Once the code completes execution you can return to your directory where the python code resides to find a PNG that shows the GPU usage, CPU usage, GPU temperature, CPU temperature and Power consumption stats of the code that lies within ```start_recording() and stop_recording()```

## LICENSE
<a href="https://github.com/ItsSiddharth/Py_Monitor_JetsonTX2/blob/master/LICENSE">MIT</a>
