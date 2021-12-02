from rnkg import *

path = os.path.join(os.environ['USERPROFILE'])+r'\Desktop\Python\GitHub'
URL = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3517143.txt?1633118389?v=1633121545763"
rank = 'Econ'
rnkg(URL,path,rank)
