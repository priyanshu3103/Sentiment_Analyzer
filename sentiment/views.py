from django.shortcuts import render

from .apps import SentimentConfig
from django.http import JsonResponse
from rest_framework.views import APIView



class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            # get the text from the request
            text = request.GET.get('text')
            # vectorize the text
            vectorized = SentimentConfig.vectorizer.transform([text])
            # predict based on the vectorized text
            prediction = SentimentConfig.model.predict(vectorized)[0]
            # build a response
            response = {'text_sentiment':prediction}
            # return the response
            return JsonResponse(response)

