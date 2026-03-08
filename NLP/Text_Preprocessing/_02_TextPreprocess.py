from textblob import TextBlob
from nltk.corpus import stopwords
import pandas as pd

#5. Chat word Treatment
from sms_dict import sms_slang
def chat_conversion(text):
    new_text = []
    for w in text.split():
        if w.upper() in sms_slang:
            new_text.append(sms_slang[w.upper()])
        else:
            new_text.append(w)
    return " ".join(new_text)

x = chat_conversion("IMHO he is the ur boss")

#6. Spelling Correction
incorrect_text = 'ceertain conditions dring sveral ggeneratioins are modified in the sama maner'

textBlb = TextBlob(incorrect_text)
textBlb = textBlb.correct().string

#7. Remove Stop words
english_stopwords = stopwords.words('english') # english stop word

def remove_stopwords(text):
    new_text = []

    for word in text.split():
        if word in english_stopwords:
            new_text.append('')
        else:
            new_text.append(word)
    x = new_text[:]
    new_text.clear()
    return " ".join(x)

text = remove_stopwords('probably my all-time favourite movie, a story of selfness, sacrifice and dedication to noble cause.') 

#apply over whole dataset
df = pd.read_csv('AI\\NLP\\dataset\\Top_rated_movies_dataset.csv')
df['overview'] = df['overview'].fillna('')
df['overview'] = df['overview'].apply(remove_stopwords)

#8. Emoji handling
import re

def remove_emoji(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map
        u"\U0001F700-\U0001F77F"
        u"\U0001F780-\U0001F7FF"
        u"\U0001F800-\U0001F8FF"
        u"\U0001F900-\U0001F9FF"  # supplemental symbols
        u"\U0001FA00-\U0001FA6F"
        u"\U0001FA70-\U0001FAFF"
        u"\U00002700-\U000027BF"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub('', text)

remove_emoji('Loved the movie. It was 😂') #Loved the movie. It was 

#understand emoji
import emoji
emoji.demojize('pyhton is ❤️')

