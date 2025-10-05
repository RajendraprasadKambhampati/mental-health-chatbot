# emotion_detection.py

from preprocess import clean_text, tokenize_text

# Simple emotion keywords dictionary
emotion_keywords = {
    "happy": ["happy", "joy", "excited", "good", "cheerful", "glad"],
    "sad": ["sad", "unhappy", "depressed", "down", "upset", "cry"],
    "angry": ["angry", "mad", "frustrated", "annoyed", "irritated"],
    "anxious": ["anxious", "nervous", "worried", "stressed", "tense"],
    "neutral": []  # Default if no keywords match
}

def detect_emotion(text):
    """
    Detect emotion from user input based on keyword matching.
    Returns one of: happy, sad, angry, anxious, neutral
    """
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)
    
    for emotion, keywords in emotion_keywords.items():
        for word in tokens:
            if word in keywords:
                return emotion
    return "neutral"

# Example usage
if __name__ == "__main__":
    sample_texts = [
        "I feel very anxious about my exams.",
        "I am so happy today!",
        "I am frustrated with my work.",
        "Just an ordinary day."
    ]
    
    for text in sample_texts:
        emotion = detect_emotion(text)
        print(f"Text: {text}\nDetected Emotion: {emotion}\n")
