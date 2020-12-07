import pandas as pd
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, KeywordsOptions

from keys_project import authenticator_ibm, service_url_ibm

authenticator = IAMAuthenticator(authenticator_ibm)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url(service_url_ibm)



 # _________________________________________ #



df = pd.read_csv('lets_go.csv')
tweets = []

for i in df['tweets']:
    tweets.append(i)

x = []

a1 = []
b1 = []
c1 = []
d1 = []

for i in tweets:
    try:
        x = natural_language_understanding.analyze(
            text = i,
            features=Features(
            categories=CategoriesOptions(limit=2),
            keywords=KeywordsOptions(sentiment=True,emotion=True,limit=3))).get_result()

        a = x['usage']['text_characters']
        b = x['keywords'][0]['text'] 
        c = x['keywords'][0]['sentiment']['label'] 
        d = x['categories'][0]['label']

        a1.append(a)
        b1.append(b)
        c1.append(c)
        d1.append(d)
    except:
        print('oh my')
        a1.append('aff')
        b1.append('aff')
        c1.append('aff')
        d1.append('aff')
d = {'tweets': tweets, 'text_characters': a1, 'keywords': b1, 'sentiment': c1, 'categories': d1}
df = pd.DataFrame(data=d)
print(df)

df.to_csv('done.csv')