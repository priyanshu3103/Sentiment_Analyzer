from django.apps import AppConfig
from django.conf import settings
import sklearn
import os
import pickle

class SentimentConfig(AppConfig):
    name = 'sentiment'
    path= os.path.join(settings.MODELS, 'models.p')
    # load model into saperate variables
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    model = data['model']
    vectorizer = data['vectorizer']
