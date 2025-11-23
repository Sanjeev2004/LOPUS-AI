import unittest
from sentiment_engine import SentimentEngine

class TestSentimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SentimentEngine()

    def test_positive_sentiment(self):
        result = self.engine.analyze_text("I am very happy and excited!")
        self.assertEqual(result['label'], "Positive")
        self.assertGreater(result['score'], 0.05)

    def test_negative_sentiment(self):
        result = self.engine.analyze_text("I am sad and angry.")
        self.assertEqual(result['label'], "Negative")
        self.assertLess(result['score'], -0.05)

    def test_neutral_sentiment(self):
        result = self.engine.analyze_text("The book is on the table.")
        self.assertEqual(result['label'], "Neutral")

    def test_trend_improvement(self):
        scores = [-0.5, -0.2, 0.1, 0.5]
        trend = self.engine.analyze_trend(scores)
        self.assertIn("Improved", trend)

    def test_trend_worsening(self):
        scores = [0.5, 0.2, -0.1, -0.5]
        trend = self.engine.analyze_trend(scores)
        self.assertIn("Worsened", trend)

if __name__ == '__main__':
    unittest.main()
