Sentiment Analysis NLP App

This Streamlit application utilizes natural language processing (NLP) for sentiment analysis. 
It uses the TextBlob library for overall sentiment analysis and the VaderSentiment library to analyze sentiment at the token level.
The app displays sentiment metrics, emoji representation of sentiment, and token-level sentiment analysis.


Getting Started
To run this Streamlit app, ensure you have the required libraries installed.
You can install them using the following commands:
![requirement](https://github.com/priyanshu3103/Sentiment_Analyzer/assets/101656280/8fb84322-da87-4a13-a773-efe581960cfd)


Running the App:
Once the dependencies are installed, you can run the app by executing the following command in your terminal:
        ![server](https://github.com/priyanshu3103/Sentiment_Analyzer/assets/101656280/8c504c76-9606-40eb-93f3-7f151df3f804)


Usage:
1) The app consists of two sections: "Home" and "About."
2) In the "Home" section, enter the text you want to analyze in the text area provided.
3) Click the "Analyze" button to initiate sentiment analysis.
4) The results will be displayed in two columns:
5) Results: Overall sentiment analysis, emoji representation, and a dataframe with sentiment metrics.
6) Token Sentiment: Analysis of sentiment at the token level, showing positive, negative, and neutral tokens.

Dependencies:
. Streamlit
. TextBlob
. Pandas
. Altair
. VaderSentiment
