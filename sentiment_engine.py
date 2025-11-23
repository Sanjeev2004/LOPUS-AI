import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class SentimentEngine:
    def __init__(self):
        # Initialize VADER analyzer
        # VADER is rule-based and optimized for social media/chat text
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except LookupError:
            logger.info("Downloading VADER lexicon...")
            nltk.download('vader_lexicon', quiet=True)
            
        self.analyzer = SentimentIntensityAnalyzer()
        logger.info("SentimentEngine initialized.")

    def analyze_text(self, text: str) -> Dict[str, any]:
        """
        Analyzes a single string and returns a dictionary with 
        compound score and label.
        """
        scores = self.analyzer.polarity_scores(text)
        compound = scores['compound']
        
        # Determine label based on compound score thresholds
        if compound >= 0.05:
            label = "Positive"
        elif compound <= -0.05:
            label = "Negative"
        else:
            label = "Neutral"
            
        logger.debug(f"Analyzed text: '{text}' -> {label} ({compound})")
            
        return {
            "score": compound,
            "label": label,
            "breakdown": scores
        }

    def analyze_trend(self, scores: List[float]) -> str:
        """
        Optional Bonus: Determines if the mood improved or worsened.
        """
        if len(scores) < 2:
            return "Insufficient data for trend."
        
        start_avg = sum(scores[:len(scores)//2]) / (len(scores)//2)
        end_avg = sum(scores[len(scores)//2:]) / (len(scores) - len(scores)//2)
        
        diff = end_avg - start_avg
        if diff > 0.1: return "Mood Improved 📈"
        if diff < -0.1: return "Mood Worsened 📉"
        return "Mood Stable ➡️"