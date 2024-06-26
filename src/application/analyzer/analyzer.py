import pandas as pd
from spacy import load
from spacy.lang.ru import Russian
from nltk.corpus import stopwords
import nltk


class Analyzer:
    def __init__(self):
        self.nlp = Russian()
        self.load_model = load('ru_core_news_sm')
        nltk.download('stopwords')
        self.stopwords_ru = stopwords.words('russian')

    def search(self, text: str, word: str) -> bool:
        result = False
        
        for doc in self.load_model.pipe([word.lower()]):
            word = [n.lemma_ for n in doc][0]

        df = pd.DataFrame([text], columns=['text'])
        df['text'] = text
        # Предобработка текста
        df['text_clean'] = df['text'].replace(r'[^\w\s]', ' ', regex=True).replace(r'\s+', ' ', regex=True).str.lower()

        # лемматизация
        lemma = []
        for doc in self.load_model.pipe(df['text_clean'].values):
            lemma.append([n.lemma_ for n in doc])
        df['text_clean_lemma'] = lemma
        df['text_clean_lemma'] = df['text_clean_lemma'].apply(
            lambda x: [item for item in x if item not in self.stopwords_ru])
        if word in df['text_clean_lemma'].values[0]:
            result = True

        return result
