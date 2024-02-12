import streamlit as st  
from textblob import TextBlob
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Fxn
def convert_to_df(sentiment):
	sentiment_dict = {'polarity':sentiment.polarity,'subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['metric','value'])
	
	return sentiment_df
	
def convert(sentiment):
	result_df = pd.DataFrame({
        'metric': ['Positive', 'Negative', 'Neutral'],
        'value': [sentiment.polarity if sentiment.polarity > 0 else 0,
                  abs(sentiment.polarity) if sentiment.polarity < 0 else 0,
                  1 if sentiment.polarity == 0 else 0]
    })
	return result_df

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
<<<<<<< HEAD
	
=======
>>>>>>> origin/main
# Function to automatically detect the text column in the DataFrame
def detect_text_column(df):
    text_column = None
    for column in df.columns:
        if pd.api.types.is_string_dtype(df[column]):
            text_column = column
            break
    return text_column



def main():
	st.title("Sentiment Analysis NLP App")
	st.subheader("Natural Language Processing on the Go!")

	menu = ["Home","About"]
<<<<<<< HEAD
	# Navigation bar at left top corner
	choice = st.sidebar.radio('Navigation', ['Home', 'About'])

=======
	# Navigation bar at the left top corner
	choice = st.sidebar.radio('Navigation', ['Home', 'About'])
>>>>>>> origin/main

	if choice == "Home":
		st.subheader("Sentiment Analysis with TextBlob")
		with st.form(key='nlpForm'):
			raw_text = st.text_area("Enter Text Here")
			submit_button = st.form_submit_button(label='Analyze')
		#Display Visualization from CSV
		st.subheader("Display Visualization from CSV")
		csv_file = st.file_uploader("Upload CSV",type=['csv'])
		if csv_file is not None:
			df_from_csv = pd.read_csv(csv_file)
			st.write(df_from_csv)
			# Automatically detect the text column
			text_column = detect_text_column(df_from_csv)
			
			if text_column:
				# Add a new column for sentiment analysis
				df_from_csv['Sentiment'] = df_from_csv[text_column].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

				# Streamlit app
				st.title('Sentiment Analysis on CSV Data')

				# Display the original DataFrame
				st.subheader('Original Data:')
				st.write(df_from_csv)

				# Display sentiment analysis results
				st.subheader('Sentiment Analysis Results:')
				df_from_csv['Sentiment'] = df_from_csv['review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
				df_from_csv['Sentiment_Category'] = df_from_csv['Sentiment'].apply(categorize_sentiment)
				st.write(df_from_csv[['review', 'Sentiment_Category']])

				# Optionally, you can display a bar chart for sentiment distribution
				st.subheader('Sentiment Distribution:')
				sentiment_chart = st.bar_chart(df_from_csv['Sentiment_Category'].value_counts())
			
				# Add sentiment labels to the bar chart
				for sentiment_category, count in df_from_csv['Sentiment_Category'].value_counts().items():
					st.text(f'{sentiment_category}: {count}')
			else:
				st.warning('No suitable text column found in the CSV file.')
    			
				# You can further customize the Streamlit app based on your requirements.
				# For example, you can add additional visualizations, filters, and interactivity to the app.
				# You can also deploy the app to a web server or share it with others using Streamlit Sharing.

			
			
				
	











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
				# Display sentiment label with big emoji
				if sentiment.polarity > 0:
					st.image('emojis\green-.png', caption="Positive Sentiment", width=200)
				elif sentiment.polarity < 0:
					st.image('emojis\red-.png', caption="Negative Sentiment", width=200)
				else:
					st.image('emojis\yellow-.png', caption="Neutral Sentiment", width=200)

				# Display sentiment label with big emoji
				if sentiment.polarity > 0:
					st.image('emojis\green-.png', caption="Positive Sentiment", width=200)
				elif sentiment.polarity < 0:
					st.image('emojis\red-.png', caption="Negative Sentiment", width=200)
				else:
					st.image('emojis\yellow-.png', caption="Neutral Sentiment", width=200)
				
				
				

				



			with col2:
				st.info("Token Sentiment")

				token_sentiments = analyze_token_sentiment(raw_text)
				st.write(token_sentiments)
				# Display the token sentiment analysis results
				st.subheader('Token Sentiment Analysis Results:')
				st.write(token_sentiments)
				# Optionally, you can display a bar chart for sentiment distribution
				st.subheader('Sentiment Distribution:')
				sentiment_chart = st.bar_chart(token_sentiments)
				

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

