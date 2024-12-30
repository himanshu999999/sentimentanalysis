**Sentiment Analysis Tool**

This Python script analyzes the sentiment of a piece of text. It uses the VADER sentiment lexicon from the NLTK library to classify sentiment into positive, negative, or neutral.

**How to Use**

1. Install the required libraries:
   ```bash
   pip install nltk
Save the script as sentiment_analysis.py.
Run the script from the command line:
Bash

python sentiment_analysis.py
Enter a piece of text when prompted.
The script will print the sentiment of the text.
Example

Enter a text: I really enjoyed this movie!
Sentiment: Positive
Explanation of the Code

The code first imports the necessary libraries: logging and nltk. It then downloads the VADER sentiment lexicon from NLTK.

The SentimentAnalyzer class is defined to perform sentiment analysis on text. The analyze method takes a piece of text as input and returns its sentiment ("Positive", "Negative", or "Neutral").

The TextProcessor class is defined to process text and analyze its sentiment. The process method takes a piece of text as input and prints the sentiment to the console.

The main function creates a TextProcessor object and uses it to process the text entered by the user.
