#First lower case or upper case the text.
"""
task for text preprocessing:
1. lower case or upper case
2. remove html tags for web scrapped data and URL -> use BeautifulSoup library for web scrapping and for removing html tags -> regular expressions can also be used for removing html tags. tools: regex101.com
3. remove punctuations and Chat word treatment
4. spelling correction and remove stop words
5. emoji handling
6. remove extra spaces
7. Tokenize
8. Stemming
9. Lemmatization
"""
from os import remove

import pandas as pd
import re #for regular expressions, it is used for removing html tags and punctuations.
import string, time

#0. load the dataset
df = pd.read_csv('AI\\NLP\\dataset\\Top_rated_movies_dataset.csv') #relative path, absolute path can also be used.

df.shape #check the shape of the dataset, it has 8560 rows and 7 columns.
df.columns #check the column names of the dataset, Index(['id', 'title', 'overview', 'release_date', 'popularity', 'vote_average','vote_count'],dtype='object')

df.head() #check the first 5 rows of the dataset. The overview column contains the text data that we will be preprocessing.

#1. lower case
df['overview'] = df['overview'].str.lower() #lower case the text in the overview column.

#for particular row let 0th -> let 0th have html tags => have to remove it
# print(df['overview'][0]) 

#2. HTML tag removal using regular expressions
def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)

df['overview'] = df['overview'].fillna('') #fill the missing values with empty string before applying the remove_html_tags function.
df['overview'] = df['overview'].apply(remove_html_tags) #remove html tags from -> direct use of apply without fillna will give error because of missing values in the overview column.

#3. Remove URL links from urls in the text, as they are not useful for text analysis.
def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub(r'', text)

df['overview'] = df['overview'].apply(remove_url)

#4. Removing Punctuation
exclude = string.punctuation #punc: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~

#too slow
def remove_punc(text):
    for char in exclude:
        text = text.replace(char, '')
    return text

#better and fast approach
def remove_punc1(text):
    return text.translate(str.maketrans('', '', exclude))

df['overview'] = df['overview'].apply(remove_punc1)

#Extras: time taken
start = time.time()
#function
time1 = time.time() - start
#print time1

print(df['overview'].head())
