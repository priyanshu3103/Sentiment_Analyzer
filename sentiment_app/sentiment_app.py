import streamlit as st  
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Fxn
def convert_to_df(sentiment):
	sentiment_dict = {'polarity':sentiment.polarity,'subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['metric','value'])
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

	result = {'positives':pos_list,'negatives':neg_list,'neutral':neu_list}
	return result 
# Function to categorize sentiment
def categorize_sentiment(sentiment):
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'


# Function to categorize sentiment
def categorize_sentiment(sentiment):
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'
	

def main():
	st.title("Sentiment Analysis NLP App")
	st.subheader("Natural Language Processing on the Go!")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu", menu, index=0, key="readonly_selectbox")

	if choice == "Home":
		st.subheader("Home")
		with st.form(key='nlpForm'):
			raw_text = st.text_area("Enter Text Here")
			submit_button = st.form_submit_button(label='Analyze')
		#Display Visualization from CSV
		st.subheader("Display Visualization from CSV")
		csv_file = st.file_uploader("Upload CSV",type=['csv'])
		if csv_file is not None:
			df_from_csv = pd.read_csv(csv_file)
			st.write(df_from_csv)
			# Visualization
			c = alt.Chart(df_from_csv).mark_bar().encode(
				x=alt.X('metric:N', title='Metric'),
    			y=alt.Y('value:Q', title='Value'),
    			color='metric:N')	
			st.altair_chart(c,use_container_width=True)
				
	











		# layout
		col1,col2 = st.columns(2)
		if submit_button:

			with col1:
				st.info("Results")
				sentiment = TextBlob(raw_text).sentiment
				st.write(sentiment)

				# Emoji
				if sentiment.polarity > 0:
					st.markdown("Sentiment:: Positive :smiley: ")
				elif sentiment.polarity < 0:
					st.markdown("Sentiment:: Negative :angry: ")
				else:
					st.markdown("Sentiment:: Neutral 😐 ")

				# Dataframe
				result_df = convert_to_df(sentiment)
				st.dataframe(result_df)

				# Visualization
				c = alt.Chart(result_df).mark_bar().encode(
					x='metric',
					y='value',
					color='metric')
				st.altair_chart(c,use_container_width=True)



			with col2:
				st.info("Token Sentiment")

				token_sentiments = analyze_token_sentiment(raw_text)
				st.write(token_sentiments)

	elif choice == "About":
		st.subheader("Sentiment Analysis:")
		st.markdown("""
    	Sentiment analysis is a natural language processing (NLP) technique that involves
		determining the sentiment or emotion expressed in a piece of text. Streamlit is 
		a Python library that makes it easy to create web applications for data exploration,
		visualization, and analysis.Combining sentiment analysis with Streamlit allows you 
		to build interactive web applications that can analyze and visualize the sentiment
		of user-provided text.
			  
		Here's a theoretical overview of sentiment analysis using Streamlit:

		Sentiment Analysis:
			  
		Sentiment analysis, also known as opinion mining, is the process of determining the
		sentiment or emotion expressed in a given piece of text. The primary goal is to understand
		whether the text conveys a positive, negative, or neutral sentiment. Sentiment analysis is 
		widely used in various applications, including customer feedback analysis, social media 
		monitoring, and product reviews.
		   


		Techniques for Sentiment Analysis:
		Rule-Based Approaches: 
		   These approaches use predefined rules and lexicons to determine sentiment. For example, 
			the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool is a 
			rule-based approach commonly used for sentiment analysis.

		Machine Learning Approaches: 
		   These approaches involve training machine learning models on labeled datasets to predict sentiment.
			Common algorithms include Naive Bayes, Support Vector Machines (SVM), and deep learning models 
			like recurrent neural networks (RNNs) and transformers.

		Streamlit for Web Applications:
		   Streamlit is a Python library that simplifies the process of creating web applications.
			 It is designed to be easy to use, enabling developers to create interactive web apps with minimal code.
			 Here's how you can integrate sentiment analysis with Streamlit:

		Streamlit Basics:
			Installation:

				You can install Streamlit using pip:
				pip install streamlit
		   
			Creating a Streamlit App:
		   		A Streamlit app is typically a Python script that contains sections
		   		 for defining the UI elements and the logic of the app.
			UI Components:
		   		Streamlit provides UI components like st.title(), st.text(), st.button(),
		   		 and st.text_area() to create a user interface.
			Interactivity:
		   Use components like st.button() and st.form() to make your app interactive.	
		""")

	else:
		st.subheader("About")



if __name__ == '__main__':
	main()

