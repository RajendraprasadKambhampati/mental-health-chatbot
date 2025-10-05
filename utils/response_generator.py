# response_generator.py

import json
from emotion_detection import detect_emotion

# Load coping strategies from JSON
with open("database/coping_strategies.json", "r") as f:
    coping_data = json.load(f)

def generate_response(user_input):
    """
    Generate a chatbot response based on user input.
    Steps:
    1. Detect emotion
    2. Retrieve coping strategies for that emotion
    3. Return a random response
    """
    # Detect emotion
    emotion = detect_emotion(user_input)
    
    # Get responses for the emotion
    responses = coping_data.get(emotion, coping_data["neutral"])
    
    # For variety, you can pick a random response
    import random
    response = random.choice(responses)
    
    return response

# Example usage
if __name__ == "__main__":
    sample_texts = [
        "I feel very anxious about my exams.",
        "I am so happy today!",
        "I am frustrated with my work.",
        "Just an ordinary day."
    ]
    
    for text in sample_texts:
        response = generate_response(text)
        print(f"User: {text}")
        print(f"Bot: {response}\n")
