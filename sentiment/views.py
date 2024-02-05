from django.shortcuts import render
from .apps import SentimentConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from .models import AnalyzedText
from .forms import SentimentForm
import os
import pickle
from .apps import SentimentConfig
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



# class call_model(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             # get the text from the request
#             text = request.GET.get('text')
#             # vectorize the text
#             vectorized = SentimentConfig.vectorizer.transform([text])
#             # predict based on the vectorized text
#             prediction = SentimentConfig.model.predict(vectorized)[0]
#             # build a response
#             response = {'text_sentiment':prediction}
#             # return the response
#             return JsonResponse(response)
        

# def sentiment_analysis(request):
#     result = None

#     if request.method == 'POST':
#         form = SentimentForm(request.POST)
#         if form.is_valid():
#                 text_to_analyze = form.cleaned_data['text_input']
            
#                 # Merged sentiment analysis logic
#                 if len(text_to_analyze) % 2 == 0:
#                     sentiment_result = "Positive"
#                 elif len(text_to_analyze) % 2 == 1:
#                     sentiment_result = "Negative"
#                 else:
#                     sentiment_result = "Neutral"

#         AnalyzedText.objects.create(text=text_to_analyze, sentiment=sentiment_result)
#         result = sentiment_result
#     else:
#         form = SentimentForm()

#         return render(request, 'index.html', {'form': form, 'result': result})
# # def your_view(request):
#     return render(request, 'index.html')
# def sentiment_analysis(request):
#     if request.method == 'GET':
#         # Retrieve the text_input parameter from the request
#         text_input = request.GET.get('text_input', '')

#         # Perform sentiment analysis on the text_input (replace this with your actual sentiment analysis logic)
#         sentiment_result = sentiment_analysis(text_input)

#         # Return the sentiment result as a JSON response
#         return JsonResponse({'result': sentiment_result})
# # def analyze_sentiment(text):
#     # Placeholder for sentiment analysis logic
#     # Replace this with your actual sentiment analysis implementation
#     # This could be a call to an NLP library or your custom logic
#     # For simplicity, just returning a dummy result here
#     if 'happy' in text.lower():
#         return 'Positive sentiment'
#     else:
#         return 'Neutral or Negative sentiment'

# def sentiment_analysis(request):
#     result = None

#     if request.method == 'POST':
#         form = SentimentForm(request.POST)
#         if form.is_valid():
#             text_to_analyze = form.cleaned_data['text_input']

#             # Load model and vectorizer from SentimentConfig
#             model = SentimentConfig.model
#             vectorizer = SentimentConfig.vectorizer

#             # Perform sentiment analysis using the loaded model and vectorizer
#             input_vector = vectorizer.transform([text_to_analyze])
#             prediction = model.predict(input_vector)[0]
            
#             # Map the prediction to a sentiment label (adjust this based on your model's output)
#             sentiment_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}
#             sentiment_result = sentiment_mapping.get(prediction, "Unknown")

#             # Save the analysis result to the database
#             AnalyzedText.objects.create(text=text_to_analyze, sentiment=sentiment_result)
#             result = sentiment_result
#     else:
#         form = SentimentForm()

#     return render(request, 'index.html', {'form': form, 'result': result})






def convert_to_df(sentiment):
    sentiment_dict = {'polarity': sentiment.polarity, 'subjectivity': sentiment.subjectivity}
    sentiment_df = pd.DataFrame(sentiment_dict.items(), columns=['metric', 'value'])
    return sentiment_df


def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []
    for i in docx.split():
        res = analyzer.polarity_scores(i)['compound']
        if res > 0.1:
            pos_list.append(i)
            pos_list.append(res)

        elif res <= -0.1:
            neg_list.append(i)
            neg_list.append(res)
        else:
            neu_list.append(i)

    result = {'positives': pos_list, 'negatives': neg_list, 'neutral': neu_list}
    return result


def home(request):
    if request.method == 'POST':
        raw_text = request.POST.get('raw_text', '')
        sentiment = TextBlob(raw_text).sentiment

        result_df = convert_to_df(sentiment)

        token_sentiments = analyze_token_sentiment(raw_text)

        context = {
            'sentiment': sentiment,
            'result_df': result_df,
            'token_sentiments': token_sentiments
        }

        return render(request, 'home.html', context)

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')






