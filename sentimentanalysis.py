import logging
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze(self, text):
        try:
            sentiment = self.sia.polarity_scores(text)
            if sentiment['compound'] > 0.05:
                return "Positive"
            elif sentiment['compound'] < -0.05:
                return "Negative"
            else:
                return "Neutral"
        except Exception as e:
            logging.error(f"Error analyzing sentiment: {e}")
            return None

class TextProcessor:
    def __init__(self):
        self.analyzer = SentimentAnalyzer()

    def process(self, text):
        sentiment = self.analyzer.analyze(text)
        if sentiment:
            print(f"Sentiment: {sentiment}")
        else:
            print("Failed to analyze sentiment")

def main():
    logging.basicConfig(level=logging.ERROR)
    text = input("Enter a text: ")
    processor = TextProcessor()
    processor.process(text)

if __name__ == "__main__":
    main()
