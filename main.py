import logging
from chatbot import SentimentBot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

def main():
    bot = SentimentBot()
    
    print("--- AI Sentiment Chatbot Initialized ---")
    print("Type 'exit' to end conversation and see the report.\n")
    
    try:
        while True:
            user_input = input("User: ")
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                break
                
            bot.process_message(user_input)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An error occurred. Please check the logs.")
    finally:
        # Trigger Tier 1 Final Report
        bot.generate_report()

if __name__ == "__main__":
    main()