def rnkg(url,path,rank):
    import requests
    import pandas as pd
    import os
    import numpy as np
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get(url,headers=headers).json()
    df = pd.json_normalize(res, record_path =['data'])
    df=df.replace(r'^\s*$', np.nan, regex=True)
    df=df.replace(np.nan,0)
    df['score']=df['score']. str.replace('','')
    df['score'].fillna(0,inplace=True)
    df['score']=df['score'].astype(float)
    left = 'k">'
    right = '</a'
    df['University'] = df['title'].str.split(left).str[1]
    df['University'] = df['University'].str.split(right).str[0]
    df.to_excel(os.path.abspath(os.path.join(path,'Ranking_'+rank+'.xlsx')),index=False)


