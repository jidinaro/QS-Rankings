# QS-Rankings
Automatically exports to excel the university rankings uploaded in QS. Given an URL containing the json file with an specific ranking, it downloads it and exports as an Excel file.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3 or higher.
* [Pandas](https://pandas.pydata.org/docs/index.html) for Python. 
 ```
      pip install pandas
 ```
* [Numpy](https://numpy.org/) for Python. 
 ```
      pip install numpy
 ```
 or just get the [Anaconda](https://docs.continuum.io/anaconda/) package where Pandas and Numpy are already installed.
* [Requests](https://docs.python-requests.org/en/latest/) for Python
```
      pip install requests
 ```
 * You have the JSON addres by having inspected with Google Chrome the QS website. In order to get this, just go to the desired ranking in the QS web, then inpsect the HTML (PRESS: ctrl + shift + i). After that, go to "Network" tab and below select "Fetch/XHR", and look for the JSON file that contains the data. It usually has a .txt extension on the name. Get the link and copy it in order to be used later on the script.
## Installing Rankings

To install the rankings script, just download Rankings.py and rnkg.py, and open with your edit IDLE to configure and execute it.

## Using Rankings.py

To use Rankings.py, follow these steps:

* Complete with your data:

```python
import os
from rnkg import *
   
path = os.path.join(os.environ['USERPROFILE'])+r'\Desktop\Python\GitHub'  #set your path
URL = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3517143.txt?1633118389?v=1633121545763" #set the QS URL obtained from inspecting the QS website
rank = 'Econ' #set a name for the ranking to download
rnkg(URL,path,rank) #Call this function as many times as you need (i.e.: subjects)
```

* Compile and run the code, it will collect all the ranking urls and export them as Excel files.

## Contact
If you want to contact me, you can reach me at juanidinaro@gmail.com
