import random
import logging
from typing import List, Dict, Any
from sentiment_engine import SentimentEngine

logger = logging.getLogger(__name__)

class SentimentBot:
    def __init__(self):
        self.engine = SentimentEngine()
        self.history: List[Dict[str, Any]] = [] # Stores full conversation context
        self.user_scores: List[float] = [] # Stores raw scores for calculation
        
        # Simple response templates to simulate conversation
        self.responses = [
            "I understand. Please tell me more.",
            "That is interesting. How does that make you feel?",
            "I am taking notes on this. Go on.",
            "Could you elaborate on that?",
            "I see. What else is on your mind?"
        ]

    def get_bot_response(self, user_input: str) -> str:
        """Simple logic to return a response."""
        # In a real app, this would be an LLM or intent classifier
        return random.choice(self.responses)

    def process_message(self, user_input: str):
        """
        Tier 2 Requirement: Statement-Level Analysis
        Process message, analyze sentiment, and store history.
        """
        # 1. Analyze current message
        analysis = self.engine.analyze_text(user_input)
        
        # 2. Generate Bot Response
        bot_reply = self.get_bot_response(user_input)

        # 3. Store in History (Tier 1 requirement)
        interaction = {
            "user_text": user_input,
            "bot_text": bot_reply,
            "user_sentiment": analysis['label'],
            "user_score": analysis['score']
        }
        self.history.append(interaction)
        self.user_scores.append(analysis['score'])
        
        logger.info(f"Processed message. Sentiment: {analysis['label']}, Score: {analysis['score']}")

        # 4. Output for User (Console Interface)
        print(f"→ Sentiment: {analysis['label']} (Score: {analysis['score']})")
        print(f"Chatbot: {bot_reply}\n")

    def generate_report(self):
        """
        Tier 1 Requirement: Conversation-Level Analysis
        Generates the final report based on full history.
        """
        if not self.history:
            print("No conversation to analyze.")
            return

        # Calculate average sentiment score
        avg_score = sum(self.user_scores) / len(self.user_scores)
        
        # Determine overall sentiment
        if avg_score >= 0.05:
            overall_mood = "Positive - The user seems generally satisfied."
        elif avg_score <= -0.05:
            overall_mood = "Negative - The user expressed dissatisfaction."
        else:
            overall_mood = "Neutral - The conversation was balanced or objective."

        # Get Bonus Trend
        trend = self.engine.analyze_trend(self.user_scores)

        print("="*40)
        print("FINAL SENTIMENT REPORT")
        print("="*40)
        print(f"Total Messages: {len(self.history)}")
        print(f"Overall Sentiment: {overall_mood}")
        print(f"Conversation Trend: {trend}")
        print("="*40)